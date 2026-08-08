---
layout: default
title: "Horizon Summary: 2026-08-08 (EN)"
date: 2026-08-08
lang: en
report: default
---

> From 239 items, 11 important content pieces were selected

---

1. [China Overtakes US in R&amp;D Spending for First Time in 2024](#item-1) ⭐️ 8.0/10
2. [Critical macOS Screen Sharing Flaw Allows Passwordless Login, Patched](#item-2) ⭐️ 8.0/10
3. [Microsoft Edge to Disable Legacy Ad-Blocker Extensions, Following Chrome](#item-3) ⭐️ 7.0/10
4. [Claude Code Auto Mode Now Default, Blocking Dangerous Commands](#item-4) ⭐️ 7.0/10
5. [xAI Releases Imagine Image 2.0 with Editing, Ranks Second on Arena](#item-5) ⭐️ 7.0/10
6. [Moonshot AI Adds State-Backed Investors, Restructures for Hong Kong IPO](#item-6) ⭐️ 7.0/10
7. [Claude Code Adds Cross-Session Messaging for AI Sessions](#item-7) ⭐️ 6.0/10
8. [X Launches Original Content Rewards, Phases Out Old Revenue Share](#item-8) ⭐️ 6.0/10
9. [Dopamine 3.0 Jailbreak Adds Support for iOS 26 on A12/A13 iPhones](#item-9) ⭐️ 6.0/10
10. [Tencent WorkBuddy Named Top Strategic AI Product, Leads China Office Agent Market](#item-10) ⭐️ 6.0/10
11. [115 Cloud Drive API Platform to Suspend Service from Aug 9, 2026](#item-11) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [China Overtakes US in R&amp;D Spending for First Time in 2024](https://www.nikkei.com/article/DGXZQOSG05ALB0V00C26A8000000/) ⭐️ 8.0/10

According to Japan&\#x27;s MEXT &\#x27;Science and Technology Indicators 2026&\#x27;, China&\#x27;s total R&amp;D spending in 2024 reached 97.1 trillion yen, up 13.1% year-on-year, surpassing the US \(95.3 trillion yen\) to rank first worldwide for the first time. The growth was driven largely by corporate investment in computer, electronics, and optical products manufacturing. This milestone signals China&\#x27;s rapid rise in global innovation and its strategic focus on high-tech industries. It may intensify technology competition and prompt other countries to reconsider their own R&amp;D policies and funding priorities, affecting governments, corporations, and research institutions worldwide. The report is published by Japan&\#x27;s Ministry of Education, Culture, Sports, Science and Technology. China&\#x27;s business-sector R&amp;D spending reached 75.4 trillion yen, and the country had previously led in scientific paper output \(2017\), top-10% cited papers \(2018\), and top-1% cited papers \(2019\).

telegram · zaihuapd · Aug 8, 06:16

**Background**: R&amp;D expenditure covers spending on research and experimental development across public and private sectors. The top-1% highly cited papers are a standard indicator of high-impact research, measured by the Essential Science Indicators \(ESI\) database. China&\#x27;s shift from a low-cost manufacturing hub to an innovation-driven economy, supported by state subsidies and corporate investment, has been a key driver of its rising R&amp;D metrics.

<details><summary>References</summary>
<ul>
<li><a href="https://zhuanlan.zhihu.com/p/602627864">一文详解ESI高被引论文评选规则！高被引论文，你想知道都在这里</a></li>
<li><a href="https://baike.baidu.com/item/ESI%E5%85%A8%E7%90%83Top1%%E9%AB%98%E8%A2%AB%E5%BC%95%E8%AE%BA%E6%96%87/63991828">ESI全球Top1%高被引论文 - 百度百科</a></li>

</ul>
</details>

**Discussion**: No community comments were available for this news item.

**Tags**: `#R&amp;D`, `#China`, `#science-policy`, `#economics`, `#technology`

---

<a id="item-2"></a>
## [Critical macOS Screen Sharing Flaw Allows Passwordless Login, Patched](https://x.com/calif_io/status/2086022794840793454) ⭐️ 8.0/10

Security researcher Calif published a proof-of-concept \(PoC\) for CVE-2026-65400, a critical macOS Screen Sharing vulnerability that lets network attackers log in as any user without a password. Apple fixed the issue in macOS 26.6.1, as well as Sequoia 15.7.9 and Sonoma 14.8.9, and a full technical analysis is expected tomorrow. This is a high-impact authentication bypass affecting a widely used remote-access feature; any Mac with Screen Sharing enabled is exposed to remote compromise. Users should upgrade immediately, and the upcoming PoC may lead to wider exploitation if patches are not applied promptly. The vulnerability is an authentication issue fixed with improved state management; affected versions include macOS Tahoe 26.6.1, Sequoia 15.7.9, and Sonoma 14.8.9. As a temporary mitigation, users can disable Screen Sharing if they cannot update immediately.

telegram · zaihuapd · Aug 8, 14:20

**Background**: Screen Sharing is a macOS feature that allows remote control of a Mac over the network. CVE-2026-65400 is an authentication bypass that does not require valid credentials; PoC \(Proof of Concept\) is a demonstration proving a vulnerability is real. Apple&\#x27;s security updates typically address such flaws by improving state management.

<details><summary>References</summary>
<ul>
<li><a href="https://www.gate.com/zh/news/detail/macos-screen-sharing-vulnerability-cve-2026-65400-patched-in-version-2661-23306391">macOS 屏幕共享漏洞（CVE-2026-65400）已在 26.6.1 版本中修复；无需...</a></li>
<li><a href="https://nvd.nist.gov/vuln/detail/CVE-2026-65400">NVD - CVE-2026-65400</a></li>
<li><a href="https://cvefeed.io/vuln/detail/CVE-2026-65400">CVE-2026-65400 - Apple macOS Screen Sharing Authentication Bypass</a></li>

</ul>
</details>

**Tags**: `#security`, `#macOS`, `#vulnerability`, `#CVE`

---

<a id="item-3"></a>
## [Microsoft Edge to Disable Legacy Ad-Blocker Extensions, Following Chrome](https://www.theverge.com/tech/976880/microsoft-edge-extensions-ad-blockers-mv2-mv3) ⭐️ 7.0/10

Microsoft Edge announced it will end support for Manifest V2 extensions, disabling legacy ad blockers like uBlock Origin, with consumer transition starting this month and completion targeted by the end of 2026. Enterprise support will end in early 2027. This marks another major browser phasing out Manifest V2, significantly narrowing the options for users of popular ad blockers such as uBlock Origin. The move forces developers to migrate to MV3, which some ad blockers argue reduces effectiveness due to API limitations. Microsoft noted that only 58 MV2 extensions in the Edge add-ons store have real usage, and only 3 of them do not yet offer an MV3 version. Affected users can switch to alternatives like uBlock Origin Lite or use browsers such as Opera or Firefox that continue to support MV2 extensions.

telegram · zaihuapd · Aug 8, 01:14

**Background**: Browser extensions are small programs that customize browsing experiences, such as ad blockers. Manifest V2 \(MV2\) and Manifest V3 \(MV3\) are the extension platform specifications in Chrome and other Chromium browsers like Edge. MV3, introduced in 2020, aims to improve privacy, security, and performance, but replaces the powerful webRequest blocking API with a less flexible declarativeNetRequest API, which some say limits ad-blocking capabilities. Chrome began phasing out MV2 earlier, and Edge is now following suit.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.chrome.com/docs/extensions/mv2/">About Manifest V2 | Chrome for Developers</a></li>
<li><a href="https://developer.chrome.com/docs/extensions/develop/migrate/what-is-mv3">Extensions / Manifest V 3 | Chrome for Developers</a></li>

</ul>
</details>

**Tags**: `#Microsoft Edge`, `#Manifest V2`, `#uBlock Origin`, `#Ad blocking`, `#Browser extensions`

---

<a id="item-4"></a>
## [Claude Code Auto Mode Now Default, Blocking Dangerous Commands](https://claude.com/blog/auto-mode-default-in-claude-code) ⭐️ 7.0/10

Starting August 14, Claude Code enables automatic mode by default for new sessions on Pro, Max, and Team plans. The built-in classifier checks each tool call and blocks irreversible, destructive, or out-of-environment operations, and the extra overhead is now free for these users. This marks a significant shift in AI coding agent safety: default-on safeguards rather than opt-in permission prompts. It could reduce human error in approving dangerous commands, as Anthropic&\#x27;s study found users only identified 13.6% of risky actions, and may push competitors toward similar automatic safety layers. Auto mode routes tool calls through a classifier; deny rules and explicit ask rules still take precedence over the classifier. Enterprise, Claude API, and cloud platform users must still enable it manually, with a gradual default rollout planned over the next month.

telegram · zaihuapd · Aug 8, 03:02

**Background**: Claude Code is Anthropic&\#x27;s agentic coding tool that helps developers understand codebases, edit files, run commands, and ship features from natural-language descriptions. Auto mode was introduced as a way to reduce permission-prompt fatigue while maintaining safety; Anthropic&\#x27;s engineering blog notes users approve 93% of permission prompts, so automated classifiers can relieve that burden. The new default rollout for paid plans reflects confidence in the classifier&\#x27;s 89% interception rate of dangerous commands.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/engineering/claude-code-auto-mode">How we built Claude Code auto mode: a safer way to skip ...</a></li>
<li><a href="https://code.claude.com/docs/en/auto-mode-config">Configure auto mode - Claude Code Docs</a></li>
<li><a href="https://claude.com/blog/auto-mode">Auto mode for Claude Code | Claude by Anthropic</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Claude Code`, `#Safety`, `#Developer Tools`

---

<a id="item-5"></a>
## [xAI Releases Imagine Image 2.0 with Editing, Ranks Second on Arena](http://grok.com/imagine) ⭐️ 7.0/10

xAI has released Imagine Image 2.0 as Quality Mode on grok.com/imagine and its iOS and Android apps. The model strengthens instruction following, text rendering, layout handling, and content preservation during multi-turn edits, and adds local editing, region segmentation, transparent background export, and multi-image reference editing with up to five input images. This release strengthens xAI&\#x27;s competitive position in AI image generation and editing, with the model ranking second on the Arena leaderboard for both text-to-image and image editing. It also highlights a growing industry trend toward unified models that combine generation and editing with multi-reference inputs, as seen in open-source projects like FLUX.2. Imagine Image 2.0 is offered as a &\#x27;Quality Mode&\#x27; for precise generation and editing. It supports proportional generation, multiple workflow templates, and reference-based editing with up to five images per input, with an API expected to arrive soon.

telegram · zaihuapd · Aug 8, 05:40

**Background**: The Arena \(LMArena\) is a community-driven leaderboard platform that ranks AI models through side-by-side user comparisons. Its text-to-image leaderboard evaluates how well models generate images from text descriptions. Multi-reference image editing, a headline feature of this release, lets users provide several input images as visual references during editing — an area also pursued by open models like Black Forest Labs&\#x27; FLUX.2, which unifies generation and editing into one model.

<details><summary>References</summary>
<ul>
<li><a href="https://lmarena.ai/leaderboard/text-to-image?ref=upmynt.com">Text-to- Image Arena | LMArena</a></li>
<li><a href="https://lmarena.ai/leaderboard/">Overview Leaderboard | LMArena</a></li>
<li><a href="https://github.com/black-forest-labs/flux2">black-forest-labs/flux2: Official inference repo for FLUX.2 models ...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#image-generation`, `#xAI`, `#image-editing`

---

<a id="item-6"></a>
## [Moonshot AI Adds State-Backed Investors, Restructures for Hong Kong IPO](https://www.theblockbeats.info//flash/360480) ⭐️ 7.0/10

Moonshot AI is restructuring its shareholding structure and bringing in multiple state-backed investors to secure regulatory approval for a Hong Kong listing. According to the Financial Times, the company converted its mainland entity to a joint-stock company last week and is coordinating with banks and lawyers to resolve the transfer of overseas investors&\#x27; shareholdings. This marks a major step for one of China&\#x27;s leading AI startups to go public, potentially at a valuation of up to $50 billion. The involvement of state-backed investors signals regulatory support and could influence how other Chinese AI companies approach IPOs amid tightening oversight. Moonshot AI recently completed two financing rounds with a valuation expected to reach up to $50 billion. Its shareholder list now includes the National Social Security Fund, Shanghai and Guizhou local government guidance funds, and an investment vehicle under People&\#x27;s Daily; the company denied rumors of filing a Hong Kong IPO this month to raise about $3 billion.

telegram · zaihuapd · Aug 8, 09:02

**Background**: Moonshot AI is a prominent Chinese artificial intelligence startup best known for developing the Kimi large language model and chatbot. In mainland China, converting a company from a limited liability company to a joint-stock company is a typical preliminary step before an IPO. Bringing in state-owned investors can help a company gain regulatory clearance, especially in sensitive sectors like artificial intelligence.

**Tags**: `#AI`, `#IPO`, `#Moonshot AI`, `#startup`, `#business`

---

<a id="item-7"></a>
## [Claude Code Adds Cross-Session Messaging for AI Sessions](https://code.claude.com/docs/en/cross-session-messaging) ⭐️ 6.0/10

Claude Code v2.1.224 introduces cross-session messaging, letting Claude discover other sessions via ListAgents and send them messages with SendMessage. The feature is available on macOS and Linux without extra setup. This removes the need to re-explain context between terminals or worktrees, enabling parallel agent coordination and long-task status reporting. It makes Claude Code a more viable tool for multi-session and multi-machine workflows. Messages are plain text and are auto-allowed or blocked based on permission modes; users can set crossSessionInbound to accept, hold, or refuse. Inbound messages cannot bypass permission prompts, modify configuration, or execute commands, and the feature does not support native Windows or platforms like Amazon Bedrock and Google Cloud Agent Platform.

telegram · zaihuapd · Aug 8, 02:12

**Background**: Claude Code is Anthropic&\#x27;s command-line agent for AI-assisted coding; each terminal session runs an independent Claude instance. Previously, sharing context between sessions required manually re-explaining tasks, which slowed parallel or long-running work. This update lets sessions discover each other and communicate automatically, and it also extends to replying from other machines via Remote Control.

<details><summary>References</summary>
<ul>
<li><a href="https://code.claude.com/docs/en/cross-session-messaging">Message your other Claude Code sessions - Claude Code Docs</a></li>
<li><a href="https://www.macrumors.com/2026/08/08/claude-code-adds-cross-session-messaging/">Claude Code Adds Cross-Session Messaging on macOS</a></li>
<li><a href="https://www.explainx.ai/blog/claude-code-cross-session-messaging-list-agents-2026">Claude Code Cross-Session Messaging Guide (2026) | explainx ...</a></li>

</ul>
</details>

**Tags**: `#Claude Code`, `#AI tools`, `#developer tools`, `#cross-session communication`, `#feature update`

---

<a id="item-8"></a>
## [X Launches Original Content Rewards, Phases Out Old Revenue Share](https://x.com/XCreators/status/2085835082166653393) ⭐️ 6.0/10

X announced a new Original Content Rewards program that pays creators based on qualified impressions from Premium subscribers. New sign-ups for the old revenue share plan are closed, with existing participants receiving final payouts and transitioning to the new program starting September 8. This shifts X&\#x27;s creator monetization away from ad revenue sharing toward rewarding original content, potentially changing what types of posts are profitable. It matters for creators who rely on X income and for the broader creator economy as platforms compete for original work. On September 8, old revenue share members can apply to the new program if they are 18+, subscribe to X Premium, have at least 500 verified followers, and earned 500,000 verified home timeline impressions in the past 90 days. Payouts are based on qualified impressions from Premium users and are settled every two weeks, with final old-plan payments on August 14, August 28, and around September 11.

telegram · zaihuapd · Aug 8, 05:17

**Background**: X Premium is a paid subscription that gives accounts a verified badge and access to extra features, and verified users&\#x27; impressions are used as the metric for creator payouts. The previous Creator Revenue Sharing program paid users a share of ad revenue; the new Original Content Rewards program instead emphasizes original posts and excludes impressions from duplicates, fraud, paid, or promoted content.

<details><summary>References</summary>
<ul>
<li><a href="https://help.x.com/en/using-x/original-content-rewards">Original Content Rewards</a></li>
<li><a href="https://www.androidheadlines.com/2026/08/x-launches-original-content-rewards-program-creator-payouts.html">X Launches New Original Content Rewards Program : Eligibility</a></li>
<li><a href="https://samodigitalagency.com/x-revenue-sharing-original-content-rewards/">X Replaces Creator Revenue Sharing With Original Content Rewards ...</a></li>

</ul>
</details>

**Tags**: `#social media`, `#monetization`, `#X`, `#creators`, `#content rewards`

---

<a id="item-9"></a>
## [Dopamine 3.0 Jailbreak Adds Support for iOS 26 on A12/A13 iPhones](https://www.macrumors.com/2026/08/07/ios-26-dopamine-jailbreak/) ⭐️ 6.0/10

Dopamine 3.0, released by developer Lars Fröder \(opa334\), becomes the first jailbreak to support iOS 26.0 and 26.0.1. The initial version is limited to devices powered by Apple A12 or A13 chips. This marks the first jailbreak for iOS 26, about 326 days after that operating system&\#x27;s release, giving the jailbreak community a foothold on Apple&\#x27;s newest platform. It also extends compatibility to all devices running iOS 16.5.1 through 17.3.1, widening the tool&\#x27;s reach for security researchers and enthusiasts. The iOS 26 support is currently limited to A12/A13-based devices such as iPhone XS, iPhone XR, iPhone 11, and iPhone SE \(2nd generation\). The release also covers all devices on iOS versions from 16.5.1 through 17.3.1, extending the previous compatibility range.

telegram · zaihuapd · Aug 8, 07:00

**Background**: iOS jailbreaking is the process of exploiting vulnerabilities to remove Apple&\#x27;s software restrictions, allowing users to install unauthorized apps and customize the system beyond what the App Store permits. Dopamine is a well-known jailbreak utility developed by opa334, previously supporting iOS 15 and 16 via exploits such as KFD and a PPL bypass. Apple&\#x27;s A12 and A13 Bionic are 64-bit ARM system-on-chip processors found in iPhone XS, iPhone 11, and related devices.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/IOS_jailbreaking">iOS jailbreaking - Wikipedia</a></li>
<li><a href="https://www.idownloadblog.com/2023/05/02/how-to-jailbreak-with-dopamine/">How to jailbreak iOS 15 and 16 with Dopamine</a></li>
<li><a href="https://en.wikipedia.org/wiki/Apple_A13">Apple A13 - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#jailbreak`, `#iOS security`, `#Dopamine`, `#iOS 26`, `#cybersecurity`

---

<a id="item-10"></a>
## [Tencent WorkBuddy Named Top Strategic AI Product, Leads China Office Agent Market](https://mp.weixin.qq.com/s/TRUjakoaprGFSYYQB301xw) ⭐️ 6.0/10

Tencent has elevated WorkBuddy to one of its highest strategic-priority AI products, with internal reputation as the third strategic product after QQ and WeChat. Analysys data shows WorkBuddy ranked first among China&\#x27;s office agent platforms in Q2 2026 with 20.97 million PC monthly visits and about 20 million monthly active users. This marks a rare public milestone for a Chinese tech giant&\#x27;s AI agent push, signaling that office automation has become a core battleground. WorkBuddy&\#x27;s scale could pressure competitors like Alibaba, ByteDance, and Baidu in the fast-growing enterprise AI market. In July, Tencent moved QClaw-related business into the department housing WorkBuddy, consolidating multiple experimental agent efforts. WorkBuddy already integrates Tencent Docs, WeCom, and Tencent Meeting, and supports multiple models including Hunyuan, DeepSeek, and GLM; it remains in investment phase with no commercialization KPI this year, focusing on expanding enterprise customer coverage.

telegram · zaihuapd · Aug 8, 13:50

**Background**: WorkBuddy is Tencent&\#x27;s full-scenario AI workbench and desktop office AI agent: users describe a goal and a team of specialist sub-agents plans, executes, and returns finished artifacts. QClaw, nicknamed &\#x27;Little Lobster&\#x27;, is another Tencent AI assistant in beta that automates tasks via WeChat/QQ and controls computer functions. Hunyuan is Tencent&\#x27;s large language model family, while DeepSeek and GLM are external models WorkBuddy can also use. Analysys \(易观\) is a Chinese market research firm providing app and platform usage data.

<details><summary>References</summary>
<ul>
<li><a href="https://www.workbuddy.ai/">WorkBuddy - AI Agent for Everyday Office Work</a></li>
<li><a href="https://qcode.cc/en/workbuddy-guide">Tencent WorkBuddy Guide: Office AI Agent, Custom API... | QCode.cc</a></li>
<li><a href="https://www.jagranjosh.com/us/tech-ai/qclaw-ai-what-is-tencent-little-lobster-tool-and-how-it-connects-with-wechat-and-qq-1860002650">QClaw AI: What Is Tencent’s ‘Little Lobster’ Tool and How It Connects...</a></li>

</ul>
</details>

**Tags**: `#Tencent`, `#AI agents`, `#office automation`, `#China tech`

---

<a id="item-11"></a>
## [115 Cloud Drive API Platform to Suspend Service from Aug 9, 2026](https://q.115.com/115/T976421.html#) ⭐️ 6.0/10

On August 8, 2026, the 115 Cloud Drive API open platform announced that all API services will be suspended starting at midnight on August 9, 2026. The official notice says recovery time and follow-up arrangements will be announced later. This suspension will directly affect developers and users who rely on official 115 APIs, especially NAS devices and third-party player integrations that use direct links. It disrupts automated workflows and could push users to alternative cloud storage services. The API platform enables file upload, download, sharing, renaming, moving, deletion, file info queries, and some playback capabilities. The suspension follows 115&\#x27;s recent crackdown on improper usage of its services.

telegram · zaihuapd · Aug 8, 19:48

**Background**: 115 Cloud Drive is a popular Chinese cloud storage service, and its API open platform allowed third-party developers to programmatically access files. Many NAS devices and media players rely on this API to stream content directly from 115, so the shutdown requires those tools to find alternatives.

<details><summary>References</summary>
<ul>
<li><a href="https://q.115.com/115/T161753.html">115 啥时候能重新考虑 开 放 网 盘 API 的事情?_ 115 _社区_ 115 ...</a></li>
<li><a href="https://www.v2ex.com/t/263061">115 云 盘 API 附赠自动 开 车器 - V2EX</a></li>

</ul>
</details>

**Discussion**: Community comments show that users have long requested a public API from 115, with some noting they abandoned the platform due to lack of API access. Others have used unofficial APIs or third-party scripts for automation, and the shutdown is likely to disappoint those relying on such integrations.

**Tags**: `#115网盘`, `#API`, `#cloud storage`, `#NAS`, `#suspension`

---