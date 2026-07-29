---
layout: default
title: "Horizon Summary: 2026-07-29 (ZH)"
date: 2026-07-29
lang: zh
report: ai
---

> 从 334 条内容中筛选出 10 条重要资讯。

---

1. [谷歌 DeepMind 解散诺贝尔奖得主 AlphaFold 团队](#item-1) ⭐️ 9.0/10
2. [Word Copilot 中的自复制提示注入蠕虫](#item-2) ⭐️ 8.0/10
3. [AI 发现 HAWK 和弱 AES 的密码学缺陷](#item-3) ⭐️ 8.0/10
4. [自主 AI：责任谁来承担？](#item-4) ⭐️ 8.0/10
5. [微软 Azure 年收入突破 1000 亿美元](#item-5) ⭐️ 8.0/10
6. [MCP 协议 v5 重大改版：无状态、自适应无服务器](#item-6) ⭐️ 8.0/10
7. [亚马逊暂停 Nova 模型开发，转向第三方模型集成](#item-7) ⭐️ 8.0/10
8. [ChatGPT 禁止模仿在世作者风格以规避版权风险](#item-8) ⭐️ 8.0/10
9. [超 1100 名 AI 员工呼吁放缓，奥特曼罕见支持](#item-9) ⭐️ 8.0/10
10. [苹果首次在安全更新中致谢 AI](#item-10) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [谷歌 DeepMind 解散诺贝尔奖得主 AlphaFold 团队](https://www.aibase.com/news/29980) ⭐️ 9.0/10

谷歌 DeepMind 悄然解散了获得诺贝尔奖的 AlphaFold 团队，将包括核心作者在内的关键研究人员重新分配到其他项目，重点转向 Gemini AI 模型。 这一战略转变表明谷歌优先发展 Gemini 项目而非基础生物学研究，可能会减缓计算生物学的进展，同时加速 AI 领域的竞争。 AlphaFold 为 Demis Hassabis 和 John Jumper 赢得了 2024 年诺贝尔化学奖，但过去一年里大部分原始论文作者已被重新分配。谷歌计划在 2026 年前完全关闭 AlphaFold 项目。

aibase · AIbase · 7月29日 16:06

**背景**: AlphaFold 是 DeepMind 开发的 AI 系统，能从氨基酸序列预测蛋白质三维结构，在 CASP 竞赛中取得突破性精度。其第三版 AlphaFold 3 将预测扩展到蛋白质与 DNA、RNA 及配体的相互作用。Gemini 是谷歌的旗舰多模态 AI 模型系列，于 2023 年 12 月首次发布，已整合到谷歌各项产品中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AlphaFold">AlphaFold</a></li>
<li><a href="https://en.wikipedia.org/wiki/Google_Gemini">Google Gemini - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AlphaFold`, `#Google DeepMind`, `#Gemini`, `#AI research team restructuring`, `#Nobel Prize`

---

<a id="item-2"></a>
## [Word Copilot 中的自复制提示注入蠕虫](https://simonwillison.net/2026/Jul/29/ai-worming-through-word/#atom-everything) ⭐️ 8.0/10

安全研究员 Håkon Måløy 发现了一种方法，将针对 Microsoft Word 的 Copilot 的提示注入攻击转化为自复制蠕虫，通过在文档中嵌入隐藏指令，在 Copilot 处理文档时将其传播到新文档。 这标志着首个自复制提示注入蠕虫的出现，展示了 AI 集成生产力工具面临的新型安全风险，可能在没有攻击者干预的情况下实现大规模自动化攻击。 该攻击使用隐藏文本（例如白底白字）作为指令，Copilot 将其解释为命令并复制到输出文档中。研究人员已向微软负责任地披露，至今已有 144 天，但尚未发布完整的缓解措施。

rss · Simon Willison · 7月29日 18:43

**背景**: 提示注入是一种网络安全利用手段，通过看似无害的输入导致大型语言模型（LLM）产生意外行为。间接提示注入将对抗性提示嵌入到 LLM 检索的内容（如网页）中。此攻击将该概念扩展到通过文档工作流进行自复制，利用 Copilot 无法区分用户命令与文档内容的弱点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection_attack">Prompt injection attack</a></li>

</ul>
</details>

**标签**: `#prompt injection`, `#security`, `#AI`, `#Microsoft Word`, `#self-replicating worm`

---

<a id="item-3"></a>
## [AI 发现 HAWK 和弱 AES 的密码学缺陷](https://simonwillison.net/2026/Jul/28/discovering-cryptographic-weaknesses-with-claude/#atom-everything) ⭐️ 8.0/10

Anthropic 的研究人员使用其 Claude Mythos AI 模型发现了 HAWK 密码协议和 AES-128 简化轮变体的数学缺陷，相关工作已在一篇新论文和配套代码仓库中公开。 这表明先进的 LLM 能够辅助密码学研究，可能加速漏洞发现，尽管所发现的缺陷对现有系统没有实际影响。 Claude Mythos 预览版模型运行了 60 小时，估计 API 成本为 10 万美元，研究人员通过精心设计的提示词鼓励模型坚持并找到可发表的结果。

rss · Simon Willison · 7月28日 22:45

**背景**: Claude Mythos 是 Anthropic 最强大的 LLM 系列，因安全问题未公开发布。HAWK 是一种用于隐私保护智能合约的密码协议，而 AES-128 简化轮变体是用于分析研究的弱化版本。该研究是与多所大学合作进行的。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Mythos">Claude Mythos</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#AI research`, `#prompt engineering`, `#security`, `#Claude`

---

<a id="item-4"></a>
## [自主 AI：责任谁来承担？](https://news.google.com/rss/articles/CBMiakFVX3lxTFBlVnBhYnNPYjVqX0pnSTRwdThUYXJQUnZsZ0ZuRnlDZHRIS1piWl9fTU1oS0xBeGR2dU56X2FMYVhpbG1RQkZzY1ZRLXRzNzhpSk5MTms1aW5CV05BUVRIeWVTbmVqTVhBbXc?oc=5) ⭐️ 8.0/10

《ACM 通讯》的一篇文章探讨了自主 AI 系统中的责任问题，这类系统能够自主执行多步骤任务，文章提出了一个关键问题：当这些系统造成损害时，谁应该承担责任？ 随着组织越来越多地部署无需人类监督就能做出决策的自主 AI 代理，建立清晰的责任框架对于法律责任、道德治理和公众信任至关重要。 该文章基于麦肯锡提出的“决策权转移”概念，并讨论了自主性-责任悖论：即使系统自主行动，人类仍需对结果承担法律和道德责任。

google\_news · Communications of the ACM · 7月29日 20:30

**背景**: 自主 AI 是指能够自主规划、使用工具并采取行动以完成目标的系统，无需人类逐步批准，这与传统的单轮 AI 不同。自主性-责任悖论源于：尽管 AI 系统独立行动，人类仍需对其行为承担法律和道德责任。这种不一致迫使企业重新思考治理和问责框架。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ibm.com/think/insights/autonomy-without-accountability">Autonomy without accountability | IBM</a></li>
<li><a href="https://atvais.com/autonomy-accountability-paradox/">The Autonomy Accountability Paradox - atvais.com</a></li>
<li><a href="https://remolda.com/en/glossary/agentic-ai">Agentic AI — definition | Remolda</a></li>

</ul>
</details>

**标签**: `#AI ethics`, `#agentic AI`, `#accountability`, `#AI governance`

---

<a id="item-5"></a>
## [微软 Azure 年收入突破 1000 亿美元](https://news.google.com/rss/articles/CBMitwFBVV95cUxPQ3gtNkFkdUk3ck5PdGZTVkI0eHhGTk56UkZWZzhqdzE5RWl4cVF2UjFJb19pTGFkYkdQWEFyRWZzcDF0aThvMnYxRk1nQWMwYVFCZEJNSXFkZFZ3NlBzS3BoeHFva2UtSXd4cENYUGo0V0hPdjJzYWhSamFJRDMzQkpLMm5FM2NIYVNkXzFaWl9pZmY1ZGlmWTNuWXdwang0Z2xnWTBzMHdrWGVCTGpLR3haZzhVcTQ?oc=5) ⭐️ 8.0/10

微软 Azure 年收入首次突破 1000 亿美元，同时创纪录的 AI 支出导致现金流减少。 这一里程碑凸显了 Azure 在云计算领域的主导地位，以及维持增长所需的大规模 AI 基础设施投资。 微软报告利润增长 31.6%，同时收入实现突破，但 AI 支出达到创纪录水平，影响了自由现金流。

google\_news · GeekWire · 7月29日 20:51

**背景**: Azure 是微软的云计算平台，与亚马逊 AWS 和谷歌云竞争。1000 亿美元的收入里程碑凸显了云服务和 AI 工作负载的快速普及。

**标签**: `#Microsoft Azure`, `#cloud computing`, `#AI infrastructure`, `#financial performance`

---

<a id="item-6"></a>
## [MCP 协议 v5 重大改版：无状态、自适应无服务器](https://www.aibase.com/news/29983) ⭐️ 8.0/10

Anthropic 发布了模型上下文协议（MCP）的第 5 版，转为无状态架构，不再需要客户端与服务器之间的持久连接，完全重构了底层通信机制。 这是 MCP 自创建以来最具颠覆性的修订，实现了 AI 工具集成的更好可扩展性和灵活性，尤其适合无服务器环境，可能加速整个 AI 生态系统的采用。 无状态架构消除了持久连接，每个请求独立，简化了部署并降低了资源开销，使 MCP 更能适应无服务器计算模型。

aibase · AIbase · 7月29日 18:06

**背景**: 模型上下文协议（MCP）是 Anthropic 于 2024 年 11 月推出的开放标准，旨在标准化 AI 系统（如大语言模型）与外部工具和数据的集成方式。它提供了统一的接口用于读取文件、执行函数和处理上下文，已被 OpenAI 和 Google DeepMind 等主要 AI 提供商采用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol</a></li>
<li><a href="https://grokipedia.com/page/model-context-protocol">Model Context Protocol</a></li>
<li><a href="https://modelcontextprotocol.io/">What is the Model Context Protocol (MCP)? - Model Context Protocol</a></li>

</ul>
</details>

**标签**: `#MCP`, `#protocol`, `#Anthropic`, `#stateless architecture`, `#AI`

---

<a id="item-7"></a>
## [亚马逊暂停 Nova 模型开发，转向第三方模型集成](https://www.aibase.com/news/29978) ⭐️ 8.0/10

亚马逊已暂停大部分 Nova 模型的开发，包括旗舰模型和视频/图像生成器，并将资源转向通过 Amazon Athena 平台集成第三方模型。该公司还解散了 AGI 部门并关闭了相关实验室。 这一战略转向凸显了云提供商在开发前沿模型方面难以与专业 AI 实验室竞争。它标志着从专有模型开发转向构建多模型集成基础设施，可能重塑 AI 平台市场。 现有 Nova 客户将继续获得维护支持，但不会开发新功能。亚马逊的新重点是 Athena，一个统一平台，用于集成来自 Anthropic 等合作伙伴的尖端模型。

aibase · AIbase · 7月29日 15:06

**背景**: Amazon Nova 是通过 AWS Bedrock 提供的基础模型组合，涵盖文本和多模态需求。Amazon Athena 原本是一个用于分析的无服务器查询服务，但亚马逊正将其重塑为集成第三方模型的 AI 平台。AGI 部门是专注于通用人工智能研究的独立单元。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.aboutamazon.com/news/aws/amazon-nova-artificial-intelligence-bedrock-aws">Amazon Nova : Meet our new foundation models in Amazon Bedrock</a></li>
<li><a href="https://hrme.economictimes.indiatimes.com/news/industry/amazon-cuts-jobs-in-agi-division-while-boosting-ai-investments/132575991">Amazon Cuts Jobs in AGI Division While Boosting AI Investments...</a></li>

</ul>
</details>

**标签**: `#AI strategy`, `#Amazon`, `#Nova models`, `#infrastructure`, `#model integration`

---

<a id="item-8"></a>
## [ChatGPT 禁止模仿在世作者风格以规避版权风险](https://www.aibase.com/news/29973) ⭐️ 8.0/10

OpenAI 悄悄更新了 ChatGPT 的规则，禁止模仿在世作者的独特风格，拒绝模仿开头、改编经典或使用风格特征的请求。此更改旨在规避版权风险，并已被确认生效。 这一政策变化影响了许多依赖 ChatGPT 进行创意写作或风格模仿的用户，可能限制其在内容创作中的实用性。同时，它突显了 AI 生成内容中日益增长的版权担忧，可能影响未来的法规和平台政策。 该限制特别适用于在世作者；已故作者可能仍可被模仿。此项更改是悄然实施的，没有公开宣布，并且影响各种形式的风格模仿，包括语气、句子结构和词汇模式。

aibase · AIbase · 7月29日 15:06

**背景**: ChatGPT 是 OpenAI 开发的大型语言模型，能够根据提示生成文本。版权法保护原创表达，模仿作者的独特风格如果存在实质性相似可能构成侵权。OpenAI 曾因版权问题面临诉讼，促使公司采取主动措施。

**标签**: `#ChatGPT`, `#OpenAI`, `#copyright`, `#AI policy`, `#writing style`

---

<a id="item-9"></a>
## [超 1100 名 AI 员工呼吁放缓，奥特曼罕见支持](https://www.aibase.com/news/29972) ⭐️ 8.0/10

来自 OpenAI、Anthropic、谷歌和 Meta 等顶级 AI 公司的超过 1100 名员工签署了一封公开信，敦促美国政府放缓 AI 开发并支持国际治理，OpenAI CEO Sam Altman 罕见地公开表示支持。 这场前所未有的全行业担忧表态表明，AI 开发者之间对监管和安全措施的共识日益增强，可能影响美国政策及全球 AI 治理讨论。 这项名为&\#x27;Steering the Frontier&\#x27;的倡议收集了 1134 个签名，并明确呼吁必要时有意放缓；Anthropic 的 CEO 和联合创始人也在签名之列，凸显了广泛的行业共识。

aibase · AIbase · 7月29日 14:06

**背景**: 这封公开信反映了关于 AI 安全和发展速度的持续辩论。行业领导者此前曾对不受控制的 AI 研究和缺乏国际协调等风险表示担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://the-decoder.com/frontier-ai-developers-urge-international-coordination-to-pace-automated-research-before-capabilities-outstrip-control/">Frontier AI developers urge international coordination to pace automated research before capabilities outstrip control</a></li>

</ul>
</details>

**标签**: `#AI Safety`, `#Regulation`, `#OpenAI`, `#Anthropic`, `#Policy`

---

<a id="item-10"></a>
## [苹果首次在安全更新中致谢 AI](https://www.aibase.com/news/29970) ⭐️ 8.0/10

苹果首次在安全更新中致谢包括 Anthropic 的 Claude 和 OpenAI 的 Codex Security 在内的 AI 模型，感谢它们发现多个漏洞。 这标志着 AI 在网络安全领域整合的一个里程碑，表明科技巨头现在依赖 AI 进行漏洞研究和操作系统加固。 苹果此次更新致谢了 Anthropic 的 Claude、OpenAI 的 Codex Security 以及 NVIDIA 的 AI 红队协助修复多个漏洞。这是苹果首次在安全公告中致谢 AI。

aibase · AIbase · 7月29日 12:06

**背景**: 像 Anthropic 的 Claude 和 OpenAI 的 Codex Security 这样的 AI 模型越来越多地被用于代码分析和漏洞检测。Claude 是一种使用宪法 AI 训练的大型语言模型，而 Codex Security 是一种 AI 驱动的应用安全代理，能够扫描 GitHub 仓库以发现安全问题。苹果的致谢表明对 AI 辅助安全研究的信任日益增强。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_%28AI%29">Claude (AI) - Wikipedia</a></li>
<li><a href="https://grokipedia.com/page/Codex_Security_OpenAI">Codex Security (OpenAI)</a></li>
<li><a href="https://github.com/openai/codex-security">GitHub - openai / codex - security : SDKs and CLI for Codex Security</a></li>

</ul>
</details>

**标签**: `#AI security`, `#Apple`, `#vulnerability detection`, `#Claude`, `#Codex`

---