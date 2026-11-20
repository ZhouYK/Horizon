---
layout: default
title: "Horizon Summary: 2026-11-20 (EN)"
date: 2026-11-20 23:04:23 +0000
lang: en
report: default
---

> From 184 items, 9 important content pieces were selected

---

1. [PHP silently disables TLS when &\#x27;https&\#x27; is written in mixed case](#item-1) ⭐️ 8.0/10
2. [Meta&\#x27;s AI agent Muse mixes up conversations, exposing users&\#x27; private data](#item-2) ⭐️ 8.0/10
3. [Linux KVM Flaw CVE-2026-99312 Lets Guests Read AMD Host Memory](#item-3) ⭐️ 8.0/10
4. [Gemini Starts Operating Macs for Users, With Background Runs and Instant Pause](#item-4) ⭐️ 7.0/10
5. [UK tribunal rules for Apple, orders Home Office to disclose its secret backdoor notice](#item-5) ⭐️ 7.0/10
6. [TikTok rolls out global AI deepfake detection and likeness protection tools](#item-6) ⭐️ 7.0/10
7. [OpenAI adds background mode for long-running API jobs with token discounts](#item-7) ⭐️ 7.0/10
8. [US chip export curbs push India to expand its AI compute capacity](#item-8) ⭐️ 6.0/10
9. [Apple Reportedly Building Its Own Autonomous AI Agent for Late 2027](#item-9) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [PHP silently disables TLS when &\#x27;https&\#x27; is written in mixed case](https://x.com/ljachowicz/status/2123477025268924514) ⭐️ 8.0/10

PHP&\#x27;s built-in HTTP and FTP stream wrappers match URL schemes case-insensitively but only enable TLS when the fifth character of the scheme is a lowercase &\#x27;s&\#x27;, so URLs such as HTTPS://, httpS:// or FTPS:// are sent over unencrypted HTTP/FTP. The 20-year-old flaw is tracked as CVE-2026-128064 \(GHSA-f6gg-rchx-xw8j\) with a CVSS 4.0 score of 8.2 and has been fixed in PHP 8.2.36, 8.3.37, 8.4.28, 8.5.13 and 8.6.0. Any PHP application that passes a mixed-case HTTPS or FTPS URL to file\_get\_contents\(\), fopen\(\) or similar stream functions — or that follows an attacker-supplied redirect to such a URL — will leak credentials, Basic auth headers, cookies, POST bodies and FTP logins in plaintext while believing the connection is encrypted. Because PHP 8.1 and earlier are end-of-life and will never receive a patch, a large installed base of legacy deployments remains silently exposed. The fix makes the wrappers compare the entire scheme case-insensitively when deciding whether TLS is required; until upgrading, the practical mitigation is to normalize every URL scheme to lowercase before handing it to a stream function. Note that the CVSS 4.0 base score of 8.2 reflects confidentiality impact rather than remote code execution, and exploitation requires only passive observation of the affected connection.

telegram · zaihuapd · Nov 20, 03:04

**Background**: PHP&\#x27;s stream wrappers are the mechanism behind functions like file\_get\_contents\(\), fopen\(\) and copy\(\) when they are given a URL instead of a local path; the built-in http, https, ftp and ftps wrappers translate those URLs into network requests. Internally the scheme was parsed loosely \(case-insensitively\) to pick the wrapper, but the TLS decision was made by a separate positional check for a lowercase &\#x27;s&\#x27;, and the two code paths disagreed. This mismatch has existed since the wrappers were introduced roughly two decades ago and went unnoticed because nearly all real-world URLs use all-lowercase schemes.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/php/php-src/security/advisories/GHSA-f6gg-rchx-xw8j">Mixed-case HTTPS and FTPS URLs can expose data in plaintext</a></li>
<li><a href="https://securityonline.info/cve-watchtower/cve-2026-128064/">CVE-2026-128064: PHP Group PHP Cleartext Transmission of ...</a></li>
<li><a href="https://stackoverflow.com/questions/2305954/how-to-enable-https-stream-wrappers">php - How to enable HTTPS stream wrappers - Stack Overflow Usage example</a></li>

</ul>
</details>

**Tags**: `#security`, `#php`, `#TLS`, `#CVE`, `#vulnerability`

---

<a id="item-2"></a>
## [Meta&\#x27;s AI agent Muse mixes up conversations, exposing users&\#x27; private data](https://techcrunch.com/2026/11/19/metas-ai-agent-muse-is-mixing-up-conversations-and-exposing-private-data-report-says/) ⭐️ 8.0/10

According to Reuters, which cited internal Meta posts, employees report that Meta&\#x27;s personal AI agent Muse is mixing conversation content between different accounts and surfacing other people&\#x27;s private information without authorization. One employee said Muse inserted a weather chat message reading &quot;by the way, Capital One balance $2,722.58, Charles Schwab balance $5,899.57,&quot; while another said it prompted her to reply to her sister&\#x27;s Signal message even though she never granted it access to other apps. The incident is a concrete, high-profile example of the cross-session and cross-account leakage risks that come with agentic AI systems, which by design hold broad permissions over a user&\#x27;s messages, accounts, and apps. For Meta, whose Muse is positioned as an always-on personal agent spanning finance, health, and shopping, such failures could erode user trust and invite regulatory scrutiny over AI data isolation. The reported leaks include never-sent parenting requests, career advice the user never asked for, orders they never placed, and bank balances belonging to other people — suggesting failures at the session/routing layer rather than simple model hallucination. The account so far rests on internal employee posts relayed by Reuters and TechCrunch rather than an official Meta disclosure, and Meta has not publicly detailed the scope or root cause.

telegram · zaihuapd · Nov 20, 05:10

**Background**: Meta announced Muse on September 8, 2026, describing it as a personal AI agent that carries out long-running tasks on a user&\#x27;s behalf rather than answering single queries like a chatbot. Because such agents must stay logged in across services such as email, banking, and messaging, they depend on strict per-user data isolation; a &quot;cross-session leak&quot; occurs when one user&\#x27;s session data bleeds into another&\#x27;s. Researchers have documented similar cross-account leakage patterns in other agent products, and defenses such as GPU-level information flow tracking are still largely in the research stage.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Muse_%28AI_agent%29">Muse (AI agent) - Wikipedia</a></li>
<li><a href="https://www.giskard.ai/knowledge/cross-session-leak-when-your-ai-assistant-becomes-a-data-breach">Cross Session Leak: LLM security vulnerability &amp; detection guide</a></li>
<li><a href="https://www.forcepoint.com/blog/insights/ai-data-leakage">AI Data Leakage: How It Happens and How to Stop It - Forcepoint</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#privacy`, `#security incident`, `#Meta`, `#LLM data leakage`

---

<a id="item-3"></a>
## [Linux KVM Flaw CVE-2026-99312 Lets Guests Read AMD Host Memory](https://thehackernews.com/2026/11/new-linux-kvm-flaw-cve-2026-99312-lets.html) ⭐️ 8.0/10

A new Linux kernel KVM vulnerability, tracked as CVE-2026-99312, affects only AMD hosts that have nested virtualization enabled; researchers demonstrated an escape in which a guest VM read roughly 127 GB of host memory on DigitalOcean. An upstream fix shipped on November 18 with stable kernel 7.3.5 and related releases, but Debian, Ubuntu and other major distribution kernels have not yet been patched. The bug breaks the core isolation guarantee of virtualization, and because it is exploitable from inside an ordinary guest, any tenant sharing an affected multi-tenant AMD cloud host could potentially read other customers&\#x27; data. Cloud providers and private-cloud operators running nested virtualization on AMD hardware therefore face a real data-confidentiality risk until they either patch or change configuration. Exploitation requires nested virtualization to be enabled on an AMD host, so hosts without that feature are not exposed; the demonstrated leak of ~127 GB shows the impact is large-scale memory disclosure rather than a narrow out-of-bounds read. The practical mitigation is to disable nested virtualization until distro kernels pick up the upstream 7.3.5 fix, which means operators must weigh that against legitimate workloads such as running hypervisors or container sandboxes inside VMs.

telegram · zaihuapd · Nov 20, 14:23

**Background**: KVM \(Kernel-based Virtual Machine\) is the open-source virtualization module built into the Linux kernel that turns the kernel into a hypervisor, and it underpins a large share of public and private cloud infrastructure. Nested virtualization is the ability to run a hypervisor inside a virtual machine, which is widely used for development, testing, CI pipelines and container sandboxing but greatly expands the attack surface of the host hypervisor. Because KVM is maintained upstream and then packaged by distributions, a fix landing in a stable kernel release does not immediately reach production systems running Debian or Ubuntu kernels.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Kernel-based_Virtual_Machine">Kernel-based Virtual Machine - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Nested_virtualization">Nested virtualization</a></li>
<li><a href="https://www.redhat.com/en/topics/virtualization/what-is-KVM">What is KVM ?</a></li>

</ul>
</details>

**Tags**: `#security`, `#KVM`, `#CVE`, `#Linux kernel`, `#virtualization`

---

<a id="item-4"></a>
## [Gemini Starts Operating Macs for Users, With Background Runs and Instant Pause](https://www.bloomberg.com/news/articles/2026-11-19/google-s-gemini-can-now-control-mac-devices-on-users-behalf) ⭐️ 7.0/10

Google Gemini added a &quot;computer operation&quot; capability on Mac that can click, type, navigate menus and fill out forms on the user&\#x27;s behalf to complete tasks. It is rolling out to US users of the Gemini Mac app who subscribe to Google AI Plus, Pro or Ultra. This moves Gemini from a chat assistant that only reads the screen to an agent that actually takes actions inside desktop apps, putting Google in direct competition with other computer-use agent efforts and with existing desktop automation tools. If it works reliably, it changes how knowledge workers hand off repetitive multi-step tasks — and raises new questions about permission, privacy and auditability of AI-driven actions on a personal machine. Gemini runs in a separate background window so users can keep using their main screen and cursor while it works, and users can restrict which apps it may access, watch its actions in real time, pause it at any moment, and approve key actions before they execute. The rollout is limited to the US and to the paid Google AI Plus, Pro and Ultra tiers, so free-tier users and other regions are not yet covered.

telegram · zaihuapd · Nov 20, 02:51

**Background**: So-called &quot;computer use&quot; agents work by taking screenshots of the screen, interpreting the interface, and then emitting synthetic mouse clicks and keystrokes to operate applications the way a person would, rather than through app-specific APIs. Earlier reviews of Gemini on Mac noted that its computer-use ability was largely observational — it could see the screen but not act on it — so this release is the step from perception to action. Google AI Plus, Pro and Ultra are Google&\#x27;s paid subscription tiers for Gemini, sitting above the free tier with higher usage quotas and access to more advanced features.

<details><summary>References</summary>
<ul>
<li><a href="https://geminidesktop.app/zh/blog/gemini-for-mac-review-100-features-100-days">Gemini for Mac 上手评测：Google 100... | GeminiDesktop 博客</a></li>
<li><a href="https://bigolab.com/guides/2215-gemini-plans-free-plus-pro-ultra">Gemini 会员有什么区别：免费版、Google AI Plus、Pro、Ultra 功能与...</a></li>

</ul>
</details>

**Tags**: `#Gemini`, `#AI agents`, `#Google`, `#desktop automation`, `#product launch`

---

<a id="item-5"></a>
## [UK tribunal rules for Apple, orders Home Office to disclose its secret backdoor notice](https://appleinsider.com/articles/26/11/19/uk-cant-hide-that-it-tried-ordering-apple-to-allow-access-to-user-data) ⭐️ 7.0/10

The UK&\#x27;s Investigatory Powers Tribunal ruled in Apple&\#x27;s favor, barring the Home Office from keeping secret a Technical Capability Notice \(TCN\) that demanded access to encrypted iPhone data, and said most of the case will now be heard in public. The Home Office subsequently confirmed it had issued the TCN, insisting it was only trying to bring criminals to justice, while the tribunal dismissed its national-security justification for secrecy as &quot;unrealistic.&quot; This is one of the first times a UK technical capability order against a major technology company has been forced into open litigation, weakening the near-total secrecy that has historically shielded such demands. The outcome could shape how far the UK and other governments can compel companies to weaken end-to-end encryption, affecting every iPhone user in the UK and setting a precedent other jurisdictions may follow. Technical Capability Notices are issued under section 253 of the Investigatory Powers Act 2016 and normally cannot even be acknowledged publicly, so the tribunal&\#x27;s rejection of the secrecy claim is the pivotal point of the ruling. The tribunal itself is a first-instance body that sits within the Home Office but operates independently and is largely inquisitorial, and the published judgment is expected to reveal only part of the underlying technical demands.

telegram · zaihuapd · Nov 20, 04:13

**Background**: A Technical Capability Notice is a UK statutory order under the Investigatory Powers Act 2016 that compels a telecommunications or postal operator to build, maintain or deploy technical capabilities so it can comply with future lawful interception or communications-data warrants — effectively a demand to engineer assistance in advance. Such notices are issued by the Secretary of State and are wrapped in secrecy, which is why the fight here was as much about whether the demand could be disclosed as about what it required. The dispute echoes the 2015–2016 Apple–FBI standoff over the San Bernardino iPhone, and follows Apple&\#x27;s earlier legal challenges after the UK pressed for access to encrypted iCloud backups. The Investigatory Powers Tribunal is the specialist UK court that hears complaints about surveillance by public bodies and intelligence services.

<details><summary>References</summary>
<ul>
<li><a href="https://www.legislation.gov.uk/ukpga/2016/25/section/253">Investigatory Powers Act 2016 - Legislation.gov.uk</a></li>
<li><a href="https://www.gov.uk/government/publications/notices-regime-code-of-practice/notices-regime-code-of-practice-accessible">Notices regime code of practice (accessible) - GOV.UK</a></li>
<li><a href="https://en.wikipedia.org/wiki/Investigatory_Powers_Tribunal">Investigatory Powers Tribunal</a></li>

</ul>
</details>

**Tags**: `#encryption`, `#privacy`, `#apple`, `#surveillance`, `#uk-policy`

---

<a id="item-6"></a>
## [TikTok rolls out global AI deepfake detection and likeness protection tools](https://www.straitstimes.com/world/tiktok-launches-tool-to-help-public-figures-detect-deepfakes-globally) ⭐️ 7.0/10

TikTok has begun a global rollout of its Likeness Detection tool, which alerts third-party-verified public figures and top creators when AI-generated content using their face or likeness appears on the platform, letting them review and report it. Launched alongside it is a free, no-login transparency checker that lets anyone upload an image or video to see whether it was produced by TikTok&\#x27;s own AI features. This is one of the first platform-wide deployments of likeness-matching protection aimed at non-consensual AI impersonation, shifting some of the detection burden from individuals to the platform itself. It also lands as the EU AI Act&\#x27;s transparency and labelling obligations for AI-generated content take effect, making such tooling increasingly a compliance requirement rather than a voluntary nicety for large platforms. Likeness Detection is opt-in and limited to accounts whose identity has been verified by a third party, so ordinary users cannot yet use it, and the public checker only identifies content made by TikTok&\#x27;s own AI tools rather than AI-generated media from other sources. Detection systems of this kind generally struggle with very high-quality or novel manipulation techniques, so coverage is likely imperfect.

telegram · zaihuapd · Nov 20, 08:14

**Background**: Deepfakes are images, video, or audio created or altered with AI, and recent生成 models have made convincing impersonations of real people cheap and fast to produce. TikTok&\#x27;s tool works by matching uploaded content against the likeness of verified individuals, then surfacing potential matches for review rather than automatically removing them. The EU AI Act, in force since 2024, requires providers and deployers of certain AI systems to label AI-generated content, and the European Commission has been drafting a code of practice to support that transparency obligation.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tiktok.com/support/faq_detail?id=7670780803776944661">TikTok Support</a></li>
<li><a href="https://www.affiversemedia.com/tiktok-ai-content-checks-likeness-detection/">TikTok Adds AI Content Checks and Likeness Detection</a></li>
<li><a href="https://en.wikipedia.org/wiki/Deepfake">Deepfake - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI deepfake detection`, `#content moderation`, `#TikTok`, `#EU AI regulation`, `#platform policy`

---

<a id="item-7"></a>
## [OpenAI adds background mode for long-running API jobs with token discounts](https://developers.openai.com/api/docs/guides/background) ⭐️ 7.0/10

OpenAI introduced a background mode for its API that runs long requests asynchronously, letting developers set background: true and choose a 2-hour or 8-hour completion window in background\_options.completion\_window. Those windows cut token rates by 30% and 40% respectively versus standard pricing, while the default soonest option gets no discount. This gives production LLM workflows a supported way to avoid synchronous timeouts on long jobs and to lower costs for latency-tolerant workloads, affecting developers building batch, agentic, or large-generation pipelines. It also shows OpenAI pricing by latency tolerance rather than only by model. The discount is in public beta on GPT-6.2 Astra, GPT-6.2 Sol, GPT-6.1 Terra, and GPT-6 Luna, and background mode temporarily stores response data even when store is false or zero data retention is enabled. That retention caveat matters for teams with strict data-handling requirements.

telegram · zaihuapd · Nov 20, 11:15

**Background**: OpenAI&\#x27;s Responses API is normally synchronous: the client sends input and waits on the same connection for the final output. Background mode changes this by turning a request into an asynchronous job that the client can poll or be notified about via webhook. Zero Data Retention \(ZDR\) is an enterprise privacy option under which OpenAI does not retain prompts or outputs, so the new caveat is notable because background mode still temporarily stores response data.

<details><summary>References</summary>
<ul>
<li><a href="https://kissapi.ai/blog/openai-background-mode-api-guide-2026.html">OpenAI Background Mode API : Run Long Tasks Without Timeouts...</a></li>
<li><a href="https://www.marketingscoop.com/ai/openai-background-mode-how-async-responses-work-what-polling-looks-like-and-when-it-fits-better-than-sync-calls/">OpenAI Background Mode : How Async... - Marketing Scoop</a></li>
<li><a href="https://www.partitech.com/en/technical-blog-article/zero-data-retention-and-private-safety-processing-understanding-the-new-privacy-architecture-api">Zero Data Retention OpenAI : architecture and limits | PartITech</a></li>

</ul>
</details>

**Discussion**: Discussion in OpenAI&\#x27;s developer community frames the feature as a way to trade latency for cost, with one example being to submit meeting notes before logging off with an 8h window and receive a morning brief. Third-party walkthroughs stress that the window is not a latency or ordering guarantee, so teams should build a reliable queue around jobs that wait, fail or finish out of order.

**Tags**: `#OpenAI API`, `#async processing`, `#LLM infrastructure`, `#pricing`, `#data retention`

---

<a id="item-8"></a>
## [US chip export curbs push India to expand its AI compute capacity](https://www.bloomberg.com/news/articles/2026-11-20/nvidia-scandal-fallout-india-ai-yotta-ambani-adani-am-intelligence-e2e-networks) ⭐️ 6.0/10

As the US tightens advanced chip exports to Malaysia, Thailand, and Singapore, India&\#x27;s AI industry is positioning itself to absorb the diverted demand. Yotta Data Services said it plans to add roughly 100,000 GPUs over the next year, an increase of about 10% on India&\#x27;s existing national compute base. The shift shows how export controls are redrawing the global map of AI infrastructure, with India trying to convert geopolitical friction into domestic capacity. If the commitments hold, India could move from a compute-constrained market to a meaningful alternative hub for AI workloads, affecting cloud pricing and where multinationals train and serve models. India currently hosts 153 data centers, ranking 14th globally, and its buildout has long been held back by infrastructure shortages and limited capital. The headline commitments are large — Reliance has pledged up to $110 billion and Adani $100 billion for AI infrastructure — but Yotta&\#x27;s own GPU addition, while sizable by Indian standards, is only about a tenth of the existing national base.

telegram · zaihuapd · Nov 20, 07:31

**Background**: Advanced AI accelerators such as Nvidia GPUs have been subject to US export licensing, and Washington has been extending scrutiny to transshipment hubs in Southeast Asia. Yotta Data Services is a data center subsidiary of the Hiranandani Group, known for its large Tier IV facility in Navi Mumbai, and is one of the companies building out GPU cloud capacity in India. Data centers are the physical layer for AI — they house the racks of servers and accelerators that models are trained and served on — so the number of GPUs a country can power and cool effectively caps its AI ambitions.

<details><summary>References</summary>
<ul>
<li><a href="https://yotta.com/">India ’s Trusted Sovereign Cloud &amp; AI Infrastructure – Yotta</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hiranandani_Group">Hiranandani Group - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI infrastructure`, `#chip export controls`, `#India AI`, `#data centers`, `#geopolitics`

---

<a id="item-9"></a>
## [Apple Reportedly Building Its Own Autonomous AI Agent for Late 2027](https://www.bloomberg.com/news/articles/2026-11-19/apple-is-working-on-ai-agent-for-device-control-apps-browsing-and-coding) ⭐️ 6.0/10

Bloomberg discovered from Apple&\#x27;s newly posted job listings this week that the company is hiring a senior engineering manager to lead development of a &quot;proactive AI agent&quot; that can write code, browse the web, and operate apps on the user&\#x27;s behalf, with an earliest launch around late 2027. In parallel, Apple&\#x27;s macOS 27.3 adds a warning screen that increases the number of steps a third-party agent must complete to obtain Mac control permissions from 4 to 14. The move would put Apple directly against OpenAI, Anthropic and Meta, whose Muse agent already runs on a dedicated secure VM and acts across everyday apps, making agentic AI the next major platform battleground after chatbots. At the same time, tightening third-party permission flows on macOS could tilt the field toward Apple&\#x27;s own agent while raising competitive-fairness questions. The project is still in an early stage and the late-2027 date is only the earliest possible launch window, with the agent reportedly positioned to go beyond Siri and Apple Intelligence by operating a computer much like a skilled human. That kind of device control depends on macOS&\#x27;s Accessibility and TCC permission framework, which is exactly the gate Apple is now making harder for outside agents to pass.

telegram · zaihuapd · Nov 20, 08:59

**Background**: A proactive AI agent is an autonomous software system that continuously observes context such as conversations, calendars and files and then takes actions or surfaces results without waiting for an explicit prompt, rather than simply answering questions. Meta&\#x27;s Muse, powered by the Muse Spark model and running in a dedicated secure VM, is an early consumer example that handles email, calendars and bookings. On macOS, control of other apps is gated by Accessibility permissions under the TCC \(Transparency, Consent and Control\) privacy framework, which means the number of consent steps directly determines how practical an outside agent is. Apple has so far shipped Apple Intelligence and a revamped Siri, but neither is a general-purpose agent that can drive arbitrary applications.

<details><summary>References</summary>
<ul>
<li><a href="https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/">Introducing Muse : The World’s First Personal AI Agent Built for...</a></li>
<li><a href="https://support.apple.com/guide/mac-help/allow-accessibility-apps-to-access-your-mac-mh43185/mac">Allow accessibility apps to access your Mac - Apple Support</a></li>
<li><a href="https://context-limit.ghost.io/what-is-a-proactive-ai-agent-2026/">What Is a Proactive AI Agent ? 2026 Definition &amp; Guide</a></li>

</ul>
</details>

**Tags**: `#Apple`, `#AI agents`, `#macOS`, `#Bloomberg`, `#industry news`

---