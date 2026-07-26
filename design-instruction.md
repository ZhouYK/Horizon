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

## 关键设计特点

1. **纯 AI 打分**：没有硬编码的规则权重，全靠 prompt 引导模型判断
2. **互动信号作为辅助**：不是独立维度，拼入 prompt 让 AI 参考
3. **失败降级**：解析失败时自动降为 0 分（`src/ai/analyzer.py:65`），不让异常内容混入结果
4. **并发控制**：通过 `analysis_concurrency` 和 `throttle_sec` 配置并发数与请求间隔（`src/ai/analyzer.py:48-56`）
5. **重试机制**：单条内容分析最多重试 3 次，指数退避 2-10 秒（`src/ai/analyzer.py:88-91`）