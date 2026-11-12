---
layout: default
title: "Horizon Summary: 2026-11-12 (EN)"
date: 2026-11-12 23:03:38 +0000
lang: en
report: default
---

> From 187 items, 4 important content pieces were selected

---

1. [Google Launches Gemini Decisions API for Fast Multimodal Decision-Making](#item-1) ⭐️ 8.0/10
2. [US Commerce Department Finalizes Rule to Block Chinese AI Firms&\#x27; Remote Chip Access](#item-2) ⭐️ 7.0/10
3. [Apple details Secure Exclaves to protect audio/video privacy](#item-3) ⭐️ 7.0/10
4. [NapCatQQ README Wiped, Replaced With Only &\#x27;Ending&\#x27;](#item-4) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Google Launches Gemini Decisions API for Fast Multimodal Decision-Making](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/) ⭐️ 8.0/10

Google released the Gemini Decisions API, powered by a new Gemini Decision 1 model, which answers closed-ended questions such as yes/no, multiple-choice \(up to 255 options\), and rubric scoring across text, images, audio, video, and PDFs. It can evaluate up to 1,000 questions in a single call, returns probabilities and confidence scores, and runs with roughly 150–250 ms end-to-end latency at $0.10 per million input tokens, with output tokens billed at no cost. Decision-making steps in AI agents — choosing a tool, checking a policy, or routing a request to the right model — are frequent, small, and latency-sensitive, and a cheap purpose-built model for them can cut both cost and response time compared with calling a general-purpose model. Google claims it is nearly 5x cheaper than a Gemini 3.5 Flash-Lite based approach, which could make it a default building block for agent pipelines and for the emerging practice of model routing. The API is scoped narrowly to closed-ended questions rather than free-form generation, and it answers in a single fast pass over the input, so it is not a substitute for a full generative model. It is already available in Google AI Studio, and the per-million-input-token price of $0.10 with free output tokens reflects the very short structured answers the model returns.

telegram · zaihuapd · Nov 12, 00:28

**Background**: AI agents built on large language models routinely need to make small judgment calls: which of many available tools to invoke, whether a planned action violates a safety or business rule, or which model in a fleet should handle a given request. Running a full generative model for each of these micro-decisions is expensive and slow, so developers have increasingly looked for lightweight classifiers or specialized endpoints. Model routing — matching each task to the cheapest model that can handle it well — has become a common cost-control strategy, and tool catalogs in agents tend to degrade accuracy as they grow, making better selection logic valuable.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/">Gemini Decisions API : Fast multimodal decisions</a></li>
<li><a href="https://aistudio.google.com/docs/decisions-api">Decisions API - Gemini API | Google AI Studio</a></li>
<li><a href="https://openrouter.ai/google/gemini-decision-1">Gemini Decision 1 - API Pricing &amp; Providers | OpenRouter</a></li>

</ul>
</details>

**Tags**: `#Google`, `#API`, `#multimodal`, `#decision-making`, `#AI`

---

<a id="item-2"></a>
## [US Commerce Department Finalizes Rule to Block Chinese AI Firms&\#x27; Remote Chip Access](https://www.theinformation.com/articles/commerce-department-finalizing-long-awaited-ai-remote-access-rule) ⭐️ 7.0/10

The US Commerce Department is finalizing a long-awaited rule that would stop Chinese AI companies from remotely accessing advanced AI chips hosted in overseas data centers, with publication possible as early as this month. The rule would extend existing semiconductor export restrictions to seven additional countries — including Malaysia, Singapore and Thailand — in order to close both the remote-access loophole and chip-smuggling routes, and is being finalized after consultations with other government agencies. This closes what Washington sees as the biggest remaining gap in its AI chip controls: restrictions have so far governed where chips can be shipped, not who can rent them remotely, so Chinese labs could train frontier models on overseas cloud capacity. The rule would reshape global AI compute access, pressure Southeast Asian data-center hubs, and potentially cost NVIDIA overseas demand it has been lobbying to protect. The rule targets remote access rather than physical shipment, meaning overseas operators of US-origin advanced accelerators could face restrictions on serving China-linked customers, and the seven-country expansion adds Malaysia, Singapore and Thailand to the list of jurisdictions under scrutiny. It is still being finalized in inter-agency review, so scope, thresholds and any grace period for existing contracts remain subject to change before publication.

telegram · zaihuapd · Nov 12, 03:42

**Background**: US export controls on advanced AI chips — principally NVIDIA&\#x27;s high-end GPUs — have restricted which countries can receive them, aimed at slowing China&\#x27;s frontier AI development. Because those rules were written around physical shipments, Chinese firms could still rent compute from data centers in third countries such as Singapore or Malaysia, or route chips through intermediaries. The White House has asked Congress to legislate on the issue and pressed Commerce to draft this rule, while NVIDIA has argued that restricting remote access would hamper the global reach of US AI infrastructure.

<details><summary>References</summary>
<ul>
<li><a href="https://www.forbes.com/sites/viviantoh/2026/08/31/the-ai-chip-wars-new-front-control-the-cloud-not-the-silicon/">The U.S. Tried To Keep AI Chips From China. The Cloud Created ...</a></li>
<li><a href="https://www.explainx.ai/blog/trump-ai-chip-export-controls-china-remote-access-august-2026">Trump AI Chip Rules: Closing the Cloud Loophole (Aug 2026 ...</a></li>

</ul>
</details>

**Tags**: `#export-controls`, `#AI-chips`, `#US-China`, `#semiconductor-policy`, `#NVIDIA`

---

<a id="item-3"></a>
## [Apple details Secure Exclaves to protect audio/video privacy](https://security.apple.com/blog/secure-exclaves/) ⭐️ 7.0/10

On November 12, Apple published a security research post detailing Secure Exclaves, a protected and compartmentalized runtime that processes camera and microphone data separately from the rest of the system. The architecture is already used by HomeView&\#x27;s face and sound recognition and by the privacy indicator on iPhone 18 Pro, where dedicated hardware verifies the microphone dot&\#x27;s color, brightness and visibility before audio is allowed into the main system. The recording indicator is the user&\#x27;s main signal that a microphone or camera is active, so hardware-enforced verification that it is genuinely visible and unspoofed closes a well-known attack surface for covert surveillance. It also signals Apple&\#x27;s broader push to move sensitive sensor processing into isolated enclaves, which could become a template for third-party apps that need ambient sensing without collecting raw data. Apps in ambient-sensing mode receive only the necessary recognition results rather than raw audio or video, and data processed inside a Secure Exclave cannot be accessed by the rest of the system. Apple additionally requires the Siri audio session indicator to stay on continuously during the session and for at least three seconds in total, making it harder to hide or fake the dot.

telegram · zaihuapd · Nov 12, 09:13

**Background**: Secure Enclaves are already familiar as the isolated chip area on iPhones that stores biometric and encryption secrets; Secure Exclaves extend the same isolation idea to runtime environments handling sensor data. Apple&\#x27;s HomeView device uses always-on cameras and microphones for face and voice recognition, which raises the obvious question of how that data is kept private. The traditional privacy indicator is a software-driven dot, and researchers have long shown that malware or display manipulation could in principle obscure it.

<details><summary>References</summary>
<ul>
<li><a href="https://security.apple.com/blog/secure-exclaves">Secure Exclaves and Ambient Sensing - Apple Security Research</a></li>
<li><a href="https://www.macrumors.com/2026/11/12/apple-homeview-secure-exclaves/">Apple Explains How HomeView Keeps Camera Data Private</a></li>
<li><a href="https://appleinsider.com/articles/26/11/12/a-detailed-explanation-of-apples-secure-exclaves-has-been-shared">A detailed explanation of Apple&#x27;s Secure Exclaves has been ...</a></li>

</ul>
</details>

**Tags**: `#Apple`, `#Security Architecture`, `#Privacy`, `#Secure Enclaves`, `#Audio/Video`

---

<a id="item-4"></a>
## [NapCatQQ README Wiped, Replaced With Only &\#x27;Ending&\#x27;](https://github.com/NapNeko/NapCatQQ) ⭐️ 6.0/10

The GitHub README of NapCatQQ, a widely-used OneBot 11 QQ bot framework, has been erased and replaced with just two lines: &quot;Ending&quot; and &quot;到这里告一段落&quot; \(roughly, &quot;this is where it ends for now&quot;\). No official explanation, announcement, or migration notice was posted alongside the change, and the repository still shows roughly 12.7k stars and 1.8k forks. NapCatQQ is one of the most popular ways to run QQ bots on top of the official NTQQ client, so its apparent shutdown leaves a large base of bot developers and server operators looking for a replacement. The silent, unexplained nature of the change also fits a pattern of third-party QQ automation projects being discontinued under platform or legal pressure, which would ripple across the broader OneBot ecosystem. The change is only visible in the README: the code repository itself has not \(as of the report\) been archived or deleted, and no deprecation timeline, successor project, or data-migration path has been communicated. Because NapCatQQ works by hooking into the official NTQQ client rather than using a public API, it has always been exposed to client updates and terms-of-service enforcement.

telegram · zaihuapd · Nov 12, 12:15

**Background**: OneBot 11 \(formerly CQHTTP\) is a widely adopted standard that lets QQ bot plugins talk to a separate &quot;protocol-side&quot; program, so developers can write bot logic once and swap out the underlying QQ connection layer. Historically those connection layers were built on third-party clients like 酷Q or on the Mirai framework; NapCatQQ represents the newer generation built on Tencent&\#x27;s official NTQQ client. Such projects sit in a grey zone — they automate an official client in ways Tencent&\#x27;s terms may not permit — and several predecessors \(including 酷Q\) have been shut down abruptly, which is why a bare &quot;Ending&quot; README reads as an ominous signal to the community.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/NapCatQQ">NapCatQQ</a></li>
<li><a href="https://www.itxiaohui.top/archives/ihMhrPSB">从 NapCat 到智能 QQ 机 器 人 ：我的 OneBot 11 实验记录与开发思路</a></li>
<li><a href="https://blog.csdn.net/weixin_41240940/article/details/114310656">推荐一个node QQ 机 器 人 框 架 - onebot _ onebot 框 架 -CSDN博客</a></li>

</ul>
</details>

**Tags**: `#open-source`, `#QQ-bot`, `#OneBot`, `#project-shutdown`, `#community-news`

---