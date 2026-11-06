---
layout: default
title: "Horizon Summary: 2026-11-06 (EN)"
date: 2026-11-06 23:04:08 +0000
lang: en
report: default
---

> From 199 items, 13 important content pieces were selected

---

1. [Baidu open-sources ERNIE 5.5 Flash Base, a 280B MoE model](#item-1) ⭐️ 8.0/10
2. [Moonshot AI reportedly negotiating to rent 8,000+ Nvidia Blackwell GPUs in Europe](#item-2) ⭐️ 7.0/10
3. [YMTC&\#x27;s Fourth Wuhan Fab Targets Up to 70% Domestic Equipment for 300-Layer NAND](#item-3) ⭐️ 7.0/10
4. [Taobao MNN team open-sources 0.3B on-device language model](#item-4) ⭐️ 7.0/10
5. [Anthropic&\#x27;s Claude Can Now Read Your Bank Accounts via Plaid](#item-5) ⭐️ 6.0/10
6. [India Targets Homegrown GPU in 24 Months, Aims to Commercialize RISC-V Chips](#item-6) ⭐️ 6.0/10
7. [China&\#x27;s NRTA Backs Live-Action Micro-Dramas, Tightens AI Rules](#item-7) ⭐️ 6.0/10
8. [China pushes embodied AI into elderly care with new six-department policy](#item-8) ⭐️ 6.0/10
9. [Tesla to wind down Cybertruck production by mid-next year](#item-9) ⭐️ 6.0/10
10. [EU Charges TikTok&\#x27;s Recommendation Algorithm With Harmful &\#x27;Rabbit Hole&\#x27; Effects](#item-10) ⭐️ 6.0/10
11. [Researcher finds ~100,000 words Apple&\#x27;s iPhone keyboard won&\#x27;t suggest](#item-11) ⭐️ 6.0/10
12. [Telegram 13.2 lets bots run interactive HTML/CSS/JS messages inside chats](#item-12) ⭐️ 6.0/10
13. [US DOJ&\#x27;s Super Intelligence Task Force Officially Goes Live](#item-13) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Baidu open-sources ERNIE 5.5 Flash Base, a 280B MoE model](https://www.news.cn/info/20261105/f3bbdb6854f5441ca9fb34062f213875/c.html) ⭐️ 8.0/10

Baidu has officially open-sourced ERNIE 5.5 Flash Base, a Mixture-of-Experts foundation model with 280 billion total parameters that activates 14 billion parameters per token. It was pretrained on 33.5 trillion tokens with a 128K pretraining context, while fine-tuning and inference support contexts of up to 1 million tokens. This is one of the largest open-weight foundation models released by a Chinese lab, and its 20:1 ratio of total to active parameters means developers get the capacity of a 280B-class model at roughly the inference cost of a 14B dense one. It strengthens the open-source MoE camp — alongside releases such as Mistral&\#x27;s Mixtral and DeepSeek&\#x27;s models — and gives teams a new option for building long-document and agentic applications. Baidu says the model was systematically optimized around efficiency, specifically in its attention mechanism, expert routing, and training objectives. Note the gap between the 128K pretraining context and the 1M-token figure, which applies only to fine-tuning and inference; long-context claims of this scale often come with degraded retrieval accuracy and much higher memory cost in practice.

telegram · zaihuapd · Nov 6, 05:41

**Background**: Mixture-of-Experts \(MoE\) models replace a single dense feed-forward layer with many smaller &quot;expert&quot; subnetworks plus a router that sends each token to only a few of them, so total parameter count can grow dramatically while per-token compute stays modest. This is why MoE models are described with two numbers: total parameters, which govern how much GPU memory is needed to hold the weights, and active parameters, which govern speed and inference cost. Long context windows, meanwhile, have become a headline metric in the LLM market, letting users feed entire codebases or document sets into a single prompt. A &quot;Base&quot; model is the raw pretrained checkpoint before instruction tuning or alignment, intended for developers to fine-tune rather than use directly.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://krunalkanojiya.com/blog/why-1m-tokens-is-a-trap">Why 1 M - Token Context Windows Can Be a Trap | Krunal Kanojiya</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#MoE`, `#open-source`, `#Baidu ERNIE`, `#long context`

---

<a id="item-2"></a>
## [Moonshot AI reportedly negotiating to rent 8,000+ Nvidia Blackwell GPUs in Europe](https://www.cnbc.com/2026/11/05/moonshot-ai-nvidia-chips-europe-china.html) ⭐️ 7.0/10

Moonshot AI is reportedly in talks with European neocloud providers to rent more than 8,000 Nvidia Blackwell GPUs, primarily for inference but also for some training work, according to people familiar with the matter cited by CNBC. The arrangement would reportedly require Moonshot to pay a 30% to 50% prepayment premium compared with non-Chinese buyers. The deal illustrates how US export controls are pushing Chinese AI labs toward offshore compute rather than blocking them outright, effectively rerouting demand for Nvidia&\#x27;s top-end chips through third-party clouds. If such arrangements become common, they could reshape the economics of global GPU capacity, raise compliance risk for European neoclouds, and widen the cost gap between Chinese and Western AI developers. The order is unusually large for a rental arrangement and is weighted toward inference, the ongoing serving of a trained model, rather than training runs. The reported 30–50% prepayment premium suggests providers are pricing in regulatory and reputational risk, and the White House said in July that Moonshot had previously obtained Blackwell chips through Thai facilities — a detail likely to intensify scrutiny of the new European route.

telegram · zaihuapd · Nov 6, 05:02

**Background**: Blackwell is Nvidia&\#x27;s GPU microarchitecture succeeding Hopper, and it is the hardware most in demand for large-scale generative AI workloads; US export controls bar selling it directly to China. Neoclouds are specialized GPU-as-a-Service providers that rent out AI accelerators with faster provisioning and simpler infrastructure than hyperscalers, which makes them plausible partners for overseas customers. Inference, the phase where a trained model answers real requests, is the dominant ongoing cost for a consumer AI product like Moonshot&\#x27;s Kimi, while training is the far more compute-intensive process of building the model itself.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Blackwell_%28microarchitecture%29">Blackwell (microarchitecture) - Wikipedia</a></li>
<li><a href="https://www.thundercompute.com/blog/neoclouds-the-new-gpu-clouds-changing-ai-infrastructure">What is a Neocloud ? The Rise of GPU-only Clouds (September 2026)</a></li>
<li><a href="https://www.ibm.com/think/topics/ai-inference">What is AI inference? - IBM</a></li>

</ul>
</details>

**Tags**: `#AI infrastructure`, `#Nvidia`, `#export controls`, `#Moonshot AI`, `#GPU compute`

---

<a id="item-3"></a>
## [YMTC&\#x27;s Fourth Wuhan Fab Targets Up to 70% Domestic Equipment for 300-Layer NAND](https://www.reuters.com/world/china/chinas-top-flash-memory-chipmaker-targets-more-homegrown-tools-new-factory-2026-11-06/) ⭐️ 7.0/10

Yangtze Memory Technologies \(YMTC\) plans to build a fourth fab in Wuhan, with construction expected to begin in 2027, and aims to source at least 60% — and as much as 70% — of its production equipment domestically, up from over 50% at its third fab. The new plant is intended to produce advanced NAND flash with more than 300 layers, aimed primarily at datacenter and AI storage demand. This is one of the clearest signals yet that US export controls are pushing China&\#x27;s memory industry toward a self-contained supply chain: if YMTC can equip a leading-edge fab mostly with domestic tools, it can keep expanding capacity without US licenses. With YMTC&\#x27;s share of China&\#x27;s NAND market already at 38.5% — ahead of Samsung — and three new fabs potentially doubling its capacity, the shift could reshape global NAND competition and prices. The incremental domestic substitution is expected to concentrate in cleaning, polishing \(CMP\) and etching tools, while advanced steps such as lithography and inspection/metrology still depend on overseas suppliers. Stacking more than 300 layers is technically demanding, requiring tight process control and error management as layer counts rise.

telegram · zaihuapd · Nov 6, 08:34

**Background**: 3D NAND is flash memory built by stacking memory cells vertically in dozens or hundreds of layers rather than spreading them across a flat surface, and adding layers is the main lever for lowering cost per gigabyte and raising capacity — which is why 300-plus-layer stacks matter for AI and datacenter SSDs. YMTC was founded in Wuhan in 2016 with government investment and a mandate to reduce China&\#x27;s dependence on foreign memory chips, and it has since become the country&\#x27;s leading 3D NAND producer. US export controls limit shipments of advanced chipmaking tools to Chinese fabs, giving YMTC a strong incentive to qualify domestic equipment suppliers in processes such as cleaning and etching, where Chinese vendors have already achieved relatively high localization rates.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Yangtze_Memory_Technologies">Yangtze Memory Technologies - Wikipedia</a></li>
<li><a href="https://www.charteredsemi.com/3d-nand-architecture-explained/">3D NAND Architecture Explained: Layers and Arrays in 2026</a></li>
<li><a href="https://china.acclime.com/news-insights/semiconductor-industry/">China &#x27;s Semiconductor Industry: The Path to Self-Sufficiency</a></li>

</ul>
</details>

**Tags**: `#semiconductor-industry`, `#NAND-flash`, `#china-tech`, `#export-controls`, `#AI-infrastructure`

---

<a id="item-4"></a>
## [Taobao MNN team open-sources 0.3B on-device language model](https://www.ithome.com/1/023/212.htm) ⭐️ 7.0/10

On November 6, Taobao&\#x27;s MNN team open-sourced MNN-Pocket-0.3B, a roughly 300-million-parameter language model designed to run entirely offline on phones, decoding at about 350 tokens per second on an iPhone 18 Pro with an INT4 deployment file of only 173 MB. The team targeted peak memory under 300 MB and decoding above 200 tokens/s, settling on a 28-layer architecture with the vocabulary pruned from 151K to 64K, and released separate checkpoints for pre-training, post-training, and on-device deployment. This is a concrete engineering data point for the sub-billion-parameter tier: it shows that a useful assistant-grade model can fit in under 200 MB and run far faster than reading speed on a stock smartphone, which makes fully offline inference viable for apps like Taobao&\#x27;s own assistants without cloud round-trips or per-token cost. It also strengthens MNN&\#x27;s position as an end-to-end stack where model architecture and inference runtime are co-designed, an approach increasingly competitive with other on-device frameworks. The model was built via co-design of architecture, data, training pipeline and inference system, with hardware-aware architecture selection and dependency-aware vocabulary pruning to fit mobile memory and compute budgets, and pre-training covered roughly 4.1 trillion high-quality Chinese and English tokens. The team positions it for on-device assistants, data extraction, and lightweight agentic pipelines, while explicitly noting that sub-billion-parameter models are not suited to reasoning-heavy work such as advanced mathematics or long-horizon code generation.

telegram · zaihuapd · Nov 6, 15:13

**Background**: MNN is Alibaba&\#x27;s open-source, lightweight deep learning inference framework, widely used inside Alibaba apps such as Taobao, Tmall and DingTalk to run neural networks directly on phones rather than on servers. Quantization compresses a model&\#x27;s weights to lower-bit integers — INT4 here means about 4 bits per weight instead of 16, shrinking the file roughly fourfold at some cost to accuracy — which is what makes a 0.3B model fit in 173 MB. Vocabulary size matters too, because the token embedding table scales with vocabulary, so pruning a 151K-token vocabulary down to 64K saves substantial memory on a device.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/taobao-mnn/MNN-Pocket-0.3B">taobao-mnn/MNN-Pocket-0.3B · Hugging Face</a></li>
<li><a href="https://huggingface.co/taobao-mnn/MNN-Pocket-0.3B-MNN">taobao-mnn/MNN-Pocket-0.3B-MNN · Hugging Face</a></li>
<li><a href="https://github.com/alibaba/MNN">GitHub - alibaba/ MNN : MNN : A blazing-fast, lightweight inference ...</a></li>

</ul>
</details>

**Tags**: `#on-device AI`, `#edge inference`, `#small language models`, `#model compression`, `#MNN`

---

<a id="item-5"></a>
## [Anthropic&\#x27;s Claude Can Now Read Your Bank Accounts via Plaid](https://www.theverge.com/ai-artificial-intelligence/1027652/anthropic-claude-plaid-personal-finance) ⭐️ 6.0/10

Anthropic launched a Personal Finance feature in Claude that uses Plaid to connect to users&\#x27; bank and credit-card accounts, letting the assistant categorize spending, review balances and credit limits, and analyze up to two years of transactions. The beta began rolling out this week to Claude Pro, Max, and Ultra subscribers in the United States. This is a notable step toward AI assistants becoming agents that touch sensitive personal financial data, and it puts Anthropic in direct competition with OpenAI, which added a similar Plaid-powered feature to ChatGPT in May. It also forces a mainstream conversation about how much financial data users are willing to hand to an AI chatbot. Access is deliberately read-only: Claude cannot move money, manage investments, or give investment advice, and it only sees the accounts a user explicitly connects — including the bank&\#x27;s name, account name, type, last four digits, balances, credit limits, and transaction history. The scope is limited to US paid subscribers and is still labeled a beta.

telegram · zaihuapd · Nov 6, 00:54

**Background**: Plaid is a data-aggregation middleware layer widely used by fintech apps: instead of storing your bank username and password, an app links through Plaid, which authenticates to the bank and returns account and transaction data via API. &quot;Read-only&quot; access means the connection is authorized only to retrieve data, not to initiate payments — but balances, transactions, and holdings remain highly sensitive, so security still depends heavily on how the receiving service stores and processes that data. Anthropic&\#x27;s move follows a broader 2025 trend of AI labs shipping agentic features that act on users&\#x27; real accounts rather than just answering questions.

<details><summary>References</summary>
<ul>
<li><a href="https://www.theverge.com/ai-artificial-intelligence/1027652/anthropic-claude-plaid-personal-finance">Claude AI can plug directly into your bank account | The Verge</a></li>
<li><a href="https://www.zdnet.com/innovation/personal-finance-claude-anthropic/">Claude &#x27;s new Personal Finance tool aims to help analyze... - ZDNET</a></li>
<li><a href="https://claude.com/resources/articles/introducing-personal-finance-in-claude">Introducing Personal Finance in Claude | Claude by Anthropic</a></li>
<li><a href="https://plaid.com/resources/open-finance/open-banking-api/">What is an open banking API ? How apps and accounts connect | Plaid</a></li>

</ul>
</details>

**Tags**: `#Anthropic`, `#Claude`, `#AI agents`, `#personal finance`, `#Plaid`, `#privacy`

---

<a id="item-6"></a>
## [India Targets Homegrown GPU in 24 Months, Aims to Commercialize RISC-V Chips](https://www.tomshardware.com/tech-industry/semiconductors/india-targets-creating-homegrown-gpus-within-2-years-and-plans-to-commercialize-indigenous-shakti-and-vega-risc-v-processors-sees-ai-boom-as-a-potential-repeat-of-the-y2k-opportunity-for-its-it-industry) ⭐️ 6.0/10

On November 4, S. Krishnan, Secretary of India&\#x27;s Ministry of Electronics and Information Technology \(MeitY\), said that under &\#x27;India Semiconductor Mission 2.0&\#x27; the country aims to develop an indigenous GPU chip in roughly 24 months, and also plans to bring its RISC-V-based SHAKTI and VEGA processors to commercial markets. He did not name any manufacturing partner or chip vendor involved in the GPU effort. If realized, an indigenous GPU would reduce India&\#x27;s dependence on Nvidia, AMD and other foreign suppliers at a time when AI compute is becoming strategic infrastructure, and it would give the country&\#x27;s large IT services industry a hardware layer to build on. India&\#x27;s semiconductor market is currently worth about $50 billion and is projected to approach $100 billion by 2030, so even partial success would shift where AI hardware is designed and eventually built. The announcement came without technical specifics — no process node, performance target, architecture licensing plan or named industry partners — making the 24-month timeline hard to verify. The processors slated for commercialization are separate, longer-running projects: SHAKTI is an open-source RISC-V family from IIT Madras, while VEGA is C-DAC&\#x27;s indigenous RISC-V line, with SoCs such as THEJAS32/THEJAS64 and the 64-bit dual-core VEGA AS2161 DHRUV64 already demonstrated booting Linux.

telegram · zaihuapd · Nov 6, 02:00

**Background**: India launched its Semiconductor Mission in 2021 with roughly $10 billion in incentives aimed mainly at attracting fabs and assembly plants; ISM 2.0 shifts emphasis toward equipment and materials, design IP, supply chains and R&amp;D centres, with a stated goal of enabling at least 50 fabless semiconductor companies. RISC-V is an open, royalty-free instruction set architecture that lets countries and startups design processors without licensing fees from Arm or x86 vendors, which is why India&\#x27;s chip self-reliance push leans on it. Krishnan framed AI as a &\#x27;Y2K-like&\#x27; opportunity, a reference to the late-1990s year-2000 remediation work that sent a wave of outsourced software contracts to Indian IT firms.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SHAKTI_%28microprocessor%29">SHAKTI (microprocessor) - Wikipedia</a></li>
<li><a href="https://vegaprocessors.in/">C-DAC | Vegaprocessors</a></li>
<li><a href="https://www.ism.gov.in/schemes/semicon2.0/index">Semicon 2.0 | India Semiconductor Mission - ism.gov.in</a></li>

</ul>
</details>

**Tags**: `#India semiconductors`, `#GPU`, `#RISC-V`, `#AI hardware`, `#semiconductor policy`

---

<a id="item-7"></a>
## [China&\#x27;s NRTA Backs Live-Action Micro-Dramas, Tightens AI Rules](https://www.ithome.com/1/023/215.htm) ⭐️ 6.0/10

On November 5, an official from China&\#x27;s National Radio and Television Administration \(NRTA\) reiterated that the micro-drama sector should support live-action productions while regulating AI-generated ones, requiring platforms to enforce &quot;review everything that airs, with full human review&quot; and to optimize their algorithms. The regulator also pledged continued crackdowns on AI content laundering \(AI 洗稿\), pirated remakes, and unauthorized use of people&\#x27;s likenesses and voices. The policy signals that AI-generated micro-dramas, which the NRTA says made up over 90% of the 430,000 micro-dramas launched in the first eight months of this year, will face a stricter compliance bar even as live-action creators get official backing. It affects platforms, AI video toolmakers, and creators who rely on synthetic content, and it reinforces a broader trend of Chinese regulators pairing AI content labeling and review mandates with copyright and likeness protections. The core requirement is &quot;凡播必审、全量人审&quot; — every episode must be reviewed before broadcast and human-reviewed in full, rather than filtered only by automated systems — while the official stressed that AI should assist quality production, with live-action creation remaining the mainstay of micro-dramas. The NRTA framed AI regulation as needing to hold the line on copyright and ethical bottom lines, and reports note that the human-review mandate is distinct from separate AI-labeling requirements under rules that took effect in September.

telegram · zaihuapd · Nov 6, 06:40

**Background**: Micro-dramas are short, vertically shot episodic series, typically a few minutes per episode, that have exploded in China as a fast-growing mobile entertainment format with a market projected to exceed 100 billion yuan. Generative AI video tools have made it cheap to mass-produce such content, prompting concerns over homogenized output, infringing remakes, and &quot;AI 洗稿&quot; — the practice of using AI to rapidly rewrite others&\#x27; work into disguised plagiarized versions. The NRTA is China&\#x27;s top broadcast regulator, and its micro-drama rules set the compliance baseline that platforms such as Douyin, Kuaishou, and iQiyi must enforce.

<details><summary>References</summary>
<ul>
<li><a href="https://news.znds.com/article/69767.html">广电总局重申AI微短剧全量人审，强调肖像声音授权_ZNDS资讯</a></li>
<li><a href="http://news.china.com.cn/live/2021-01/15/content_1120191.htm">什 么 是 “ 洗 稿 ”？ “伪原创”为何不断壮大？_ 新闻中心_中国网</a></li>
<li><a href="https://h5.ifeng.com/c/vivoArticle/v002vFceNufryf3FyIxRS1tauskK43yUH4QpWgs6AOM1138__?isNews=1&amp;showComments=0">文艺圆桌丨站上风口的 微 短 剧 ，期待更多“好风”吹来</a></li>

</ul>
</details>

**Tags**: `#AI regulation`, `#generative AI`, `#content moderation`, `#China policy`, `#media industry`

---

<a id="item-8"></a>
## [China pushes embodied AI into elderly care with new six-department policy](https://api3.cls.cn/share/article/2527197?sv=859&amp;amp;os=web) ⭐️ 6.0/10

On November 4, six Chinese government departments led by the Ministry of Civil Affairs issued measures aimed at boosting consumption of age-friendly products, calling for accelerated application of embodied AI, large language models, brain-computer interfaces, and exoskeletons in elderly care. The document also encourages faster deployment of smart elderly-care robots, promotion of rent-instead-of-buy leasing models, and creation of new retail formats such as &quot;silver-hair MALLs&quot; and senior markets. This is a top-level policy signal that could channel state science funding and procurement demand toward robotics and AI companies targeting China&\#x27;s fast-aging population. It suggests embodied AI and assistive hardware may move from lab demos into subsidized care facilities and consumer channels, shaping the near-term direction of China&\#x27;s silver economy. The measures frame national major science and technology programs as the牵引 force but give no specific funding figures, timelines, or certification standards, leaving implementation to follow-up rules. The emphasis on rental and leasing models is notable because high unit costs of care robots and exoskeletons have been a major barrier to adoption in institutional elderly care.

telegram · zaihuapd · Nov 6, 07:31

**Background**: Embodied AI refers to artificial intelligence embedded in physical systems such as robots, humanoid machines, and autonomous vehicles, letting them perceive and act in the real world rather than only process data. Brain-computer interfaces aim to link neural signals with external devices, and research has explored their use for cognitive and motor rehabilitation in older adults, while exoskeletons provide physical support to stabilize gait and restore mobility. China&\#x27;s population is aging rapidly, and the government has repeatedly promoted smart elderly-care technology as a way to ease pressure on caregivers and care facilities.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/glossary/embodied-ai/">What is Embodied AI? | NVIDIA Glossary</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC11737249/">Brain computer interfaces for cognitive enhancement in older ...</a></li>
<li><a href="https://biologyinsights.com/exoskeleton-for-elderly-how-they-assist-seniors/">Exoskeleton for Elderly: How They Assist Seniors</a></li>

</ul>
</details>

**Tags**: `#AI policy`, `#embodied AI`, `#elderly care`, `#robotics`, `#China`

---

<a id="item-9"></a>
## [Tesla to wind down Cybertruck production by mid-next year](https://www.theverge.com/transportation/1028542/tesla-cybertruck-winding-down-production-2027) ⭐️ 6.0/10

Elon Musk announced on X on Friday that Tesla will &quot;wind down&quot; Cybertruck production at Giga Texas by mid-next year, freeing factory space to ramp up Cybercab output. The Texas plant is the only known site assembling the Cybertruck, and Tesla has not said whether production will move elsewhere. The move marks an unusually public retreat from a flagship vehicle and signals that Tesla is reallocating manufacturing capacity toward its autonomous Robotaxi/Cybercab ambitions rather than niche, low-volume consumer trucks. It also reinforces concerns about softening demand for high-priced electric pickups, a segment where rivals like Ford and Rivian have also struggled. Since launching in 2023, Cybertruck deliveries have peaked at roughly 70,000 units, far below the 250,000-per-year target Musk once touted, and the announcement gave no timeline for a replacement model or relocation of tooling. Production is described as winding down gradually through mid-next year rather than stopping immediately, leaving existing owners and reservation holders in an unclear position.

telegram · zaihuapd · Nov 6, 12:28

**Background**: The Cybertruck is Tesla&\#x27;s angular stainless-steel electric pickup, unveiled in 2019 and finally reaching customers in late 2023 after repeated delays and manufacturing challenges. Giga Texas, located near Austin, is Tesla&\#x27;s global headquarters and its main U.S. plant, producing the Model Y alongside the Cybertruck. The Cybercab is Tesla&\#x27;s purpose-built two-seat robotaxi, revealed in October 2024, which has no steering wheel or pedals and is intended to underpin a Tesla-operated autonomous ride-hailing network.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tesla.com/giga-texas">Giga Texas | Tesla</a></li>
<li><a href="https://zh.wikipedia.org/wiki/%E7%89%B9%E6%96%AF%E6%8B%89Cybercab">特斯拉Cybercab - 维基百科，自由的百科全书</a></li>
<li><a href="https://www.tesla.com/robotaxi">Robotaxi | Tesla</a></li>

</ul>
</details>

**Tags**: `#特斯拉`, `#Cybertruck`, `#电动汽车`, `#制造业`, `#行业动态`

---

<a id="item-10"></a>
## [EU Charges TikTok&\#x27;s Recommendation Algorithm With Harmful &\#x27;Rabbit Hole&\#x27; Effects](https://www.cnbc.com/2026/11/06/eu-charges-tiktok-harmful-algorithmic-rabbit-hole-effects.html) ⭐️ 6.0/10

The European Commission has formally charged TikTok&\#x27;s recommendation system under the Digital Services Act, saying the platform failed to take effective measures against the risk that its &quot;For You&quot; feed pushes users down harmful &quot;rabbit hole&quot; loops. The Commission is demanding that TikTok rework the algorithm to lean more heavily on users&\#x27; explicit preferences, improve user controls and regularly test the system, with parent company ByteDance potentially facing fines of up to 6% of global annual revenue next year if the case is not resolved. This is one of the most direct challenges yet to how a major short-video platform&\#x27;s core recommendation engine is designed, and it could force concrete changes to the &quot;For You&quot; feed for hundreds of millions of European users. It also sets a precedent for how the DSA&\#x27;s systemic-risk rules can be applied to algorithmic amplification, which other platforms such as Meta, YouTube and X are watching closely. The charge is part of a broader EU investigation into TikTok, and the Commission frames repeated exposure to similar content as a potential risk to users&\#x27; mental health. Under the DSA, penalties can reach 6% of a company&\#x27;s global annual turnover, though platforms typically get a chance to submit remedies or commit to changes before any fine is imposed.

telegram · zaihuapd · Nov 6, 14:03

**Background**: The Digital Services Act \(Regulation \(EU\) 2022/2065\) is the EU&\#x27;s rulebook for online platforms, and it imposes extra &quot;systemic risk&quot; obligations on very large platforms — including assessing and mitigating risks arising from how their recommender systems shape what users see. The &quot;rabbit hole&quot; effect refers to the concern that recommendation algorithms keep serving increasingly similar or more extreme content, drawing users deeper into a topic or worldview. Academic work on algorithmic amplification frames this as a design issue: recommender systems do not create content, but they decide which content gets attention. The case therefore hinges less on any single video than on how TikTok&\#x27;s ranking and personalization design is built and tested.

<details><summary>References</summary>
<ul>
<li><a href="https://telegram.org/tos/eu-dsa">User guidance for the EU Digital Services Act</a></li>
<li><a href="https://css.engineering.upenn.edu/new-study-challenges-youtubes-rabbit-hole-effect-on-political-polarization/">New Study Challenges YouTube’s Rabbit Hole Effect on Political...</a></li>
<li><a href="https://leibniz-hbi.de/en/algorithmic-amplification-of-negative-discourse-as-a-systemic-risk/">Algorithmic Amplification of Negative Discourse as a Systemic Risk</a></li>

</ul>
</details>

**Tags**: `#EU Digital Services Act`, `#TikTok`, `#recommendation algorithms`, `#platform regulation`, `#content moderation`

---

<a id="item-11"></a>
## [Researcher finds ~100,000 words Apple&\#x27;s iPhone keyboard won&\#x27;t suggest](https://thenextweb.com/news/apple-iphone-keyboard-hidden-list) ⭐️ 6.0/10

Independent researcher Derik Kauffman discovered roughly 100,000 terms that Apple&\#x27;s iOS keyboard will not autocomplete or swipe-type, including political phrases such as &quot;Dictator Trump,&quot; &quot;Sleepy Joe,&quot; &quot;right wing conspiracy,&quot; &quot;Tibetan independence&quot; and &quot;United Ireland.&quot; Apple confirmed the keyboard is designed to avoid suggesting inappropriate or offensive language but did not explain why political terms were included, prompting criticism from the Electronic Frontier Foundation&\#x27;s David Greene, who argued the list should not be secret. The finding turns a mundane input feature into a platform-governance question: even though users can still type these phrases by hand, quietly shaping what a keyboard suggests nudges how millions of people write and search. It adds pressure on Apple to disclose and justify the editorial rules baked into its software, at a time when regulators and civil-liberties groups are scrutinizing how large platforms moderate speech. The restrictions only suppress autocomplete and swipe-to-type suggestions — manually typed text is unaffected — and non-English languages carry their own separate flagged lists, which makes the filtering harder to audit across markets. The list&\#x27;s size \(~100,000 entries\) and its mix of insults, political slogans and geopolitical phrases blur the line between anti-harassment filtering and viewpoint-based curation.

telegram · zaihuapd · Nov 6, 15:25

**Background**: iPhone keyboards use predictive text models that suggest the next word as you type and power QuickPath swipe typing; like most commercial keyboards, iOS filters out suggestions it deems offensive so users don&\#x27;t get embarrassing or abusive completions. What is unusual here is not the existence of a blocklist but its scope and secrecy — Apple has not published the criteria, and there is no user-facing way to inspect or adjust it. The EFF is a San Francisco-based digital-rights nonprofit founded in 1990 that has long campaigned for transparency in how platforms restrict speech.

<details><summary>References</summary>
<ul>
<li><a href="https://www.straitstimes.com/world/united-states/apples-predictive-text-restrictions-include-dictator-trump-and-sleepy-joe-researcher-finds">Apple’s predictive text restrictions include ‘Dictator Trump ...</a></li>
<li><a href="https://economictimes.indiatimes.com/tech/technology/apples-predictive-text-restrictions-include-dictator-trump-and-sleepy-joe-researcher-finds/articleshow/135608356.cms">Apple&#x27;s predictive text restrictions include &#x27;Dictator Trump ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Electronic_Frontier_Foundation">Electronic Frontier Foundation - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#privacy`, `#Apple`, `#censorship`, `#keyboard`, `#platform-transparency`

---

<a id="item-12"></a>
## [Telegram 13.2 lets bots run interactive HTML/CSS/JS messages inside chats](https://play.google.com/store/apps/details?id=org.telegram.messenger&amp;amp;hl=en_US) ⭐️ 6.0/10

Telegram&\#x27;s Android, iOS and macOS clients have been updated to version 13.2, with Desktop reaching 7.4, adding the ability for developers to build interactive messages with HTML, CSS and JavaScript that run directly inside the chat instead of opening a Mini App — for example small games with touch controls and saved progress. The release also introduces a new sidebar layout for group and bot topics, where the topic list slides out from the right side of the screen and is enabled automatically in channel direct messages and Saved Messages. This lowers the friction for bot and Mini App developers by letting lightweight interactive content render inline in the message stream rather than requiring a full-screen Mini App launch, which could make Telegram chats feel more like an app surface and less like a plain message log. For the broader messaging ecosystem it signals continued convergence of chat clients and web runtimes, a direction competitors such as WeChat and Discord have also been pushing. The feature arrives as a client-side update spanning Android, iOS, macOS \(13.2\) and Desktop \(7.4\), so availability depends on users upgrading their apps, and in-chat HTML messages should be understood as a lighter-weight alternative to full Mini Apps rather than a replacement for them. The topic sidebar is not purely optional in every context: it is turned on by default in channel direct messages and Saved Messages.

telegram · zaihuapd · Nov 6, 15:56

**Background**: Telegram Mini Apps are web applications built with JavaScript, HTML5 and CSS that run inside Telegram, usually opening as a full-screen view launched from a chat or bot button, and they underpin a large ecosystem of games, utilities and TON-based services. Previously, bot messages supported only limited HTML or Markdown formatting for styling text, so anything genuinely interactive required leaving the conversation for a Mini App. Telegram Topics are a separate feature that splits a group into threaded discussions on different subjects, and the new sidebar layout changes how those topic lists are presented.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.telegram-mini-apps.com/">Home | Telegram Mini Apps</a></li>
<li><a href="https://www.bnbchain.org/en/blog/what-are-telegram-mini-apps">What Are Telegram Mini Apps? - BNB Chain Blog</a></li>
<li><a href="https://blog.invitemember.com/telegram-topics/">Telegram Topics : How to Organize a Group with Topics</a></li>

</ul>
</details>

**Tags**: `#Telegram`, `#interactive messages`, `#HTML/CSS/JS`, `#messaging platforms`, `#Mini Apps`

---

<a id="item-13"></a>
## [US DOJ&\#x27;s Super Intelligence Task Force Officially Goes Live](https://www.theregister.com/ai-and-ml/2026/11/06/dojs-super-intelligence-task-force-up-and-running/5308074) ⭐️ 6.0/10

The US Department of Justice announced that its Super Intelligence Task Force \(SINTF\) is now up and running, following an October 13 memo from President Donald Trump authorizing its creation. The task force is led by Director of National Intelligence Jay Clayton together with Associate Attorney General Stanley Woodward, and will coordinate the DOJ&\#x27;s AI-related criminal and civil cases while pushing back on what it calls burdensome regulation. This marks one of the first dedicated AI enforcement bodies inside a Western justice ministry, signaling that AI governance is shifting from white papers toward prosecutorial and legal action. Its dual mandate — chasing malicious AI actors while lobbying against strict rules — could shape how aggressively AI companies are investigated and how much regulation actually lands in the US. The task force is chaired by the Director of National Intelligence alongside an associate attorney general, and is also expected to coordinate with the president&\#x27;s broader &quot;Super Intelligence Force.&quot; Defense Department CTO Emil Michael said further AI regulation details would be published later this month, though the announcement gave no specifics on staffing, budget, or which cases it will prioritize.

telegram · zaihuapd · Nov 6, 17:01

**Background**: Superintelligence refers to a hypothetical AI agent whose cognitive performance greatly exceeds humans across virtually all domains, a concept popularized by philosopher Nick Bostrom in his 2014 book of the same name. No such system exists today, but governments are already building institutional machinery to handle the legal, security, and competition questions it might raise. The DOJ&\#x27;s move follows a pattern of the US executive branch creating AI-focused bodies through presidential memos rather than legislation, which lets them be stood up quickly but leaves their authority ambiguous.

<details><summary>References</summary>
<ul>
<li><a href="https://www.justice.gov/opa/pr/department-justice-launches-super-intelligence-task-force">Department of Justice Launches Super Intelligence Task Force</a></li>
<li><a href="https://www.theregister.com/ai-and-ml/2026/11/06/dojs-super-intelligence-task-force-up-and-running/5308074">DoJ&#x27;s &#x27;Super Intelligence Task Force&#x27; up and running</a></li>
<li><a href="https://en.wikipedia.org/wiki/Superintelligence">Superintelligence - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI policy`, `#regulation`, `#US DOJ`, `#national security`, `#superintelligence`

---