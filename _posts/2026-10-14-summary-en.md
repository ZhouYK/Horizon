---
layout: default
title: "Horizon Summary: 2026-10-14 (EN)"
date: 2026-10-14 23:05:14 +0000
lang: en
report: default
---

> From 182 items, 7 important content pieces were selected

---

1. [First Stargardt patient implanted with PRIMA visual chip reads a word](#item-1) ⭐️ 8.0/10
2. [GitHub Suspends KernelSU Developer&\#x27;s Account and Related Organizations](#item-2) ⭐️ 7.0/10
3. [Anthropic replaces Git with in-house Scion version control system](#item-3) ⭐️ 7.0/10
4. [DeepMind and Singapore Launch On-Device AI Scam Detector](#item-4) ⭐️ 7.0/10
5. [OPPO Partners with Manus to Bring AI Agents to ColorOS 17](#item-5) ⭐️ 6.0/10
6. [Doubao Phone Assistant Opens Third-Party App Screen Automation via SAEP](#item-6) ⭐️ 6.0/10
7. [EU Weighs Lifting Chinese Firm&\#x27;s Sanctions to Save ASML Supplier](#item-7) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [First Stargardt patient implanted with PRIMA visual chip reads a word](https://science.xyz/news/stargardt-first-rehab/) ⭐️ 8.0/10

Science Corporation has implanted its PRIMA vision-restoring chip into the first patient with Stargardt disease; the surgery took place in May at the Sydney Eye Hospital in Australia, and during rehabilitation the patient first perceived letters and then read a word out loud, according to an announcement by CEO Max Hodak. Stargardt disease blinds roughly 150,000 people worldwide and has no cure, so a patient moving from blindness to reading a word is a meaningful milestone for retinal prosthetics; because PRIMA is already approved in Europe for age-related macular degeneration, this trial extends an existing clinical platform to a new inherited retinal disease population rather than starting from scratch. PRIMA is a roughly 2mm x 2mm subretinal implant that bypasses lost photoreceptors and electrically stimulates surviving retinal cells, receiving both power and data from a special pair of glasses worn by the patient; this Stargardt implantation is part of a clinical trial and rests on a single patient&\#x27;s early rehabilitation results, and current retinal prostheses generally deliver limited resolution — mainly brightness, contours and motion rather than natural vision.

telegram · zaihuapd · Oct 14, 04:30

**Background**: Stargardt disease is the most common inherited single-gene retinal disease, usually inherited in an autosomal recessive pattern linked to bi-allelic ABCA4 gene variants, and it causes macular degeneration that begins in childhood, adolescence or adulthood and progressively destroys central vision, often leading to legal blindness by the second or third decade of life. Retinal prostheses such as PRIMA are designed to replace the function of dead photoreceptors by stimulating the remaining retinal neurons, which then send signals to the brain. Science Corporation is the neurotechnology company founded by Max Hodak, formerly president of Neuralink.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Stargardt_disease">Stargardt disease</a></li>
<li><a href="https://science.xyz/technologies/prima/general-interest/">PRIMA Visual Prosthesis | Science Corporation</a></li>
<li><a href="https://techcrunch.com/2026/10/13/science-corporation-implants-its-vision-restoring-chip-in-its-first-stargardt-disease-patient/">Science Corporation implants its vision-restoring chip in its ...</a></li>

</ul>
</details>

**Tags**: `#neurotech`, `#visual prosthesis`, `#clinical trial`, `#Stargardt disease`, `#Science Corporation`

---

<a id="item-2"></a>
## [GitHub Suspends KernelSU Developer&\#x27;s Account and Related Organizations](https://x.com/realnullptr/status/2110025105338519970) ⭐️ 7.0/10

Developer RealNullptr says GitHub suspended his personal account \(Dr-TSNG\) along with several open-source organizations he co-owned — KernelSU-Module-Repo, Kernel-SU and libxposed — roughly a month ago, taking the associated community infrastructure offline. As of now GitHub has issued no public explanation for the suspensions. KernelSU and libxposed underpin widely used Android rooting and module-hooking workflows, so losing their hosting, releases and issue trackers disrupts downstream users and module developers who depend on them. The lack of any public explanation also sharpens long-standing concerns about opaque platform governance and the risk of building critical open-source infrastructure on a single, privately controlled host. GitHub has published no stated reason for the bans, and RealNullptr himself speculates it may be connected to an eligibility review of the GitHub Student Developer Pack, meaning the trigger could be an account-tier or identity check rather than a code or content violation. It is also worth noting that the flagship KernelSU repository is hosted under the separate tiann/KernelSU organization, so the practical damage to the upstream project depends on which forks, mirrors or auxiliary repos were actually taken down.

telegram · zaihuapd · Oct 14, 01:34

**Background**: KernelSU is a free and open-source, GPLv3-licensed kernel-space root solution for Android, offering an alternative approach to granting root privileges compared with traditional userspace solutions such as Magisk. libxposed is an API layer related to the Xposed module framework, which lets add-on modules hook and modify app behaviour at runtime and is used by projects such as LSPosed. For these projects GitHub is not just a code host but the distribution channel for releases, CI builds, documentation and community issue tracking, which is why losing access has an outsized operational impact.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/KernelSU">KernelSU</a></li>
<li><a href="https://github.com/tiann/KernelSU">GitHub - tiann/KernelSU: A Kernel based root solution for ...</a></li>
<li><a href="https://gitlab.com/xposed_grp/LSPosed/libxposed">libxposed - GitLab</a></li>

</ul>
</details>

**Tags**: `#GitHub`, `#open-source`, `#KernelSU`, `#Android`, `#platform-governance`

---

<a id="item-3"></a>
## [Anthropic replaces Git with in-house Scion version control system](https://www.anthropic.com/engineering/redesigning-source-control) ⭐️ 7.0/10

Anthropic announced on October 13, 2026 that it has fully migrated its internal monorepo off Git and onto a purpose-built version control system called Scion, completed in about five months by a team of roughly seven engineers. The company says daily merged changes rose from about 2,500 in May 2026 to more than 30,000 by September 2026. This is one of the first cases of a major AI lab concluding that Git itself, not coding, had become its development bottleneck — a signal that AI-generated code volume may be outgrowing traditional developer tooling. If Scion&\#x27;s reported gains hold up, it could push other large monorepo operators and CI vendors toward more server-centric version control designs. Scion keeps the client permanently online and moves the heavy work to the server, which handles file history, blame, commits, merges and rebases while storing data in a distributed fashion; Anthropic reports CPU and memory usage at roughly 1/200 of its previous Git mirror architecture, about 100x faster CI checkouts, and 25% lower CI compute cost. These figures are self-reported by Anthropic, the system is not open sourced, and the details come from a short company engineering post plus secondary coverage rather than independent benchmarks.

telegram · zaihuapd · Oct 14, 02:30

**Background**: Git is a distributed version control system created by Linus Torvalds in 2005; in Git, every developer holds a full copy of the repository history and most operations happen locally. Large companies that keep all code in a single giant repository \(a monorepo\) often struggle with Git&\#x27;s performance, and they typically add layers such as server-side Git mirrors or virtual filesystems to make CI checkouts tolerable. Scion reverses this model: like older centralized systems such as Subversion \(SVN\), it keeps the authoritative logic and computation on the server rather than in each client. Anthropic is the AI company behind the Claude family of models, which are widely used to generate and modify code.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/engineering/redesigning-source-control">Redesigning source control at Anthropic \ Anthropic</a></li>

</ul>
</details>

**Discussion**: Public reaction has been mixed and largely observational: commentator Simon Willison described Scion as effectively a reinvention of centralized source control along the lines of Subversion, while Reddit threads on r/technology, r/ClaudeAI and r/Anthropic focused on the headline 30,401 merges-in-one-day figure and questioned whether such numbers justify abandoning Git. Skepticism centers on the lack of published technical detail or independent verification.

**Tags**: `#Anthropic`, `#Scion`, `#Version Control`, `#Git`, `#CI/CD`

---

<a id="item-4"></a>
## [DeepMind and Singapore Launch On-Device AI Scam Detector](https://deepmind.google/blog/on-device-ai-scam-detection-mddi/) ⭐️ 7.0/10

Google DeepMind and Singapore&\#x27;s Government Technology Agency \(GovTech\) unveiled a lightweight, fine-tuned Gemma model that runs entirely on-device to analyze conversations and warn users about scams in real time, without uploading any data to the cloud. The collaboration was showcased at Singapore International Cyber Week 2026. It is a large-scale government deployment of an on-device LLM that addresses a pressing public-safety problem — scams account for more than half of all reported crimes in Singapore and over S$4 billion in losses since 2019 — while keeping user conversations private. Success here could become a template for other governments looking to apply generative AI to citizen-facing services without sacrificing privacy. The system is built on a fine-tuned version of Gemma, Google DeepMind&\#x27;s family of lightweight open-weight models, which is small enough to run locally on a phone so that message content never leaves the device. Social-engineering scams account for about 80% of total scam losses in Singapore, but the announcement did not disclose benchmarks, latency figures, or false-positive rates.

telegram · zaihuapd · Oct 14, 03:11

**Background**: Fine-tuning is the process of taking a pre-trained model and giving it additional task-specific training so it can specialize — here, recognizing the conversational patterns of scams. &quot;On-device AI&quot; means the model runs locally on the user&\#x27;s own phone rather than on remote servers, which preserves privacy and cuts latency but requires the model to be small and efficient. Gemma, first released by Google DeepMind in February 2024 and built from the same technology as Gemini, is designed for exactly this kind of lightweight, deployable use.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/gemma_language_model">Gemma (language model)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Fine-tuning_%28machine_learning%29">Fine-tuning (machine learning)</a></li>
<li><a href="https://grokipedia.com/page/On-device_artificial_intelligence">On-device artificial intelligence</a></li>

</ul>
</details>

**Tags**: `#on-device AI`, `#Gemma`, `#AI safety`, `#privacy`, `#public sector AI`

---

<a id="item-5"></a>
## [OPPO Partners with Manus to Bring AI Agents to ColorOS 17](https://www.oppo.com/en/newsroom/press/oppo-manus/) ⭐️ 6.0/10

On October 13, 2026, OPPO announced a partnership with the AI agent platform Manus to integrate its agent capabilities into OPPO&\#x27;s AI Mind Pilot, turning complex multi-step tasks into directly usable results. The feature will debut on the OPPO Find X10 series running ColorOS 17, though further availability and market details will be disclosed at launch. The deal signals that mainstream smartphone makers are moving beyond chat-style assistants toward autonomous agents that execute tasks across apps, potentially reshaping how users interact with mobile operating systems. It also positions Manus, an already prominent general-purpose agent, as a key infrastructure provider for consumer hardware rather than just a standalone web service. OPPO says content from local tasks stays on the device and is not shared with Manus, and that any task requiring external processing will first require explicit user confirmation. Specific availability timelines, supported regions, and market details have not yet been announced.

telegram · zaihuapd · Oct 14, 00:13

**Background**: Manus is a general-purpose autonomous AI agent developed by the Chinese team Monica.im, designed to plan and carry out multi-step tasks such as research, data handling, and content production with limited human intervention. ColorOS 17 is OPPO&\#x27;s latest Android-based mobile system, positioned as a &quot;personalized AIOS&quot; that shifts from reactive voice assistants to proactive, context-aware services; AI Mind Pilot is the personal AI layer within it. OPPO&\#x27;s claimed approach combines on-device processing with cloud capabilities, which is why privacy handling of local versus external tasks is a central selling point.

<details><summary>References</summary>
<ul>
<li><a href="https://zh.wikipedia.org/wiki/Manus">Manus - 维基百科，自由的百科全书</a></li>
<li><a href="https://www.oppo.com/en/coloros17/">OPPO ColorOS 17 - Flow with AI | OPPO Global</a></li>
<li><a href="https://we0.ai/zh/articles/oppo-and-manus-bring-agent-mode-to-find-x-9ce79921">OPPO 与 Manus 将 Agent Mode 引入搭载 ColorOS 17 的 Find X10 | We0</a></li>

</ul>
</details>

**Tags**: `#AI Agents`, `#OPPO`, `#Manus`, `#Mobile OS`, `#ColorOS`

---

<a id="item-6"></a>
## [Doubao Phone Assistant Opens Third-Party App Screen Automation via SAEP](https://o.doubao.com/developer) ⭐️ 6.0/10

On October 14, 2026, Doubao Phone Assistant announced that the 30-day public comment period for its Screen Automation Operation Protocol \(SAEP\) had ended, and that it will now gradually open screen-automation permissions so its AI agent can operate inside third-party apps. Apps from Alibaba and Tencent have explicitly declared that they refuse such automation. This is an early attempt to write formal rules for how AI agents may act inside apps they do not own, a question that will shape every mobile assistant in China. If major platforms such as Alibaba and Tencent opt out, the practical reach of Doubao&\#x27;s agent is limited, and the episode becomes a test case for the emerging tension between agent automation and platform control. The protocol is opt-out in design: developers may declare refusal at any time, and once an app explicitly refuses, the agent will not operate on it, with Doubao saying it will promptly disable related operations. Automation is built on Android&\#x27;s AccessibilityService, and reports alternate between expanding SAEP as &quot;Screen Automation Execution Protocol&quot; and &quot;Screen Automation Operation/Declaration Protocol.&quot;

telegram · zaihuapd · Oct 14, 05:00

**Background**: Android&\#x27;s AccessibilityService API lets an app read what is displayed on screen and simulate taps and gestures, and it underpins virtually every mobile automation framework and script tool. Doubao Phone Assistant launched its consumer version on September 14, 2026, opening its &quot;operate the phone&quot; capability as a beta and simultaneously publishing SAEP with a 30-day public comment period, so that third-party apps could declare whether they accept an AI assistant performing screen automation inside them.

<details><summary>References</summary>
<ul>
<li><a href="https://m.21jingji.com/article/20260915/herald/b777fd804dd1d9d19f4aac8c0b58a61e.html">豆 包 手机助手推出GUI合 作 协 议 支持第三方应用 自 主选择 - 21财经</a></li>
<li><a href="https://news.qq.com/rain/a/20261014A05OVM00">豆包手机助手放开第三方应用自动化权限_腾讯新闻</a></li>
<li><a href="https://www.163.com/dy/article/L96O6SLC05198UNI.html">豆包手机助手将陆续放开第三方应用操作权限|智能体|腾讯版小龙虾_网易...</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#mobile automation`, `#Android`, `#platform policy`, `#China tech`

---

<a id="item-7"></a>
## [EU Weighs Lifting Chinese Firm&\#x27;s Sanctions to Save ASML Supplier](https://www.bloomberg.com/news/articles/2026-10-14/eu-set-to-lift-sanction-on-chinese-firm-to-save-asml-supplier) ⭐️ 6.0/10

The EU is negotiating with China to remove sanctions on German company Sindlhauser Materials, a supplier in ASML&\#x27;s supply chain, and in exchange would lift trade restrictions on a Chinese firm accused of aiding Russia&\#x27;s war effort. The topic was discussed by EU trade chief Šefčovič with Chinese Commerce Minister Wang Wentao during Šefčovič&\#x27;s visit to China last week, according to Bloomberg. The case shows how the EU-China sanctions spiral over the war in Ukraine is now feeding directly into the semiconductor supply chain, where a single materials supplier can hold up equipment deliveries to a company as strategically important as ASML. It also highlights Europe&\#x27;s exposure to China&\#x27;s dominance in rare earths and processed materials, a lever Beijing has repeatedly used in trade disputes. Sindlhauser Materials was placed on a Chinese list in July alongside 13 other European firms, apparently in retaliation for EU sanctions related to Russia; the company depends on Chinese rare earth inputs and could reportedly collapse within months if the sanctions persist. The deal under discussion would trade relief for that German supplier against the removal of EU trade restrictions on a Chinese company accused of helping Russia.

telegram · zaihuapd · Oct 14, 15:36

**Background**: Since Russia&\#x27;s full-scale invasion of Ukraine, the EU has imposed successive sanctions packages and has also targeted Chinese companies it suspects of helping Moscow circumvent them — moves Beijing considers unlawful and has answered with countermeasures against European firms. Rare earths matter here because China controls the overwhelming majority of global processing capacity for these elements, which are essential to magnets, electronics and defense production. ASML, the Dutch maker of advanced lithography machines, sits at the centre of the global chip supply chain and relies on a wide network of specialised European materials and components suppliers such as Sindlhauser. That combination — sanctions politics plus a chokepoint material — is what makes a small German supplier a bargaining chip between Brussels and Beijing.

<details><summary>References</summary>
<ul>
<li><a href="https://zh.wikipedia.org/zh-hans/ASML">阿斯麦 - 维基百科，自由的百科全书 艾司摩尔 - 维基百科，自由的百科全书 ASML 是什么？为什么一台 EUV 光刻机，扼住全球最先进的芯片 | 小企鹅... 荷兰ASML公司_百度百科 关于ASML | 光刻技术的领导者 ASML | The world&#x27;s supplier to the semiconductor industry</a></li>
<li><a href="https://juejin.cn/post/7502263728433692709">掌握未来科技的关键...</a></li>
<li><a href="https://www.sindlhauser.de/en/">Sindlhauser Materials GmbH in Kempten (Allgäu)</a></li>

</ul>
</details>

**Tags**: `#semiconductors`, `#EU-China relations`, `#sanctions`, `#supply-chain`, `#ASML`

---