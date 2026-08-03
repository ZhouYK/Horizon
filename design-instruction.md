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

---

## 8. MCP Server 设计说明（`src/mcp/`）

### 8.1 模块职责

`src/mcp/` 把 Horizon 的抓取/打分/过滤/增强/摘要 pipeline 包装成一个 **MCP（Model Context Protocol）server**，供外部 MCP client（Claude Desktop、Claude Code 等）调用。**不重新实现业务逻辑**，只是加一层可分阶段调用、可续跑的工具外壳。

| 文件 | 作用 |
|---|---|
| `server.py` | MCP 入口，用 `FastMCP` 注册工具/资源，统一包一层 `_ok`/`_err` 响应格式，维护调用次数、耗时等 metrics |
| `service.py` | `HorizonPipelineService`，真正的业务编排层，调用 orchestrator 各阶段函数，做 config 校验和敏感字段脱敏（`_redact_config` 遮蔽 key/token/secret 等字段） |
| `horizon_adapter.py` | 适配层，动态加载 Horizon 主代码库（`load_runtime`/`make_orchestrator`/`make_storage`），复用主仓库的 `ContentItem`/`Config`/orchestrator，而不是重写 |
| `run_store.py` | 每次 pipeline 运行的中间产物持久化到 `data/mcp-runs/<run_id>/`，分 `raw/scored/filtered/enriched` 四个 stage 文件，支持从中间阶段续跑 |
| `errors.py` | 统一的 `HorizonMcpError`（code + message + details）异常类型 |

设计原则：① Horizon 是唯一的业务逻辑来源；② 保留分阶段落盘，支持从中间产物续跑；③ 默认无额外副作用，除非显式要求。

### 8.2 提供的 Tools / Resources

| Tool | 说明 |
|---|---|
| `hz_validate_config` | 校验 config 和必需的环境变量 |
| `hz_fetch_items` | 抓取并去重，写入 `raw` stage |
| `hz_score_items` | 对某个 stage 打分，写入 `scored` |
| `hz_filter_items` | 过滤 `scored`，写入 `filtered` |
| `hz_enrich_items` | 增强 `filtered`，写入 `enriched` |
| `hz_generate_summary` | 从某个 stage 生成 markdown 摘要 |
| `hz_run_pipeline` | 一次性跑完 fetch → score → filter → enrich → summarize |
| `hz_list_runs` / `hz_get_run_meta` / `hz_get_run_stage` / `hz_get_run_summary` | 读取历史 run 的元信息/分阶段数据/摘要 |
| `hz_get_metrics` | 读取 server 内存中的调用统计 |
| `hz_send_webhook` | 用 config 里的模板发送 webhook 通知 |

对应的 Resources（只读，URI 形式）：`horizon://server/info`、`horizon://metrics`、`horizon://runs`、`horizon://runs/{run_id}/meta`、`horizon://runs/{run_id}/items/{stage}`、`horizon://runs/{run_id}/summary/{language}`、`horizon://config/effective`。

**Tool 与 Resource 的边界**：有副作用（写文件、发网络请求）的一律是 tool；纯读取的一律是 resource，两者在 MCP 协议里语义不同，不能混用。Horizon 目前没有定义任何 **prompt**（`prompts/get` 返回的是给 LLM 的对话消息模板，Horizon 是纯数据 pipeline，用不到这个抽象）。

### 8.3 MCP 协议规则

MCP 建立在 **JSON-RPC 2.0** 之上，核心约束：

- **传输层**：Horizon 用 stdio transport——消息是换行分隔的 JSON-RPC 对象（不是 LSP 那种 `Content-Length` 头+body）；stdout 只能写协议消息，日志必须走 stderr。
- **生命周期握手**：连接建立后必须先完成握手，不能跳过直接调工具：
  ```
  client → initialize（声明 protocolVersion、capabilities）
  server → initialize 响应（声明支持 tools/resources/prompts 里的哪些）
  client → notifications/initialized（握手完成）
  ```
- **三种核心原语**：

  | 原语 | 只读/有副作用 | 发现方式 | 调用方式 |
  |---|---|---|---|
  | Tools | 可以有副作用 | `tools/list` | `tools/call` |
  | Resources | 必须只读 | `resources/list` | `resources/read` |
  | Prompts | 模板 | `prompts/list` | `prompts/get` |

- **返回结构**：`CallToolResult` 至少带 `content`（展示层）；工具若声明了输出类型（Horizon 靠 `-> dict[str, Any]` 类型标注触发），还会带 `structuredContent`（程序解析用）；失败时 `isError: true`。

**两层信封**：Horizon 的 tool 返回值有内外两层——外层 `isError`/`content` 是 MCP 协议要求的；内层 `ok`/`error.code`（`server.py` 里 `_ok`/`_err` 组装）是 Horizon 自己的业务约定。业务失败时（比如抛出 `HorizonMcpError`），协议层 `isError` 仍是 `false`（调用本身成功了），但内层 `ok:false` 携带具体错误码，调用方需要自己解析内层结构判断业务是否成功。

### 8.4 调用示例（tools / resources / prompts）

**Tool 调用**（对应 `hz_list_runs`）：
```json
→ {"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"hz_list_runs","arguments":{"limit":5}}}
← {"jsonrpc":"2.0","id":1,"result":{
    "content":[{"type":"text","text":"{\"ok\":true,\"tool\":\"hz_list_runs\",\"data\":{...}}"}],
    "structuredContent":{"ok":true,"tool":"hz_list_runs","data":{"runs":[...]}},
    "isError":false
}}
```

**Resource 读取**（对应 `horizon://server/info`）：
```json
→ {"jsonrpc":"2.0","id":2,"method":"resources/read","params":{"uri":"horizon://server/info"}}
← {"jsonrpc":"2.0","id":2,"result":{"contents":[
    {"uri":"horizon://server/info","mimeType":"application/json",
     "text":"{\"name\":\"horizon-mcp\",\"started_at\":\"...\",\"runs_root\":\"...\"}"}
]}}
```

**Prompt**（Horizon 未实现，假设加一个 `summarize_run_prompt` 说明机制）：
```json
→ {"jsonrpc":"2.0","id":3,"method":"prompts/get","params":{"name":"summarize_run_prompt","arguments":{"run_id":"run_xxx","tone":"简洁"}}}
← {"jsonrpc":"2.0","id":3,"result":{"messages":[
    {"role":"user","content":{"type":"text","text":"请用简洁的风格,总结 run_id=run_xxx 里被筛选出来的重要内容。"}}
]}}
```

Python client 端可以用官方 SDK 调用：
```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

params = StdioServerParameters(command="uv", args=["run", "horizon-mcp"], cwd="/path/to/Horizon")

async with stdio_client(params) as (read, write):
    async with ClientSession(read, write) as session:
        await session.initialize()
        result = await session.call_tool("hz_list_runs", arguments={"limit": 5})
        print(result.structuredContent)
```

### 8.5 `uv run horizon-mcp` 做了什么

`pyproject.toml` 里注册了 console script：
```toml
[project.scripts]
horizon-mcp = "src.mcp.server:main"
```
`main()` 就是 `mcp.run()`（`server.py` 末尾）。所以 `uv run horizon-mcp` = **同步依赖 + 启动 MCP server，在当前进程的 stdin/stdout 上跑 stdio transport，等待 client 发协议消息**。它不是常驻网络服务、不监听端口——正常用法是被 client **当子进程 spawn**，而不是手动在终端里一直挂着（手动跑会看到进程"卡住"，其实是在等 stdin 输入，不是卡死）。

典型 client 侧配置（如 Claude Desktop）：
```json
{
  "mcpServers": {
    "horizon": { "command": "uv", "args": ["run", "horizon-mcp"], "cwd": "/path/to/Horizon" }
  }
}
```

### 8.6 本地调用 vs 远程调用

MCP 支持两种 transport，行为差异很大：

| | stdio（本地） | Streamable HTTP / SSE（远程） |
|---|---|---|
| 连接方式 | client 直接 spawn 子进程，管道通信 | client 发 HTTP 请求到一个 URL |
| 部署形态 | 不需要单独部署，跟着 client 走 | 需要独立部署、常驻监听端口 |
| 生命周期 | 和 client 绑定，client 退出即结束 | 独立于 client，可以一直跑着 |
| 多 client | 一个进程只服务一个 client | 可以同时服务多个 client |
| Horizon 现状 | ✅ 用的这种（`mcp.run()` 默认 stdio） | ❌ 没配置 |

Horizon 目前只支持本地 stdio 这一种；如果要让远程/其他机器接入，需要显式改成 `mcp.run(transport="streamable-http")` 并部署常驻服务。

### 8.7 底层机制：为什么 `session.call_tool("hz_list_runs", ...)` 能找到并执行

这是**进程编程 + 进程间通信（IPC）**的范畴，不是 shell 编程——`stdio_client` 内部直接调用 `subprocess`（`fork()` + `pipe()` + `execve()`），完全没有 shell 参与解析命令行，管道属于 OS 提供的 IPC 机制，shell 的 `|` 语法只是这个机制的另一种使用方式。完整链路分六步：

1. **进程建立**：`stdio_client(params)` fork 子进程执行 `uv run horizon-mcp`，把子进程 stdin/stdout 接到 client 手里的两根管道（`read`/`write`）
2. **注册表建好**（发生在 server 启动、模块 import 时，早于任何调用）：`@mcp.tool()` 装饰器用 `inspect.signature()` 读取函数签名生成 JSON Schema，把 `"hz_list_runs"` 这个字符串 key 和函数对象存进内部字典——纯粹是字典查找，不是运行时反射搜索
3. **握手**：`session.initialize()` 走 8.3 节的 `initialize` → `initialized` 流程
4. **发起调用**：`call_tool()` 生成唯一请求 id，组装 `tools/call` JSON-RPC 消息写入 `write` 管道；同时在 client 内部登记 `{id: Future}`，`await` 挂起
5. **server 侧执行**：读到消息后按 `name` 字段去阶段 2 的字典查表，取出函数和 schema，校验/转换参数后真正调用 `hz_list_runs(limit=5)`，把返回值包装成 `CallToolResult` 写回 stdout
6. **响应回来**：client 后台任务读到响应，按 `id` 找到对应 Future 并唤醒，`call_tool()` 返回，`result.structuredContent` 就是最终数据

一句话：函数名从头到尾就是一个**字符串 key**，装饰器在启动时把它注册进字典，收到请求后按 key 查表直接调用——和 Flask/FastAPI 的路由表本质相同，只是传输载体是 stdio 管道而不是 HTTP。