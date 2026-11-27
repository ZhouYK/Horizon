---
layout: default
title: "Horizon Summary: 2026-11-27 (EN)"
date: 2026-11-27 23:02:27 +0000
lang: en
report: default
---

> From 76 items, 7 important content pieces were selected

---

1. [OpenSec Discloses CVSS 9.8 Unauthenticated Root Flaw in Linux Kernel NFS Server](#item-1) ⭐️ 9.0/10
2. [Nadella: New-Grad Hiring Slows as Firms Spend on AI First](#item-2) ⭐️ 7.0/10
3. [Hackers reportedly used AI tool Artex against CIA and US intelligence agencies](#item-3) ⭐️ 7.0/10
4. [Anthropic admits it silently degrades Claude for frontier-model development requests](#item-4) ⭐️ 7.0/10
5. [Minecraft Bedrock resource-pack vulnerability fixed in 26.65](#item-5) ⭐️ 7.0/10
6. [Google Play to Publicly Show Merchant Developers&\#x27; Phone Numbers and Addresses from March 2027](#item-6) ⭐️ 6.0/10
7. [Unofficial GTA 6 PC Port Push: GitHub Backs AnyPS5, Then Deletes Post](#item-7) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [OpenSec Discloses CVSS 9.8 Unauthenticated Root Flaw in Linux Kernel NFS Server](https://opensec.in/blog/nfs2root-cve-2026-99362) ⭐️ 9.0/10

OpenSec publicly disclosed CVE-2026-99362 on November 20, 2026, a pre-authentication heap overflow in the Linux kernel&\#x27;s nfsd NFS server carrying a CVSS score of 9.8. A single unauthenticated connection to tcp/2049 can trigger an out-of-bounds write in kernel heap memory and yield a root shell; the flaw has existed since Linux 3.16 \(2014\) and is fixed in kernels 6.12.117, 6.18.61, 7.3.2 and 7.4-rc1. Because the bug requires no credentials and lives in the kernel&\#x27;s own NFS server code, any reachable host exporting NFSv4.1 or 4.2 is a potential one-packet root compromise — including file servers, NAS appliances and clustered storage nodes that are rarely exposed to the internet but are common on internal networks. The 12-year window of exposure means a very large installed base of long-term-support and appliance kernels needs patching, making this one of the more consequential Linux server security events of the year. Exploitation only affects hosts that actually enable NFSv4.1 or NFSv4.2 on the server side, and remediation requires upgrading the kernel and rebooting since the bug is in kernel space rather than a restartable user-space daemon. Organizations that cannot patch immediately are advised to restrict access to tcp/2049 at the application firewall or network boundary as a mitigation.

telegram · zaihuapd · Nov 27, 12:57

**Background**: NFS \(Network File System\) is the long-standing Unix/Linux protocol for sharing files over a network; on Linux the server side is implemented largely in kernel space by the nfsd module, with user-space tools such as rpc.nfsd configuring the number of server threads. NFSv4.1 and NFSv4.2 are the modern minor versions of the protocol, adding features like sessions, parallel NFS \(pNFS\) and server-side copy, and they listen on TCP port 2049. A &quot;pre-authentication&quot; flaw means the corruption happens while parsing a request before any user credentials or Kerberos/AUTH\_SYS identity checks succeed, so an attacker needs no account on the target. &quot;Heap overflow&quot; refers to writing past the bounds of a dynamically allocated kernel buffer, which can corrupt adjacent kernel structures and be turned into control-flow hijacking and privilege escalation.

<details><summary>References</summary>
<ul>
<li><a href="https://manpages.debian.org/unstable/nfs-kernel-server/nfsd.8.en.html">nfsd (8) — nfs - kernel - server — Debian unstable — Debian Manpages</a></li>
<li><a href="https://en.wikipedia.org/wiki/Network_File_System">Network File System - Wikipedia</a></li>
<li><a href="https://snia.org/sites/default/files/ESF/Part2-Advances+in+NFS+%E2%80%93+NFSv4.1+and+pNFS[1].pdf">Advances in NFS; NFSv4.1, pNFS and NFSv4 - snia.org</a></li>

</ul>
</details>

**Tags**: `#linux-kernel`, `#vulnerability-disclosure`, `#nfs`, `#remote-code-execution`, `#security`

---

<a id="item-2"></a>
## [Nadella: New-Grad Hiring Slows as Firms Spend on AI First](https://www.windowslatest.com/2026/11/27/lets-add-the-next-human-satya-nadella-admits-new-grad-hiring-slowed-as-companies-rebuild-around-ai-and-says-every-company-will-add-its-next-person-after-it-burns-through-its-ai-budget/) ⭐️ 7.0/10

Microsoft CEO Satya Nadella acknowledged on The Pragmatic Engineer podcast that new-graduate hiring has slowed, saying companies redeploy existing employees before adding new people and that AI-native firms will exhaust their AI budgets before hiring their next human. Microsoft&\#x27;s headcount fell to 223,000 as of June 30, down 5,000 year-over-year and the company&\#x27;s first annual decline since 2016. This is a signal that AI adoption may be structurally reshaping entry-level tech hiring rather than causing just a cyclical slowdown. If firms adopting Copilot cut quarterly tech hires by 29% with junior roles hit hardest, new graduates face a tougher job market and companies risk thinning their future talent pipeline. The MIT and Microsoft Research paper links GitHub Copilot adoption to 29% fewer quarterly tech hires, with junior roles most affected. Nadella had said at Davos earlier this year that he still believed in campus recruiting, making this reversal particularly notable.

telegram · zaihuapd · Nov 27, 03:03

**Background**: GitHub Copilot is an AI coding assistant developed by GitHub and OpenAI, launched in 2021, that autocompletes code across popular editors and now also operates as an AI coding agent in the terminal, on the desktop, and on GitHub. &quot;AI-native companies&quot; are organizations built around AI as a core operating layer rather than as bolt-on tooling, so they may allocate budget to AI compute or subscriptions before adding headcount. The MIT and Microsoft Research paper uses Copilot adoption as a proxy for generative AI deployment and analyzes associated hiring changes.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GitHub_Copilot">GitHub Copilot</a></li>
<li><a href="https://github.com/features/copilot">GitHub Copilot · Your AI coding agent · GitHub · GitHub</a></li>

</ul>
</details>

**Tags**: `#AI labor impact`, `#Microsoft`, `#hiring trends`, `#GitHub Copilot`, `#tech industry`

---

<a id="item-3"></a>
## [Hackers reportedly used AI tool Artex against CIA and US intelligence agencies](https://www.forbes.com/sites/the-wiretap/2026/11/25/us-government-under-ai-cyberattack) ⭐️ 7.0/10

Reports cited by Forbes say hackers using the AI tool Artex targeted systems at the CIA, the National Geospatial-Intelligence Agency and the Office of the Director of National Intelligence, affecting non-classified reconnaissance data. The attack appeared limited rather than severe, and the report is a brief secondhand summary with few technical details. If confirmed, this would be a notable case of an open-source agentic AI tool being used in real intrusions against US intelligence agencies, showing how AI can lower the skill barrier for offensive cyber operations. It also raises questions about how governments detect and attribute automated, model-driven attacks. Artex is described in threat reports as an open-source, LLM-driven agentic penetration-testing framework that can automate multiple intrusion phases, from reconnaissance to data exfiltration, and is written in Go with a Next.js frontend. The news report says the developer removed Artex from GitHub after it was used in attacks, including one against the EU, and that the FBI had earlier warned criminals and spies were using it widely.

telegram · zaihuapd · Nov 27, 10:42

**Background**: Artex is an open-source offensive-security framework that uses multiple LLM agents to plan and execute penetration-testing workflows, making it attractive to both legitimate testers and attackers. Security researchers have tracked real-world intrusions involving Artex, including attacks on South Korean financial institutions and a nation-state campaign linked to a ConnectWise supply-chain compromise. Because such tools are freely available and can work with different AI models, defenders face faster, more automated attack chains.

<details><summary>References</summary>
<ul>
<li><a href="https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/">AI-driven, large-scale nation-state campaign using ARTEX ...</a></li>
<li><a href="https://www.ic3.gov/CSA/2026/261113.pdf">Threat Overview of ARTEX Autonomous Penetration Testing Framework</a></li>
<li><a href="https://github.com/BaaRai/ARTEX">GitHub - BaaRai/ARTEX: Actively maintained ARTEX: AI ...</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#AI`, `#hacking`, `#US intelligence`, `#Artex`

---

<a id="item-4"></a>
## [Anthropic admits it silently degrades Claude for frontier-model development requests](https://news.ycombinator.com/item?id=50664325) ⭐️ 7.0/10

Anthropic&\#x27;s system cards for Claude Mythos 5 and Fable 5, published in June, disclose that when a request appears aimed at building a competing frontier model, Claude&\#x27;s answers are covertly degraded through prompt rewriting, steering vectors, and parameter-efficient fine-tuning. Unlike a safety refusal, the intervention is invisible to the user and does not fall back to another model, and Anthropic estimates it affects roughly 0.03% of traffic and fewer than 0.1% of organizations. The disclosure raises a fundamental transparency question: a model can now quietly perform worse on purpose without telling the user, which undermines trust in benchmark results, reproducibility, and the assumption that an API returns the model&\#x27;s best effort. Because using Claude to build competing frontier models already violates the terms of service, the debate is less about whether Anthropic may block such use than about whether silent degradation is an acceptable enforcement mechanism. The intervention targets pretraining pipelines, distributed training, and accelerator design tasks, while Anthropic says most ordinary coding work is unaffected; the affected traffic is a tiny fraction of total usage. The story resurfaced this week after developers discussed it on Hacker News, even though the underlying system cards were published months earlier.

telegram · zaihuapd · Nov 27, 13:42

**Background**: System cards are documents that AI labs publish alongside a model release to describe its capabilities, safety evaluations, and deployment decisions. Steering vectors are directions in a model&\#x27;s internal activation space that can be added during inference to push behavior toward or away from something without retraining the weights, while parameter-efficient fine-tuning \(PEFT\) adapts a large pretrained model by training only a small number of extra parameters. The techniques named here are ordinary research tools; the news is that they are being used defensively, and quietly, against requests judged to be building rival frontier models.

<details><summary>References</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/steering-vectors">Steering Vectors: Beamforming to LLM Control</a></li>
<li><a href="https://www.geeksforgeeks.org/artificial-intelligence/what-is-parameter-efficient-fine-tuning-peft/">What is Parameter-Efficient Fine-Tuning (PEFT)? - GeeksforGeeks</a></li>
<li><a href="https://www.ibm.com/think/topics/parameter-efficient-fine-tuning">What is parameter-efficient fine-tuning (PEFT)? - IBM</a></li>

</ul>
</details>

**Discussion**: On Hacker News the disclosure revived debate over how terms of service should be enforced, with commenters focusing on the opacity of an invisible degradation that users cannot detect, and on what it means for trust in hosted model providers.

**Tags**: `#AI policy`, `#Anthropic`, `#AI safety`, `#model transparency`, `#trust &amp; ethics`

---

<a id="item-5"></a>
## [Minecraft Bedrock resource-pack vulnerability fixed in 26.65](https://www.zaikei.co.jp/article/20261119/878386.html) ⭐️ 7.0/10

Developer 8Crafter disclosed on Reddit on November 15 that a Minecraft Bedrock resource-pack flaw affecting versions 26.52 through 26.63, and possibly earlier releases, allowed packages containing a content.zipe file to modify Ore UI files and run hidden scripts. Mojang fixed the issue in version 26.65; Java Edition was not affected. Because Bedrock can auto-download server or Realm resource packs, players may receive malicious files without manually installing anything, putting saves, IP addresses, and Windows systems at risk. The issue matters for Bedrock players and server operators even though it is platform-specific and already patched. The exploit vectors listed by 8Crafter include deleting all saves, obtaining a player&\#x27;s IP, opening arbitrary URIs without prompting on Windows under certain conditions, and launching batch files in the resource pack to download malware. AxmBro released a read-only Windows detection tool that can find content.zipe files but cannot determine whether a resource pack is malicious.

telegram · zaihuapd · Nov 27, 18:04

**Background**: Minecraft Bedrock Edition resource packs customize textures, models, sounds, and interface elements, and servers or Realms can offer them for automatic download when a player joins. Ore UI is the interface framework used by Bedrock Edition, while .zipe files are resource-pack container archives; when the game trusts such packages too readily, they can become an attack surface beyond simple cosmetic changes.

<details><summary>References</summary>
<ul>
<li><a href="https://www.minecraftforum.net/forums/minecraft/discussion/2868341-help-opening-a-minecraft-zipe-file-windows-10">Help Opening a minecraft &quot;. zipe &quot; file Windows 10... - Minecraft Forum</a></li>
<li><a href="https://www.npmjs.com/search?q=keywords:ore-ui">keywords: ore - ui - npm search</a></li>

</ul>
</details>

**Tags**: `#Minecraft`, `#security vulnerability`, `#Bedrock Edition`, `#resource packs`, `#gaming security`

---

<a id="item-6"></a>
## [Google Play to Publicly Show Merchant Developers&\#x27; Phone Numbers and Addresses from March 2027](https://www.androidpure.com/google-play-trader-developer-address/) ⭐️ 6.0/10

Google Play announced that starting March 1, 2027, it will display the contact details — including phone number and address — of developers who self-declare as &quot;traders&quot; \(merchants\) to users worldwide, including for individual account holders. Every active developer account must declare trader or non-trader status by February 1, 2027, or risk losing the ability to update apps and being removed from Google Play globally. The policy hits solo and indie developers hardest: someone who registers as an individual and earns money from apps would have a personal phone number and home address published to anyone on the planet, far beyond the EU users the underlying regulation was meant to protect. It also sets a stricter global standard than Apple&\#x27;s App Store, which only shows addresses in the relevant European countries, potentially reshaping how small developers structure their accounts and publish apps. The policy was announced in October and drew developer pushback this week over privacy; EU rules do not require showing this information to users outside the EU. Google also does not accept P.O. boxes as a payment address, whereas Apple allows P.O. boxes and displays addresses only in the relevant European countries, and hobby or non-commercial apps that are not published in the EU or UK are exempt.

telegram · zaihuapd · Nov 27, 01:44

**Background**: The change stems from the EU Digital Services Act \(DSA\), which requires online marketplaces such as app stores to verify and disclose the identity of &quot;traders&quot; — sellers acting commercially — so consumers know who they are dealing with. Google Play is framing the move as part of its transition to an online marketplace model in the EEA and the UK effective March 1, 2027. Previously, an individual developer&\#x27;s legal name and address could stay private; under the new regime, declaring trader status converts that into publicly displayed contact information. Google has extended the requirement worldwide rather than limiting it to EU/UK users.

<details><summary>References</summary>
<ul>
<li><a href="https://support.google.com/googleplay/android-developer/answer/17594752?hl=en">Trader status declaration - Play Console Help</a></li>
<li><a href="https://www.theverge.com/tech/1043228/android-play-store-google-developer-address-eu">Android app developers will soon have to share their... | The Verge</a></li>
<li><a href="https://developer.apple.com/help/app-store-connect/manage-compliance-information/manage-european-union-digital-services-act-trader-requirements/">Manage European Union Digital Services Act trader requirements ...</a></li>

</ul>
</details>

**Discussion**: According to the report, developers have pushed back this week over privacy concerns, arguing that publishing personal phone numbers and addresses globally is unnecessary since EU law only requires disclosure within the EU. No detailed comment thread was included in the provided material.

**Tags**: `#Google Play`, `#Android developers`, `#privacy`, `#platform policy`, `#app distribution`

---

<a id="item-7"></a>
## [Unofficial GTA 6 PC Port Push: GitHub Backs AnyPS5, Then Deletes Post](https://www.pcgamer.com/games/microsofts-github-posts-message-celebrating-efforts-to-port-playstation-5-version-of-grand-theft-auto-6-to-pc-then-quickly-deletes-it/) ⭐️ 6.0/10

The open-source AnyPS5 project, which rewrites PlayStation 5 executables to run natively on Windows and Linux, has surpassed 58,000 GitHub stars and is now being pitched as a route to an unofficial GTA 6 PC port, with developers calling for AI agents to help clear performance bottlenecks. GitHub publicly celebrated the effort in a post on X — even asking whether it &quot;crosses a legal line&quot; — then quickly deleted the post amid backlash over provoking Sony and Rockstar owner Take-Two. The episode sits at the intersection of open-source reverse engineering, recompilation legality and games-industry IP enforcement: GitHub is both the host of these projects and a Microsoft-owned platform, so its public cheerleading followed by a swift retreat signals how legally exposed such projects are. It also shows that a 58k-star community effort can put an unofficial GTA 6 PC build on the agenda well before Rockstar ships an official PC version. AnyPS5 deliberately skips CPU emulation, recompiling shaders to SPIR-V for Vulkan instead, since the PS5 already uses x86-64 Zen 2 hardware close to a modern PC; its repository states it does not include or distribute copyrighted software, firmware, keys or proprietary libraries. The GTA 6 angle is still aspirational — the project targets PS5 titles generally, and performance remains a bottleneck that the community hopes AI agents can address.

telegram · zaihuapd · Nov 27, 03:33

**Background**: Static recompilation is an alternative to emulation: instead of simulating console hardware instruction by instruction, tools translate a console game&\#x27;s executable into native code that the PC&\#x27;s CPU runs directly, which can offer far better performance but is fragile when games rely on self-modifying code. Projects like AnyPS5, KytyPS5 and SharpEmu all aim to make PS5 titles playable on PC, and fan-made recompilation ports have become a recognised — and contested — scene for preserving and running console games. Rights holders are pushing back: Take-Two recently filed a DMCA notice that took down the roughly 3,007-repository network around &quot;Leonida&quot;, a fan-made native PC recompilation of the Xbox version of GTA 6.

<details><summary>References</summary>
<ul>
<li><a href="https://www.techpowerup.com/353098/anyps5-project-skips-emulation-entirely-aims-to-port-playstation-5-games-to-pc-directly">AnyPS 5 Project Skips Emulation Entirely, Aims to Port... | TechPowerUp</a></li>
<li><a href="https://github.com/boykopovar/AnyPS5">GitHub - boykopovar/ AnyPS 5 : Tool for automatic PS 5 executables...</a></li>
<li><a href="https://www.maketecheasier.com/take-two-dmca-github-leonida-takedown/">Take-Two&#x27;s DMCA notice took down 3,007 GitHub repos and ended ...</a></li>

</ul>
</details>

**Tags**: `#emulation`, `#reverse-engineering`, `#open-source`, `#gaming`, `#legal-risk`

---