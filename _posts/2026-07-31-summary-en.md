---
layout: default
title: "Horizon Summary: 2026-07-31 (EN)"
date: 2026-07-31
lang: en
report: default
---

> From 400 items, 10 important content pieces were selected

---

1. [ByteDance&\#x27;s Seedance 2.5 generates 30-second videos with multi-modal references](#item-1) ⭐️ 8.0/10
2. [DeepSeek Launches V4-Flash Official API Public Beta](#item-2) ⭐️ 8.0/10
3. [Huawei Open-Sources 505B-Parameter MoE Model openPangu-2.0-Pro](#item-3) ⭐️ 8.0/10
4. [Judge Says US Still Lacks Evidence to Label Anthropic Supply Chain Risk](#item-4) ⭐️ 8.0/10
5. [MiniMax to Open-Source Multimodal Video Model H3 on August 3](#item-5) ⭐️ 8.0/10
6. [German Court Rules AI Music Firm Suno Violated Copyright](#item-6) ⭐️ 8.0/10
7. [China Announces 21 &\#x27;Paper Mill&\#x27; Research Misconduct Cases](#item-7) ⭐️ 6.0/10
8. [Trump Administration Weighs $100,000 Fee for Foreign Graduates to Work in US via OPT](#item-8) ⭐️ 6.0/10
9. [Meituan and Suzhou Launch &\#x27;Traffic-Light Timer&\#x27; to Extend Delivery Deadlines](#item-9) ⭐️ 6.0/10
10. [YouTube Bans ASMR Creators Citing Sexual Gratification Policy](#item-10) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [ByteDance&\#x27;s Seedance 2.5 generates 30-second videos with multi-modal references](https://seed.bytedance.com/zh/blog/%E4%B8%80%E9%95%9C%E6%88%90%E7%89%87-%E9%9A%8F%E5%BF%83%E5%8F%82%E8%80%83-seedance-2-5-%E6%AD%A3%E5%BC%8F%E5%8F%91%E5%B8%83) ⭐️ 8.0/10

ByteDance officially launched Seedance 2.5 on July 31, doubling the single-generation video length from 15 to 30 seconds. It accepts up to 30 reference images, 10 reference videos, and 10 audio clips per input, and is rolling out to Jimeng AI and Doubao Pro, with an API coming to Volcano Ark. This release pushes the boundaries of AI video generation, enabling longer, more coherent narratives that were previously difficult to produce. With strong multimodal reference and timestamp control, it opens up practical applications in education, industrial simulation, embodied intelligence, and autonomous driving data generation. Seedance 2.5 supports multi-round extension, allowing users to produce several minutes of high-quality coherent video, and uses timestamps for precise control over scenes and pacing. It is already powering video generation in education, industrial simulation, embodied intelligence, and autonomous driving, including the creation of teaching materials and synthetic training data.

telegram · zaihuapd · Jul 31, 04:16

**Background**: Seedance 2.5 is the latest video generation model from ByteDance, building on an earlier version that produced only 15-second clips. Video generation models create moving images from text prompts and increasingly from extra reference materials like images, video clips, and audio; ByteDance&\#x27;s new model supports up to 30 images, 10 videos, and 10 audio clips per request. Such models are typically accessed through consumer apps like Jimeng AI and Doubao Pro, or via enterprise platforms such as Volcano Ark, which provides AI model APIs. Seedance 2.5 is also being applied to embodied intelligence and autonomous driving, where AI-generated synthetic training data supplements real-world data for model training.

<details><summary>References</summary>
<ul>
<li><a href="https://ai.fenmiao.group/archives/463.html">火 山 引擎给大模型造大底座！ MiniMax、智谱AI等已登陆 – 分秒AI研究院</a></li>
<li><a href="http://www.broadview.com.cn/article/420497">被众多AI大佬看好的 具 身 智 能 到底 是 什 么 ？ 它凭 什 么 成为下一个AI...</a></li>
<li><a href="https://m.21jingji.com/article/20240529/herald/0f5ac19b473ddf016a76965057af41f2_zaker.html">AI 训 练 数 据 荒下， 合 成 数 据 成 为“开源”新解法？ - 21世纪经济报道</a></li>

</ul>
</details>

**Tags**: `#video generation`, `#ByteDance`, `#AI model`, `#multimodal`, `#Seedance`

---

<a id="item-2"></a>
## [DeepSeek Launches V4-Flash Official API Public Beta](https://api-docs.deepseek.com/zh-cn/updates) ⭐️ 8.0/10

On July 31, 2026, DeepSeek launched the official V4-Flash API public beta with significantly improved agent capabilities. The model now natively supports the Responses API format and is adapted for Codex, while benchmark scores far exceed those of V4-Pro-Preview. This release gives developers a more powerful and compatible API option for building agentic applications, and it signals DeepSeek&\#x27;s push to compete in the agent-ready model space. The benchmark gains indicate practical improvements for tasks like terminal operations, cybersecurity, and full-stack development, and an official V4-Pro release is expected next. Benchmark results include Terminal Bench 2.1 at 82.7, Cybergym at 76.7, DSBench-FullStack at 68.7, and DSBench-Hard at 59.6. The model structure and size remain the same as V4-Flash-preview, but the post-training has been redone; only the V4-Flash API is updated, while the V4-Pro API and APP/WEB endpoints remain unchanged, and a DeepSeek Harness minimal mode was mentioned for testing.

telegram · zaihuapd · Jul 31, 05:50

**Background**: DeepSeek is an AI lab that offers large language models through developer APIs. The Responses API, popularized by OpenAI, is a developer-friendly interface for building agentic applications, combining chat completions with tool-calling capabilities. Benchmarks like Terminal-Bench assess AI agents on complex, real-world command-line tasks, while Cybergym and DSBench target cybersecurity and full-stack software development. DeepSeek Harness is an upcoming open-source evaluation tool designed to measure agent performance.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/OpenAI_Responses_API">OpenAI Responses API</a></li>
<li><a href="https://grokipedia.com/page/Terminal-Bench">Terminal-Bench</a></li>
<li><a href="https://dlcmh.github.io/">DeepSeek Agent Harness : Technical deep -dive &amp; the open-source...</a></li>

</ul>
</details>

**Tags**: `#deepseek`, `#api`, `#model-release`, `#agent`, `#benchmarks`

---

<a id="item-3"></a>
## [Huawei Open-Sources 505B-Parameter MoE Model openPangu-2.0-Pro](https://huggingface.co/openpangu/openPangu-2.0-Pro) ⭐️ 8.0/10

Huawei released openPangu-2.0-Pro on Hugging Face, a 505B-parameter mixture-of-experts \(MoE\) large language model trained on Ascend NPUs. It supports a 512k-token context and reports strong reasoning results, including 95.4 on AIME 2026 math and 87.9 on GPQA-Diamond for the Thinking version. Open-sourcing a model of this scale is a significant move for the AI ecosystem, offering developers an alternative to closed or Western-centric models. It also showcases Huawei&\#x27;s full-stack AI capability, from Ascend hardware to large-model training and alignment. The model uses mixture-of-experts \(MoE\) with about 505B total parameters and roughly 18B activated per token, trained on about 34T tokens. Architecturally, it employs multi-head latent attention \(MLA\), a DSA+SWA hybrid layer design, and a 3-head MTP self-speculative decoding module, with post-training combining fast/slow unified fine-tuning and specialized reinforcement learning.

telegram · zaihuapd · Jul 31, 06:50

**Background**: Mixture-of-experts \(MoE\) models scale up parameter counts while keeping inference costs lower by activating only a subset of parameters per token. Huawei&\#x27;s Ascend NPUs are specialized AI accelerators designed to provide an alternative to NVIDIA GPUs, especially under U.S. export restrictions. Multi-head latent attention \(MLA\), popularized by DeepSeek, reduces key-value cache overhead, and multi-token prediction \(MTP\) is a form of speculative decoding that boosts throughput by predicting several tokens per forward pass.

<details><summary>References</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/ascend-neural-processing-units-npus">Ascend NPUs : Huawei &#x27;s AI Accelerator</a></li>
<li><a href="https://arxiv.org/pdf/2502.07864">TransMLA: Multi - Head Latent Attention Is All You Need</a></li>
<li><a href="https://docs.vllm.ai/projects/ascend/en/latest/user_guide/feature_guide/speculative_decoding.html">Speculative Decoding - vLLM Ascend</a></li>

</ul>
</details>

**Tags**: `#Huawei`, `#MoE`, `#Large Language Model`, `#Open Source`, `#AI`

---

<a id="item-4"></a>
## [Judge Says US Still Lacks Evidence to Label Anthropic Supply Chain Risk](https://techcrunch.com/2026/07/30/judge-says-trump-admin-still-lacks-evidence-for-anthropic-supply-chain-risk-label/) ⭐️ 8.0/10

At a Thursday hearing, US District Judge Rita Lin said the Trump administration still lacks sufficient evidence to justify labeling Anthropic a supply chain risk and banning federal government use of its AI technology. Lin previously issued a temporary block on the ban and is now considering permanently reversing it. The case could set a precedent on whether the government may retaliate against federal contractors for disagreeing with its policies. It also carries significant implications for AI industry-government relations, as it touches on military use of AI and contractors&\#x27; freedom of speech. The dispute began when contract negotiations broke down between Anthropic and the Department of Defense over Anthropic&\#x27;s demand that its AI not be used for mass surveillance of Americans or lethal weapons decisions. Anthropic filed two lawsuits in March, and government lawyers said they plan to complete phasing out Anthropic products by September 30.

telegram · zaihuapd · Jul 31, 08:00

**Background**: The supply chain risk designation is normally used to restrict government purchases from companies seen as security threats. In this case, the government based the designation on Anthropic&\#x27;s public criticism of the Department of Defense, a logic Judge Lin called very troubling, arguing it could set a precedent for retaliating against contractors who disagree with government policy. Lin also said the case record had in some ways gotten worse for the government. The dispute stems from Anthropic&\#x27;s refusal to allow its AI to be used for mass surveillance of Americans or lethal weapons decisions during contract negotiations with the Pentagon.

**Tags**: `#AI policy`, `#Anthropic`, `#legal`, `#government`, `#supply chain`

---

<a id="item-5"></a>
## [MiniMax to Open-Source Multimodal Video Model H3 on August 3](https://modelscope.cn/models/MiniMax/MiniMax-H3) ⭐️ 8.0/10

MiniMax announced that its next-generation multimodal video model H3 will be open-sourced on August 3, 2026, via the ModelScope community. The model natively supports understanding and generation across text, image, audio, and video modalities. Open-sourcing H3 gives researchers and developers access to an advanced omni-modal model, potentially accelerating innovation in video generation, multimodal understanding, and commercial content production. This move could lower barriers for startups and studios targeting film, advertising, e-commerce, and gaming. H3 can generate videos with native stereo audio at up to 2K resolution and 15 seconds in length, and it supports multi-dimensional editing controls for tasks like adding subtitles, brand messages, effects, product displays, and UI animations. The model also handles multiple reference inputs for coherent creation.

telegram · zaihuapd · Jul 31, 12:37

**Background**: Multimodal AI integrates and processes multiple types of data, such as text, images, audio, and video, enabling a more holistic understanding than single-modality models. MiniMax H3 is a general-purpose omni-modal generation model that advances this trend by jointly handling multimodal context and producing synchronized video and audio. ModelScope is a one-stop platform for exploring, deploying, and open-sourcing machine learning models, making it a natural home for this release.

<details><summary>References</summary>
<ul>
<li><a href="https://www.minimax.io/blog/minimax-h3">MiniMax H 3 : An Open Model Breaking the Boundaries Between Tasks...</a></li>
<li><a href="https://modelscope.ai/">ModelScope</a></li>
<li><a href="https://en.wikipedia.org/wiki/Multimodal_AI">Multimodal AI</a></li>

</ul>
</details>

**Tags**: `#AI`, `#multimodal`, `#video generation`, `#open-source`, `#MiniMax`

---

<a id="item-6"></a>
## [German Court Rules AI Music Firm Suno Violated Copyright](https://www.dw.com/en/german-court-rules-that-ai-music-firm-suno-violated-copyrights/a-78152227) ⭐️ 8.0/10

The Munich Regional Court ruled that AI music company Suno infringed copyright by training its models on protected music. Suno must disclose its profits and pay damages, the amount of which is still to be determined, and the company says it will consider an appeal. This is one of the first major court decisions testing how copyright law applies to AI music training, and it sets a precedent for generative music companies. The ruling could pressure AI firms to seek proper licenses and fair compensation from rights holders before using their works. GEMA, Germany&\#x27;s music rights collective, filed the lawsuit in January 2025 and demonstrated songs generated by Suno that were highly similar to protected originals during the hearing. GEMA represents more than 95,000 musicians in Germany and over 2 million rights holders worldwide, while Suno disagrees with the ruling and is evaluating all options, including appeal.

telegram · zaihuapd · Jul 31, 13:11

**Background**: Suno is a generative AI music platform that creates songs from text prompts, and GEMA is a German performing rights society that collectively licenses and enforces copyrights for composers, lyricists, and music publishers. The case centers on whether training AI models on copyrighted recordings without permission constitutes infringement, a question that courts worldwide are still exploring. Collecting societies like GEMA act as trustees for rights holders and aim to secure equitable licensing terms for AI uses.

<details><summary>References</summary>
<ul>
<li><a href="https://suno.com/">Suno | AI Music Generator</a></li>
<li><a href="https://en.wikipedia.org/wiki/GEMA_%28German_organization%29">GEMA ( German organization) - Wikipedia</a></li>
<li><a href="https://www.gema.de/en/about-gema/organisation">GEMA as an organisation: its governing bodies, committees etc.</a></li>

</ul>
</details>

**Tags**: `#AI copyright`, `#Suno`, `#legal ruling`, `#generative music`, `#GEMA`

---

<a id="item-7"></a>
## [China Announces 21 &\#x27;Paper Mill&\#x27; Research Misconduct Cases](https://www.nhc.gov.cn/qjjys/ycdtxx/202607/22372dfb50574e56b12827f142c873f2.shtml) ⭐️ 6.0/10

On July 30, 2026, China&\#x27;s National Health Commission publicly announced the fifth batch of research misconduct cases involving &\#x27;paper mills,&\#x27; totaling 21 cases. The cases involve medical staff from hospitals in Fujian, Jiangxi, Zhejiang, Hubei, Guangdong, Gansu and other regions, with misconduct including buying experimental data, fabricating research processes, and ghostwriting/ghost-submitting papers. This announcement underscores China&\#x27;s escalating enforcement against research misconduct in the healthcare sector. The penalties—including lifetime bans from state-funded research and entry into a national misconduct database—serve as a strong deterrent and affect the careers of implicated researchers. The penalties range from admonishment talks and public notification to bans on state-funded scientific activities for a fixed period or for life, along with recovery of research awards. Two individuals, Shao Liang and Zhang Ping, received lifetime bans due to combined previous cases, while Liang Weiguo was dismissed from public office and is currently serving a prison sentence, so the investigation against him was terminated.

telegram · zaihuapd · Jul 31, 05:40

**Background**: A &\#x27;paper mill&\#x27; is a business that produces poor-quality or fabricated academic papers and sells authorship to researchers who need publications. China has been stepping up efforts to combat such fraud, using a national research misconduct database and holding both individuals and institutions accountable, though previous policies have focused mainly on individual authors.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Research_paper_mill">Research paper mill - Wikipedia</a></li>
<li><a href="https://www.academicjobs.com/research-publication-news/china-research-misconduct-crackdown-universities-punished-or-academicjobs-4091">China Research Misconduct Crackdown: Universities Punished</a></li>

</ul>
</details>

**Tags**: `#research integrity`, `#scientific misconduct`, `#paper mills`, `#healthcare`, `#academic publishing`

---

<a id="item-8"></a>
## [Trump Administration Weighs $100,000 Fee for Foreign Graduates to Work in US via OPT](https://www.bloomberg.com/news/articles/2026-07-30/trump-weighs-100-000-fee-for-foreign-students-to-work-post-grad) ⭐️ 6.0/10

The Trump administration is considering a $100,000 fee for international students to work in the United States after graduation through the Optional Practical Training \(OPT\) program. White House officials say no policy change is imminent but have not denied that discussions are underway. If implemented, the fee would heavily impact universities that depend on international student tuition, as well as Silicon Valley and Wall Street firms that hire international graduates. Nearly 300,000 international students were on OPT last fall, and the move is part of a broader tightening of international student policies. The reported fee targets the OPT program specifically. Earlier this month, the Department of Homeland Security shortened student visa stay limits to four years; the administration also proposed a similar fee for H-1B visas, but a federal judge ruled that illegal in June and the White House is appealing.

telegram · zaihuapd · Jul 31, 09:00

**Background**: Optional Practical Training \(OPT\) is a work authorization that allows eligible F-1 international students to gain practical work experience in the United States related to their field of study. The H-1B visa, by contrast, is a non-immigrant visa that lets US employers temporarily hire foreign workers in specialty occupations such as IT, engineering, medicine, and finance. Both programs are common pathways for international graduates to enter the US workforce, and changes to them affect both the tech industry and university finances.

<details><summary>References</summary>
<ul>
<li><a href="https://www.waypointimmigration.org/copy-of-o-1">OPT | Waypoint Immigration USA</a></li>
<li><a href="https://www.irishtimes.com/business/2025/09/22/what-is-happening-with-the-h-1b-visa-scheme-in-the-us-and-how-will-it-affect-irish-tech-workers/">What is the H - 1 B visa and how will changes to the scheme affect 372...</a></li>

</ul>
</details>

**Tags**: `#immigration`, `#international-students`, `#tech-industry`, `#policy`, `#OPT`

---

<a id="item-9"></a>
## [Meituan and Suzhou Launch &\#x27;Traffic-Light Timer&\#x27; to Extend Delivery Deadlines](https://www.meituan.com/news/NN260731177009116) ⭐️ 6.0/10

On July 31, Meituan and the Suzhou Public Security officially launched the &\#x27;Traffic-Light Stop Timer&\#x27; \(等灯停表\) for delivery riders, piloting at about 1,100 intersections in Gusu District and Suzhou Industrial Park. The system records how long a rider waits at red lights and automatically extends the latest delivery time for the order accordingly. This matters because it breaks away from the &\#x27;one-size-fits-all&\#x27; delivery timing algorithm that has long forced riders to run red lights and speed to meet deadlines. It is a practical step toward algorithmic fairness in the gig economy and is already being evaluated in more than 20 cities, including Shanghai and Hangzhou. The system combines riders&\#x27; GPS trajectories with real-time traffic-signal data to determine waiting status, and when a rider is delivering multiple orders, the wait time is credited to each order. Beijing and Wuxi have already started integration testing, and Suzhou&\#x27;s first batch covers roughly 1,100 intersections.

telegram · zaihuapd · Jul 31, 11:00

**Background**: Delivery platforms have long relied on strict algorithms to calculate delivery times, which often push riders to break traffic rules, drawing public criticism and legislative attention. The &\#x27;Traffic-Light Stop Timer&\#x27; originated from rider suggestions; Meituan had been internally testing it and expects to cover more than one million riders within the year. Real-time signal-light data can be obtained by connecting directly to traffic-police systems, as Amap does in partnered cities, with errors controllable to about one second.

<details><summary>References</summary>
<ul>
<li><a href="https://article.pchome.net/info/14911.html">美团已初步搭建“骑手 等 灯 停 表 ”功能，预计年内覆盖超百万骑手</a></li>
<li><a href="https://m.mp.oeeee.com/a/BAAFRD0000202607241631724.html">苏州试点骑手等红灯不扣 配 送 时 长，多地立 法 加强平台 算 法 治理</a></li>
<li><a href="https://juejin.cn/post/7619885691574009898">juejin.cn/post/7619885691574009898</a></li>

</ul>
</details>

**Tags**: `#delivery`, `#gig economy`, `#algorithmic fairness`, `#smart city`, `#logistics`

---

<a id="item-10"></a>
## [YouTube Bans ASMR Creators Citing Sexual Gratification Policy](https://www.404media.co/youtube-asmr-ban-sex-and-nudity-policy/) ⭐️ 6.0/10

This week YouTube terminated the channels of multiple well-known ASMR creators, including ItsBunniiASMR, Slight Sounds, Nananightray, and Roseasmr, citing its sexual gratification content policy. The creators received removal notices with no prior warning, and their appeals reportedly failed. This enforcement shows how YouTube&\#x27;s content moderation rules can be ambiguously applied to ASMR, a genre generally meant for relaxation and sleep, not sexual content. The bans threaten creators&\#x27; livelihoods and spark concerns about fairness and transparency in platform enforcement. The banned channel ItsBunniiASMR had roughly 227,000 subscribers and 55 million views. YouTube introduced its sexual gratification policy in 2019 and clarified it for ASMR in 2022, but creators argue the standard remains ill-defined.

telegram · zaihuapd · Jul 31, 15:58

**Background**: ASMR stands for Autonomous Sensory Meridian Response, a calming tingling sensation in the head or spine triggered by soft sounds or visuals such as whispering, tapping, or brushing. Such videos are widely used on YouTube for sleep, relaxation, and anxiety relief. YouTube prohibits content whose primary purpose is sexual gratification and has repeatedly updated its rules around ambiguous content categories.

<details><summary>References</summary>
<ul>
<li><a href="https://36kr.com/p/1866824783286790">深受年轻人追捧，令人上头的 ASMR 究竟 是 什 么 ？ -36氪</a></li>
<li><a href="https://blog.witsper.com/tips/autonomous-sensory-meridian-response/">ASMR 是 什 麼意思？ 這些聲音竟然會讓人「顱內高潮」 | 智選Blog</a></li>

</ul>
</details>

**Tags**: `#YouTube`, `#ASMR`, `#内容审核`, `#平台政策`, `#创作者经济`

---