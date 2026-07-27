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

---

## 5. LLM 客户端抽象层（`src/ai/client.py`）

所有 LLM 调用统一通过 `AIClient.complete(system, user) -> str` 接口，由 `create_ai_client(config)` 工厂方法按配置创建具体实现。

### 5.1 支持的 Provider

| 类 | Provider | 底层 SDK |
|---|---|---|
| `AnthropicClient` | anthropic | `AsyncAnthropic` |
| `OpenAIClient` | openai / ali / doubao / minimax / deepseek / ollama | `AsyncOpenAI` |
| `AzureOpenAIClient` | azure | `AsyncAzureOpenAI` |
| `GeminiClient` | gemini | `google.genai` |
| `ChainedAIClient` | 多 Provider 链 | 依次 fallback |

默认模型配置定义在 `src/models.py:84`（`AI_PROVIDER_DEFAULTS`），如 Anthropic 默认 `claude-3-5-sonnet-20241022`、阿里云默认 `qwen-plus`。

### 5.2 ChainedAIClient fallback 机制

配置 `provider_chain`（如 `"openai,anthropic"`）时创建 `ChainedAIClient`，触发 fallback 的错误类型（`src/ai/client.py:620`）：

- `429` / `rate limit` — 限流
- `401` / `403` / `quota` / `exceeded` — 鉴权失败或配额耗尽
- `502` / `503` / `service unavailable` — 服务不可用
- 空响应 — 模型返回空字符串

切换时打印黄色提示，所有 Provider 均失败则抛出 `RuntimeError`。

---

## 6. LLM 调用方式（per Provider）

### 6.1 Anthropic（`src/ai/client.py:157`）

```python
message = await self.client.messages.create(
    model=self.model,
    max_tokens=max_tokens,       # 默认 4096
    temperature=temperature,     # 默认 0.3
    system=system,               # system prompt 作为顶层独立字段
    messages=[{"role": "user", "content": user}]
)
```

`system` 不放入 `messages` 数组，是 Anthropic API 的专有结构。

### 6.2 OpenAI 系（`src/ai/client.py:316`）

涵盖 openai / ali / doubao / minimax / deepseek / ollama：

```python
await self.client.chat.completions.create(
    model=self.model,
    messages=[
        {"role": "system", "content": system},
        {"role": "user",   "content": user},
    ],
    max_tokens=max_tokens,                         # o1/o3/o4/gpt-5 用 max_completion_tokens
    temperature=temperature,
    response_format={"type": "json_object"},       # minimax 不支持，跳过
)
```

两个运行时自适应机制：
- **temperature 不支持**：首次 400 报错后设 `_supports_temperature = False`，后续请求不带该参数
- **token 参数名**：o1/o3/o4/gpt-5 系列需要 `max_completion_tokens`，首次失败后自动切换并记住

### 6.3 Azure（`src/ai/client.py:454`）

```python
await self.client.chat.completions.create(
    model=self.model,            # 传 deployment name，不是模型名
    messages=[...],              # 同 OpenAI 格式
    temperature=temperature,
    response_format={"type": "json_object"},
    max_tokens=max_tokens,       # 同样支持自动切换 max_completion_tokens
)
```

额外需要 `azure_endpoint`（从 `azure_endpoint_env` 环境变量读取）和 `api_version`（默认 `2024-10-21`）。

### 6.4 Gemini（`src/ai/client.py:514`）

```python
await self.client.aio.models.generate_content(
    model=self.model,
    contents=user,
    config=types.GenerateContentConfig(
        system_instruction=system,
        temperature=temperature,
        max_output_tokens=max_tokens,
        response_mime_type="application/json"    # 等价于 OpenAI 的 response_format
    )
)
```

---

## 7. 获取与处理 LLM 返回

### 7.1 从响应对象提取文本

| Provider | 文本取法 | Input Token 取法 | Output Token 取法 |
|---|---|---|---|
| Anthropic | `message.content[0].text` | `usage.input_tokens` | `usage.output_tokens` |
| OpenAI 系 | `response.choices[0].message.content` | `usage.prompt_tokens` | `usage.completion_tokens` |
| Azure | 同 OpenAI | 同 OpenAI | 同 OpenAI |
| Gemini | `response.text` | `usage_metadata.prompt_token_count` | `total_token_count - prompt_token_count` |

Token 用量通过 `tokens.record_usage(provider, input, output)` 写入全局内存计数器（`src/ai/tokens.py`），运行结束后汇总打印。

### 7.2 JSON 解析（`src/ai/utils.py:8`）

LLM 可能在 JSON 外包裹 Markdown 代码块或前缀文字，`parse_json_response()` 依次尝试 5 级策略：

| 优先级 | 策略 |
|---|---|
| 1 | `json.loads(text)` 直接解析 |
| 2 | 提取 ` ```json ... ``` ` 块后解析 |
| 3 | 提取 ` ``` ... ``` ` 块后解析 |
| 4 | 花括号深度匹配，找第一个完整 `{...}` |
| 5 | `re.search(r"\{[\s\S]*\}", text)` 正则兜底 |

全部失败返回 `None`。

### 7.3 按场景校验与写入

#### 评分场景（`src/ai/analyzer.py:169`）

```python
parsed = parse_json_response(response)            # → dict | None
result = AnalysisResult.model_validate(parsed)    # Pydantic 校验
# AnalysisResult: score(float, 0-10), reason(str), summary(str), tags(list[str])

item.ai_score   = result.score
item.ai_reason  = result.reason
item.ai_summary = result.summary
item.ai_tags    = result.tags
```

校验失败 → `ai_score=0.0`，`ai_reason="Analysis response parse failed"`，`ai_summary=item.title`

#### 增强场景（`src/ai/enricher.py:194`）

分三步调用 LLM：

1. **概念提取**（`CONCEPT_EXTRACTION_SYSTEM/USER`）：返回 1-3 个搜索词
2. **DuckDuckGo 网页搜索**（`ddgs` 库，`asyncio.to_thread`）：每词取 3 条结果
3. **双语增强**（`CONTENT_ENRICHMENT_SYSTEM/USER`，含搜索结果 grounding）：返回结构化双语 JSON

增强结果写入 `item.metadata`：

| Key | 说明 |
|---|---|
| `title_en` / `title_zh` | 双语标题 |
| `detailed_summary_en` / `detailed_summary_zh` | 由 `whats_new` + `why_it_matters` + `key_details` 三段拼接 |
| `background_en` / `background_zh` | 背景知识（2-4句） |
| `community_discussion_en` / `community_discussion_zh` | 社区讨论摘要 |
| `sources` | 仅保留确实出现在搜索结果中的 URL（防止模型捏造链接） |

解析失败降级 → `_translate_item()`，仅翻译标题和摘要为中文，不补背景。

### 7.4 重试与降级策略

```
_analyze_item / _enrich_item
    └── @retry(stop_after_attempt(3), wait_exponential(min=2s, max=10s))
            ├── 成功 → 写入 item 字段
            ├── JSON 解析 / 校验失败 → 写默认值 / 降级 _translate_item
            └── 网络/API 错误 → tenacity 重试，3次全败后抛出

ChainedAIClient.complete()
    └── Provider A 失败（限流/鉴权/服务不可用/空响应）
            → 自动切换 Provider B → Provider C → 全败抛 RuntimeError
```

### 7.5 完整数据流（以评分为例）

```
ContentItem
    ↓ 拼接 CONTENT_ANALYSIS_USER（title/source/content/engagement）
    ↓
AIClient.complete(system=CONTENT_ANALYSIS_SYSTEM, user=...)
    ↓
raw_str: '{"score": 8.5, "reason": "...", "summary": "...", "tags": [...]}'
    ↓
parse_json_response() → dict（5 级解析）
    ↓
AnalysisResult.model_validate(dict)  ← Pydantic 确保 score ∈ [0, 10]
    ↓
item.ai_score=8.5 / ai_summary="..." / ai_tags=[...]
```