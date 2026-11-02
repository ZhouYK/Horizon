---
layout: default
title: "Horizon Summary: 2026-11-02 (EN)"
date: 2026-11-02 23:04:11 +0000
lang: en
report: default
---

> From 189 items, 5 important content pieces were selected

---

1. [ChatGPT Share-Link Flaw Enabled Account Takeover](#item-1) ⭐️ 8.0/10
2. [Anthropic Posts $33.2B Revenue and $104B Net Loss in IPO Filing Update](#item-2) ⭐️ 8.0/10
3. [WIRED: 400+ Mundane AI Apps Covertly Hid Sexual Deepfake Tools](#item-3) ⭐️ 7.0/10
4. [Abu Dhabi Signs Four OpenAI Deals, Including &\#x27;Machine-Readable Government&\#x27;](#item-4) ⭐️ 7.0/10
5. [Swedish ICA stores hit by cyberattack that set freezers to 50°C](#item-5) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [ChatGPT Share-Link Flaw Enabled Account Takeover](https://www.parameter.ai/labs/we-found-a-gap-at-openai) ⭐️ 8.0/10

Parameter researchers disclosed a ChatGPT share-link vulnerability that let a malicious link execute code in a signed-in user&\#x27;s session, read private conversations, and exfiltrate data to an external server; OpenAI fixed it on October 26 and rated it P1. Because ChatGPT share links are a normal way to pass around conversations, a link that compromises the viewer&\#x27;s authenticated session turns a routine click into a potential account takeover and exposes unrelated private chats. Public reports describe the chain as a shared link reaching a postMessage listener that trusted any sender and ultimately an innerHTML sink, so the victim only had to open the link and did not need to install anything. OpenAI paid a $5,000 bounty, but the public write-up provides relatively little exploit detail beyond the attack chain and its P1 severity rating.

telegram · zaihuapd · Nov 2, 10:24

**Background**: ChatGPT share links create a public URL for a conversation, and when a logged-in user opens one, the content is rendered inside the ChatGPT web app with that user&\#x27;s authenticated session. postMessage is a browser API that lets different windows or frames exchange messages; if a listener does not verify the sender&\#x27;s origin, a malicious page can send crafted data. This is why a rendering bug in shared content can escalate from cross-site scripting to session compromise and private-data exfiltration.

<details><summary>References</summary>
<ul>
<li><a href="https://thehackernews.com/2026/10/a-shared-chatgpt-link-could-run.html">A Shared ChatGPT Link Could Run Attacker Code in Your Session ...</a></li>
<li><a href="https://aicybr.com/blog/chatgpt-shared-link-session-takeover-parameter-labs-october-2026">ChatGPT Shared-Link Session Takeover: October 2026 Fix ...</a></li>
<li><a href="https://aiweekly.co/alerts/openai-patches-chatgpt-share-link-flaw-that-hijacked-sessions">OpenAI Patches ChatGPT Share-Link Flaw That Hijacked Sessions</a></li>

</ul>
</details>

**Tags**: `#security`, `#ChatGPT`, `#vulnerability`, `#account-takeover`, `#AI`

---

<a id="item-2"></a>
## [Anthropic Posts $33.2B Revenue and $104B Net Loss in IPO Filing Update](https://www.cnbc.com/2026/11/02/anthropic-ant-s-1-quarter-financials.html) ⭐️ 8.0/10

Anthropic updated its IPO prospectus on Monday, disclosing $33.24 billion in revenue for the nine months ended September 30, 2026 — growth of roughly 1,200% year over year — including about $17 billion in the third quarter alone. At the same time, its net loss for the period widened to $104 billion, up sharply from $25.1 billion a year earlier. The filing offers an unusually detailed look at the economics of a frontier AI lab, showing explosive revenue growth sitting alongside enormous losses and roughly $895 billion in cumulative purchase and lease commitments, almost all for compute and infrastructure. That combination is likely to shape how public investors value AI labs as Anthropic approaches a Nasdaq listing, and it underscores how capital-intensive the frontier model business has become. Anthropic said the net loss is largely an accounting effect: the first-half figure was mainly driven by fair value changes on convertible notes and derivative liabilities, and therefore does not fully reflect actual operating cash burn. The roughly $895.4 billion in purchase and lease obligations is almost entirely tied to compute and infrastructure, meaning the commitments represent future spending rather than money already spent.

telegram · zaihuapd · Nov 2, 15:12

**Background**: Anthropic formally filed its S-1 with the SEC on October 26 and plans to list on the Nasdaq Global Select Market under the ticker &quot;ANT&quot;, with earlier filings showing an $80.7 billion net loss for the first half of the year. A large part of that headline loss comes from fair value accounting on convertible redeemable preferred shares: when the company&\#x27;s valuation rises, the liability is marked up and booked as a loss, a pattern seen before in pre-IPO filings from companies such as Xiaomi and Kuaishou, where bigger paper losses actually signaled a higher valuation. Investors are also split on what Anthropic is worth, with Silicon Valley expectations cited around $2 trillion against more conservative Wall Street estimates near $1.5 trillion.

<details><summary>References</summary>
<ul>
<li><a href="https://www.163.com/dy/article/LA6S4ONO05198NMR.html">史上最大 IPO 来了！ Anthropic 正式提交 IPO 申请，上半年净亏损807...</a></li>
<li><a href="https://www.yicai.com/news/5419839.html">小米一年 亏 损 439亿 的 秘密：系优先股 公 允 值 “作怪”</a></li>

</ul>
</details>

**Tags**: `#Anthropic`, `#AI industry`, `#IPO`, `#financials`, `#compute infrastructure`

---

<a id="item-3"></a>
## [WIRED: 400+ Mundane AI Apps Covertly Hid Sexual Deepfake Tools](https://www.wired.com/story/hundreds-of-mundane-ai-apps-are-hiding-abusive-deepfake-features/) ⭐️ 7.0/10

A WIRED investigation published on November 2 identified a network of more than 400 linked apps and websites that masquerade as ordinary AI tools — pet portraits, language learning and similar utilities — but quietly load a sexual deepfake interface under certain conditions, letting users upload someone else&\#x27;s photos to generate explicit images or videos. Twenty-seven of the apps were still live on Google Play in September with more than 350,000 combined downloads; after WIRED contacted them, Apple pulled 19 apps, Google had already removed most of them, and Meta said it blocked ads for 209 related apps. The case shows that app-store review can be defeated at scale by swapping in remote web content after approval, meaning store badges and &quot;all ages&quot; ratings offer little protection against non-consensual intimate imagery tools. It puts pressure on Apple, Google and Meta to police not just app binaries but the server-side content and ad pipelines that distribute such services. According to Apple, the developers passed review with a benign app and then swapped the remote web content served to users, and many of the apps carried ratings suitable for all ages. WIRED linked the network to Chinese developers and a Hong Kong-registered company using Chinese-language code, hosting records, domain data and ad-tracking footprints — a link the outlet describes as an investigative assessment, and the operators did not respond to requests for comment.

telegram · zaihuapd · Nov 2, 12:45

**Background**: Sexual deepfakes \(often called &quot;nudify&quot; tools\) use generative AI to digitally strip or alter a person&\#x27;s clothing or insert their face into explicit imagery without consent, and such content is increasingly used as a form of image-based sexual abuse. Mobile app stores rely heavily on upfront review of the submitted binary, which is why some developers ship a harmless app and later change what is delivered from their servers — a trick previously documented with pirate streaming and photo-management apps that slipped past Apple&\#x27;s review. Ad networks and shared domain or code infrastructure are often the thread investigators pull to map such operations.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Deepfake_pornography">Deepfake pornography - Wikipedia</a></li>
<li><a href="https://www.wired.com/story/deepfake-nudify-technology-is-getting-darker-and-more-dangerous/">Deepfake ‘Nudify’ Technology Is Getting Darker—and More... | WIRED</a></li>
<li><a href="https://9to5mac.com/2024/08/02/developers-trick-app-store-review/">How developers trick App Store into approving malicious apps</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#deepfakes`, `#content moderation`, `#app store policy`, `#privacy &amp; ethics`

---

<a id="item-4"></a>
## [Abu Dhabi Signs Four OpenAI Deals, Including &\#x27;Machine-Readable Government&\#x27;](https://thenextweb.com/news/openai-abu-dhabi-deals-machine-readable-government-mubadala) ⭐️ 7.0/10

Abu Dhabi signed four agreements with OpenAI on Monday, including a &quot;machine-readable government&quot; initiative that converts policies and regulations into AI-readable formats to help officials review permit and certificate applications, already piloted on food imports. Mubadala will partner with OpenAI and G42&\#x27;s Inception42 on investment analysis, Inception42 signed a separate five-year deal to supply models to the UAE government, enterprises and schools, and ADNOC became the first energy company to use OpenAI&\#x27;s Frontier platform. The deals mark one of the most concrete examples of a national government embedding OpenAI models directly into regulatory and administrative workflows, rather than just experimenting with chatbots. If the model works, it could become a template for sovereign AI adoption across the Gulf and other governments seeking efficiency gains in permitting, investment screening and energy operations. Officials retain final decision-making authority in the machine-readable government pilot, which currently focuses on food import permits, and the agreements are partnership announcements rather than technical breakthroughs. The Frontier platform referenced by ADNOC is OpenAI&\#x27;s enterprise offering for building, deploying and monitoring AI agents, launched in early 2026.

telegram · zaihuapd · Nov 2, 15:55

**Background**: &quot;Machine-readable government&quot; refers to the idea that public-sector data, rules and documents should be published in structured, standardized formats that software can parse directly, rather than as PDFs or scanned files. G42 is an Abu Dhabi-based AI conglomerate whose subsidiary Inception42 develops Arabic-focused models such as the Jais series and positions itself around &quot;sovereign AI&quot; — AI infrastructure and models built and governed locally. Mubadala is one of Abu Dhabi&\#x27;s main sovereign wealth funds, and ADNOC is the national oil company.

<details><summary>References</summary>
<ul>
<li><a href="https://news.aibase.com/news/25321">OpenAI Launches Frontier Platform : Building AI Colleagues to...</a></li>
<li><a href="https://inception42.ai/">Inception AI | Pioneering Industry-Specific AI Solutions</a></li>
<li><a href="https://www.arabianbusiness.com/abnews/g42s-inception-rebrands-as-inception42-to-accelerate-uaes-sovereign-ai-ambitions-exclusive">G 42 &#x27;s Inception rebrands as Inception 42 to accelerate...</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#Abu Dhabi`, `#Government AI`, `#AI Governance`, `#Digital Policy`

---

<a id="item-5"></a>
## [Swedish ICA stores hit by cyberattack that set freezers to 50°C](https://x.com/InsiderGeo/status/2117164877701595165) ⭐️ 6.0/10

Swedish supermarket chain ICA reported that several stores were hit by a nighttime cyberattack in which refrigerators and freezers connected to the store network were remotely set to 50°C, threatening large amounts of food with spoilage. Affected locations, including Sjöbo and Tomelilla, closed temporarily in the morning and were expected to reopen around 9 a.m. local time, with ICA apologizing to customers. This is a concrete example of an attack crossing from the digital realm into the physical world: instead of stealing data, the intruders manipulated cooling equipment to destroy inventory and disrupt operations. It underscores how exposed networked building and refrigeration systems in retail are, and the incident follows reports of similar attacks on businesses in France and the United States in recent weeks. The reports do not disclose how attackers gained access — whether through exposed internet-facing controllers, weak credentials, or compromise of a store network — nor how many stores were affected or the scale of food losses. Because refrigeration units are operational technology rather than ordinary IT, incidents like this typically require manual on-site resets and inspections before cooling can be trusted again.

telegram · zaihuapd · Nov 2, 13:52

**Background**: Retail stores increasingly run refrigeration, HVAC, and energy monitoring on internet-connected systems so they can be managed centrally and monitored remotely — part of what is often called the Internet of Things \(IoT\). Such devices fall under operational technology \(OT\) and industrial control systems \(ICS\), which prioritize availability and physical safety over the confidentiality concerns of conventional IT security. Historically these controllers were isolated on separate networks, but as they are merged with store IT and reachable from the internet, attacks that once could only break data systems can now alter temperature settings, locks, or other physical processes.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cisco.com/site/us/en/learn/topics/security/what-is-ot-security.html">OT security: protect ICS and infrastructure [Explained] - Cisco</a></li>
<li><a href="https://www.paloaltonetworks.com/cyberpedia/ot-vs-ics-vs-scada-security">What Are the Differences Between OT, ICS, &amp; SCADA Security?</a></li>
<li><a href="https://kopiustech.com/insights-innovation/iot-security-and-its-importance-in-retail/">Understanding IoT Security and Its Importance in Retail</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#IoT security`, `#OT/ICS`, `#retail`, `#cyberattack`

---