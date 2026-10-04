---
layout: default
title: "Horizon Summary: 2026-10-04 (EN)"
date: 2026-10-04 23:03:05 +0000
lang: en
report: default
---

> From 139 items, 3 important content pieces were selected

---

1. [Tianjin University Unveils 3-Gram Non-Invasive Brain-Computer Interface](#item-1) ⭐️ 6.0/10
2. [Data breaches hit peripheral systems at four South Korean banks](#item-2) ⭐️ 6.0/10
3. [Google Releases VeriHarness for Long-Horizon Task Verification](#item-3) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Tianjin University Unveils 3-Gram Non-Invasive Brain-Computer Interface](https://news.tju.edu.cn/info/1005/615029.htm) ⭐️ 6.0/10

Tianjin University&\#x27;s Haihe Laboratory of Brain-Computer Interaction and Human-Machine Integration announced &quot;Shengong·Xumi·Naolifang,&quot; a non-invasive brain-computer interface integrated system weighing just 3 grams and occupying less than 2 cubic centimeters. The university claims it is the smallest and lightest non-invasive BCI system in the world to date. If the claim holds up, it would mark a shift of non-invasive brain-computer interfaces away from bulky caps, helmets and headbands toward wearable form factors that can be worn discreetly all day. That could broaden BCI use beyond hospital labs into consumer, education and industrial safety applications, a market segment that invasive implants cannot easily reach. The device integrates EEG electrodes, circuitry, a battery and wireless transmission into a single tiny unit, and is designed to be hidden among hair strands while being worn. The announcement comes as a brief university press release, so key performance figures such as channel count, signal quality, battery life and validation data have not yet been disclosed.

telegram · zaihuapd · Oct 4, 03:24

**Background**: Brain-computer interfaces are broadly split into invasive and non-invasive categories: invasive systems use electrodes implanted in the brain and can read neural signals at high fidelity, but require surgery and carry medical risk. Non-invasive systems read electrical activity from the scalp through EEG electrodes, which is safer but historically requires bulky headgear and produces noisier signals. Tianjin University&\#x27;s Haihe Laboratory has been working on this trade-off, and its new system is aimed at shrinking the non-invasive hardware to a nearly invisible size.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ithome.com/1/009/617.htm">ithome.com/1/009/617.htm</a></li>
<li><a href="https://tech.ifeng.com/c/8wwYf4tJvTw">全球最小的无创 脑 机一体化系统“ 神 工 · 须 弥 · 脑 立 方 ”在天津发布_凤凰网</a></li>
<li><a href="https://en.tju.edu.cn/info/1010/7179.htm">TJU Researchers Make New World Record in Non - invasive ...</a></li>

</ul>
</details>

**Tags**: `#Brain-Computer Interface`, `#Wearable Technology`, `#Neurotechnology`, `#Hardware Miniaturization`, `#Tianjin University`

---

<a id="item-2"></a>
## [Data breaches hit peripheral systems at four South Korean banks](https://www.thelec.net/news/articleView.html?idxno=14402) ⭐️ 6.0/10

Four South Korean banks — Shinhan, Kookmin, Hana and BNK Busan Bank — reported a string of data breaches affecting employee or external partner systems, with Shinhan&\#x27;s loan agency query system compromised for three days and exposing 25,729 customers, while Kookmin and Hana reported 119 and 89 affected customers respectively and Busan Bank leaked the personal data of 11 outsourced developers. In response, South Korean financial regulators said they will expand IT security inspections to employee business systems and external partners, and are requiring banks to hunt for vulnerabilities in externally exposed systems and strengthen authentication and access controls. The incidents show that attackers are shifting away from heavily defended core banking systems toward weaker peripheral and third-party systems, turning vendor and employee-facing platforms into a soft entry point for the whole financial sector. Because the regulator is now widening inspections beyond core infrastructure, Korean banks and their IT outsourcing partners will likely face tighter audits, mandatory access-control upgrades and potential penalties. The affected Shinhan system was a loan agency query system, a peripheral function rather than a core transaction ledger, and it remained compromised for three days — a notably long dwell time. Reported victim counts vary widely from 25,729 customers at Shinhan down to just 11 outsourced developers at Busan Bank, and the regulator is also asking institutions to share attacker IPs and attack techniques with one another.

telegram · zaihuapd · Oct 4, 09:02

**Background**: In banking IT, &quot;core systems&quot; handle deposits, payments and the general ledger, while &quot;peripheral systems&quot; cover everything around them — employee business tools, query and referral services, and systems operated by outside vendors or contractors. Because these peripheral systems are often less strictly segmented, slower to patch and reachable from outside the network, they are attractive to attackers looking for any foothold into a bank. Authentication and access controls are the mechanisms that verify who a user is and limit what data or functions they can reach, so weaknesses there often determine how far a breach spreads.

<details><summary>References</summary>
<ul>
<li><a href="https://ng-branch-technology.com/">Multi-Vendor TCR &amp; Peripheral Device... | NG Branch Technology</a></li>
<li><a href="https://www.axxiome.com/news/2025/how-digital-banking-is-redefining-the-branch/">How Digital Banking Is Redefining the Branch</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#data-breach`, `#banking`, `#financial-regulation`, `#South Korea`

---

<a id="item-3"></a>
## [Google Releases VeriHarness for Long-Horizon Task Verification](https://arxiv.org/abs/2610.00972v1) ⭐️ 6.0/10

Google researchers released VeriHarness, a training-free, plug-and-play agentic verification harness that uses the same model that generated candidate results to verify them: it checks disputed claims against environment evidence, actively challenges consensus claims, and then selects, revises, or rebuilds the final output. The project reports the highest selection scores on 5 long-horizon task benchmarks across 2 models, with evidence-driven revision improving Gemini 3.5 Flash by 6.2 points and Claude Opus 4.8 by 6.4 points on average over single-pass generation, alongside the release of roughly 26,000 rollouts. Long-horizon agentic tasks are a major frontier for LLM agents, yet they remain hard to complete reliably in a single pass, making verification a key bottleneck. A harness that adds measurable gains without any fine-tuning and works across different benchmarks and models could become a general-purpose wrapper for making existing agents more reliable. VeriHarness is described as the first agentic verification harness for long-horizon tasks and is explicitly training-free and plug-and-play across benchmarks and models, so it requires no additional model training. The released artifact includes a paper, a website, a dataset of around 26k rollouts, and a Google Research GitHub repository, and it separates the roles of selection \(choosing among candidates\) and revision \(repairing a chosen output\).

telegram · zaihuapd · Oct 4, 13:32

**Background**: A long-horizon task is a task that requires an AI agent to make many decisions over an extended sequence of steps and cannot be reliably completed by a single prompt, a single retrieval, or one short exchange. Self-verification is a technique in which a large language model checks its own outputs, which prior research has shown can help models avoid incorrect chains of thought. A known limitation of this approach is bias, because the same model both generates and judges the answer, which is exactly the tension VeriHarness tries to manage by grounding verification in environment evidence.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2610.00972">VeriHarness : Scaling Agentic Verification for Long-Horizon Tasks</a></li>
<li><a href="https://github.com/google-research/veriharness">GitHub - google -research/ veriharness · GitHub</a></li>
<li><a href="https://promptmetheus.com/resources/llm-knowledge-base/long-horizon-task">Long - Horizon Task | LLM Knowledge Base</a></li>

</ul>
</details>

**Tags**: `#AI/ML`, `#LLM verification`, `#long-horizon tasks`, `#research`, `#Google`

---