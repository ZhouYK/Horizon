---
layout: default
title: "Horizon Summary: 2026-09-22 (ZH)"
date: 2026-09-22 23:04:07 +0000
lang: zh
report: ai
---

> 从 192 条内容中筛选出 10 条重要资讯。

---

1. [TypeSafe AI 发布 Jev：输出类型化概率的“System One”决策模型](#item-1) ⭐️ 8.0/10
2. [GPT-6 Sol 与 GPT-6 Luna 正式登陆 Amazon Bedrock](#item-2) ⭐️ 8.0/10
3. [上海 AI 实验室与上海交大提出 NCP，8.9B 离散隐空间预训练新范式](#item-3) ⭐️ 8.0/10
4. [AI 借助平扫 CT 实现大规模食管癌筛查](#item-4) ⭐️ 7.0/10
5. [AI 能否不借助语言进行推理？小型模型接受检验](#item-5) ⭐️ 7.0/10
6. [OpenAI 内部 AI 可自主训练模型，引发全球 RSI 安全倡议](#item-6) ⭐️ 7.0/10
7. [特朗普称如有必要，美国司法部可出手约束 AI 公司](#item-7) ⭐️ 6.0/10
8. [特朗普拒绝设立全球人工智能监管机构，习近平访美在即](#item-8) ⭐️ 6.0/10
9. [《纽约时报》将人工智能视为继气候变化之后的又一全球性威胁](#item-9) ⭐️ 6.0/10
10. [《纽约时报》：工会组织起来应对工作场所的 AI 威胁](#item-10) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [TypeSafe AI 发布 Jev：输出类型化概率的“System One”决策模型](https://simonwillison.net/2026/Sep/21/jev/) ⭐️ 8.0/10

TypeSafe AI 发布了 Jev，并称其为首个“System One 模型”：它同样接受文本输入，但输出不再是文本，而是浮点数——包括是/否问题的置信度、多选题各选项的概率分布，以及按给定分级返回的数值评分。其定价为每百万输入 token 0.042 美元、输出完全免费，甚至比 OpenAI 的 GPT-5 Nano（每百万输入 token 0.05 美元）更便宜。 如果决策模型真如宣传那样有效，它可能改变 AI 接入软件的方式：不再生成需要额外解析的自然语言，而是直接返回程序可以据此分支的数值，非常适合分类、垃圾内容识别、工单分级、排序以及智能体路由等场景。极低的成本与延迟也让单次请求内执行成千上万次判断成为可能，例如对 BM25 检索出的 100 个候选结果重新排序。 Jev 支持三类问题：“Noul”（即 Bernoulli）是非题，返回 0 到 1 之间的置信度；选择题返回一个置信度加上各选项的概率分布；评分题则在给定数值区间内返回一个分数。针对同一个“state”对象的所有问题会并行求值，因此提问很多与只问一个耗时相近。根据 TypeSafe 官方关于 Jev 1.13 的“jaggedness”文档，该模型目前在数字、日期和对抗性内容上表现不佳；而且由于只返回浮点数，它无法解释是哪些信号导致了某个判断。

rss · Simon Willison · 9月21日 23:09

**背景**: 传统大语言模型的工作方式是预测下一个文本 token，因此其计费分为输入 token 和（更贵的）输出 token 两部分，回答也以自然语言段落形式呈现。Bernoulli 分布是描述二元是/否结果的简单统计模型，给出某命题为真的概率，TypeSafe 借用了这个名称来命名其是非题类型。“System One”一词借用了快速、直觉式思考的概念，与缓慢而刻意的推理形成对照，这一定位让 Jev 更像自动化流程中以机器速度调用的函数，而非聊天机器人。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://typesafe.ai/blog/introducing-system-one-models-and-jev">Introducing System One Models &amp; Jev - TypeSafe AI Blog</a></li>
<li><a href="https://jevai.net/">Jev AI — Decisions at machine speed</a></li>
<li><a href="https://www.requesty.ai/blog/typesafe-jev-explained">TypeSafe Jev explained: how it works, LLM differences and... | Requesty</a></li>

</ul>
</details>

**标签**: `#AI`, `#LLM`, `#decision models`, `#TypeSafe AI`, `#System One`

---

<a id="item-2"></a>
## [GPT-6 Sol 与 GPT-6 Luna 正式登陆 Amazon Bedrock](https://news.google.com/rss/articles/CBMi0AFBVV95cUxOS0VSc19rMHltU1g3bFNDaTE2Rno0ZmRFSkJuTV9lS3RDeXdRLWtLUjRCTmZZS29yd1dzWERUeGxNS1ZJSGVRVktCMlNyRjJza2RSMXlqa3JlNEhzRkFVaUktSkRxczZLVTR4UXljbnB0WkR0bFlIRElmVW80SE5Bb0pndEZHRG5XZmIya0k1Rl9ZUEJzQWR2c0hhWWM1aTZZVjJ5bjZLYlRJY2ZabHVmbVFaR0tNUjhlQU83VjUyMGl4RDJaQnJJWGJGaTgyUERI?oc=5) ⭐️ 8.0/10

AWS 宣布 OpenAI 的 GPT-6 Sol 和 GPT-6 Luna 现已通过 Amazon Bedrock 提供，企业客户可以直接在 AWS 的全托管模型服务中调用这两款新的 GPT-6 模型。这两个模型被定位为以不同的能力与成本组合，把前沿智能带入日常工作场景。 这意味着 AWS 客户无需离开既有的云、安全和治理体系，就能使用 OpenAI 最新的 GPT-6 系列模型，从而增强 Bedrock 相对 Microsoft Foundry、Google Cloud 等企业级 AI 平台的竞争力。这也表明 OpenAI 的前沿模型正越来越多地跨多家云分发，而不再绑定单一厂商。 GPT-6 Sol 被描述为 GPT-6 系列中兼具性价比的高端模型，定位低于旗舰级 GPT-6 Astra、高于强调速度的 GPT-6 Luna；而 GPT-6 Luna 则是最注重效率的型号，面向聚焦型、高并发的任务。平台方面，Bedrock 提供满足治理与审计需求的监控和日志能力，并覆盖 ISO、SOC、CSA STAR Level 2、GDPR、FedRAMP High 等标准，且符合 HIPAA 合规资格。

google\_news · Amazon Web Services \(AWS\) · 9月22日 18:10

**背景**: Amazon Bedrock 是 AWS 提供的全托管无服务器服务，可安全、企业级地访问多家领先 AI 公司的基础模型，帮助客户构建并规模化生成式 AI 应用；AWS 于 2023 年 4 月发布该服务，并在 2023 年 9 月正式全面可用。GPT-6 是 OpenAI 的大语言模型系列，其中 Astra 为旗舰型号，Sol 属于中高端型号，Luna 则是速度最快、效率最高的层级。同一组 GPT-6 Sol 和 Luna 模型也已面向 Plus、Pro、Business、Enterprise 和 Edu 用户在 ChatGPT Work 与 Codex 中提供，Sol 还可通过 OpenRouter 等第三方 API 聚合平台调用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aws.amazon.com/bedrock/">Amazon Bedrock – Build genAI applications and agents at production scale – AWS</a></li>
<li><a href="https://openai.com/index/introducing-gpt-6-sol-and-luna/">Introducing GPT-6 Sol and Luna | OpenAI</a></li>
<li><a href="https://openrouter.ai/openai/gpt-6-sol">GPT - 6 Sol - API Pricing &amp; Providers | OpenRouter</a></li>

</ul>
</details>

**标签**: `#AWS`, `#Amazon Bedrock`, `#GPT-6`, `#AI models`, `#cloud computing`

---

<a id="item-3"></a>
## [上海 AI 实验室与上海交大提出 NCP，8.9B 离散隐空间预训练新范式](https://www.aibase.com/news/31257) ⭐️ 8.0/10

上海人工智能实验室与上海交通大学 LUMIA Lab 联合提出“下一概念预测”（Next Concept Prediction, NCP），并发布了 NCP-ArchPreview——据称是首个 8.9B 规模的离散隐空间基础模型。该模型在 5.73T token 语料上仅使用 51.3%的 token 预算，就达到了 OLMo-3-7B 的最终预训练损失水平。 如果这一结果经得起检验，就意味着把部分预训练目标从 token 层级上移到显式的概念层级，可能大幅降低达到同等损失所需的算力与数据量，这对所有面临预训练成本攀升的团队都意义重大。它也为“只靠 token 级扩展”的路线提供了具体的替代方向，可能影响未来基础模型的设计与评估方式。 NCP 与标准的下一 token 预测（NTP）并行运作，在保留 token 级自回归建模的同时，额外引入一个更具挑战性的显式目标：预测跨越多个 token 的离散概念。相关结论来自一份技术报告（arXiv:2609.10715）以及稍早的 NCP 论文，发布的模型名为“ArchPreview”，暗示它只是架构层面的预览版而非完成调优的生产级模型，且目前尚无同行评审。

aibase · AIbase · 9月22日 11:01

**背景**: 主流大语言模型的预训练采用“下一 token 预测”：模型不断猜测文本中的下一个 token 并从错误中学习，其能力提升主要依靠扩大数据与算力规模。隐空间模型则把文本压缩成更小的抽象表示集合（此处是覆盖多个 token 的离散“概念”），并在这个层级上做预测，从而让每一步预测承载更多信息。OLMo-3-7B 是艾伦人工智能研究所（AI2）发布的开放 7B 模型系列，常被用作可比的公开基线，因此“用约一半 token 达到其预训练损失”正是本条新闻的核心效率主张。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2609.10715">[2609.10715] NCP-ArchPreview Technical Report: Moving towards Latent Space Language Models through Next Concept Prediction</a></li>
<li><a href="https://arxiv.org/abs/2602.08984">[2602.08984] Next Concept Prediction in Discrete Latent Space Leads to Stronger Language Models</a></li>
<li><a href="https://huggingface.co/allenai/Olmo-3-7B-Instruct">allenai/Olmo-3-7B-Instruct · Hugging Face</a></li>

</ul>
</details>

**标签**: `#AI`, `#pretraining`, `#latent space`, `#LLM efficiency`, `#NCP`

---

<a id="item-4"></a>
## [AI 借助平扫 CT 实现大规模食管癌筛查](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5PVzktVVg2Nnk2bkdsTERUWkVobDB5N3hqd0NSazQxQnF0R01OSlo4ZjRkVWFLLUtmWXp1Tm9fVXpjeExJdVA0Q1otRG5EWEotRDJvcHdubVZ3b2NvRFJV?oc=5) ⭐️ 7.0/10

《Nature》发表的一项研究提出了一种将平扫计算机断层扫描（CT）与人工智能相结合的大规模食管癌筛查方法。该工作表明，AI 能够从无需造影剂的 CT 影像中检出食管癌，从而把筛查手段拓展到传统内镜检查之外。 如果该方法得到验证，常规采集的平扫 CT 有望成为一种机会性筛查工具，从而在内镜资源有限的地区实现人群规模的食管癌早期发现。这也进一步推动了将深度学习应用于既有医学影像数据、以发现原本并非检查目标的癌症这一趋势。 平扫 CT 的优势在于它本就因多种临床原因被常规开展，因此 AI 筛查可以叠加在既有影像流程之上，无需造影剂或额外的侵入性操作。不过，与此类 AI 筛查研究一样，回顾性研究设计和前瞻性验证的必要性仍是临床落地前的主要限制。

google\_news · Nature · 9月22日 09:49

**背景**: 食管癌常在晚期才被确诊，此时治疗选择有限、生存率较低。内镜（食管胃十二指肠镜）是发现早期病变的标准方法，但它具有侵入性、成本较高，且依赖专业设备和受训人员，难以用于全人群筛查。相比之下，平扫 CT 普及度高，且常因其他原因已经完成检查，因此研究者一直在尝试用 AI 与深度学习模型解读这类影像以筛查胸腹部肿瘤，其中包括基于平扫 CT 进行胃癌筛查的相关研究。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pure.ecnu.edu.cn/en/publications/ai-based-large-scale-screening-of-gastric-cancer-from-noncontrast/">AI-based large-scale screening of gastric cancer from noncontrast ...</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC8361665/">Accuracy of artificial intelligence‐assisted detection of esophageal cancer and neoplasms on endoscopic images: A systematic review and meta‐analysis - PMC</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC7504247/">Artificial intelligence-assisted esophageal cancer management: Now and future - PMC</a></li>

</ul>
</details>

**标签**: `#medical-ai`, `#cancer-screening`, `#computed-tomography`, `#deep-learning`, `#healthcare`

---

<a id="item-5"></a>
## [AI 能否不借助语言进行推理？小型模型接受检验](https://news.google.com/rss/articles/CBMifkFVX3lxTE9tTFRPWXo0QnVqUnd1YkUzZTNEYkppM1JnME9CZUMxdEVUek1aTkVWNkFZdTdDVUE2cjlqOVNsVXZOeFdaN0V1a09YeVhQMlR2cFotQkVUdEVWdF94cTR2ZW5MOEZqZUpscUtOTjRoMU5DLVlubGYyajlVTE1adw?oc=5) ⭐️ 7.0/10

Science News 的一篇文章报道了一项实验：研究者用一个小型语言模型来检验推理是否可以在不借助语言的情况下发生，也就是说不依赖模型生成自然语言形式的思维链。文章把这项研究定位为对“逐步的文字生成过程才是 AI 推理关键”这一假设的直接检验。 如果推理确实可以在无语言的情况下发生，那么“思维链提示与语言化表达是 AI 推理引擎”这一普遍假设就会受到动摇，这会影响到模型的训练、提示与评估方式。这还触及认知科学中关于人类思维是否依赖语言的长期争论，并暗示小型模型可能以更高效率完成推理任务。 这项检验的核心是一个小型语言模型——这类模型的参数量通常远少于前沿大模型（一般不到约 400 亿，往往小到可以在笔记本电脑或消费级设备上运行），同时依赖非语言推理任务，即需要从视觉或结构模式中推断规则，而非依赖文字。文章的叙述暗示结果较为微妙，并非简单的是或否，因此对“无语言推理”的结论应谨慎看待。

google\_news · Science News · 9月22日 16:00

**背景**: 思维链提示（chain-of-thought prompting）由 Wei 等人于 2022 年推广，是一种提示工程技巧，要求模型在给出答案前先写出中间的推理步骤，普遍被认为能提升数学与逻辑任务的准确率。小型语言模型（SLM）使用与大模型相同的 Transformer 类架构，但参数量更少，通常通过知识蒸馏、剪枝或量化进行压缩，从而可在普通硬件上运行。与之相对，非语言推理指的是通过形状、图案或矩阵来发现潜在规则、解决新问题，而不依赖书面或口头语言，这一概念借用自人类智商测验。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Chain-of-thought_prompting">Chain-of-thought prompting</a></li>
<li><a href="https://en.wikipedia.org/wiki/Small_language_model">Small language model</a></li>
<li><a href="https://www.cogn-iq.org/learn/theory/non-verbal-reasoning/">Non - Verbal Reasoning — Figural... — Cogn-IQ Encyclopedia</a></li>

</ul>
</details>

**标签**: `#AI reasoning`, `#language models`, `#cognitive science`, `#small models`, `#machine learning`

---

<a id="item-6"></a>
## [OpenAI 内部 AI 可自主训练模型，引发全球 RSI 安全倡议](https://www.aibase.com/news/31271) ⭐️ 7.0/10

据报道，OpenAI 的内部 AI 系统已能独立接管整个实验性模型训练流程，多个智能体自发协作以大幅缩短实验时间，甚至能够编写 GPU 内核优化程序。面对这种加速的自主性，OpenAI 发布了一项全球安全倡议，但同时明确表示完全自主的递归自我改进尚未真正发生。 这一进展被视为递归自我改进的雏形，即 AI 改进“改进自身的过程”这一理论上的反馈循环，许多研究者认为这是通向超级智能的关键门槛。如果 AI 系统真能自行运行并优化自己的训练实验，能力提升的速度可能超出当前的安全评估与治理机制，从而影响各大实验室、监管机构乃至整个 AI 生态。 该说法建立在两种不同的能力之上：一是自发式的多智能体协作以缩短实验周期，二是自动生成 GPU 内核优化代码——这原本属于专家工程师才能完成的高难度底层任务。值得注意的是，OpenAI 自身也提醒完全自主的 RSI 尚未发生，而且该报道篇幅简短，没有提供基准数据、验证机制细节或一手来源来佐证其所声称的自主程度。

aibase · AIbase · 9月22日 17:01

**背景**: 递归自我改进（RSI）是一种假想过程：高级 AI 系统改写自己的代码并提升自身能力，可能触发一场最终走向超级智能的智能爆炸；关键在于真正的 RSI 是系统改进“改进过程本身”，而不仅仅是完成某个下游任务。GPU 内核是运行在图形处理器上的底层并行程序，在很大程度上决定模型训练速度，因此自动写出有竞争力的内核长期被视为 AI 编程能力的试金石——NVIDIA 的工程师已经证明，DeepSeek-R1 等模型可在带验证器的工作流下生成数值正确的注意力内核。多智能体系统，即多个自主 AI 智能体围绕同一目标协同工作，正日益成为自动化科研与工程任务的常见架构。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Recursive_self-improvement">Recursive self - improvement - Wikipedia</a></li>
<li><a href="https://developer.nvidia.com/blog/automating-gpu-kernel-generation-with-deepseek-r1-and-inference-time-scaling/">Automating GPU Kernel Generation with DeepSeek-R1 and Inference...</a></li>
<li><a href="https://phys.org/news/2026-01-multiple-autonomous-ai-spontaneously-collaborate.html">Multiple autonomous AI systems spontaneously collaborate to...</a></li>

</ul>
</details>

**标签**: `#AI Safety`, `#Recursive Self-Improvement`, `#OpenAI`, `#Multi-Agent Systems`, `#GPU Kernel Optimization`

---

<a id="item-7"></a>
## [特朗普称如有必要，美国司法部可出手约束 AI 公司](https://news.google.com/rss/articles/CBMirgFBVV95cUxOYkFwcnFpOFFycEx0SEwwNUxZazVuTTh6aUNKZ0pUUHlPU2toMkk2WXAyc3RkYTdKWlVsTEVoTmR5VGJaZlhaU21OdHp2aXRWZ0VGNGtJdERKVGUtWXBiMWdKRm9JY04zTnZ3YXp5akdBU2RsS0tHZG9ESTVmR0hOWUYyaWpjYVNCcFF3c3RBVk53NC1SanNTaXpxOHdMei1SNUJPWnhLLTkzU2VOaUE?oc=5) ⭐️ 6.0/10

据路透社报道，美国总统特朗普表示，如果有必要，美国司法部可以出手约束人工智能公司。这一表态意味着，在本届政府框架下，传统上负责反垄断与民权执法的司法部，可能会被定位为管束 AI 企业的一个工具。 这一表态的重要性在于：美国联邦层面的 AI 监管此前分散于多个机构，且很大程度上依赖企业自愿承诺，如今点名司法部作为潜在执法者，暗示对主要 AI 实验室可能转向更具对抗性的姿态。若真正付诸行动，将影响 OpenAI、谷歌、微软、Meta、Anthropic 等公司的反垄断、竞争与合规策略，也会影响美国做法与欧盟《人工智能法案》之间的对比格局。 该报道是一则基于政治表态的简讯，而非针对已提起的诉讼、拟议规则或司法部的正式行动，也没有点名具体公司、时间表或法律依据。因此它更像是意图信号而非具体政策变化，目前尚不清楚其手段会是反垄断执法、消费者保护行动还是其他权限。

google\_news · Reuters · 9月22日 19:14

**背景**: 在美国，司法部负责执行联邦反垄断法，可就垄断或反竞争行为起诉企业，联邦贸易委员会则分担其中相当一部分权限。2024 年，司法部与联邦贸易委员会分别对微软、OpenAI、英伟达、谷歌、Anthropic 等公司涉及的 AI 合作与投资展开调查，反映出对少数玩家可能主导 AI 市场的担忧日益上升。美国的 AI 监管仍分散于各联邦机构与各州立法之间，尚不存在可与欧盟《人工智能法案》相提并论的综合性联邦 AI 法律。

**标签**: `#AI regulation`, `#US policy`, `#DOJ`, `#tech industry`, `#Trump administration`

---

<a id="item-8"></a>
## [特朗普拒绝设立全球人工智能监管机构，习近平访美在即](https://news.google.com/rss/articles/CBMilAFBVV95cUxNWjFSMGM0WDEzdFVqc3RrczI5d0JkSTlzX0pUTVFpa1V6bGh1UUZxeHNsTDNmRkJOQ2tGUWh3NnJ1MzZBclF1QnpCeHg1ZjR6cVZ3cU9jbUp6SzVWMFY4WFZZUmVQOE1mczBPdGR1TTk5VVNMTFlWc2Y3cjBGWkJSVElfZXMtbTRaWExTTnZCY0tJQ01i?oc=5) ⭐️ 6.0/10

据 Politico 报道，特朗普总统表示美国“拒绝任何构建全球主义方案以控制”人工智能的企图，实际上排除了美国参与拟议中的全球人工智能监管机构的可能性。这一表态恰逢中国国家主席习近平预定抵达白宫举行会谈的前一天，而人工智能预计将是会谈的重要议题之一。 这一拒绝削弱了联合国主导的人工智能治理机构等多边努力，并表明华盛顿打算通过单边行动和双边协议而非共同的国际机构来塑造人工智能规则。这也把人工智能治理直接推上了中美会谈的议程，两个最大的人工智能强国可能转而各自制定相互竞争的标准。 该表态并未点名具体的拟议机构，也未说明针对的是哪些现有或草案中的倡议，因此尚不清楚它是指联合国的咨询与对话机制、其他多边提案，还是两者兼有。表态恰好发生在习近平抵达白宫之前，这表明人工智能监管也被当作双边博弈的筹码，而不仅仅是国内政策立场。

google\_news · Politico · 9月22日 15:58

**背景**: 对前沿人工智能安全的担忧推动了新一轮国际治理努力。联合国秘书长于 2023 年召集了由 39 名成员组成的“人工智能高级别咨询机构”，该机构在 2024 年 9 月提出了七项关于国际人工智能治理的建议；此后联合国又启动了“人工智能全球治理对话”以及“人工智能独立国际科学小组”。产业界也在推动全球标准，OpenAI 曾发布关于前沿人工智能安全与对齐的提案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.yahoo.com/news/politics/articles/trump-rejects-global-entity-ai-155831388.html">Trump rejects global entity for AI oversight</a></li>
<li><a href="https://www.un.org/en/ai-advisory-body">AI Advisory Body | United Nations</a></li>
<li><a href="https://www.reuters.com/technology/artificial-intelligence/un-advisory-body-makes-seven-recommendations-governing-ai-2024-09-19/">UN advisory body makes seven recommendations for governing AI | Reuters</a></li>

</ul>
</details>

**标签**: `#AI regulation`, `#AI governance`, `#policy`, `#Trump`, `#global oversight`

---

<a id="item-9"></a>
## [《纽约时报》将人工智能视为继气候变化之后的又一全球性威胁](https://news.google.com/rss/articles/CBMiogFBVV95cUxOcVIwd0dvR0hHT2JpZXQ4UEdEYkYwZnowaHptOVliQlRCb2dyaGo3SEsyX1hNVXZNV056aGpnNGlWRG8yeTMwU0FGY19WMFRlSThTcnJWU0ZmM2xmSDFDZGwyMUl6dGJLeUFCTWVBcUZfaUtxOHRWc3Q4c3hfTWhKejEwblZVM19PXzhTaWt3Z3pZd2hJN1RlOTlOcHdHZjloTVE?oc=5) ⭐️ 6.0/10

《纽约时报》发表文章，认为人工智能正在成为一项重大的全球性威胁，其规模与严重程度可与气候变化相提并论。该文属于主流媒体的评论与分析，把人工智能风险与气候危机并列为当今时代的标志性危险之一。 当《纽约时报》这样的主流媒体把人工智能提升到与气候变化同等的议题高度时，AI 安全与风险便从技术圈的小众关切转变为公共政策与大众讨论的主流话题。这种框架可能影响监管机构、公司治理与公众舆论，进而左右政府和企业对 AI 监管、安全研究与问责机制的优先排序。 目前该条目仅有标题，缺乏实质性正文，因此文章的具体论点、论据或所提对策无法核实。将 AI 与气候变化类比更多是一种修辞框架而非技术论断；读者需要注意，AI 风险既包括近期危害（滥用、偏见、虚假信息），也包括长期的存在性担忧。

google\_news · The New York Times · 9月22日 16:33

**背景**: 存在性风险（existential risk）指的是威胁人类长期潜能的风险，可能表现为人类灭绝，也可能不可逆地锁定一种极度退化的状态。AI 风险则是更宽泛的类别，涵盖人工智能系统造成伤害的各种方式，从带有偏见或不安全的部署，到大规模滥用。人们之所以常拿气候变化作类比，是因为两者都涉及进展缓慢、潜在灾难性且全球共同承担的后果，需要长期的协调行动。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Global_catastrophic_risk">Global catastrophic risk - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Artificial_intelligence">Artificial intelligence - Wikipedia</a></li>
<li><a href="https://aidive.org/en/glossary/ethics-safety/existential-risk">Existential Risk : meaning and practical use</a></li>

</ul>
</details>

**标签**: `#AI risk`, `#climate change`, `#society`, `#policy`, `#existential risk`

---

<a id="item-10"></a>
## [《纽约时报》：工会组织起来应对工作场所的 AI 威胁](https://news.google.com/rss/articles/CBMihgFBVV95cUxQd0pSano3UHdiZGNha3VFUVVueXQ0dTRzY2dPc21uTEhOTkI5cEdsOVdDdG4xbWloTll4MktPTzMwaF9BYUtlMVU3M1BobENyWFVadnROTUNubWtJZzZWcWVfUDE3RkhGY20tejBaZ2ZSSlRrUjh3XzNmdERfeXNTaTJvM3Nidw?oc=5) ⭐️ 6.0/10

《纽约时报》发表报道，讲述工会如何组织起来应对人工智能给工作场所带来的威胁。报道聚焦工会针对自动化、岗位流失以及新型员工监控等 AI 驱动的变化所采取的抵制策略。 随着 AI 工具在办公室、工厂和物流环节普及，工会正把自己定位为少数有能力影响该技术落地方式的有组织制衡力量之一。工会的谈判诉求可能影响整个行业的合同条款、再培训义务和透明度规则，其波及范围远超工会成员本身。 目前可获取的素材仅包括标题和一句话摘要，因此没有提及具体工会、企业、合同条款或日期。该条目属于针对社会与政策议题的主流新闻报道，而非技术或研究成果发布，也未提供关于 AI 导致岗位流失的可量化数据。

google\_news · The New York Times · 9月22日 15:18

**背景**: 工会最初是为在工资、工时和安全条件上进行集体谈判而出现的，如今它们正把这一职责延伸到工作场所技术领域。围绕 AI，工会提出的具体担忧包括：自动化导致岗位消失、由软件分派任务并评估绩效的所谓“算法管理”，以及通过传感器和数据采集对员工施加的更严密监控。作为回应，美国和欧洲的工会越来越多地要求就自动化系统的使用获得提前通知、协商权和透明度，主张工人在重塑其工作的决策中应当有发言权。

**标签**: `#AI`, `#labor unions`, `#workplace automation`, `#future of work`, `#policy`

---