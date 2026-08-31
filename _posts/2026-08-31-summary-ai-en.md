---
layout: default
title: "Horizon Summary: 2026-08-31 (EN)"
date: 2026-08-31 23:07:34 +0000
lang: en
report: ai
---

> From 302 items, 10 important content pieces were selected

---

1. [OpenAI Reportedly Completes Pre-Training of 10-Trillion-Parameter Model &\#x27;Bel&\#x27;](#item-1) ⭐️ 9.0/10
2. [ChatGPT Work Is Two Products: Cloud and Local Desktop App](#item-2) ⭐️ 8.0/10
3. [Anthropic Warns Claude Users of Info-Stealing Malware That Stole Session Tokens](#item-3) ⭐️ 8.0/10
4. [Sony Leads 35 Music Publishers in Suing Anthropic for Billions in Copyright Case](#item-4) ⭐️ 8.0/10
5. [OpenClaw 2.0 has been released with rebuilt infrastructure and multi-user cloud sessions.](#item-5) ⭐️ 8.0/10
6. [Huawei and Ruijin Hospital Launch RuiPath 2.0 Pathology AI in 90+ Hospitals](#item-6) ⭐️ 8.0/10
7. [FSB Chair warns frontier AI models pose financial stability risks](#item-7) ⭐️ 7.0/10
8. [American College of Physicians Issues Ethical Guidelines for AI in Medicine](#item-8) ⭐️ 7.0/10
9. [RAND Report on Tax Policy Options for the AI Age](#item-9) ⭐️ 7.0/10
10. [AWS Launches Agent Registry to Manage AI Agents, Tools, and Skills at Scale](#item-10) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [OpenAI Reportedly Completes Pre-Training of 10-Trillion-Parameter Model &\#x27;Bel&\#x27;](https://www.aibase.com/news/30718) ⭐️ 9.0/10

According to reports, OpenAI has completed pre-training on a new model codenamed &quot;Bel,&quot; which has over 10 trillion total parameters. It is the successor to the &quot;Doug&quot; pretrain and is expected to serve as a base for future models like Astra and GPT-6, potentially underpinning an AGI-threshold system after further reinforcement learning. If confirmed, Bel would mark a major leap in model scale and a significant step toward AGI, with reported advances in coding, reasoning, and long-horizon agent tasks. It signals OpenAI&\#x27;s continued push to stay ahead in the increasingly competitive AI race. The model reportedly has more than 10 trillion total parameters, comparable in scale to GPT-4.5, and is intended as a post-GPT-6 base model. Note that this information comes from unofficial reports and rumors, so details have not been confirmed by OpenAI.

aibase · AIbase · Aug 31, 15:01

**Background**: Parameter count is a common proxy for a model&\#x27;s capacity, though large models also require enormous compute and data for pre-training. Long-horizon agent tasks involve AI agents autonomously executing many interdependent actions to achieve open-ended objectives, which is an active area of research. OpenAI has previously built models like GPT-4 and GPT-5, and &quot;Bel&quot; is reportedly one in a series of internal pretrains leading toward GPT-6 and beyond.

<details><summary>References</summary>
<ul>
<li><a href="https://wccftech.com/openais-bel-has-over-10-trillion-parameters-and-it-might-just-be-the-worlds-first-agi-threshold-base-model/">OpenAI&#x27;s &#x27;Bel&#x27; Has Over 10 Trillion Parameters, And It Might Just Be The World&#x27;s First &quot;AGI-Threshold&quot; Base Model</a></li>
<li><a href="https://digitalphablet.com/ai/ai-competition-heats-up-openai-pre-trains-bel-model-with-10t-parameters/">AI Competition Heats Up: OpenAI Pre-Trains BEL Model with 10T+ Parameters</a></li>
<li><a href="https://x.com/wallstengine/status/2092328264060764586">Wall St Engine on X: &quot;Rumor: OpenAI has reportedly completed a new pretraining run codenamed “Bel,” the successor to “Doug,” with more than 10T total parameters. &quot;Bel&quot; is said to be intended as a post-GPT-6 base model and could potentially underpin an AGI-threshold system after further RL.&quot; / X</a></li>

</ul>
</details>

**Discussion**: Community reaction is a mixture of excitement and caution. Some see Bel as a potential &quot;AGI-threshold&quot; foundation model, while others note that the report is still a rumor and the actual performance depends on further reinforcement learning and evaluation. The X post from Wall St Engine frames it as a rumor, with many discussing the implications for the AI race.

**Tags**: `#OpenAI`, `#Large Language Models`, `#AGI`, `#Pre-training`, `#AI Research`

---

<a id="item-2"></a>
## [ChatGPT Work Is Two Products: Cloud and Local Desktop App](https://simonwillison.net/2026/Aug/30/understanding-chatgpt-work/) ⭐️ 8.0/10

Simon Willison&\#x27;s analysis clarifies that OpenAI&\#x27;s ChatGPT Work actually consists of two distinct products: a cloud-based version \(Work Cloud\) accessible via chatgpt.com and mobile apps, and a local desktop app \(Work Local\) renamed from the Codex app. He also details exclusive Work features such as GPT-5.6 Sol/Luna/Terra model selection, code execution with internet access, a headless Chrome browser, and a persistent shared filesystem. This analysis helps users navigate a confusing product launch, clarifying when to use Chat versus Work and what capabilities are unique to Work. It is especially valuable for developers and power users who rely on ChatGPT for complex, multi-step tasks. Work Cloud is also available from the ChatGPT desktop app via a &\#x27;Where should this chat run?&\#x27; dropdown. ChatGPT Work is currently limited to subscribers paying $20/month or more; free and $8/month Go users have no access. Work offers GPT-5.6 Sol, Luna, and Terra models with reasoning levels from Light to Ultra, while standard Chat offers a different model selection, with some options requiring $100/month.

rss · Simon Willison · Aug 30, 23:59

**Background**: OpenAI announced ChatGPT Work on July 9th and has been iterating rapidly since. The product name is confusing because the cloud version and the local desktop app share the same name but are fundamentally different. The desktop app was previously known as Codex, an OpenAI coding agent that can run locally on a computer, access files, and execute programs.

<details><summary>References</summary>
<ul>
<li><a href="https://intelligenttools.co/tools/openai-codex">OpenAI Codex - OpenAI coding agent for the terminal, IDE,..</a></li>
<li><a href="https://github.com/openai/codex">GitHub - openai / codex : Lightweight coding agent that runs in your...</a></li>

</ul>
</details>

**Tags**: `#ChatGPT`, `#OpenAI`, `#AI tools`, `#product analysis`, `#cloud computing`

---

<a id="item-3"></a>
## [Anthropic Warns Claude Users of Info-Stealing Malware That Stole Session Tokens](https://www.aibase.com/news/30730) ⭐️ 8.0/10

Anthropic has issued a security alert warning that some Claude users&\#x27; devices were infected with info-stealing malware, which compromised active session tokens. The attackers used the stolen sessions to access accounts and steal usage data, prompting Anthropic to urge affected users to change their passwords and credentials. This incident highlights that even AI platform users are vulnerable to credential and session token theft, a growing cybercrime trend. It underscores the importance of session-level security and proactive mitigation, affecting trust in AI services and user data safety. The malware is designed to steal sensitive information such as login credentials, session tokens, and cookies, potentially bypassing multi-factor authentication. Anthropic advised affected users to change passwords and credentials promptly, but did not disclose the number of affected accounts or full technical details.

aibase · AIbase · Aug 31, 18:01

**Background**: Info-stealing malware is a type of malicious software silently installed on devices to collect sensitive data like passwords, credit card details, and session cookies. Session token theft occurs when attackers steal an active session identifier \(such as an OAuth token or session cookie\), allowing them to take over a user&\#x27;s session without needing credentials. This attack method is particularly dangerous because it can bypass multi-factor authentication and remain undetected for long periods.

<details><summary>References</summary>
<ul>
<li><a href="https://www.kaseya.com/blog/what-is-token-theft/">What is token theft? - Kaseya</a></li>
<li><a href="https://www.obsidiansecurity.com/blog/session-hijacking-how-it-works-how-to-stop-it">Session Hijacking: How It Works &amp; How to Stop It</a></li>
<li><a href="https://www.spamtitan.com/blog/massive-threat-information-stealing-malware/">Researchers Confirm Massive Threat From Information Stealing ...</a></li>

</ul>
</details>

**Tags**: `#security`, `#Anthropic`, `#Claude`, `#malware`, `#session tokens`

---

<a id="item-4"></a>
## [Sony Leads 35 Music Publishers in Suing Anthropic for Billions in Copyright Case](https://www.aibase.com/news/30724) ⭐️ 8.0/10

Sony Music and Warner Chappell, along with 33 other music publishers, filed a lawsuit against AI company Anthropic and its co-founders Dario Amodei and Daniela Amodei in the U.S. District Court for the Northern District of California. The suit alleges that Anthropic used unauthorized BitTorrent downloads and web scraping to train its AI models on copyrighted music, seeking damages that could reach billions of dollars. This lawsuit could set a major legal precedent for how AI companies use copyrighted material in training datasets, potentially reshaping the AI industry&\#x27;s data practices. If successful, it would have a significant financial impact on leading AI firms like Anthropic and could embolden other content industries to file similar claims. Unusually, the lawsuit names Anthropic&\#x27;s co-founders as individual defendants, rather than just the company. The plaintiffs describe the alleged conduct as &\#x27;one of the most blatant IP thefts in history,&\#x27; and the case is being heard in the Northern District of California.

aibase · AIbase · Aug 31, 16:01

**Background**: Anthropic is an AI safety and research company founded in 2021 by former OpenAI members, including siblings Daniela Amodei and Dario Amodei, who serve as president and CEO respectively. The company develops AI systems such as the Claude chatbot. Web scraping is an automated technique for extracting data from websites, and it is commonly used to gather large datasets for AI training, which is at the center of this legal dispute.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Anthropic">Anthropic - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Web_scraping">Web scraping</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Copyright`, `#Anthropic`, `#Lawsuit`, `#Music Industry`

---

<a id="item-5"></a>
## [OpenClaw 2.0 has been released with rebuilt infrastructure and multi-user cloud sessions.](https://www.aibase.com/news/30720) ⭐️ 8.0/10

OpenClaw 2.0 was released on August 30, following a roughly seven-week rebuild that merged over 16,000 pull requests from 933 contributors. The release simplifies installation, revamps browser and messaging features, and introduces multi-user shared cloud sessions. This major overhaul addresses the limitations of OpenClaw&\#x27;s original architecture as project workload grew, making it easier to install and more powerful for long-running, cloud-based AI interactions. With 310k+ GitHub stars and a large contributor base, this release solidifies OpenClaw&\#x27;s position as a leading open-source personal AI assistant. The v2.0 release notes indicate that sessions can now run on paired devices or cloud workers, with the ability to move the session workspace and reuse warm machines and project seeds for later cloud sessions. It also adds support for GPT-5.6 and expanded model support, along with upgrades to memory, skills, automation, and security.

aibase · AIbase · Aug 31, 15:01

**Background**: OpenClaw is a free, open-source autonomous AI agent that executes tasks via large language models and uses messaging platforms such as iMessage, Slack, WhatsApp, and Discord as its main user interface. It is self-hosted software that runs on user-owned devices like a Mac, phone, or server, rather than a browser-based chatbot, enabling 24/7 operation and full data ownership. The project has gained significant popularity, with over 310,000 GitHub stars and a large community of contributors.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.openclaw.ai/releases/2026.8.1">v2026.8.1 (AKA OpenClaw 2 . 0 ) - OpenClaw</a></li>
<li><a href="https://learnopenclaw.com/getting-started/what-is-openclaw">What is OpenClaw? – Learn OpenClaw</a></li>
<li><a href="https://openclaws.io/">OpenClaw | The AI That Actually Does Things</a></li>

</ul>
</details>

**Tags**: `#OpenClaw`, `#open-source`, `#AI`, `#software-release`

---

<a id="item-6"></a>
## [Huawei and Ruijin Hospital Launch RuiPath 2.0 Pathology AI in 90+ Hospitals](https://www.aibase.com/news/30710) ⭐️ 8.0/10

Huawei and Ruijin Hospital officially launched RuiPath 2.0, a pathology large model, and have deployed it in over 90 hospitals across China. The model significantly improves detection of subtle and rare subtypes of common cancers. This marks one of the largest real-world deployments of an AI pathology model in clinical settings, potentially improving diagnostic accuracy and efficiency for pathologists. It demonstrates how collaboration between tech giants and top medical institutions can bring foundation model-based AI into routine healthcare. RuiPath 2.0 is a pathology large model designed to overcome traditional challenges in pathology diagnosis, particularly for rare and uncommon cancer subtypes. No technical specifications were disclosed in the announcement, but the model builds on Huawei&\#x27;s AI infrastructure and Ruijin Hospital&\#x27;s pathology expertise.

aibase · AIbase · Aug 31, 10:01

**Background**: Pathology foundation models are large neural networks trained on vast, often unlabeled datasets of whole-slide images, allowing them to generalize to tasks like cancer detection. Recent research, such as Microsoft&\#x27;s foundation models and models like Virchow and TITAN, has shown promise in computational pathology and rare cancer detection. Deploying such models at scale in hospitals requires robust pipelines, validation, and workflow integration to be clinically useful.

<details><summary>References</summary>
<ul>
<li><a href="https://www.microsoft.com/en-us/research/blog/large-scale-pathology-foundation-models-show-promise-on-a-variety-of-cancer-related-tasks/">Large-scale pathology foundation models show promise on a variety of cancer-related tasks - Microsoft Research</a></li>
<li><a href="https://www.nature.com/articles/s41591-024-03141-0">A foundation model for clinical-grade computational pathology and rare cancers detection | Nature Medicine</a></li>
<li><a href="https://www.nature.com/articles/s41591-025-03982-3">A multimodal whole-slide foundation model for pathology | Nature Medicine</a></li>

</ul>
</details>

**Tags**: `#AI in Healthcare`, `#Pathology`, `#Large Language Model`, `#Huawei`, `#Medical AI`

---

<a id="item-7"></a>
## [FSB Chair warns frontier AI models pose financial stability risks](https://news.google.com/rss/articles/CBMirgFBVV95cUxQbmJIcDlHZ0Y3aGJ0VHA1ZUNOaTIzSkR3YThzNVdKdkVMQUhRU252NWpTV3ZQMHoyYnNjZWEtcWowTW9jNjhPaWxuT1JZQjUxb0tlS3ROaTJkVmNfRDh0dGxZVWs4OG5mTXFib3lsMVd5TVczZEEwTWlPMnd6R0hlZHQ0WXVtaTdUTWt1WWFqU0h1ZWhwLWd2bWV4WmlKVU4ybWVfT1lZNkVob0J0R2c?oc=5) ⭐️ 7.0/10

The Financial Stability Board \(FSB\) Chair issued a warning about financial stability risks arising from frontier artificial intelligence \(AI\) models, emphasizing the need for oversight. This is a high-level policy statement rather than a technical deep-dive. As frontier AI models become more integrated into financial services, their potential to amplify systemic risks demands regulatory attention. The warning signals that global financial regulators are increasingly focused on AI governance beyond individual firms. The warning focuses on frontier AI models—the most advanced, general-purpose AI systems with capabilities in reasoning, multimodal understanding, and autonomous task execution. The FSB highlights the need for oversight, though specific policy measures are not detailed.

google\_news · Financial Stability Board · Aug 31, 06:04

**Background**: Frontier AI models are the most advanced AI systems available at a given time, trained on massive datasets to deliver state-of-the-art performance across many tasks. They sit at the &quot;frontier&quot; of current capabilities in areas such as reasoning, multimodal understanding, and autonomous execution. Because these models can exhibit emergent behaviors and are increasingly adopted in finance, regulators worry that failures or misuse could create systemic financial risks.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/glossary/frontier-models/">What Are Frontier AI Models and How They Work | NVIDIA Glossary</a></li>
<li><a href="https://www.crowdstrike.com/en-us/cybersecurity-101/artificial-intelligence/frontier-ai/">Frontier AI Explained: Key Models, Players, and Business Impact</a></li>
<li><a href="https://www.paloaltonetworks.com/cyberpedia/what-is-frontier-ai">What Is Frontier AI? - Palo Alto Networks</a></li>

</ul>
</details>

**Discussion**: No community discussion was available for this news item.

**Tags**: `#AI regulation`, `#financial stability`, `#frontier AI`, `#policy`

---

<a id="item-8"></a>
## [American College of Physicians Issues Ethical Guidelines for AI in Medicine](https://news.google.com/rss/articles/CBMizwFBVV95cUxNU2FHTXh4LTJ0MlNHWU01WU1jenBCd1hHR2VteFczaDE3UkRWMkx2dDRiM0ttcVpjd3o2UmxmWkZFbzNjY2RFelVCSVJSMzZLRUtYYTNEQy1ISk1CcC1HU2tQd09VWHRTOFJIZEdVOWh2ZmtXbFVNXzhmdERwcnFIUXhqQW1ELWdpZUFJSXNuTFpVaHN0d1h4SXlaWEI2c1czZTY3dW9Yb25yRXg4bnVLRXZtZ1ZnaDhnajZkNnNEcnZ0SGxfWDlnZENSd3ZWQU0?oc=5) ⭐️ 7.0/10

The American College of Physicians \(ACP\) has released a position statement on the ethical use of artificial intelligence in medical practice. This formal guidance establishes the organization&\#x27;s stance on responsible AI deployment in clinical care. As AI tools become more prevalent in diagnostics and treatment decisions, ethical guidance from a major medical organization helps protect patient safety, privacy, and equity. This position statement may shape how AI systems are developed, adopted, and regulated in healthcare. The position statement comes from the ACP, one of the largest medical specialty societies in the United States. The provided summary does not include the specific recommendations or technical details contained in the statement.

google\_news · Psychiatric Times · Aug 31, 21:07

**Background**: The American College of Physicians is a national organization of internists that regularly issues policy statements on medical practice. Artificial intelligence in medicine includes applications such as clinical decision support, diagnostic algorithms, and administrative automation, which bring ethical challenges like algorithmic bias, transparency, and accountability. The ACP&\#x27;s statement is part of a wider movement among medical societies to create governance frameworks for AI in healthcare.

**Tags**: `#AI ethics`, `#healthcare`, `#medical practice`, `#policy`

---

<a id="item-9"></a>
## [RAND Report on Tax Policy Options for the AI Age](https://news.google.com/rss/articles/CBMiY0FVX3lxTE9ndzRES3VJc2laT0dSaVVsYUtKRGFFREZKUE5lQVp4ZTR4VmNNU2NKSmZ2ZTJqdGNQNFRkN09rWXZURHpfdTVsV2JZbmdJUTZEdEs2UDN3aTQyT3Z4UkhUWkNKbw?oc=5) ⭐️ 7.0/10

RAND Corporation has released a report titled &\#x27;Tax Policy Options to Promote Employment and Stabilize Revenue in the AI Age,&\#x27; which examines how policymakers can adapt tax systems as artificial intelligence reshapes the economy. The report presents a set of tax policy options aimed at supporting employment while maintaining stable government revenue. As AI-driven automation spreads, traditional tax bases such as wage income and payroll taxes may shrink even as demand for public services grows. The report provides policymakers with options for responding to this fiscal challenge, making it a timely contribution to debates about AI policy and the future of work. The analysis is published by RAND Corporation, a nonprofit policy research institution, and targets policymakers navigating AI-driven economic change. Specific recommendations are not available from the headline alone; the report evaluates how tax systems can adapt without undermining employment.

google\_news · RAND · Aug 31, 10:14

**Background**: RAND Corporation is a nonprofit research organization that has provided analysis on public policy issues since the 1940s. A central economic concern of the AI age is that automation and artificial intelligence may displace workers, shrinking income and payroll tax revenues while increasing the need for social safety-net spending. Tax policy options commonly debated include &\#x27;robot taxes&\#x27; on automated production, reform of capital taxation, and tax credits to encourage labor-friendly investments. This report sits within that ongoing policy conversation.

**Tags**: `#AI policy`, `#tax policy`, `#employment`, `#economics`, `#RAND`

---

<a id="item-10"></a>
## [AWS Launches Agent Registry to Manage AI Agents, Tools, and Skills at Scale](https://news.google.com/rss/articles/CBMirwFBVV95cUxPWkQteXoyZjY2T3JVWFdkeEFOaUZBd0phcTNKbzlDZXFlNEI2aFNCYWNOaDIzd05HZTVJYm55b3h5ZzlxWW9JYmhmVjBzTENnR05nVVd4M2gxX2VOR2IwdG95b3dtY3VSTVNmb2V3dm1EYTNlYWNJckVMa0tYeW9EWU9uZ09xVWQwY2hKemdqdWhmZFBOR3N5WUpJNHdPRlh4ajlPR3YzUHl3dUh4bzEw?oc=5) ⭐️ 7.0/10

AWS announced AWS Agent Registry, a fully managed discovery service currently in preview, that provides a centralized catalog for organizing, curating, and discovering agents, tools, skills, and MCP servers. The launch was publicized in April 2026. This addresses a growing operational challenge for organizations building multi-agent AI systems: finding and reusing the right agents, tools, and skills at scale. It creates a central control plane for agent assets, which could accelerate enterprise adoption of agentic AI on AWS. The registry supports publishing MCP servers, tools, agents, agent skills, and custom resources, with access controlled via an approval workflow. Discovery includes both semantic and keyword search, and all access and administrative actions are audited through AWS CloudTrail. The public preview bedrock-agentcore namespace will be retired on September 17, 2026, in favor of the new agent-registry namespace.

google\_news · Amazon Web Services \(AWS\) · Aug 31, 19:18

**Background**: AI agents are software systems that use large language models to perform tasks, often calling external tools or following structured &\#x27;skills&\#x27;. As organizations build more agents, managing and discovering these reusable components becomes difficult. AWS Agent Registry is part of Amazon Bedrock AgentCore and provides a searchable catalog with human- and agent-accessible discovery, along with governance controls. MCP \(Model Context Protocol\) is an open standard for connecting AI models to tools and data sources.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry.html">AWS Agent Registry: Discover and manage agents, tools, and ...</a></li>
<li><a href="https://aws.amazon.com/about-aws/whats-new/2026/04/aws-agent-registry-in-agentcore-preview/">AWS Agent Registry for centralized agent discovery and ...</a></li>

</ul>
</details>

**Tags**: `#AWS`, `#AI agents`, `#MLOps`, `#cloud`

---