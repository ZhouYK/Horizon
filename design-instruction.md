# 消息可信度评分设计说明

## 评分流程概览

项目通过 AI 对每条内容打 **0-10 的重要性分数**，核心逻辑分三个层次。

---

## 1. 输入信号

`ContentAnalyzer._analyze_item`（`src/ai/analyzer.py:92`）构建提示词时组合以下信号：

**内容本身：**
- 标题、正文（最多 1000 字）、评论（最多 1500 字）

**互动数据**（来自 `item.metadata`）：

| 字段 | 来源平台 |
|------|----------|
| `score` | HN / Reddit 点数 |
| `descendants` | HN / Reddit 评论数 |
| `upvote_ratio` | Reddit 点赞率 |
| `favorite_count` | Twitter 点赞 |
| `retweet_count` | Twitter 转发 |
| `reply_count` | Twitter 回复 |
| `views` | Twitter 浏览量 |
| `bookmarks` | Twitter 书签 |
| `community_note` | Twitter 社区注记 |

---

## 2. 评分标准

评分标准定义在 `src/ai/prompts.py:23`（`CONTENT_ANALYSIS_SYSTEM`），AI 用以下 rubric 打分：

| 分段 | 含义 |
|------|------|
| **9-10** | 突破性 — 重大版本发布、研究突破、行业变革 |
| **7-8** | 高价值 — 深度技术分析、新颖方法、有价值的工具 |
| **5-6** | 一般有趣 — 渐进式改进、教程、中等热度 |
| **3-4** | 低优先级 — 常规更新、过度推广 |
| **0-2** | 噪音 — 垃圾、无关、琐碎内容 |

综合考量维度：
- 技术深度与新颖性
- 领域影响力
- 写作质量
- 与软件工程、AI/ML、系统研究的相关性
- 社区讨论质量（有意义的争论可提升分数）
- 互动信号（高点赞 + 有实质性讨论 → 社区验证的重要性）

---

## 3. 结果存储与过滤

- 分数写入 `item.ai_score`（float，0-10），定义见 `src/models.py:61`
- 默认过滤阈值 `ai_score_threshold = 7.0`（`src/models.py:484`），低于该值不展示
- 同时输出：
  - `ai_reason`：打分理由
  - `ai_summary`：一句话摘要
  - `ai_tags`：3-5 个标签

---

## 4. 内容筛选与分组流程

完整的 pipeline 在 `src/orchestrator.py` 中按以下顺序执行：

### 4.1 全局分数阈值

`filter_items`（`src/orchestrator.py:806`）对所有来源的 item 统一过滤，只保留 `ai_score >= ai_score_threshold`（当前配置 6.0）的条目，并按分数降序排列。

### 4.2 话题去重

对高分 item 做跨来源的话题级去重（`merge_topic_duplicates`），合并报道同一事件的重复内容。

### 4.3 分组配额（apply_balanced_digest）

`apply_balanced_digest`（`src/orchestrator.py:904`）对去重后的 item 按 `category_groups` 配置独立分配配额，各组互不干扰：

| 组 | limit | 说明 |
|----|-------|------|
| AI 资讯 | 10 | category 为 ai-news / ai-tools / news |
| 股票资讯 | 20 | category 为 finance-cn / finance / stocks / investing |
| other | 不限 | 其余 category |

**股票资讯组的特殊逻辑**（按优先级依次执行）：

1. **标题过滤（优先）**：只保留标题中含有配置股票名称或代码的文章；不符合的暂存为兜底候选
2. **per-stock 限额**：匹配到具体股票的文章每只股票最多 `stock_limit`（当前 5）条，通过 `feed_name` 或标题识别所属股票
3. **兜底补全**：若股票过滤后条数不足 `limit`（20），从兜底候选（通用财经文章）中按分数降序补入
4. **最终排序**：所有选中条目（含兜底）按 `ai_score` 降序重新排列

### 4.4 按 report 拆分

`_split_items_by_report`（`src/orchestrator.py:853`）将选中 item 按 `category_groups[].report` 字段拆入各自的报告桶。配置了 `report` 的分组即使 0 条也会生成空文件，避免旧文件残留。

---

## 关键设计特点

1. **纯 AI 打分**：没有硬编码的规则权重，全靠 prompt 引导模型判断
2. **互动信号作为辅助**：不是独立维度，拼入 prompt 让 AI 参考
3. **失败降级**：解析失败时自动降为 0 分（`src/ai/analyzer.py:65`），不让异常内容混入结果
4. **并发控制**：通过 `analysis_concurrency` 和 `throttle_sec` 配置并发数与请求间隔（`src/ai/analyzer.py:48-56`）
5. **重试机制**：单条内容分析最多重试 3 次，指数退避 2-10 秒（`src/ai/analyzer.py:88-91`）