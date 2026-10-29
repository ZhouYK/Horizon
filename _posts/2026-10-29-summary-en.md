---
layout: default
title: "Horizon Summary: 2026-10-29 (EN)"
date: 2026-10-29 23:03:53 +0000
lang: en
report: default
---

> From 195 items, 6 important content pieces were selected

---

1. [Anthropic rewrote its Messages API in Rust with Claude writing the code, cutting CPU use 40–50%](#item-1) ⭐️ 7.0/10
2. [Google Opens Third-Party Android App Store Registration With $10,000 Annual Fee](#item-2) ⭐️ 7.0/10
3. [Hacker group leaks records of over 41,000 DHS employees via Okta](#item-3) ⭐️ 7.0/10
4. [Google takes AI Mode search ads global as core ad growth slows](#item-4) ⭐️ 6.0/10
5. [Synology NAS Users Hit by LOCK3D Ransomware Campaign](#item-5) ⭐️ 6.0/10
6. [Claude Enterprise smart reports let managers flag off-topic AI use](#item-6) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Anthropic rewrote its Messages API in Rust with Claude writing the code, cutting CPU use 40–50%](https://latent.space/p/opus55/) ⭐️ 7.0/10

Anthropic migrated its Messages API from a single-region Python monolith to Rust, with Claude generating the implementation while engineers handled system design and validation by diffing old and new system outputs. The rewrite reduced CPU usage by roughly 40–50% and cut first-token latency by about 10–20%. This is a high-profile case of a major AI company rewriting a critical production API in Rust largely through AI-assisted coding, offering a concrete template for teams weighing similar migrations. The quantified CPU and latency gains also highlight that serving overhead — not just GPU inference — is a meaningful lever for LLM API performance and cost. Notably, the team started with no Rust developer on staff — the meeting-room joke being that they had none — with Claude producing code that engineers then designed around and validated through output diffing against the legacy Python service. The reported gains are CPU reduction of about 40–50% and first-token latency improvement of roughly 10–20%, meaning the win is concentrated in serving efficiency rather than model quality.

telegram · zaihuapd · Oct 29, 03:13

**Background**: Rust is a systems programming language that emphasizes performance, type safety and memory safety, enforcing memory safety at compile time via its borrow checker without a garbage collector, which is why it is increasingly adopted for high-throughput web services. Anthropic&\#x27;s Messages API is the core endpoint developers call to interact with Claude models, so its per-request overhead directly affects both latency and the cost of running the service at scale. First-token latency — the time between sending a prompt and receiving the first output token — is a key user-perceived responsiveness metric distinct from overall throughput.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Rust_%28programming_language%29">Rust (programming language)</a></li>
<li><a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-anthropic-claude-messages.html">Anthropic Claude Messages API - Amazon Bedrock</a></li>
<li><a href="https://inference.net/content/llm-latency/">9 Smart Ways to Reduce LLM Latency for Faster AI... | Inference.net</a></li>

</ul>
</details>

**Tags**: `#Rust`, `#Anthropic`, `#Claude`, `#AI-assisted development`, `#performance optimization`, `#code migration`

---

<a id="item-2"></a>
## [Google Opens Third-Party Android App Store Registration With $10,000 Annual Fee](https://www.landian.news/archives/127767.html) ⭐️ 7.0/10

Google has opened applications for third-party Android app stores to register for a new program that grants system-level privileges, including one-tap installation and background auto-updates, so users no longer see a confirmation dialog for every install from those stores. The program starts on December 1, 2026, on devices running Android 17 QPR2 or later, is voluntary, excludes the US, and costs $10,000 per year. This effectively lets approved third-party stores behave like first-party system software on Android, lowering the friction that has historically kept users and developers tied to Google Play. It could reshape app distribution economics outside the US, but the steep fee and Google&\#x27;s review requirements mean only well-funded players are likely to qualify. Applicants must hold an enterprise developer account and submit their full app catalog for Google&\#x27;s security scanning, and the program is limited to designated regions outside the United States. Rollout is future-dated to Android 17 QPR2 in December 2026, so no device supports it today, and Google retains approval authority over who gets the system-level install and update permissions.

telegram · zaihuapd · Oct 29, 04:39

**Background**: Android normally reserves privileged permissions such as silent app installation and background updates for system and preinstalled apps; sideloaded installs instead trigger a per-app confirmation flow. QPR stands for Quarterly Platform Release, a maintenance-and-feature update cadence Google introduced with Android 16, so Android 17 QPR2 would be the second such release of the Android 17 cycle. Google&\#x27;s app store rules have faced sustained antitrust scrutiny, including a US jury verdict that it illegally maintained a monopoly through Google Play, which adds pressure to open distribution.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.android.com/blog/posts/android-16-qpr-2-is-released?hl=zh-cn">Android 16 QPR2 已发布 - Android Developers&#x27; Blog</a></li>

</ul>
</details>

**Tags**: `#Android`, `#app stores`, `#Google`, `#mobile platforms`, `#platform policy`

---

<a id="item-3"></a>
## [Hacker group leaks records of over 41,000 DHS employees via Okta](https://www.theverge.com/tech/1021528/ice-cbp-data-leak) ⭐️ 7.0/10

A hacker group calling itself &quot;Department of Peace&quot; obtained records on more than 41,000 U.S. Department of Homeland Security employees through the Okta identity management service DHS uses, exposing names, job titles, phone numbers, email addresses and office locations. Roughly 21,000 of the records belong to Customs and Border Protection \(CBP\) and nearly 7,000 to Immigration and Customs Enforcement \(ICE\), with CISA and other DHS components also affected. The leak puts detailed contact and role information for tens of thousands of federal law enforcement and cybersecurity staff into public circulation, creating a ready-made target list for phishing, social engineering and harassment campaigns. It also raises fresh questions about how much sensitive employee data flows through third-party identity providers like Okta that government agencies rely on. The dataset is being hosted by DDoSecrets under the name &quot;Icepick&quot; and is said to also include information about surveillance tools available to the affected agencies. DHS did not respond to a request for comment, and it remains unclear whether login credentials or authentication secrets were exposed, or only directory-style profile data.

telegram · zaihuapd · Oct 29, 07:04

**Background**: Okta is one of the most widely used identity and access management \(IAM\) platforms, handling single sign-on, authentication and access control for employees of large enterprises and government agencies, which means it holds extensive user directories. DDoSecrets \(Distributed Denial of Secrets\) is a nonprofit leak-publishing site founded in 2018, often described as a successor to WikiLeaks, which previously released the 2020 &quot;BlueLeaks&quot; trove of U.S. police documents. Breaches touching Okta matter because compromising an identity provider can give attackers a foothold across every service that relies on it.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Okta,_Inc.">Okta, Inc. - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/DDoSecrets">DDoSecrets</a></li>
<li><a href="https://www.okta.com/solutions/iam-identity-and-access-management/">IAM (Identity and Access Management) - Okta</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#data breach`, `#Okta`, `#DHS`, `#privacy`

---

<a id="item-4"></a>
## [Google takes AI Mode search ads global as core ad growth slows](https://techcrunch.com/2026/10/28/google-expands-ai-search-ads-globally-as-core-ad-growth-slows/) ⭐️ 6.0/10

On Alphabet&\#x27;s third-quarter earnings call, Google said it is expanding ads in AI Mode to more markets worldwide and launching multi-turn conversational ads in the United States, as it tries to turn generative AI search into a new revenue stream. The company also said click-through rates on sponsored shopping listings inside AI Mode are now close to those of organic search results. This is one of the clearest signals yet that Google intends to monetize AI-generated search answers rather than let them cannibalize its advertising business, which matters for advertisers, publishers and rivals building AI search products. The timing is sensitive because Alphabet&\#x27;s stock fell more than 10% after hours as search ad growth decelerated, fueling doubts about how quickly AI search can offset slowing legacy ad revenue. Alphabet&\#x27;s third-quarter revenue reached $127.6 billion, up 25% year over year, but search ad revenue grew only 12%, down from 17% and 19% in the two prior quarters. The new formats include conversational ads that support multiple turns of dialogue and Gemini-powered ads that surface product details inside AI answers, though Google has not disclosed how much of total ad revenue AI Mode currently contributes.

telegram · zaihuapd · Oct 29, 01:43

**Background**: AI Mode is Google&\#x27;s generative AI layer inside Search, which answers queries with synthesized responses and follow-up suggestions instead of a plain list of blue links. Because these answers can absorb clicks that would otherwise reach advertisers&\#x27; sites, Google has been testing ad formats built with Gemini — including sponsored product listings and conversational ads — to keep the query commercially valuable. AI Overviews and AI Mode have already been shown to reduce click-through rates on top organic results, which is why ad placement inside AI answers is closely watched by marketers.

<details><summary>References</summary>
<ul>
<li><a href="https://business.google.com/us/accelerate/announcements/ads-in-ai-mode/">Ads in AI Mode - Accelerate with Google US</a></li>
<li><a href="https://blog.google/products/ads-commerce/google-marketing-live-search-ads/">New ad formats built with Gemini coming to Google Search</a></li>
<li><a href="https://icoda.io/ai/google-ai-mode-ads/">Google AI Mode Ads : What Marketers Must Know</a></li>

</ul>
</details>

**Tags**: `#Google`, `#AI search`, `#advertising`, `#monetization`, `#tech business`

---

<a id="item-5"></a>
## [Synology NAS Users Hit by LOCK3D Ransomware Campaign](https://www.v2ex.com/t/1252735) ⭐️ 6.0/10

Users are reporting that their Synology NAS devices have been infected by ransomware that encrypts files and appends the .LOCK3D or .L0CK3D extension, with ransom notes appearing in some directories. V2EX discussion threads include cases where even recently updated DSM systems were compromised, prompting an advisory with prevention and incident-response steps. NAS boxes hold years of personal and business data and are frequently exposed to the internet for remote access, making them a high-value, low-defensibility target. Because confirmed infections appear on current DSM versions, self-hosters and small IT admins cannot assume that simply staying patched is enough protection. The advisory&\#x27;s checklist is practical rather than technical: look for the .LOCK3D/.L0CK3D suffixes and ransom notes, shut down unnecessary public-facing services, update packages and container images, and verify that offline or offsite backups are genuinely immutable and not writable. If a device is already infected, the advice is to disconnect it from the network immediately and preserve logs and ransom notes before any cleanup.

telegram · zaihuapd · Oct 29, 05:22

**Background**: Synology NAS devices run DiskStation Manager \(DSM\), a Linux-based operating system that includes a built-in rule-based firewall for controlling inbound traffic, alongside file sharing, container hosting and remote-access packages. The .LOCK3D extension has previously been associated with C3RB3R, a ransomware strain from the Cerber family that was reported attacking TerraMaster TNAS devices as far back as late 2022, encrypting data and leaving the management interface unreachable. Ransomware typically renames victim files to mark them as encrypted, and C3RB3R uses two variants — appending &\#x27;.LOCK3D&\#x27; or inserting &\#x27;.L0CK3D&\#x27; — which is exactly the pattern reported here on Synology hardware.

<details><summary>References</summary>
<ul>
<li><a href="https://malware-guide.com/blog/how-to-remove-c3rb3r-ransomware-and-recover-lock3d-files">How to Remove C3RB3R Ransomware And Recover .LOCK3D Files</a></li>
<li><a href="https://www.youtube.com/watch?v=8RG-nCsjkM8">C3RB3R ransomware removal [.LOCK3D file virus]. - YouTube Urgent! .LOCK3D ransomware is attacking your TNAS Understanding Ransomware Threat Actors: LockBit - CISA C3RB3R Ransomware Removal Report - EnigmaSoft Ltd Decrypt .LOCK3D Virus File| (.LOCK3D) Ransomware Removal ...</a></li>
<li><a href="https://grokipedia.com/page/Synology_DSM_firewall">Synology DSM firewall</a></li>

</ul>
</details>

**Discussion**: The V2EX thread is largely cautionary: commenters report that infection occurred even on up-to-date DSM installations, which pushes the discussion toward limiting public exposure \(VPN, firewall rules, disabling QuickConnect-style access\) and toward treating tested, offline backups as the only reliable recovery path rather than paying a ransom.

**Tags**: `#security`, `#ransomware`, `#NAS`, `#Synology`, `#backup`

---

<a id="item-6"></a>
## [Claude Enterprise smart reports let managers flag off-topic AI use](https://mashable.com/tech/claude-smart-reports-anthropic-ai-worker-overview) ⭐️ 6.0/10

Anthropic has made smart reports generally available for Claude Enterprise, giving admins a dashboard that analyzes team conversations and surfaces usage, spend, output, and exchanges classified as personal or off-topic over the last 28 days. Paid Claude Enterprise customers can generate 10 reports per month at no extra cost. The feature pushes AI assistants deeper into workforce monitoring territory, letting companies justify per-seat AI spend with ROI data while raising uncomfortable questions about how employees&\#x27; chats with an AI are read, categorized, and reported to managers. It signals that enterprise AI competition is shifting from raw model capability toward governance, cost control, and administrative visibility. Reports only cover a rolling 28-day window and are capped at 10 free generations per month, and Anthropic notes availability varies by configuration, including for organizations using HIPAA configurations or customer-managed encryption keys. The smart reports ship alongside two other admin features, pooled group budgets and in-app surveys, all of which had previously been in beta.

telegram · zaihuapd · Oct 29, 07:49

**Background**: Claude Enterprise is Anthropic&\#x27;s top-tier plan for organizations deploying Claude at scale, offering admin controls, compliance options such as a HIPAA-ready configuration with a signed BAA, and centralized billing. As companies roll out AI assistants to hundreds of employees, IT and finance teams have demanded ways to see where token spend goes and whether usage is work-related. Smart reports, pooled budgets, and in-app surveys are Anthropic&\#x27;s answer: a set of admin-facing analytics tools rather than new model capabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://claude.com/resources/articles/smart-reports-surveys-pooled-budgets">Smart reports , surveys, and pooled group... | Claude by Anthropic</a></li>
<li><a href="https://www.zdnet.com/innovation/claude-enterprise-efficiency-cost-tracking/">These Claude Enterprise features let you track AI ROI... - ZDNET</a></li>
<li><a href="https://explainx.ai/blog/claude-enterprise-smart-reports-surveys-pooled-group-budgets-token-spend-roi-2026">Claude Enterprise Smart Reports : See What Spend Buys | explainx.ai</a></li>

</ul>
</details>

**Tags**: `#Anthropic`, `#Claude Enterprise`, `#AI monitoring`, `#workplace privacy`, `#enterprise AI`

---