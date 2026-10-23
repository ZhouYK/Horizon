---
layout: default
title: "Horizon Summary: 2026-10-23 (EN)"
date: 2026-10-23 23:03:20 +0000
lang: en
report: default
---

> From 163 items, 5 important content pieces were selected

---

1. [Kimi Releases K3.1 Pro: 3-Trillion-Parameter Model With 1M-Token Context](#item-1) ⭐️ 8.0/10
2. [ByteDance Releases Seedance 2.5 4K AI Video Model for the Big Screen](#item-2) ⭐️ 7.0/10
3. [China&\#x27;s State Council Issues Guidance to Cushion AI-Driven Job Displacement](#item-3) ⭐️ 7.0/10
4. [PHP Foundation Urges Disabling Upload Progress Over Unpatched RCE \(CVE-2026-115560\)](#item-4) ⭐️ 7.0/10
5. [Sweden&\#x27;s Government Offices Ban ChatGPT and Claude on Work Computers](#item-5) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Kimi Releases K3.1 Pro: 3-Trillion-Parameter Model With 1M-Token Context](https://www.kimi.ai/blog/kimi-k3-1-pro) ⭐️ 8.0/10

Kimi \(Moonshot AI\) launched K3.1 Pro, the first model in its K3.1 family and its strongest 3-trillion-parameter model, featuring a 1-million-token context window and now available through Kimi, Work, Code and the API. A parallel &quot;Highspeed&quot; variant runs 2–3x faster than the standard version, and the company says full model weights will be published by November 4, 2026. This is the first time a soon-to-be open-weight model has scored this close to the frontier: Artificial Analysis rated K3.1 Pro at 55, ahead of GPT-6 Astra, Gemini 4 Argon and Claude Fable 5.1 \(all 53\) and behind only Claude Opus 5.5 \(58\). At $2 per million input tokens and $10 per million output tokens — about half the price of Opus 5.5 — it puts frontier-adjacent capability within reach of teams that want to self-host or cut API costs. The weights are not downloadable yet — the model is API-only until the promised November 2026 release — and most benchmark figures are self-reported, including Terminal-Bench 4.0 at 65.7% \(vs. GPT-6 Astra 58.2% and Claude Opus 5.5 66.4%\), BenchCAD tool-use at 92.7%, and an internal hallucination rate drop from 23.4% to 8.3%, which the post explicitly says does not reflect everyday error rates. The Highspeed version costs twice as much except on cached input tokens, which are priced the same.

telegram · zaihuapd · Oct 23, 17:14

**Background**: An &quot;open-weight&quot; model is one whose trained parameters are publicly released so anyone can download and run it on their own hardware, as opposed to closed models accessible only through an API — it differs from open source, which would also include training code and data. Terminal-Bench 4.0 is a 66-task benchmark of complex terminal work spanning software, ML, science, operations and security, while BenchCAD measures programmatic CAD generation over roughly 17,900 execution-verified CadQuery programs. Artificial Analysis maintains an independent composite index that aggregates such evaluations into a single score, which is why its 55 rating is often cited as a neutral counterpoint to vendor-reported numbers.

<details><summary>References</summary>
<ul>
<li><a href="https://artificialanalysis.ai/evaluations/terminalbench-4-0">Terminal-Bench 4.0 Benchmark - Artificial Analysis</a></li>
<li><a href="https://benchcad.com/">BenchCAD — a benchmark for programmatic CAD</a></li>
<li><a href="https://nhimg.org/glossary/open-weight-model/">What Is Open - Weight Model ? Definition &amp; Examples</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#Kimi`, `#open-weight models`, `#coding benchmarks`, `#AI release`

---

<a id="item-2"></a>
## [ByteDance Releases Seedance 2.5 4K AI Video Model for the Big Screen](https://mp.weixin.qq.com/s/yUa8oh-IWfl5lDQzGSKWeg) ⭐️ 7.0/10

ByteDance&\#x27;s cloud arm Volcano Engine has officially released Seedance 2.5 4K, the most capable version of its Seedance video generation model line so far. The new version was specifically trained to better learn facial expressions, subtle movements and fine image detail, and it introduces a Draft mode that lets users validate storyboards with a fast 480p preview before rendering the final 4K footage. The jump to 4K with 10-bit color pushes generative video from social-media clips toward professional film and television workflows, where color grading headroom and believable facial performance are prerequisites. If access broadens beyond the current enterprise pilot, it could reshape how studios and advertising teams produce storyboards and pre-visualization. The model supports 10-bit color depth for smoother gradients and richer tonal layering, which is what makes the output viable on a cinema screen. In drama-style tests, the 4K version reportedly captured more of a performer&\#x27;s micro-reactions, giving the acting more nuance, but access is currently limited to a small set of enterprise clients with no public timeline for wider availability.

telegram · zaihuapd · Oct 23, 08:27

**Background**: Seedance is ByteDance&\#x27;s family of AI video generation models, delivered to enterprise customers through Volcano Engine, the company&\#x27;s cloud platform that packages ByteDance&\#x27;s internal technical capabilities as external services. Bit depth refers to how many bits represent color per channel per pixel: 8-bit is the consumer norm, while 10-bit offers far more color steps per channel, which reduces banding in gradients and leaves room for color correction — the reason 10-bit is effectively required for HDR and professional grading. A draft-then-final workflow mirrors how animation and VFX studios already iterate on low-resolution previews before committing compute to final renders.

<details><summary>References</summary>
<ul>
<li><a href="https://seed.bytedance.com/en/seedance2_5">Seedance 2.5 - seed.bytedance.com</a></li>
<li><a href="https://filmdaft.com/what-is-bit-depth-definition-8-bit-vs-10-bit-vs-12-bit/">Bit Depth | Definition and 8-Bit vs 10-Bit vs 12-Bit Video ...</a></li>
<li><a href="https://www.volcengine.com/lang/en">Volcano Engine</a></li>

</ul>
</details>

**Tags**: `#AI video generation`, `#ByteDance`, `#Seedance`, `#generative AI`, `#4K video`

---

<a id="item-3"></a>
## [China&\#x27;s State Council Issues Guidance to Cushion AI-Driven Job Displacement](https://mp.weixin.qq.com/s/St8URoMYcV-voM7kLAK3Bw) ⭐️ 7.0/10

The General Office of China&\#x27;s State Council issued a guiding opinion on building an &quot;employment-friendly development model&quot; adapted to AI, explicitly calling for steps to mitigate AI&\#x27;s job-substitution effects. It directs that AI be deployed first in roles facing labor shortages or high environmental risk, that its rollout in labor-intensive industries be advanced prudently in scope, intensity and pace, and that firms be encouraged to trial unemployment buffer periods with advance notice and retraining/redeployment support for affected workers. This is one of the clearest signals yet that Beijing intends to shape the pace of AI adoption around employment stability rather than leaving it purely to market forces, which could affect how quickly automation is rolled out in manufacturing, logistics, customer service and other labor-intensive sectors. For companies deploying AI in China, it introduces a policy expectation of workforce consultation and transition planning, potentially adding compliance considerations to automation business cases. The document is a State Council guiding opinion \(意见\) rather than a binding regulation, and the summary disclosed no hard quotas, timelines or penalties — the &quot;unemployment buffer period&quot; is framed as something enterprises are encouraged to explore rather than a mandated requirement. The emphasis on &quot;scope, intensity and pace&quot; in labor-intensive sectors gives regulators room to slow specific deployments case by case.

telegram · zaihuapd · Oct 23, 12:54

**Background**: China&\#x27;s State Council General Office is the administrative hub of the central government, and its &quot;guiding opinions&quot; set policy direction that ministries and local governments then translate into implementing rules. Chinese policymakers have simultaneously pushed for rapid AI diffusion across the economy and for employment stability, and labor-intensive sectors such as manufacturing assembly, logistics and customer service are widely seen as the most exposed to automation. The new document tries to reconcile those two goals by steering AI first toward jobs people cannot easily fill, such as dangerous or physically demanding work.

**Tags**: `#AI policy`, `#employment`, `#China regulation`, `#labor market`, `#AI adoption`

---

<a id="item-4"></a>
## [PHP Foundation Urges Disabling Upload Progress Over Unpatched RCE \(CVE-2026-115560\)](https://x.com/ThePHPF/status/2113580383875019242) ⭐️ 7.0/10

The PHP Foundation is advising users to set session.upload\_progress.enabled=0 before the next PHP release to mitigate an unpatched remote code execution vulnerability tracked as CVE-2026-115560. The Foundation had previously issued similar guidance to keep the feature disabled because of CVE-2026-109619. PHP underpins a huge share of the web, so an RCE-class flaw in a core session feature is a serious concern for anyone running PHP applications, and the advice arrives with no patch available yet, leaving configuration changes as the only mitigation. Administrators of PHP-based platforms and container images should audit their INI settings now rather than wait for the next release. Only applications that switch the session.serialize\_handler to the &\#x27;php&\#x27; handler at runtime are believed to be affected, which PHP describes as an unusual, non-default configuration; for example, container images that set igbinary as the session serializer could reach the vulnerable path if code changes the handler on the fly. The setting session.upload\_progress.enabled is a per-directory INI directive that has existed since PHP 5.4 and defaults to enabled.

telegram · zaihuapd · Oct 23, 13:46

**Background**: PHP&\#x27;s session.upload\_progress feature, added in PHP 5.4, lets an application track the progress of individual file uploads by writing status data into the $\_SESSION superglobal while an upload is in flight, which is why it depends on the session subsystem rather than only on the upload code. The session.serialize\_handler directive controls how session data is converted to and from a storable string; &\#x27;php&\#x27; is the built-in serializer, while extensions such as igbinary provide faster alternatives, and mixing handlers across the lifecycle of a session can produce inconsistent or attacker-influenced data. An RCE in this area means a crafted request could potentially execute arbitrary code on the server, the most severe class of web vulnerability. This advisory follows a string of recent PHP security notices, including the widely discussed &\#x27;PHP 2Shell&\#x27; flaws that were patched shortly after administrators were told to prepare for updates.

<details><summary>References</summary>
<ul>
<li><a href="https://thehackernews.com/2026/10/urgent-php-warns-of-another-unpatched.html">PHP Warns of Another Unpatched RCE Risk Two Days After...</a></li>
<li><a href="https://www.bleepingcomputer.com/news/security/php-shares-mitigation-for-new-and-unpatched-rce-vulnerability/">PHP shares mitigation for new RCE vulnerability with no patch</a></li>
<li><a href="https://www.php.net/manual/en/session.upload-progress.php">PHP : Session Upload Progress - Manual</a></li>

</ul>
</details>

**Tags**: `#PHP`, `#security`, `#CVE`, `#RCE`, `#vulnerability-disclosure`

---

<a id="item-5"></a>
## [Sweden&\#x27;s Government Offices Ban ChatGPT and Claude on Work Computers](https://www.sverigesradio.se/artikel/chat-gpt-och-claude-forbjuder-regeringskansliet) ⭐️ 6.0/10

Sweden&\#x27;s Government Offices \(Regeringskansliet\) will ban ChatGPT and Claude on employees&\#x27; work computers starting next Monday, requiring staff to use approved AI tools such as Microsoft Copilot instead. The agency had previously restricted DeepSeek, and its digitalisation chief said on the internal website that using AI services without a signed agreement could jeopardise information security. This is one of the clearest examples yet of a national government treating consumer AI chatbots as an unsanctioned data-processing risk and steering staff toward contractually vetted tools instead. It adds to a broader public-sector trend in Sweden—the Tax Agency and SiS have already imposed similar bans—and signals that procurement and data-processing agreements, rather than model quality, may decide which AI assistants public employees can use. The ban applies to work computers rather than a full organisational prohibition, and some employees will still be able to reach ChatGPT and Claude through an in-house developed platform. Enforcement follows the earlier DeepSeek restriction, while Kronofogden \(the Swedish Enforcement Authority\) is still assessing whether to adopt a similar policy.

telegram · zaihuapd · Oct 23, 14:11

**Background**: Regeringskansliet is the Swedish government&\#x27;s central administrative body, handling policy preparation and day-to-day operations for the cabinet, and it sets IT-security rules for its own staff. ChatGPT \(OpenAI\) and Claude \(Anthropic\) are general-purpose chatbots that transmit user prompts to external cloud servers unless deployed under a dedicated enterprise agreement, which is why public bodies often restrict them on security grounds. Microsoft Copilot, which is built on OpenAI&\#x27;s GPT models and sold through Microsoft&\#x27;s enterprise licensing, is typically already covered by existing government contracts and data-protection terms. Sweden is not alone in this: agencies across Europe have been weighing bans or formal approvals for generative AI tools used with official information.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_%28chatbot%29">Claude (chatbot)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Microsoft_Copilot_%28current%29">Microsoft Copilot (current)</a></li>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek_%28AI%29">DeepSeek (AI) - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI governance`, `#ChatGPT`, `#Claude`, `#data security`, `#public sector`

---