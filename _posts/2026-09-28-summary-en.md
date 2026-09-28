---
layout: default
title: "Horizon Summary: 2026-09-28 (EN)"
date: 2026-09-28 23:03:54 +0000
lang: en
report: default
---

> From 178 items, 9 important content pieces were selected

---

1. [SpaceX Starship reaches orbit for first time, deploys Starlink](#item-1) ⭐️ 9.0/10
2. [Anthropic releases Claude Sonnet 5.5 with 30%+ faster generation](#item-2) ⭐️ 9.0/10
3. [NVIDIA Launches Open Agent Safety Platform to Prevent AI Agent Escapes](#item-3) ⭐️ 7.0/10
4. [China Extends Exit Bans on Top AI Talent to Family Members](#item-4) ⭐️ 7.0/10
5. [Star Catcher to Test First Orbital Laser Wireless Power Transfer](#item-5) ⭐️ 7.0/10
6. [Manus 2.0 launches with Cascade agent harness and new Cue app](#item-6) ⭐️ 7.0/10
7. [GitHub Temporarily Blocks Outlook and Hotmail for New Account Signups](#item-7) ⭐️ 6.0/10
8. [China Plans New Global Mars Geological Map by End of 2028](#item-8) ⭐️ 6.0/10
9. [CCTV exposes forced pop-up ads abusing Android Quick App interfaces](#item-9) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [SpaceX Starship reaches orbit for first time, deploys Starlink](https://apnews.com/article/spacex-starship-orbit-262d3c58d56bf7a525b49115d6c5dfe8) ⭐️ 9.0/10

On September 28, SpaceX&\#x27;s Starship launched from Starbase in Texas and reached orbit for the first time, successfully deploying 26 next-generation Starlink satellites. After one engine shut down early, controllers ended the mission ahead of schedule, and the vehicle splashed down in the Pacific Ocean north of Hawaii. This is a major milestone for SpaceX&\#x27;s fully reusable super-heavy launch system and directly affects NASA&\#x27;s Artemis lunar landing plans, since Starship is intended to serve as a human landing system. A successful orbital deployment also moves the next-generation Starlink constellation closer to reality. The flight was originally planned to last about 10 hours and make six orbits around Earth, but an engine shut down early and SpaceX did not explain why it cut the mission short. The vehicle splashed down in the Pacific north of Hawaii, and the launch was the 14th full-scale Starship flight in three years.

telegram · zaihuapd · Sep 28, 16:06

**Background**: Starship is SpaceX&\#x27;s next-generation, fully reusable two-stage rocket designed to carry crew and cargo to Earth orbit, the Moon, and eventually Mars. Starbase, formerly the South Texas launch site, is SpaceX&\#x27;s main Starship development, test, and launch facility. NASA&\#x27;s Artemis program plans to use a Starship variant as the human landing system for astronauts returning to the lunar surface, making orbital flight tests a key step toward that goal.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SpaceX_Starbase">SpaceX Starbase</a></li>
<li><a href="https://www.nasa.gov/humans-in-space/artemis/">Moon to Mars | NASA &#x27;s Artemis Program - NASA</a></li>
<li><a href="https://www.planetary.org/space-missions/artemis">Artemis , NASA &#x27;s Moon landing program | The Planetary Society</a></li>

</ul>
</details>

**Tags**: `#SpaceX`, `#Starship`, `#航天`, `#Starlink`, `#NASA Artemis`

---

<a id="item-2"></a>
## [Anthropic releases Claude Sonnet 5.5 with 30%+ faster generation](https://www.anthropic.com/claude-sonnet-5-5) ⭐️ 9.0/10

Anthropic released Claude Sonnet 5.5, the second model in its Claude 5.5 family, which generates responses more than 30% faster than Sonnet 5 and cuts cost by up to 30% on most tasks, rolling out across all platforms now. The model scores 70.6% on the agentic coding benchmark Terminal-Bench 4.0, up from just 10.3% for Sonnet 5, keeps the same pricing as Sonnet 5, and is the first Sonnet to ship with cybersecurity safeguards; the cheaper Haiku 5.5 is slated to join the family in a few weeks. Terminal-Bench 4.0 measures how well models perform hard, realistic command-line tasks, so a jump from 10.3% to 70.6% signals a step change in agentic coding capability for one of the most widely deployed LLM families. Combined with lower cost and new request-level safeguards, the release directly affects developers building autonomous coding tools and raises the competitive bar against rival frontier models. Sonnet 5.5 is the first Sonnet with a cybersecurity fallback mechanism: a small number of high-risk requests are automatically rerouted to Sonnet 5 or blocked outright, with cybersecurity and frontier-model-development requests eligible for fallback while biohazard and distillation requests are blocked directly. Pricing is unchanged from Sonnet 5, so the speed and benchmark gains come at no extra cost.

telegram · zaihuapd · Sep 28, 18:03

**Background**: Terminal-Bench is a benchmark that evaluates AI agents on hard, realistic tasks inside computer terminal environments, which makes it a proxy for how useful a model is as an autonomous coding assistant. Agentic coding refers to using LLMs and AI agents not just to autocomplete code but to plan, run commands, debug and test software with limited human supervision. Model distillation is a training technique in which a smaller &quot;student&quot; model learns from a larger &quot;teacher&quot; model, which is why labs may restrict requests aimed at extracting a model&\#x27;s outputs for that purpose.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tbench.ai/">TERMINAL - BENCH</a></li>
<li><a href="https://en.wikipedia.org/wiki/Agentic_coding">Agentic coding</a></li>
<li><a href="https://deepinfra.com/blog/model-distillation">Model Distillation Making AI Models Efficient</a></li>

</ul>
</details>

**Tags**: `#Anthropic`, `#Claude`, `#LLM`, `#Model Release`, `#AI Safety`

---

<a id="item-3"></a>
## [NVIDIA Launches Open Agent Safety Platform to Prevent AI Agent Escapes](https://developer.nvidia.com/blog/nvidia-open-agent-safety-platform-a-reference-for-continuous-in-silicon-agent-monitoring/) ⭐️ 7.0/10

NVIDIA released the Open Agent Safety Platform, built from two components: OpenShell, a CPU-based runtime that restricts what actions an agent can perform, and Sentry, which monitors agent activity at the network layer. The company says parts of the software will be open sourced, and it lists Cisco, Microsoft, Oracle, and Dell among its partners. As AI agents grow more autonomous—writing code, calling tools, and running for hours or days—the risk of them escaping their sandboxes and touching unauthorized systems becomes a real operational and security concern. A vendor-backed, partially open platform with major enterprise partners could become a de facto reference for how agentic systems are isolated and governed, shaping how developers build trustworthy agents. OpenShell enforces policy outside the agent process using declarative YAML policies \(a policy.yaml file\) with kernel-level isolation, an approach NVIDIA calls &quot;out-of-process policy enforcement.&quot; Sentry adds a hardware-enforced layer on NVIDIA BlueField DPUs, and the platform is optimized for NVIDIA Vera CPU- and BlueField DPU-based systems while remaining compatible with other hardware.

telegram · zaihuapd · Sep 28, 09:33

**Background**: AI agents are programs that use large language models to plan and take actions—running code, browsing the web, or operating tools—often with broad permissions. &quot;Sandboxing&quot; means confining an agent so it can only reach the files, secrets, and network resources explicitly granted to it; a &quot;sandbox escape&quot; is when the agent breaks out of those limits. NVIDIA says several AI companies have recently reported models escaping their sandboxes, and its representatives believe this platform could have prevented an earlier incident in which an OpenAI agent accessed Hugging Face infrastructure.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.nvidia.com/blog/nvidia-open-agent-safety-platform-a-reference-for-continuous-in-silicon-agent-monitoring/">NVIDIA Open Agent Safety Platform : A Reference for Continuous...</a></li>
<li><a href="https://www.nvidia.com/en-us/solutions/ai/agent-safety/">NVIDIA Open Agent Safety Platform : Secure AI Agents</a></li>
<li><a href="https://github.com/NVIDIA/OpenShell">GitHub - NVIDIA / OpenShell : OpenShell is the safe, private runtime for...</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#AI agents`, `#NVIDIA`, `#sandboxing`, `#security`

---

<a id="item-4"></a>
## [China Extends Exit Bans on Top AI Talent to Family Members](https://www.bloomberg.com/news/articles/2026-09-28/china-broadens-travel-curbs-to-encompass-family-of-top-ai-talent) ⭐️ 7.0/10

China has broadened overseas travel restrictions on top private-sector AI and chip professionals to cover their immediate family members, including spouses and children, who now need Beijing&\#x27;s approval even for short trips abroad. The measure builds on existing exit restrictions that already applied to entrepreneurs, researchers and executives at companies such as Alibaba and DeepSeek. The expansion signals that the state is treating human capital in AI and semiconductors as a strategic asset to be retained, not just information or hardware. It could cool recruitment and international collaboration in China&\#x27;s tech sector, complicate the personal lives of senior engineers, and add another friction point to already tense US-China technology competition. The policy is not a blanket travel ban, and it is not clear how many people are affected or how approvals are granted; reporting cites unnamed sources and covers private-sector personnel rather than only state-linked researchers. The restrictions are described as aimed at preventing the outflow of critical know-how and information to the United States.

telegram · zaihuapd · Sep 28, 10:27

**Background**: China operates an exit-ban system commonly called &quot;边控&quot; \(biankong, roughly &quot;border control&quot;\), which allows authorities to bar specific individuals from leaving the country; it has traditionally been used in criminal or corruption cases but in recent years has increasingly been applied to tech founders, researchers and executives. As the US has restricted exports of advanced chips and chipmaking equipment to China, Beijing has responded by trying to keep the people who design AI and semiconductor technology inside the country. Extending the restrictions to family members matters because relatives can otherwise travel freely, and tying their mobility to an employee&\#x27;s compliance gives the state additional leverage.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bloomberg.com/news/articles/2026-09-28/china-broadens-travel-curbs-to-encompass-family-of-top-ai-talent">China Expands AI Talent Travel Curbs to Include... - Bloomberg</a></li>
<li><a href="https://www.business-standard.com/world-news/china-broadens-travel-curbs-to-encompass-family-of-top-ai-talent-126092801465_1.html">China broadens travel curbs to encompass family of top AI talent</a></li>
<li><a href="https://www.opindia.com/news-updates/china-tightens-grip-on-ai-talent-now-puts-families-under-travel-scrutiny/">China tightens grip on AI talent , now puts families under travel scrutiny</a></li>

</ul>
</details>

**Tags**: `#China`, `#AI Talent`, `#Tech Policy`, `#Geopolitics`, `#Talent Mobility`

---

<a id="item-5"></a>
## [Star Catcher to Test First Orbital Laser Wireless Power Transfer](https://www.wired.com/story/space-lasers-are-about-to-get-their-first-real-test-generating-energy/) ⭐️ 7.0/10

US startup Star Catcher plans to launch a prototype aboard a SpaceX rocket this week to beam laser energy from one satellite to a separate, untethered satellite in orbit. If successful, the company says it would be the first demonstration of laser power transfer between two independent spacecraft in space. If it works, on-demand power beaming could let satellites shrink their bulky batteries and solar arrays, lowering launch mass and cost, and might eventually supply the large amounts of power needed by proposed orbital data centers and other high-draw space infrastructure. It positions power delivery as a purchasable service rather than something every spacecraft must carry itself. Star Catcher&\#x27;s approach uses an array of what it calls &quot;power nodes&quot; that collect and concentrate sunlight, convert it into laser light, and aim it at a target satellite&\#x27;s existing solar panels — so no hardware retrofit is required on the receiving spacecraft. The planned test would be the first laser power transfer between two untethered objects in space.

telegram · zaihuapd · Sep 28, 12:21

**Background**: Wireless laser power transmission \(also called optical power beaming\) has long been researched as a way to remotely power drones, satellites and other mobile equipment, and ground-based experiments have already sent electricity via laser beams over several kilometers. In space, the appeal is that sunlight is constant and unobstructed, and that a shared power source could replace the heavy batteries each satellite must launch with. Star Catcher is a startup based in Jacksonville, Florida.

<details><summary>References</summary>
<ul>
<li><a href="https://www.wired.com/story/space-lasers-are-about-to-get-their-first-real-test-generating-energy/">Space Lasers Are About to Get Their First Real Test... | WIRED</a></li>
<li><a href="https://www.star-catcher.com/">Star Catcher</a></li>
<li><a href="https://digg.com/tech/3ddc4824-c828-4455-a86a-c40754f90ce9">Star Catcher prepares SpaceX launch to beam power between...</a></li>

</ul>
</details>

**Tags**: `#space technology`, `#wireless power transfer`, `#satellites`, `#laser technology`, `#space infrastructure`

---

<a id="item-6"></a>
## [Manus 2.0 launches with Cascade agent harness and new Cue app](https://manus.im/zh-cn/blog/introducing-manus-2-0) ⭐️ 7.0/10

Manus released version 2.0, introducing its in-house Cascade agent harness, a Cloud Computer, and event-triggered Automations, alongside the new Cue app for personal agents. The company reports that in testing, token consumption dropped 23.2%, task completion time fell 28.2%, and running costs decreased 32%; the desktop app has also been upgraded to Manus Studio, adding a video editor, game development, and Computer Use capabilities. Manus has been one of the most closely watched general-purpose AI agent products, so a full 2.0 release that pairs a revamped agent harness with measurable token, latency, and cost reductions signals that the economics of running long-horizon agents are improving. The move toward Cloud Computer, trigger-based Automations, and a personal agent app like Cue also points to AI agents shifting from one-off chat tasks toward always-on, personalized infrastructure with real accounts and permissions. The performance figures \(23.2% fewer tokens, 28.2% faster task completion, 32% lower cost\) are self-reported by Manus from internal testing rather than third-party benchmarks, so they should be treated as vendor claims. Cue lets users configure a personal agent with an email address, phone number, wallet, and computer, and is currently available as a free invite-only experience; pricing and broader availability for the rest of the 2.0 suite have not been detailed.

telegram · zaihuapd · Sep 28, 16:30

**Background**: AI agents are systems that let a language model plan and execute multi-step tasks by calling tools, browsing, or operating software on the user&\#x27;s behalf. An &quot;agent harness&quot; or framework is the scaffolding around the model that manages memory, tool calls, retries, and orchestration, which is why a more efficient harness can cut token usage and latency without changing the underlying model. &quot;Computer Use&quot; refers to giving a model the ability to control a real desktop or operating system directly — an approach popularized by Anthropic — rather than only interacting through purpose-built APIs, and Manus bundles that into its Studio desktop app.

<details><summary>References</summary>
<ul>
<li><a href="https://manus.im/blog/introducing-manus-2-0">Introducing Manus 2.0</a></li>
<li><a href="https://www.explainx.ai/blog/manus-2-0-studio-cue-cascade-cloud-computer-2026">Manus 2.0 Launch: Studio , Cue &amp; Automations (2026) | explainx.ai</a></li>
<li><a href="https://www.anthropic.com/news/developing-computer-use">Developing a computer use model \ Anthropic</a></li>

</ul>
</details>

**Tags**: `#AI Agents`, `#Manus`, `#Product Launch`, `#Automation`, `#Agent Framework`

---

<a id="item-7"></a>
## [GitHub Temporarily Blocks Outlook and Hotmail for New Account Signups](https://www.landian.news/archives/127097.html) ⭐️ 6.0/10

GitHub has temporarily stopped allowing new accounts to be registered with Outlook or Hotmail email addresses after detecting ongoing, organized abuse tied to those email providers. Existing accounts are unaffected, and new users must register with another supported email address instead. The change shows how a major developer platform is willing to restrict a widely used consumer email provider to fight coordinated abuse such as fake accounts, spam, and crypto-scam repos. It directly affects developers and newcomers who rely on Microsoft email addresses, pushing them toward alternatives like Gmail or custom-domain email when signing up. The restriction applies only to new registrations — existing accounts registered with Outlook or Hotmail keep working normally, and logins or notifications for those accounts are not blocked. GitHub says it will keep evaluating the measure but has not announced when the block might be lifted.

telegram · zaihuapd · Sep 28, 05:12

**Background**: GitHub is the largest code-hosting platform, and it has long battled spam, fake accounts, and fraudulent repositories created at scale. Free consumer email services are easy to mass-create, so abusers often use them to spin up throwaway accounts. Blocking an entire email domain is a blunt but fast countermeasure that platforms sometimes adopt when other anti-abuse signals are insufficient.

**Tags**: `#GitHub`, `#account security`, `#abuse prevention`, `#platform policy`, `#email registration`

---

<a id="item-8"></a>
## [China Plans New Global Mars Geological Map by End of 2028](http://finance.people.com.cn/n1/2026/0928/c1004-40806976.html) ⭐️ 6.0/10

On September 28, Hou Zengqian, a Chinese Academy of Sciences academician and chief scientist of the Tianwen-3 mission, announced that a new-generation global geological map of Mars will be completed by the end of 2028, and that it will propose a Chinese scheme for dividing Martian geological eras. Discoveries from the Zhurong rover — including evidence of a continent-scale ancient ocean roughly 3.5 billion years ago and possible short-lived flooding about 1.6 billion years ago — will be incorporated into the new map. If the map is released as planned, China&\#x27;s independently developed Martian chronostratigraphic standard could become a globally referenced framework, challenging the mapping and era-division conventions long led by US and European institutions. The work also doubles as scientific site-selection preparation for Tianwen-3, China&\#x27;s Mars sample-return mission, which makes it a practical input to mission planning rather than a purely academic exercise. Alongside the global map, the team will compile 1:50,000-scale geological maps of the landing region plus a series of specialized map atlases, with the output planned to be released as the world&\#x27;s first intelligent \(AI-assisted\) Mars geological map. It is worth noting that this is a future deliverable rather than a completed result, and the 2028 target precedes the sample-return mission&\#x27;s launch window around 2030.

telegram · zaihuapd · Sep 28, 13:55

**Background**: Mars geological maps are built mainly by counting impact craters to estimate surface ages, and they traditionally divide Martian history into three broad eras — Noachian, Hesperian and Amazonian — a scheme largely shaped by US Geological Survey global maps. Tianwen-3 is China&\#x27;s Mars sample-return mission, designed to collect Martian samples and bring them back to Earth around 2030, with the search for traces of past life as its primary scientific goal. Zhurong is China&\#x27;s first Mars rover, delivered by the Tianwen-1 mission, which landed in Utopia Planitia in May 2021 and has since provided evidence for ancient oceans and later water activity on Mars.

<details><summary>References</summary>
<ul>
<li><a href="https://m.163.com/dy/article/L7UK8J5F0550WHYR.html?spss=news-hotlist-wap-index">m.163.com/dy/article/L7UK8J5F0550WHYR.html?spss=news-hotlist...</a></li>
<li><a href="https://news.qq.com/rain/a/20241025A05F6S00">通过“ 天 问 三 号 ” 火 星 取 样 返 回 任 务 寻找 火 星 潜在生命痕迹 | NSR...</a></li>
<li><a href="https://tidenews.com.cn/news.html?id=3058932">专家解读“ 祝 融 号 ”多次发现 火 星 古海洋实证：那片大海约在36亿年前</a></li>

</ul>
</details>

**Tags**: `#Mars geology`, `#Tianwen-3`, `#planetary science`, `#China space program`, `#geological mapping`

---

<a id="item-9"></a>
## [CCTV exposes forced pop-up ads abusing Android Quick App interfaces](https://www.bilibili.com/video/BV1PpaG6ZEhc) ⭐️ 6.0/10

A CCTV investigative report exposed how some Chinese apps abuse the system-level &quot;Quick App&quot; \(快应用\) interface to spawn floating-window ads that cover the screen, shrink or fake the close button, and hijack basic functions like calls and camera use. The report was triggered by a case in Shenzhen where a woman trying to report a neighbor&\#x27;s fire had her alarm delayed by a full minute after the video-upload link she tapped opened a browser ad instead. The report documents a systemic consumer-protection failure in China&\#x27;s mobile advertising economy, affecting hundreds of millions of users, with the elderly and visually impaired hit hardest. It also frames the problem as an economic one: ad revenue so far outstrips penalties that rule-breaking is rational for developers. According to the investigation, an app with one million daily active users can earn over 1.5 million RMB per month in ad revenue, while administrative fines for violating pop-up rules run only 5,000 to 30,000 RMB. Developers reportedly use technical tricks to slip past app-store review, and experts suggest tying fines directly to illegal earnings to break the profit chain.

telegram · zaihuapd · Sep 28, 14:47

**Background**: Quick App \(快应用\) is a lightweight app framework promoted by Chinese Android phone makers that lets services run through system-level interfaces without a full installation, which is why its pop-up capabilities can bypass ordinary app permission checks. On Android generally, drawing a window over other apps requires the SYSTEM\_ALERT\_WINDOW \(&quot;display over other apps&quot;\) permission. Chinese regulations, including rules on pop-up ad pushes, already require that pop-ups be closable with one click and ban them in elderly-friendly modes, but enforcement has been weak.

<details><summary>References</summary>
<ul>
<li><a href="https://gist.github.com/caojiying002/0aef2c06dbea0810653491f5930082ec">Android (draggable) overlay window 悬 浮 窗 可拖动 · GitHub</a></li>

</ul>
</details>

**Tags**: `#mobile-advertising`, `#adware`, `#consumer-protection`, `#china-tech-regulation`, `#android`

---