---
layout: default
title: "Horizon Summary: 2026-09-11 (EN)"
date: 2026-09-11 23:04:26 +0000
lang: en
report: default
---

> From 199 items, 8 important content pieces were selected

---

1. [OpenAI ships GPT-Live-1, a full-duplex voice model, in its API](#item-1) ⭐️ 8.0/10
2. [GitLab patches CVSS 10.0 flaw allowing unauthenticated file reads](#item-2) ⭐️ 8.0/10
3. [OpenAI launches public beta Agents API for production cloud agents](#item-3) ⭐️ 8.0/10
4. [OpenAI Open to Slowing Frontier AI Development, Altman Tells Staff](#item-4) ⭐️ 7.0/10
5. [China Merges Lunar Programs, Cancels Chang&\#x27;e 8 South Pole Mission](#item-5) ⭐️ 7.0/10
6. [The Waymo Effect: How AI Quietly Weakens Research Collaboration](#item-6) ⭐️ 7.0/10
7. [Report: Anthropic Building Surveillance System to Track Anti-AI Activists](#item-7) ⭐️ 7.0/10
8. [Japan&\#x27;s Digital Agency Hit by Unauthorized Server Access, Data of ~246,000 at Risk](#item-8) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [OpenAI ships GPT-Live-1, a full-duplex voice model, in its API](https://openai.com/index/introducing-gpt-live-1-in-the-api/) ⭐️ 8.0/10

OpenAI launched GPT-Live-1 in its API on September 10, 2026, a full-duplex speech model that can listen and speak at the same time, supporting natural interruptions, background-noise handling, long conversations and telephony voice agents, while offloading complex reasoning and tool calls to backend models. OpenAI claims GPT-Live-1 improves by 30 points over GPT-Realtime-2.1 on Full Duplex Bench, with the API voice front end priced at $0.05 per minute. True full-duplex speech-to-speech with interruptibility and delegated tool use is a meaningful step toward voice agents that feel like real phone conversations rather than walkie-talkie turn taking, which matters for customer-support, outbound calling and in-app assistants. The explicit $0.05-per-minute price also makes large-scale voice-agent economics calculable for builders who previously had to weigh latency, quality and cost trade-offs across multiple cascaded components. The headline claim is a 30-point gain on Full Duplex Bench versus GPT-Realtime-2.1, which itself supports configurable reasoning effort at the cost of higher latency and token usage. The announcement is a brief, second-hand relay with no benchmark breakdowns, latency figures or independent verification, and its stated date \(September 10, 2026\) is anomalous relative to prior OpenAI release timelines, so the numbers should be treated as vendor claims until confirmed.

telegram · zaihuapd · Sep 11, 03:09

**Background**: Traditional voice assistants work in turns: you speak, the system waits for you to finish, then it answers, which is why they cannot handle being interrupted mid-sentence. Full-duplex models instead keep both an input and an output audio stream open continuously so they can listen while speaking, produce backchannels like &quot;mm-hmm&quot;, and handle barge-ins, and Full Duplex Bench is a public benchmark built specifically to measure these turn-taking behaviours. OpenAI&\#x27;s Realtime API family \(gpt-realtime-2.1 and its mini variant\) was its earlier streaming speech-to-speech line, and GPT-Live-1 is positioned as its successor for live conversational and telephony use.

<details><summary>References</summary>
<ul>
<li><a href="https://full-duplex-bench.github.io/">Full - Duplex - Bench : A Benchmark for Full - duplex Spoken Dialogue...</a></li>
<li><a href="https://developers.openai.com/api/docs/models/gpt-realtime-2.1">GPT-Realtime-2.1 Model | OpenAI API</a></li>
<li><a href="https://research.nvidia.com/labs/adlr/personaplex/">NVIDIA PersonaPlex: Natural Conversational AI With Any Role ... Fullduplex — an observatory for speech-to-speech, full-duplex ... nvidia/personaplex-7b-v1 · Hugging Face PersonaPlex: NVIDIA’s Real-Time Full‑Duplex Voice ...</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#voice-ai`, `#real-time-speech`, `#API-release`, `#LLM`

---

<a id="item-2"></a>
## [GitLab patches CVSS 10.0 flaw allowing unauthenticated file reads](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-3-2-released/) ⭐️ 8.0/10

GitLab released emergency patch versions 19.3.2, 19.2.6 and 19.1.8 on September 10 to fix CVE-2026-85706, a vulnerability rated CVSS 10.0 in which an unauthenticated user can, under certain conditions, exploit path-restriction and authentication flaws in the repository commits API to read arbitrary files on the GitLab server. GitLab strongly urges anyone running a self-managed instance to upgrade immediately, while GitLab.com has already been patched and GitLab Dedicated customers need take no action. A maximum-severity, unauthenticated arbitrary file read is about as serious as a web-application bug gets, because any attacker who can reach the instance can potentially harvest tokens, secrets, database credentials and configuration files without needing an account. Because GitLab is widely self-hosted inside enterprises, every organization running an affected self-managed instance faces a direct, immediate exposure that only patching resolves. The affected range covers versions from 18.7 up to but not including 19.1.8, the 19.2 branch before 19.2.6, and the 19.3 branch before 19.3.2, and the flaw was reported by researcher s3ntago through HackerOne. GitLab has not published the precise preconditions required to trigger the bug, no reproducible public proof-of-concept has appeared online, and there is currently no evidence of exploitation in the wild.

telegram · zaihuapd · Sep 11, 11:05

**Background**: CVSS \(Common Vulnerability Scoring System\) is the industry-standard framework for rating the severity of software vulnerabilities, and 10.0 is its highest possible base score, indicating an easily exploitable flaw with maximum impact. GitLab is a DevOps platform for hosting source code, CI/CD pipelines and issue tracking that many organizations run on their own servers \(self-managed\) rather than on GitLab&\#x27;s SaaS offering; the commits API is the REST endpoint used to retrieve information about Git commits. GitLab Dedicated is GitLab&\#x27;s single-tenant SaaS offering hosted and maintained by GitLab itself, which is why its users do not need to patch.

<details><summary>References</summary>
<ul>
<li><a href="https://nvd.nist.gov/vuln-metrics/cvss">NVD - Vulnerability Metrics</a></li>
<li><a href="https://docs.gitlab.com/api/commits/">Documentation for the REST API for Git commits in GitLab .</a></li>
<li><a href="https://docs.gitlab.com/subscriptions/gitlab_dedicated/">GitLab Dedicated | GitLab Docs</a></li>

</ul>
</details>

**Tags**: `#GitLab`, `#security-vulnerability`, `#CVE`, `#infosec`, `#patch-release`

---

<a id="item-3"></a>
## [OpenAI launches public beta Agents API for production cloud agents](https://openai.com/index/introducing-the-agents-api/) ⭐️ 8.0/10

On September 10, 2026, OpenAI launched the public beta of its Agents API, which lets developers create production-grade cloud agents with a single API call and run them either in an OpenAI-hosted sandbox, on their own infrastructure, or in a partner environment. The API is built on the open-source Codex harness and initially supports long-session context compression, tool search, parallel tool calling, and sub-agent collaboration. This turns agent orchestration — previously something every team had to hand-build with custom loops, sandboxing, and memory management — into a managed platform service, which could significantly lower the barrier to shipping agentic products. It also intensifies competition among agent infrastructure vendors and pushes OpenAI&\#x27;s Codex stack further toward being a general platform rather than just a coding tool. The API reuses the open-source Codex harness, so developers can pick from several integration surfaces of that stack, and it offers deployment flexibility through hosted sandboxes, self-managed infrastructure, or partner environments. During the beta there is no additional platform fee — users only pay for the tokens and tools their agents actually consume.

telegram · zaihuapd · Sep 11, 11:12

**Background**: The Codex harness is the open-source agent runtime behind OpenAI&\#x27;s Codex, exposing entry points such as a non-interactive exec mode, an SDK for programmatic workflows, and an app-server for persistent conversations, streamed events, and approval handling. Context compression addresses a core problem of long-running agents: continuous interaction makes the context window grow without bound, driving up memory cost and latency, so frameworks compress history and observations on the fly. Sub-agent collaboration means a main agent delegates subtasks to specialized agents that work in parallel and return results, an increasingly common pattern for handling complex multi-step work, while a sandbox is an isolated environment where an agent can safely execute code and call tools.

<details><summary>References</summary>
<ul>
<li><a href="https://developers.openai.com/blog/codex-as-a-platform">Codex as a platform: build on the open agent harness | OpenAI ...</a></li>
<li><a href="https://openai.com/index/unlocking-the-codex-harness/">Unlocking the Codex harness: how we built the App Server - OpenAI</a></li>
<li><a href="https://arxiv.org/html/2510.00615">Acon: Optimizing Context Compression for Long-horizon LLM Agents</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#AI Agents`, `#API`, `#Developer Tools`, `#LLM`

---

<a id="item-4"></a>
## [OpenAI Open to Slowing Frontier AI Development, Altman Tells Staff](https://www.bloomberg.com/news/articles/2026-09-11/openai-is-open-to-slowing-cutting-edge-ai-ceo-sam-altman-tells-staff) ⭐️ 7.0/10

According to a Bloomberg report citing multiple people familiar with the matter, CEO Sam Altman told OpenAI staff at an all-hands meeting this week that the company is open to slowing its frontier AI development in coordination with other AI labs, while acknowledging that some companies may not want to cooperate. OpenAI has reportedly already slowed work on some models and paused certain internal AI training runs over safety concerns, and the company declined to comment on the report. A leading frontier lab publicly signalling willingness to coordinate a slowdown is a notable shift in the competitive dynamics of the AI industry, where labs have long raced to release ever more capable models. If such coordination materialises — even voluntarily — it could reshape release timelines, influence AI governance and regulation debates, and pressure rivals such as Anthropic and Google DeepMind to take similar positions. The account is secondhand, attributed to unnamed sources, and OpenAI declined to comment, so the scope, timeframe and any concrete conditions of a slowdown remain unverified. Altman&\#x27;s reported caveat that some labs may not cooperate highlights the core collective-action problem: a unilateral pause by one lab can simply hand the lead to competitors, and the company&\#x27;s chief scientist has separately called for a voluntary slowdown until shared safety standards exist.

telegram · zaihuapd · Sep 11, 02:23

**Background**: Frontier AI refers to the most advanced models at the leading edge of capability, a term popularised by the 2023 Bletchley Declaration signed by 28 countries at the first global AI Safety Summit and now used in major regulatory frameworks. It is typically defined by a combination of very high training compute, broad applicability, and evidence of potentially dangerous emergent capabilities. AI safety as a field covers both technical research and the norms, policies and industry coordination intended to reduce societal-scale risks from such models, and concern about a competitive &\#x27;race&\#x27; dynamic has made voluntary, coordinated slowdowns a recurring proposal among researchers and executives.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_safety">AI safety - Wikipedia</a></li>
<li><a href="https://aisecurityandsafety.org/en/glossary/frontier-ai/">Frontier AI — Definition &amp; Implications for AI Safety</a></li>
<li><a href="https://www.ncsc.gov.uk/frontier-ai">Frontier AI: what you need to know | National Cyber Security ...</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#OpenAI`, `#frontier AI`, `#AI governance`, `#industry news`

---

<a id="item-5"></a>
## [China Merges Lunar Programs, Cancels Chang&\#x27;e 8 South Pole Mission](https://spacenews.com/china-alters-change-8-lunar-south-pole-mission-amid-lunar-program-reorganization/) ⭐️ 7.0/10

In May 2026 the China Manned Space Agency announced that the uncrewed lunar exploration program previously run by the China National Space Administration and the crewed lunar landing effort would be merged into a single &quot;Lunar Exploration Project,&quot; unified in terms of missions, resources and personnel. As a result, the standalone Chang&\#x27;e 8 mission — originally slated to launch around 2029 and land at Moulton crater near the lunar south pole — has been cancelled or substantially restructured, and Pakistan confirmed in September 2026 that it was one of the international payload partners affected, with its payload to be moved to other lunar missions in 2030–2031. This consolidation puts China&\#x27;s robotic and crewed lunar efforts under one management structure, a reorganization that could speed up the crewed landing goal and reshape the schedule for the China-led International Lunar Research Station. It also disrupts the planning of foreign payload partners and removes a dedicated south-pole science mission from the near-term manifest, affecting lunar science and international cooperation timelines. According to Chinese Wikipedia, Chang&\#x27;e 8 was to land at Moulton crater in the lunar south polar region and, together with Chang&\#x27;e 7, form the basic configuration of a south-pole research station as part of the International Lunar Research Station; it was to be China&\#x27;s first probe in the ILRS construction phase. Some Chinese reports suggest the mission may have been shifted to roughly 2030–2031 rather than entirely abandoned, with its payloads reassigned to other lunar landing missions.

telegram · zaihuapd · Sep 11, 04:00

**Background**: China&\#x27;s lunar exploration program, named Chang&\#x27;e after the Chinese moon goddess, has progressed from orbiters and landers \(Chang&\#x27;e 1–4\) to sample returns: Chang&\#x27;e 5 brought back near-side samples in 2020, and Chang&\#x27;e 6 returned the first far-side samples in 2024. Chang&\#x27;e 7 is planned to scout the lunar south pole, where permanently shadowed craters may hold water ice, and Chang&\#x27;e 8 was meant to follow as a technology and resource-utilization precursor. The International Lunar Research Station is a China-led, Russia-partnered plan for a long-term lunar base, while the crewed landing effort — run by the China Manned Space Agency with the Long March 10 rocket, Mengzhou spacecraft and Lanyue lander — targets a Chinese astronaut on the Moon before 2030.

<details><summary>References</summary>
<ul>
<li><a href="https://zh.wikipedia.org/wiki/%E5%AB%A6%E5%A8%A5%E5%85%AB%E5%8F%B7">嫦娥八号 - 维基百科，自由的百科全书</a></li>
<li><a href="https://finance.sina.com.cn/jjxw/2026-05-23/doc-inhyvxrt7118669.shtml">我国整合现有载人登月和无人探月任务，整合后统称为月球探测工程|月球...</a></li>
<li><a href="https://www.sina.cn/news/detail/5341741499812583.html">嫦娥八号任务取消及载荷转移|ce8|30/31任务_新浪新闻</a></li>

</ul>
</details>

**Tags**: `#space`, `#china`, `#lunar-exploration`, `#chang&\#x27;e-8`, `#policy`

---

<a id="item-6"></a>
## [The Waymo Effect: How AI Quietly Weakens Research Collaboration](https://www.researchagenda.news/articles/the-waymo-effect.html) ⭐️ 7.0/10

Daniel Hook, Chief Scientific Officer at Holtzbrinck, published a new article for Research Agenda introducing the &quot;Waymo effect&quot; as an analogy for large language models in research: just as self-driving cars remove the driver, LLMs remove friction from collaboration but may also remove questioning, serendipitous encounters, and joint thinking from the research process. The article argues that the answer is not to ban AI, but to ensure humans retain control over research questions, methods, and conclusions. The piece shifts the debate about AI in science away from pure productivity metrics toward the social fabric of research, warning that faster individual output may come at the cost of more homogeneous ideas and weakened collaboration networks. Its policy recommendations — treating face-to-face exchange, visits, and unstructured discussion as research infrastructure, and reducing the single-minded reward for speed — are aimed at funders and institutions that shape how science actually gets done. The argument is framed as an analogy rather than an empirical study: it claims that LLMs behave like the &quot;frictionless colleague,&quot; smoothing away the friction that ironically produces critical challenge and chance encounters. Daniel Hook is Chief Scientific Officer at Holtzbrinck, the publisher group behind Springer Nature and other research businesses, giving the commentary institutional weight in research-policy circles.

telegram · zaihuapd · Sep 11, 13:57

**Background**: Waymo is Alphabet&\#x27;s autonomous ride-hailing service, whose driverless cars made the removal of the human operator a mundane, everyday experience — hence the analogy&\#x27;s name. Large language models have been rapidly adopted across research for literature review, drafting, coding, and brainstorming, and the debate over whether they boost or homogenize science has become a central topic in research policy. Research Agenda is a publication focused on analysis and commentary about the research ecosystem, and this article sits alongside a broader discussion of how AI-driven competition may be reducing openness and collaboration in research.

<details><summary>References</summary>
<ul>
<li><a href="https://www.researchagenda.news/articles/the-waymo-effect.html">The Waymo effect : how AI is quietly making research less...</a></li>
<li><a href="https://www.linkedin.com/posts/digital-science_the-waymo-effect-how-ai-is-quietly-making-activity-7502685867598159872-7Q_8">The Waymo effect : how AI is quietly making research less...</a></li>
<li><a href="https://aidownload.com/updates/93935e75-836c-4422-8e0b-dfc390cbb508">The Waymo effect : how AI is quietly making research ... | AI Download</a></li>

</ul>
</details>

**Tags**: `#AI 与科研`, `#研究协作`, `#大语言模型`, `#科研政策`, `#技术哲学`

---

<a id="item-7"></a>
## [Report: Anthropic Building Surveillance System to Track Anti-AI Activists](https://prospect.org/2026/09/09/anthropic-artificial-intelligence-surveillance-system-monitor-activists/) ⭐️ 7.0/10

According to a report published by The American Prospect on September 9, 2026, Anthropic is reportedly building a predictive security and surveillance apparatus to track anti-AI activists, monitor protests near its executives and assets, and flag suspects to police. Job postings and executive interviews indicate the effort sits with Anthropic&\#x27;s Global Safety, Intelligence, and Security \(GSIS\) team, which also uses external risk-detection services to follow protests; Anthropic did not respond to a request for comment. If accurate, the report puts one of the world&\#x27;s leading AI safety labs — a company that publicly frames its mission around responsible AI development — in the position of using AI-driven risk prediction against its own critics, raising hard questions about corporate governance, civil liberties, and surveillance norms that could spread across the AI industry. It is likely to intensify scrutiny from regulators, employees, and researchers who doubt that AI companies can police dissent while claiming to serve the public interest. The claim is a secondhand relay based on job postings and executive statements rather than documentation of a deployed system, and the GSIS team&\#x27;s stated scope covers intelligence, executive protection, investigations, travel and event security, and security operations. Reported capabilities range from monitoring protests near executives and assets to pre-emptively scoring risk and reporting suspects to law enforcement — a practice critics liken to corporate &quot;threat intelligence&quot; programs historically aimed at labor and environmental activists.

telegram · zaihuapd · Sep 11, 15:33

**Background**: Anthropic is an AI safety and research company, structured as a public benefit corporation, best known for its Claude family of large language models and for stressing AI alignment and interpretability. Its Global Safety, Intelligence, and Security \(GSIS\) team is described in the company&\#x27;s own job listings as responsible for protecting its people, facilities, and operations worldwide. &quot;Predictive risk assessment&quot; is a corporate security approach that uses data analytics to anticipate incidents before they happen, and vendors market external digital risk-detection services that scan open sources for emerging threats. The American Prospect is a US progressive policy magazine that originally published this report.

<details><summary>References</summary>
<ul>
<li><a href="https://prospect.org/2026/09/09/anthropic-artificial-intelligence-surveillance-system-monitor-activists/">Anthropic Is Building a Predictive... - The American Prospect</a></li>
<li><a href="https://jobs.menlovc.com/companies/anthropic/jobs/76278239-head-of-resilience-operations-global-safety-intelligence-security">Head of Resilience Operations, Global Safety , Intelligence ...</a></li>
<li><a href="https://www.anthropic.com/">Home \ Anthropic</a></li>

</ul>
</details>

**Tags**: `#AI ethics`, `#Anthropic`, `#surveillance`, `#AI governance`, `#privacy`

---

<a id="item-8"></a>
## [Japan&\#x27;s Digital Agency Hit by Unauthorized Server Access, Data of ~246,000 at Risk](https://www.bloomberg.com/news/articles/2026-09-11/japan-s-digital-agency-hit-by-unauthorized-access-to-servers) ⭐️ 6.0/10

Japan&\#x27;s Digital Agency disclosed that its servers were accessed without authorization, potentially exposing the personal data of roughly 246,000 people. An investigation found that the attacker exploited a VPN vulnerability in late June and used a maintenance account to reach a large number of files. The breach strikes the very agency created to modernize and secure Japan&\#x27;s public-sector IT, so it is likely to raise questions about whether centralizing government systems has widened the blast radius of a single compromised account. It also affects a large number of ordinary citizens whose names, emails and phone numbers could be abused for phishing and identity fraud. The potentially exposed data includes names, email addresses and phone numbers, though the agency says it has not yet confirmed any actual misuse of the information. Notably, the intrusion did not rely on sophisticated malware but on a VPN flaw combined with a maintenance account, a combination that suggests a gap in privileged-account controls and network segmentation.

telegram · zaihuapd · Sep 11, 05:10

**Background**: Japan&\#x27;s Digital Agency is the government body responsible for consolidating and modernizing the country&\#x27;s public digital services, which means it handles systems and data used across many ministries and citizen-facing services. A VPN \(virtual private network\) creates an encrypted tunnel that lets remote staff reach internal systems, and vulnerabilities in such remote-access gateways are a common entry point for attackers because they sit directly on the network perimeter. A maintenance account is a privileged login typically used for administration, so if it is not protected with strong authentication and strict access rules, it can give an intruder broad reach inside a network.

**Tags**: `#cybersecurity`, `#data breach`, `#Japan`, `#government`, `#VPN vulnerability`

---