---
layout: default
title: "Horizon Summary: 2026-11-23 (EN)"
date: 2026-11-23 23:03:50 +0000
lang: en
report: default
---

> From 177 items, 8 important content pieces were selected

---

1. [Codex2api hit by suspected supply-chain poisoning via hijacked author account](#item-1) ⭐️ 8.0/10
2. [Google built a simulated internet, Mirror Dimension, to test Chrome&\#x27;s AI agents](#item-2) ⭐️ 7.0/10
3. [Windows Server 2028 drops WoW64 by default, so 32-bit apps need a manual reinstall](#item-3) ⭐️ 7.0/10
4. [Meta AI Chief Alexandr Wang Says Superintelligence Is Arriving, Warns Control at Risk](#item-4) ⭐️ 7.0/10
5. [Ant Group leads $100M pre-A round in Simplexity Robotics at $1.6B valuation](#item-5) ⭐️ 6.0/10
6. [GLM-5.4 Rolls Out to All GLM Coding Plan Users With Vision and 50% More Quota](#item-6) ⭐️ 6.0/10
7. [Anthropic Caps IPO Underwriter Teams at Four, Bans Rival Work](#item-7) ⭐️ 6.0/10
8. [Open-source nospeaker makes MacBook trackpad vibrations speak words aloud](#item-8) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Codex2api hit by suspected supply-chain poisoning via hijacked author account](https://github.com/WormW/codex2api-incident-2026-11) ⭐️ 8.0/10

The Codex2api project appears to have suffered a supply-chain attack after its author&\#x27;s account was compromised; the attacker bypassed the main branch by pushing tags directly, causing Release builds to ship backdoored versions 3.1.10 through 3.1.12. Version 3.1.11 removed authentication entirely, effectively giving attackers password-free remote command execution, while a malicious workflow exfiltrated 16 GitHub Actions secrets and affected at least 21 repositories under the same account. Anyone running a compromised release should assume full host and credential compromise, since unauthenticated remote command execution plus stolen CI secrets can cascade into source code, cloud resources and third-party API accounts. The incident also shows that tag-level pushes can slip past branch protection, a pattern that has hit thousands of GitHub accounts in recent large-scale CI secret-stealing campaigns, so developers should treat release artifacts as untrusted until verified. The report advises users who installed or upgraded to 3.1.10–3.1.12 to stop using the tool immediately, roll back to 3.1.9, and rotate every related credential, including GitHub tokens, SSH keys, database passwords and DeepSeek API keys. The fact that 16 secrets across roughly 21 repositories were readable suggests the author account carried broad, long-lived permissions rather than being scoped per repository.

telegram · zaihuapd · Nov 23, 11:21

**Background**: A supply-chain attack targets the build and distribution pipeline rather than the source code users read, so the malicious change never has to appear on the main branch — pushing a Git tag is enough to trigger a release build. GitHub Actions secrets are encrypted environment variables injected into CI jobs to hold tokens, SSH keys and API credentials; once a workflow is compromised, those values can be printed to logs or sent to an attacker-controlled endpoint. Branch protection rules often fail here because accounts with maintainer or admin rights can bypass them, which is why tag protection and required reviews on release workflows matter.

<details><summary>References</summary>
<ul>
<li><a href="https://cheatsheetseries.owasp.org/cheatsheets/GitHub_Actions_Security_Cheat_Sheet.html">GitHub Actions Security - OWASP Cheat Sheet Series</a></li>
<li><a href="https://www.endorlabs.com/learn/github-actions-supply-chain-attack-targeting-ci-secrets-at-scale">Hijacked GitHub Accounts Push “wfx” CI Secret Stealer to... | Endor Labs</a></li>
<li><a href="https://vapi.ai/blog/our-response-to-june-3-supply-chain-incident">Our response to the June 3, 2026 supply chain incident - Vapi AI Blog</a></li>

</ul>
</details>

**Discussion**: The item was relayed by a group member who warned that anyone who updated codex2api that afternoon should check immediately; no extended discussion thread with additional technical analysis was available.

**Tags**: `#supply-chain-security`, `#backdoor`, `#github-actions`, `#security-incident`, `#credential-rotation`

---

<a id="item-2"></a>
## [Google built a simulated internet, Mirror Dimension, to test Chrome&\#x27;s AI agents](https://www.landian.news/archives/128701.html) ⭐️ 7.0/10

Google reportedly built a simulated internet called Mirror Dimension, containing thousands of synthetic websites, to test Chrome&\#x27;s AI agent as it opens sites, searches and browses, logs in, adds items to a cart and completes tasks. Each engineer runs tests in a separately isolated environment, with more than 1,000 test cases executed per day, focused on defending against prompt-injection attacks from malicious web pages. Browser-based agents constantly ingest untrusted web content, which makes prompt injection the defining security risk for this product category, so a large-scale mirrored web gives Google a way to train and evaluate its agent without touching real sites or real user accounts. How Google tests here will likely become a reference point for how other browser vendors and agent builders validate safety before shipping. The setup reportedly covers thousands of synthetic sites with per-engineer isolation and a daily workload of over 1,000 test cases, emphasizing resistance to prompt injection embedded in malicious pages. Caveats: this is a second-hand summary without disclosed technical details, and a mirrored web may not fully capture the adversarial diversity and evolving trickery of the real internet.

telegram · zaihuapd · Nov 23, 01:30

**Background**: AI agents that drive a browser work by reading page content and deciding what to click or type next, which means any web page can feed instructions into the model&\#x27;s context — an indirect prompt injection attack that tries to make the agent ignore its developer&\#x27;s instructions or perform unauthorized actions. Because these payloads can be hidden in ordinary-looking HTML, vendors such as Anthropic and Perplexity have published dedicated defenses and detection systems that run alongside the agent. Sandboxed, disposable environments have therefore become standard practice for testing agents before they are exposed to real sites and real credentials.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2511.20597">BrowseSafe: Understanding and Preventing Prompt Injection ... BrowseSafe: Understanding and Preventing Prompt Injection ... Top Stories News about AI, MCP, OWASP News about AI, KnowBe4 Platform, MCP Also in the news BrowseSafe: Understanding and preventing prompt injection ... How Prompt Injection Attacks Compromise AI Agents in 2026 Fooling AI Agents: Web-Based Indirect Prompt Injection ... Prompt Injection Attacks on AI Agents: How to Detect and ... Mitigating prompt injections in browser use \ Anthropic</a></li>
<li><a href="https://arxiv.org/html/2511.20597v1">BrowseSafe: Understanding and Preventing Prompt Injection ...</a></li>
<li><a href="https://www.perplexity.ai/hub/blog/browsesafe">BrowseSafe: Understanding and preventing prompt injection ...</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#browser security`, `#prompt injection`, `#Chrome`, `#testing infrastructure`

---

<a id="item-3"></a>
## [Windows Server 2028 drops WoW64 by default, so 32-bit apps need a manual reinstall](https://www.windowslatest.com/2026/11/23/32-bit-apps-days-are-numbered-as-microsoft-strips-support-bit-by-bit-starting-with-windows-server-2028-but-windows-11-is-safe-for-now/) ⭐️ 7.0/10

At Ignite 2026, Microsoft said Windows Server 2028 will ship without the WoW64 compatibility subsystem, meaning 32-bit applications will not run out of the box. Administrators who still need them can re-add WoW64 as a Features on Demand \(FoD\) package, typically via PowerShell or DISM on Server Core, and the release is planned for fall 2027 alongside Windows 11 27H2. This is a significant compatibility shift for enterprise IT, since many organizations still run legacy 32-bit line-of-business applications, management agents, or installers on their servers, and those will now fail silently unless WoW64 is explicitly added during image building or upgrades. It also signals Microsoft&\#x27;s broader direction of trimming legacy subsystems to shrink the attack surface, with client Windows potentially following later. WoW64 as an FoD must be sourced from a side-by-side store, Windows Update, or installation media, which matters for air-gapped and locked-down servers built from custom images. Microsoft frames the change as reducing attack surface and blocking 32-bit malware, and it notes that Windows 11 still retains WoW64 with no removal plan announced; note also that 64-bit Windows has never supported 16-bit binaries or 32-bit drivers regardless of WoW64.

telegram · zaihuapd · Nov 23, 03:03

**Background**: WoW64 stands for &quot;Windows 32-bit on Windows 64-bit&quot; and is the lightweight compatibility layer that lets 32-bit programs run unmodified on 64-bit Windows, handling structural differences such as registry and file-system redirection into locations like SysWOW64 and Wow6432Node. It has shipped in every 64-bit edition of Windows since the XP/Server 2003 era, so two decades of software assumes it is present. Features on Demand \(FoD\) are optional capability packages that Microsoft unbundles from the base OS image, letting administrators install roles and compatibility components only when needed — the same mechanism previously used to add the Application Compatibility FoD to Server Core.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/WoW64">WoW64 - Wikipedia</a></li>
<li><a href="https://learn.microsoft.com/en-us/windows-server/get-started/server-core-app-compatibility-feature-on-demand">Install Server Core Application Compatibility Feature on Demand Usage example</a></li>
<li><a href="https://wccftech.com/microsoft-is-removing-32-bit-app-support-by-default-in-windows-server-2028-but-windows-11-remains-unaffected/">Microsoft Is Removing 32-Bit App Support By Default In Windows ...</a></li>

</ul>
</details>

**Tags**: `#Windows Server`, `#WoW64`, `#32-bit compatibility`, `#Microsoft`, `#enterprise IT`

---

<a id="item-4"></a>
## [Meta AI Chief Alexandr Wang Says Superintelligence Is Arriving, Warns Control at Risk](https://thenextweb.com/news/metas-ai-chief-says-superintelligence-is-arriving-and-control-is-at-risk) ⭐️ 7.0/10

Meta Chief AI Officer and Meta Superintelligence Labs head Alexandr Wang published a long post on X arguing that superintelligence is no longer a &quot;someday&quot; question, pointing to a Riemann Hypothesis proof produced by mathematician Levent Alpöge with Anthropic&\#x27;s Claude that was machine-verified by the Lean and Mathlib community over the weekend. Wang used the result to claim the gap between AI and top human researchers is down to three things — concrete knowledge, engineering integration, and experimentation — and called for urgent investment in safety, alignment, and safeguard research. This is a sitting chief AI officer at a frontier lab publicly declaring superintelligence imminent and human control doubtful, which could shape how labs, regulators, and funders weigh safety work against capability races. The claim&\#x27;s centerpiece is equally consequential: if a machine-verified proof of the Riemann Hypothesis really came out of an AI-assisted effort, it would be a landmark demonstration of AI doing first-rate mathematics rather than merely assisting. The proof currently has no human-readable version, and the claim is circulating secondhand through a Telegram aggregator rather than a primary announcement or paper, so it has not been independently confirmed in a form mathematicians can actually inspect. Formal verification in Lean with Mathlib guarantees that the proof term checks against the stated formal theorem, but it does not by itself guarantee that the formal statement faithfully captures the intended mathematical claim.

telegram · zaihuapd · Nov 23, 12:49

**Background**: The Riemann Hypothesis, proposed by Bernhard Riemann in 1859, is the conjecture that the non-trivial zeros of the Riemann zeta function all lie on a single critical line, a statement whose truth would pin down the apparently random distribution of prime numbers; it remains unproven and is one of the most famous open problems in mathematics. Lean is a functional programming language and interactive theorem prover built for formalizing mathematics, in which a proof is a machine-checkable object rather than a human argument; Mathlib is the community-driven library of formalized mathematics built on top of it. Superintelligence here refers to a hypothetical system that greatly exceeds human intelligence and can recursively improve itself, and &quot;alignment&quot; refers to the problem of ensuring such systems reliably pursue intended goals.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Riemann_hypothesis">Riemann hypothesis - Wikipedia</a></li>
<li><a href="https://www.scientificamerican.com/article/anthropic-mathematician-claims-to-prove-riemann-hypothesis-most-famous-problem-in-all-of-math/">Anthropic mathematician proves Riemann hypothesis , most famous...</a></li>
<li><a href="https://lean-lang.org/learn/">Learn — Lean Lang</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#superintelligence`, `#AI alignment`, `#frontier AI`, `#formal verification`

---

<a id="item-5"></a>
## [Ant Group leads $100M pre-A round in Simplexity Robotics at $1.6B valuation](https://www.bloomberg.com/news/articles/2026-11-22/ant-group-bets-on-simplexity-to-thrive-in-china-s-humanoid-race) ⭐️ 6.0/10

Chinese embodied-intelligence startup Simplexity Robotics closed a $100 million pre-A round led by Jack Ma-backed Ant Group, at a post-money valuation of $1.6 billion, with existing investors Alibaba, Tencent, HongShan \(Sequoia China\) and BlueRun Ventures following on. Chairman and co-founder Wang Kai confirmed the round to Bloomberg, which reported the deal on November 22, 2026. The round shows China&\#x27;s largest internet platforms converging on humanoid robotics as a strategic bet, and at a $1.6 billion valuation it makes Simplexity one of the country&\#x27;s most highly valued early-stage embodied-AI startups before shipping a commercial product. Bloomberg notes China already accounts for roughly 97% of global humanoid robot shipments, so this capital is aimed at defending that lead against US rivals while fighting for share at home. The company was founded in July 2025 with a core team drawn from Li Auto, including CEO Jia Peng, COO Wang Jiajia and chairman Wang Kai; in March it disclosed it had closed five funding rounds worth a cumulative 2 billion yuan within six months of launch, at a valuation already above $1 billion. Bloomberg reports the new capital will go toward competing with more established manufacturers such as Unitree and UBTECH.

telegram · zaihuapd · Nov 23, 02:02

**Background**: Embodied AI refers to AI models embedded in physical hardware that can perceive multimodal inputs from the real world and act on them, with humanoid robots being the most visible form. Simplexity describes its approach as combining unified \(end-to-end\) models, data closed loops and high-reliability hardware, the same three pillars that most Chinese humanoid startups emphasize. China&\#x27;s robotics sector has drawn heavy state and private investment, and internet giants like Alibaba, Tencent and Ant have been building stakes across the supply chain, from model developers to component makers.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bloomberg.com/news/articles/2026-11-22/ant-group-bets-on-simplexity-to-thrive-in-china-s-humanoid-race">Ant Group Bets on Simplexity in China’s Humanoid Race - Bloomberg</a></li>
<li><a href="https://www.linkedin.com/posts/caproasia_china-robot-startup-simplexity-robotics-raised-activity-7438465152846385152-3W35">China Robot Startup Simplexity Robotics Raised $290 Million...</a></li>
<li><a href="https://www.aastocks.com/en/usq/quote/stock-news-content.aspx?symbol=LI&amp;id=NOW.1507775">CN Embodied Intelligence Startup Simplexity Robotics Total...</a></li>

</ul>
</details>

**Tags**: `#embodied-ai`, `#humanoid-robotics`, `#venture-funding`, `#china-tech`, `#industry-news`

---

<a id="item-6"></a>
## [GLM-5.4 Rolls Out to All GLM Coding Plan Users With Vision and 50% More Quota](https://x.com/ZixuanLi_/status/2124719275864670681) ⭐️ 6.0/10

GLM-5.4 is now available to all GLM Coding Plan subscribers, bringing new vision \(multimodal image understanding\) capabilities and stronger overall programming performance compared with GLM-5.3. For plans whose quota is counted on a weekly basis, GLM-5.4 also raises the allowance by 50% relative to GLM-5.3. Coding-plan subscribers are heavy daily users of AI-assisted development, so adding vision plus a 50% larger weekly quota directly extends what they can do inside tools such as Claude Code, Cline, Kilo Code and OpenCode without hitting limits. It also signals that Z.ai is iterating its flagship GLM line quickly to stay competitive with other frontier coding models. The announcement gives no benchmark numbers or context-window details, and the vision capability is described only in general terms, so concrete quality gains still need independent verification. Quota only increases for weekly-billed plans, meaning monthly or per-token API billing arrangements are unaffected.

telegram · zaihuapd · Nov 23, 04:47

**Background**: GLM is the model family from Z.ai \(Zhipu AI\); GLM-5.3, released in August 2026 with 753 billion parameters \(40 billion active\), was positioned as the strongest open-weights model for coding. The GLM Coding Plan is Z.ai&\#x27;s subscription aimed at developers, starting at roughly $18/month for the Lite tier and usable inside third-party coding agents like Claude Code and Cline. Subscribers pick which GLM model to run, so a new version like GLM-5.4 can be adopted simply by switching models in their client.

<details><summary>References</summary>
<ul>
<li><a href="https://z.ai/subscribe">GLM Coding Plan — AI Coding Powered by GLM-5.4 &amp; GLM-5.3 ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/GLM_%28AI%29">GLM (AI) - Wikipedia</a></li>
<li><a href="https://z.ai/blog/glm-5.3">GLM-5.3: Frontier Coding with Emergent Cyber Capabilities - z.ai</a></li>

</ul>
</details>

**Tags**: `#GLM-5.4`, `#AI coding`, `#model release`, `#multimodal`, `#developer tools`

---

<a id="item-7"></a>
## [Anthropic Caps IPO Underwriter Teams at Four, Bans Rival Work](https://www.reuters.com/world/like-spacex-anthropic-ran-an-unusual-ipo-process-chafing-some-bankers-2026-11-22/) ⭐️ 6.0/10

According to Reuters, Anthropic imposed unusually strict terms on the banks underwriting its record-setting IPO, requiring that deal teams be capped at four senior bankers and asking some bank executives to sign six-month non-compete clauses barring them from working for OpenAI, Cursor, DeepSeek, Hugging Face and other rivals. The company also tracked document access through a watermarked online system that blocked downloads, and sent a revised prospectus at 2 a.m. before the roadshow with only a few hours for banks to sign off — prompting some bankers to refuse to sign at all. The episode shows how much leverage top AI labs now hold over Wall Street, and it could set a precedent for how AI companies structure future offerings and guard competitive secrets during the disclosure-heavy IPO process. It also signals that the talent and information rivalry among AI firms has extended into their banking relationships, not just their engineering teams. The confidentiality measures included a watermarked online document system that logged who viewed files and prevented saving, while the compressed four-person teams mean far fewer bankers than usual get visibility into the deal. The combination of tight exclusivity terms and a rushed signing window was severe enough that some bankers declined to sign the agreements.

telegram · zaihuapd · Nov 23, 05:15

**Background**: In a traditional IPO, the lead underwriters advise the company on valuation and pricing, market the shares to investors, and often commit to buying unsold stock; syndicates can involve dozens of bankers across several firms. Because underwriters see confidential financials and strategy before the public does, issuers commonly impose confidentiality rules, and non-compete or &quot;quiet period&quot; restrictions on the banks involved are not unheard of — though a six-month ban covering named AI competitors is unusually broad. Watermarking is a common document-protection technique that embeds a visible or invisible identifier tied to a specific recipient so that any leak can be traced back to its source, and it is widely used in deal rooms and other high-stakes document sharing.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Digital_watermarking">Digital watermarking - Wikipedia</a></li>
<li><a href="https://digify.com/blog/pdf-document-watermarking/">PDF &amp; document watermarking : How to add watermarks ... - Digify</a></li>

</ul>
</details>

**Tags**: `#Anthropic`, `#IPO`, `#AI industry`, `#non-compete`, `#business news`

---

<a id="item-8"></a>
## [Open-source nospeaker makes MacBook trackpad vibrations speak words aloud](https://m.mydrivers.com/newsview/1167826.html?ref=https%3A//www.google.com/) ⭐️ 6.0/10

Developer Cody Collier has open-sourced a tool called nospeaker that turns a MacBook&\#x27;s Force Touch trackpad into a loudspeaker by driving its haptic motor at up to 4,000 vibrations per second, fast enough for the glass surface to become audible. The tool feeds text through macOS speech synthesis, samples two formants every 10 milliseconds, and replays them together with loudness and pitch data, producing a distinctly robotic voice. The project is a striking demonstration that the haptic actuators already inside millions of laptops can be pushed far beyond click simulation and into the audible range, blurring the line between feedback hardware and audio output. It also shows how hobbyists keep finding unintended uses for Apple&\#x27;s tightly controlled trackpad hardware, even when that means reaching for private frameworks. The tool can only reproduce speech — music and video playback are out of scope — and it bypasses Apple&\#x27;s public haptics APIs by calling the private MultitouchSupport framework, which makes it fragile across OS versions. It requires a Force Touch trackpad, and the author says it has only been verified on a MacBook Pro, which the report describes as an &quot;M5 Max&quot; model; measured output spans roughly 100 Hz to 4 kHz, with the clearest response around 1 kHz.

telegram · zaihuapd · Nov 23, 07:16

**Background**: Apple&\#x27;s Force Touch trackpad has no physical button that moves; instead, electromagnetic actuators create a vibration that the finger perceives as a click, which is why the surface can in principle be driven at other frequencies too. Formant synthesis, the technique used here, models human speech as a set of resonant peaks in the vocal tract — such as F1 and F2 — rather than by stitching together recorded samples, which is why the result sounds synthetic. MultitouchSupport is a private Apple framework that apps can use to talk to the trackpad directly, but because it is undocumented and not part of the public SDK, software that depends on it can break with any macOS update.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Force_Touch">Force Touch - Wikipedia</a></li>
<li><a href="https://www.macworld.com/article/671590/how-does-force-touch-work.html">Inside Apple&#x27;s Force Touch trackpad | Macworld Force Touch - Wikipedia What is Force Touch? Apple&#x27;s haptic feedback technology explained Haptic Touchpad vs Regular Touchpad: Which One is Better? MacBook modder turns Apple’s Force Touch trackpad into a ... How to Turn Touchpad Haptic Feedback on or off in Windows 11</a></li>
<li><a href="https://stackoverflow.com/questions/36201217/how-to-link-against-frameworks-that-are-not-in-the-standard-location">macos - How to link against frameworks that are not... - Stack Overflow</a></li>

</ul>
</details>

**Tags**: `#haptics`, `#open-source`, `#macOS`, `#speech-synthesis`, `#hardware-hacking`

---