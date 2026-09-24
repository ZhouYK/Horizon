---
layout: default
title: "Horizon Summary: 2026-09-24 (EN)"
date: 2026-09-24 23:04:00 +0000
lang: en
report: default
---

> From 153 items, 6 important content pieces were selected

---

1. [Anthropic Engineer Explains Why Claude&\#x27;s Writing Feels AI-to-AI](#item-1) ⭐️ 7.0/10
2. [OpenAI Says Apple&\#x27;s ChatGPT Integration Underperformed, Straining Partnership](#item-2) ⭐️ 7.0/10
3. [OpenAI Releases MentalHealthBench, an Open Benchmark for AI Mental Health Responses](#item-3) ⭐️ 7.0/10
4. [Claude Code cloud sessions go GA, with up to $250 in credits](#item-4) ⭐️ 6.0/10
5. [China&\#x27;s Three Telecom Operators Halt Installment Phone Financing, Ending &\#x27;0 Yuan Phone&\#x27; Deals](#item-5) ⭐️ 6.0/10
6. [US ITC Opens Section 337 Investigation into DRAM Devices After Netlist Complaint](#item-6) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Anthropic Engineer Explains Why Claude&\#x27;s Writing Feels AI-to-AI](https://tech.ifeng.com/c/8wfFOVTfzvZ) ⭐️ 7.0/10

Anthropic engineer Jackson Kernion publicly explained that later Claude models have degraded in writing style because training shifted toward math and code, and because the models were heavily trained to write technical explanations aimed at other AI models rather than humans, producing a recognizable &quot;Claude voice.&quot; He attributes the root cause to reinforcement learning reward design, saying models need stronger rewards for concise, easy-to-understand prose, and notes that Opus 5.5 has improved the balance though it is not yet clearly better than Opus 4.6. This is a rare first-party account of how reward design in reinforcement learning directly shapes the everyday reading experience of millions of users, and it affects anyone who relies on Claude for writing, documentation, or customer-facing copy. It also highlights a broader industry tension: as models are increasingly trained and evaluated for agentic, code-heavy, machine-consumed tasks, human-facing prose quality can quietly erode. Kernion&\#x27;s explanation ties the degradation to two concrete training pressures — an emphasis on math and coding, and large-scale generation of technical explanations consumed by other AI models — and he identifies reward shaping, not data alone, as the root cause. The remedy he describes is straightforward in principle: reward concise, accessible expression more heavily, though the improvement he cites \(Opus 5.5\) is modest and not yet a clear win over Opus 4.6.

telegram · zaihuapd · Sep 24, 02:00

**Background**: Large language models are typically fine-tuned with reinforcement learning, where a reward signal tells the model which outputs are &quot;good,&quot; so whatever the reward function measures tends to become the model&\#x27;s habit. If rewards disproportionately favor correct math, working code, or explanations that another model can parse, the model has little incentive to polish style for human readers. Anthropic&\#x27;s Claude family, including the Opus line, is one of the leading commercial assistants — Claude Opus 5.5 is described as Anthropic&\#x27;s flagship model for demanding reasoning, coding, and long-horizon agentic work.

<details><summary>References</summary>
<ul>
<li><a href="https://openrouter.ai/anthropic/claude-opus-5.5">Claude Opus 5.5 - API Pricing &amp; Benchmarks | OpenRouter</a></li>
<li><a href="https://claude.com/product/overview">The AI for Problem Solvers | Claude by Anthropic</a></li>
<li><a href="https://www.emergentmind.com/topics/behavior-shaping-incentive-mechanism">Behavior-Shaping Incentive Mechanism</a></li>

</ul>
</details>

**Tags**: `#Anthropic`, `#Claude`, `#LLM`, `#Reinforcement Learning`, `#AI Writing Quality`

---

<a id="item-2"></a>
## [OpenAI Says Apple&\#x27;s ChatGPT Integration Underperformed, Straining Partnership](https://www.ft.com/content/256c4b36-a6c8-49ee-aa15-81cb089b2ced) ⭐️ 7.0/10

In a court filing dated September 23, 2026, OpenAI stated that Apple&\#x27;s ChatGPT integration &quot;performed severely poorly&quot; and expressed frustration that users showed little interest in it. The revelation comes as the two companies&\#x27; relationship has deteriorated: Apple has sued OpenAI over trade secrets and in January partnered with Google to rebuild Siri AI using Gemini, while the filing itself emerged from an antitrust lawsuit brought by xAI. The disclosure publicly confirms that the 2024 Apple–OpenAI deal failed to deliver the reach OpenAI expected, and Apple&\#x27;s pivot to Google Gemini for Siri reshapes who controls the default AI assistant on hundreds of millions of iPhones. It also injects OpenAI&\#x27;s own complaints into antitrust litigation over AI distribution deals, potentially becoming evidence about how such partnerships are structured and whether they foreclose rivals. The ChatGPT integration inside Apple Intelligence was opt-in and default-off, requiring several steps to activate, which OpenAI points to as a key reason for low adoption. Notably, these complaints surfaced through legal filings in xAI&\#x27;s antitrust suit rather than through any product or partnership announcement.

telegram · zaihuapd · Sep 24, 05:15

**Background**: Apple Intelligence is Apple&\#x27;s suite of AI features, announced at WWDC in June 2024 and built into iOS 18, iPadOS 18 and macOS Sequoia, which combined on-device processing with server-side models and included an integration with OpenAI&\#x27;s ChatGPT. xAI is the AI company founded by Elon Musk in 2023 and maker of the Grok chatbot, whose antitrust suit against OpenAI and Apple provides the legal venue for these filings. Antitrust scrutiny in this space focuses on whether exclusive default-assistant deals on dominant platforms unfairly lock out competing AI providers.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Apple_Intelligence">Apple Intelligence</a></li>
<li><a href="https://grokipedia.com/page/XAI_%28company%29">xAI</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#Apple`, `#ChatGPT`, `#Antitrust`, `#AI Partnerships`

---

<a id="item-3"></a>
## [OpenAI Releases MentalHealthBench, an Open Benchmark for AI Mental Health Responses](https://openai.com/zh-Hans-CN/index/introducing-mentalhealthbench/) ⭐️ 7.0/10

OpenAI released MentalHealthBench, an open benchmark designed to evaluate how AI models respond in real mental health conversations, developed together with more than 80 licensed mental health experts across 22 countries. The benchmark covers scenarios involving adults, adolescents, caregivers, and clinicians, and it measures behaviors such as safety, gathering context, preserving user autonomy, and offering actionable advice. Mental health is one of the highest-stakes domains where people increasingly turn to chatbots, so a shared, expert-vetted evaluation standard gives model developers and clinicians a common yardstick for measuring risk and progress. It also fits a broader trend of AI labs publishing domain-specific safety benchmarks rather than relying only on generic capability tests. The benchmark focuses on behavioral criteria rather than pure knowledge accuracy, spanning dimensions like safety, context gathering, respecting user autonomy, and giving actionable guidance. OpenAI reports that AI performance on mental health questions shows steady improvement, but it explicitly cautions that ChatGPT is not a substitute for professional treatment.

telegram · zaihuapd · Sep 24, 06:00

**Background**: AI benchmarks are standardized test suites that let researchers compare models on the same tasks, and in recent years labs have created specialized ones for safety-critical areas such as medicine, cybersecurity, and mental health. Mental health conversations are especially sensitive because poor model responses — failing to recognize crisis signals, giving unsafe advice, or overriding a user&\#x27;s decisions — can cause real harm, and regulators and clinicians have pushed for transparent evaluation methods.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/introducing-mentalhealthbench/">Introducing MentalHealthBench | OpenAI</a></li>
<li><a href="https://www.unite.ai/openai-debuts-mentalhealthbench-for-ai-mental-health-conversations/">OpenAI Debuts MentalHealthBench for AI Mental Health Conversations</a></li>
<li><a href="https://cdn.openai.com/ctf-cdn/MentalHealthBench_A_Comprehensive_Benchmark_of_AI_Capabilities_in_Realistic_Mental_Health_Conversations.pdf">[PDF] MentalHealthBench: An Expert-Informed Benchmark of AI Capabilities in Realistic Mental Health Conversations - OpenAI</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#mental health`, `#benchmark`, `#OpenAI`, `#evaluation`

---

<a id="item-4"></a>
## [Claude Code cloud sessions go GA, with up to $250 in credits](https://code.claude.com/docs/en/claude-code-on-the-web) ⭐️ 6.0/10

Anthropic has graduated Claude Code cloud sessions \(previously known as Claude Code on the web\) out of research preview into general availability for Pro, Max, Team, and Enterprise users. To mark the launch, existing subscribers get a one-time cloud credit — $100 for Pro and $250 for Max — claimable via an official sign-up page or the /claim-credit command inside Claude Code. The shift from a browser-based beta to persistent cloud sessions turns Claude Code from a tool you have to babysit in a terminal into an always-on agent you can dispatch work to and check on later. That matters for developers running long builds, test suites, or multi-step refactors, and it puts Anthropic in more direct competition with cloud-hosted coding agents from other vendors. Cloud sessions keep running after you close your laptop and can be viewed or taken over from a browser, phone, desktop app, or terminal — the docs also mention moving sessions with --cloud and --teleport flags and auto-fixing pull requests. There are real caveats: credits must be claimed by 11:59 PM Pacific on October 7 and expire at 11:59 PM on November 4, eligibility is determined per account after login, and Anthropic&\#x27;s supported-region list currently excludes mainland China, Hong Kong, and Macau.

telegram · zaihuapd · Sep 24, 02:45

**Background**: Claude Code is Anthropic&\#x27;s agentic coding tool, originally a terminal-based assistant that reads and edits files in a local repository. Cloud sessions extend the same workflow to Anthropic-hosted environments, so an agent can keep working on a task without a developer&\#x27;s machine being online. Cloud environments are configurable — network access can be allowed or denied, environment variables can be set, and setup scripts can run before the agent starts.

<details><summary>References</summary>
<ul>
<li><a href="https://code.claude.com/docs/en/claude-code-on-the-web">Use Claude Code in the cloud - Claude Code Docs</a></li>
<li><a href="https://claude.com/blog/claude-code-on-the-web">Claude Code on the web | Claude by Anthropic</a></li>
<li><a href="https://code.claude.com/docs/en/cloud-environments">Configure cloud environments - Claude Code Docs</a></li>

</ul>
</details>

**Tags**: `#claude-code`, `#anthropic`, `#ai-agents`, `#developer-tools`, `#cloud-computing`

---

<a id="item-5"></a>
## [China&\#x27;s Three Telecom Operators Halt Installment Phone Financing, Ending &\#x27;0 Yuan Phone&\#x27; Deals](https://finance.sina.com.cn/jjxw/2026-09-24/doc-inisxhnx5270778.shtml) ⭐️ 6.0/10

Starting September 24, 2026, China Mobile, China Telecom, and China Unicom have stopped accepting new applications for their financial installment phone-purchase services, fully suspending &\#x27;0 yuan phone&\#x27; programs such as Hebao Credit Buy \(和包信用购\), Cheng Fenqi \(橙分期\), and Wo Fenqi \(沃分期\). Existing customers who already signed installment contracts are unaffected and their agreements remain in force, while customer service representatives have confirmed the suspension but the operators have issued no formal statement. These installment schemes were one of the heaviest sources of consumer complaints in China&\#x27;s telecom sector, so their suspension marks a significant shift in how operators bundle devices with consumer credit and could reshape phone retail channels and the consumer-finance business that operators and their partners relied on. It also signals growing regulatory and consumer-protection pressure on &\#x27;free phone&\#x27; marketing that in practice signed users up for loans. The suspension applies only to new applications; previously signed installment contracts continue to be honored, and neither a concrete reason nor a resumption date has been given, with operators describing it vaguely as a &\#x27;product upgrade.&\#x27; Because these deals were typically structured as loans issued through partner financial institutions, users often faced credit-report implications, early-termination fees, and contract lock-ins that were not obvious at the point of sale.

telegram · zaihuapd · Sep 24, 08:46

**Background**: &\#x27;0 yuan phone&\#x27; promotions let customers take a handset home without paying upfront, but in reality they sign an installment loan whose repayments are bundled into a monthly telecom plan, usually over 12 to 36 months. The loan is issued by a bank or consumer-finance company partnered with the operator, so missing a payment can affect the user&\#x27;s credit record and early cancellation can trigger penalties. Regulators and consumer groups have repeatedly flagged such offers for opaque terms and aggressive sales tactics, making them a frequent subject of complaints.

<details><summary>References</summary>
<ul>
<li><a href="https://www.3dmgame.com/news/202609/3954492.html">三大运营商叫停 “0元购机” 实为金融 分 期 购机_3DM单机</a></li>
<li><a href="https://waphn.189.cn/hd/zifeizq/wap/zfzx/yxhdHYcfq.html">橙 分 期</a></li>

</ul>
</details>

**Tags**: `#中国电信运营商`, `#金融分期`, `#消费者权益`, `#行业监管`, `#0元购机`

---

<a id="item-6"></a>
## [US ITC Opens Section 337 Investigation into DRAM Devices After Netlist Complaint](https://mp.weixin.qq.com/s/YtQiGdMulacmBbG6_pC_HQ) ⭐️ 6.0/10

On September 23, 2026, the US International Trade Commission voted to institute a Section 337 investigation into certain DRAM devices, their downstream products and components. The complaint was filed on August 11, 2026 by Netlist, which alleges infringement of multiple US patents and requests a limited exclusion order and a cease-and-desist order, naming Micron, Hewlett Packard Enterprise, Lenovo and Supermicro as respondents. Section 337 remedies are import bans, so if Netlist prevails the affected DRAM products and the servers and modules built around them could be barred from entering the United States, hitting memory supply chains and the server OEMs named as respondents. It also underscores how patent licensing disputes over memory technology increasingly play out at the ITC, where proceedings are typically faster than district court litigation. The ITC action is at the institution stage, meaning the Commission has only agreed to investigate and has made no finding on the merits; the case will proceed before an administrative law judge with possible review by the full Commission. Remedies in Section 337 cases are exclusion orders and cease-and-desist orders rather than monetary damages, and because downstream product makers such as HPE, Lenovo and Supermicro are named, the dispute reaches beyond DRAM chips themselves to the systems that incorporate them.

telegram · zaihuapd · Sep 24, 10:25

**Background**: DRAM \(dynamic random-access memory\) is the type of semiconductor memory used as main memory in computers, servers and many consumer devices; each cell stores a bit as charge on a microscopic capacitor switched by a transistor. Section 337 of the Tariff Act of 1930 \(19 U.S.C. § 1337\) gives the US International Trade Commission authority to investigate unfair practices in import trade, most commonly patent infringement, with hearings before administrative law judges and final review by the Commission. Netlist is a US intellectual-property licensing company that has for years asserted memory-module and DRAM-related patents against major memory makers and system vendors, and this complaint is the latest step in that campaign.

<details><summary>References</summary>
<ul>
<li><a href="https://patentcourt.org/procedure/itc-section-337/">ITC Section 337 investigations — Patent Court</a></li>
<li><a href="https://en.wikipedia.org/wiki/Dynamic_random-access_memory">Dynamic random-access memory - Wikipedia</a></li>
<li><a href="https://www.lippes.com/capabilities/itc-section-337-investigations-476.pdf">ITC Section 337 Investigations</a></li>

</ul>
</details>

**Tags**: `#DRAM`, `#ITC Section 337`, `#patent litigation`, `#semiconductor industry`, `#supply chain`

---