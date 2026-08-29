---
layout: default
title: "Horizon Summary: 2026-08-29 (EN)"
date: 2026-08-29 04:33:53 +0000
lang: en
report: default
---

> From 292 items, 6 important content pieces were selected

---

1. [Tencent Hunyuan Releases Hy4 Preview: Edges GLM-5.3, Kimi K3 in Blind Tests](#item-1) ⭐️ 8.0/10
2. [Changxin Tech H1 2026 Net Profit Hits 77.6B Yuan, Reversing Loss](#item-2) ⭐️ 8.0/10
3. [Zhipu AI Open-Sources GLM-5.3, Focusing on Agentic Coding and Cyber Defense](#item-3) ⭐️ 8.0/10
4. [OpenAI to Cut Off Cursor Model Access After SpaceX Acquisition](#item-4) ⭐️ 8.0/10
5. [US FTC Probes YouTube Account Bans, Says Content Policies May Mislead Users](#item-5) ⭐️ 7.0/10
6. [Google Employees Test Gemini 3.8 Flash Preview, Praised Over 3.7 Flash](#item-6) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Tencent Hunyuan Releases Hy4 Preview: Edges GLM-5.3, Kimi K3 in Blind Tests](https://mp.weixin.qq.com/s/ymr3X878B8oa2XP15CH8TQ) ⭐️ 8.0/10

On August 28, 2026, Tencent released Hy4 preview, its strongest open-source model to date, with 770B total parameters, 49B active parameters, and a 1M-token context window. In blind evaluations across 203 engineering tasks, it scored 2.99, narrowly beating GLM 5.3 \(2.92\) and Kimi K3 \(2.94\), and it is now available on Tencent Cloud, GitHub, HuggingFace, ModelScope, AtomGit, and OpenRouter. Hy4 preview strengthens the open-source LLM ecosystem by offering a frontier-scale model with a 1M context window at competitive API prices. Its strong showing in engineering-task blind tests suggests open models are closing the gap with proprietary systems in real-world software engineering. The model uses a Mixture-of-Experts \(MoE\) architecture, where only 49B of its 770B parameters are active per token. API pricing is $0.834 per 1M input tokens and $2.501 per 1M output tokens, and the model focuses on long-horizon software engineering, document office work, and scientific research.

telegram · zaihuapd · Aug 28, 06:11

**Background**: Hy4 preview is a Mixture-of-Experts \(MoE\) model, meaning it does not use all parameters for every prompt; &\#x27;total parameters&\#x27; refers to the full model size, while &\#x27;active parameters&\#x27; are those actually used per token, giving the speed of a smaller model with the knowledge of a larger one. A context window dictates how much text the model can consider when generating responses, and 1M tokens is very large, enabling long-horizon tasks. Blind testing is an evaluation approach that prevents benchmark contamination—similar to the double-blind evaluations piloted by Google DeepMind—by hiding model identity or test details from participants.

<details><summary>References</summary>
<ul>
<li><a href="https://localmodel.run/guides/mixture-of-experts">Mixture of experts ( MoE ) explained for local LLMs · localmodel.run</a></li>
<li><a href="https://aiunderstanding.org/news/google-deepmind-pilots-double-blind-evaluations-for-proprietary-ai-models">Google DeepMind pilots double- blind evaluations ... | AI Understanding</a></li>

</ul>
</details>

**Tags**: `#AI模型`, `#开源`, `#腾讯混元`, `#大语言模型`

---

<a id="item-2"></a>
## [Changxin Tech H1 2026 Net Profit Hits 77.6B Yuan, Reversing Loss](https://telegram.me/zaihuapd/43468) ⭐️ 8.0/10

Changxin Technology reported H1 2026 revenue of 150.31 billion yuan \(up 873.64% year-over-year\) and net profit attributable to shareholders of 77.61 billion yuan, reversing a prior-year loss of 2.33 billion yuan. The company&\#x27;s gross margin reached 84.84% for the period. This financial turnaround underscores the rapid growth of China&\#x27;s domestic memory industry and its improving competitiveness in the global DRAM market. It also signals that Chinese memory chip makers are moving from survival to profitable expansion, which could reshape industry dynamics. Quarterly net profit was 24.76 billion yuan in Q1 and 52.84 billion yuan in Q2, a sequential increase of 113%. Operating cash flow reached 131.16 billion yuan, up 2985.64% year-over-year, with basic EPS of 1.2893 yuan.

telegram · zaihuapd · Aug 28, 11:34

**Background**: DRAM \(dynamic random access memory\) is a type of volatile semiconductor memory that temporarily stores data for processing by the CPU. Changxin Technology is a leading Chinese DRAM maker, and its results are closely watched as a barometer for China&\#x27;s push to build a self-sufficient domestic chip industry.

<details><summary>References</summary>
<ul>
<li><a href="https://www.lenovo.com/nz/en/glossary/what-is-dram/index.html">Dram : What is DRAM Memory ? | Understanding... | Lenovo NZ</a></li>

</ul>
</details>

**Tags**: `#semiconductor`, `#DRAM`, `#financial results`, `#memory chips`, `#China tech`

---

<a id="item-3"></a>
## [Zhipu AI Open-Sources GLM-5.3, Focusing on Agentic Coding and Cyber Defense](http://z.ai/) ⭐️ 8.0/10

Zhipu AI has released the open-source model GLM-5.3, with weights now available for download, running, and customization. The model shares the same base model as GLM-5.2, with all improvements coming from post-training, achieving Terminal Bench 2.1 score of 88.2 and DeepSWE score of 66.9, significantly ahead of GLM-5.2. This is a significant open-source LLM release from a major Chinese AI lab, demonstrating major gains in agentic programming and long-horizon tasks. Its dual focus on agentic coding and cyber defense, along with a nuanced licensing model, could influence how enterprises adopt open-source models for autonomous software development and security applications. GLM-5.3 uses a custom GLM-5.3 License: individuals and small-to-medium enterprises are free to use, fine-tune, and commercialize the model, but companies with over $10 billion in annual revenue for 12 consecutive months that offer model-as-a-service must first pass Z.AI&\#x27;s safety review. The model is a post-training-enhanced version of GLM-5.2, meaning the base architecture was not changed.

telegram · zaihuapd · Aug 28, 15:32

**Background**: Agentic programming is a software design pattern where an AI model does not just answer questions but takes actions, uses tools, and completes multi-step tasks autonomously. Terminal-Bench is a benchmark for evaluating AI agents in terminal environments, while DeepSWE is a long-horizon software engineering benchmark introduced by Datacurve to measure coding agents on original, contamination-free tasks spanning multiple repositories and languages. GLM-5.2 is the previous open-source model from Zhipu AI, and GLM-5.3 builds on it through post-training improvements.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tbench.ai/">Terminal - Bench</a></li>
<li><a href="https://deepswe.net/">DeepSWE Benchmark : GPT vs Claude for Agentic Coding</a></li>
<li><a href="https://www.emergentmind.com/topics/ai-agentic-programming">AI Agentic Programming</a></li>

</ul>
</details>

**Tags**: `#AI`, `#LLM`, `#open-source`, `#agentic programming`, `#GLM`

---

<a id="item-4"></a>
## [OpenAI to Cut Off Cursor Model Access After SpaceX Acquisition](https://openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex/) ⭐️ 8.0/10

OpenAI announced it will terminate its model-supply contract with Cursor, setting the suggested service cutoff date for November 12, 2026, and providing the maximum notice period allowed by the agreement. The decision follows SpaceX&\#x27;s acquisition of Cursor and cites concerns that SpaceX may not comply with OpenAI&\#x27;s service terms. Cursor is one of the most prominent AI coding tools, so this move signals that OpenAI is willing to enforce contractual terms even against a fast-growing ecosystem partner. It also intensifies the competitive split between OpenAI and Elon Musk&\#x27;s SpaceXAI, potentially affecting developers who rely on OpenAI-powered features inside Cursor. OpenAI said it could not be confident that SpaceX would honor the service terms, citing a track record of contract breaches, including behavior after acquiring Twitter and xAI&\#x27;s under-oath admission earlier this year that it had violated OpenAI&\#x27;s terms. The custom partnership had lasted nearly four years and included provisions allowing termination on a limited basis after a change of control.

telegram · zaihuapd · Aug 29, 02:24

**Background**: Cursor is an AI-powered code editor created by Anysphere, founded in 2022, and is a fork of Visual Studio Code that lets developers write code through natural-language instructions. By early 2026 it had reached a $29.3 billion valuation and more than $3 billion in annual recurring revenue. Its parent, SpaceXAI \(formerly xAI\), is Elon Musk&\#x27;s AI company that was acquired by SpaceX in February 2026 and later acquired Cursor in August 2026. OpenAI had a custom agreement to supply models to Cursor, which allowed it to wind down the relationship after a change of ownership.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cursor_%28code_editor%29">Cursor (code editor)</a></li>
<li><a href="https://en.wikipedia.org/wiki/XAI_%28company%29">XAI (company)</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#Cursor`, `#SpaceX`, `#AI`, `#Business`

---

<a id="item-5"></a>
## [US FTC Probes YouTube Account Bans, Says Content Policies May Mislead Users](https://www.bloomberg.com/news/articles/2026-08-27/us-ftc-probing-youtube-over-social-media-policies) ⭐️ 7.0/10

The US Federal Trade Commission is investigating YouTube&\#x27;s account bans and content moderation practices over potential violations of consumer protection law. The probe, which began last year, is in its final stages and nearing a potential lawsuit. This investigation could result in litigation against YouTube, potentially reshaping how major platforms enforce content policies and communicate them to users. It signals increased regulatory scrutiny of content moderation practices in the US. The FTC is examining whether YouTube violates its own user policies when banning or demoting content, and whether users are misled into believing they can post certain content that is later removed. Alphabet and YouTube have not been accused of wrongdoing, and both declined to comment.

telegram · zaihuapd · Aug 28, 07:48

**Background**: The Federal Trade Commission is a US agency that enforces consumer protection and antitrust laws. This probe reflects growing government scrutiny of how social media platforms moderate content and whether their stated policies align with their actual enforcement practices.

**Tags**: `#FTC`, `#YouTube`, `#content moderation`, `#consumer protection`, `#regulatory investigation`

---

<a id="item-6"></a>
## [Google Employees Test Gemini 3.8 Flash Preview, Praised Over 3.7 Flash](https://www.businessinsider.com/google-employees-testing-next-gemini-flash-3-8-model-2026-8) ⭐️ 6.0/10

Google employees have begun internal testing of a Gemini 3.8 Flash Preview, made available through Google&\#x27;s internal coding platform Jetski. One tester said the new model is clearly better than the recently released Gemini 3.7 Flash, though Google declined to comment. The news signals Google is accelerating its Flash model release cadence, reportedly aiming for near-monthly launches as its flagship Gemini models face delays. It suggests Google is prioritizing faster, cheaper models for practical, high-throughput deployments. Gemini 3.6 Flash was released in July 2026, with 3.7 Flash following about three weeks later. The 3.8 Flash Preview is accessible to staff via Jetski, an internal coding platform where early builds can be tested against real workloads before a public API or Vertex AI listing.

telegram · zaihuapd · Aug 28, 09:38

**Background**: Gemini Flash is Google&\#x27;s lighter, more cost-efficient line of large language models, designed for speed and high-volume tasks. Internal dogfooding platforms like Jetski are common in AI labs, letting employees evaluate early builds before public release. Google has also been developing agentic coding tools, with Jetski described as Google&\#x27;s internal version of Antigravity.

<details><summary>References</summary>
<ul>
<li><a href="https://www.businessinsider.com/google-employees-testing-next-gemini-flash-3-8-model-2026-8">Google Employees Are Already Testing the Next... - Business Insider</a></li>
<li><a href="https://shattered.io/gemini-3-8-flash-preview-google-testing-2026/">Google Tests Gemini 3.8 Flash 14 Days After 3.7</a></li>
<li><a href="https://rywalker.com/research/google-agent-smith">Google Agent Smith | Ry Walker Research | Ry Walker</a></li>

</ul>
</details>

**Tags**: `#Gemini`, `#Google`, `#AI`, `#Large Language Models`

---