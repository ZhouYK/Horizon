---
layout: default
title: "Horizon Summary: 2026-08-03 (EN)"
date: 2026-08-03
lang: en
report: default
---

> From 376 items, 8 important content pieces were selected

---

1. [Qwen Releases 3.8-Max: 2.4 Trillion Parameter Open-Source Model](#item-1) ⭐️ 9.0/10
2. [Apple sues UK government over iCloud backdoor demand](#item-2) ⭐️ 9.0/10
3. [DNA Analysis Equipment Flaw Exposes 30 Years of Evidence to Tampering](#item-3) ⭐️ 8.0/10
4. [Police Misused License Plate Cameras to Spy on Exes, Investigation Finds](#item-4) ⭐️ 8.0/10
5. [Nvidia CMP 170HX Cracked: 80GB VRAM Unlocked, Second-Hand Prices Surge](#item-5) ⭐️ 8.0/10
6. [CXMT Plans Beijing DRAM Fab Expansion Amid AI Chip Demand](#item-6) ⭐️ 7.0/10
7. [Apple Photos faces $32.5B class action over facial data in Illinois](#item-7) ⭐️ 7.0/10
8. [US States Reconsider Data Center Tax Breaks, Raising AI Infrastructure Costs](#item-8) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Qwen Releases 3.8-Max: 2.4 Trillion Parameter Open-Source Model](https://qwen.ai/blog?id=qwen3.8) ⭐️ 9.0/10

Qwen officially released Qwen 3.8-Max, a 2.4-trillion-parameter Mixture-of-Experts model with 95B active parameters, and announced that its weights will be open-sourced next week. This marks the first time Qwen has publicly released weights for a Max-level model. This release is significant because it makes a frontier-scale, state-of-the-art model openly available, which could democratize access to top-tier AI capabilities and intensify competition with closed-source proprietary models. Developers and researchers can now build on and fine-tune a Max-level model, potentially accelerating innovation across the open-source AI ecosystem. Based on the Qwen 3.5 architecture, Qwen 3.8-Max supports a 1M-token context window and accepts text, image, and video inputs. In benchmark tests, it autonomously ran coding projects for over 10 days and finished in the top tier of a WWW2025 multimodal competition, and it is already available via the QwenCloud API.

telegram · zaihuapd · Aug 3, 02:31

**Background**: Qwen is Alibaba&\#x27;s family of large language models, where the &\#x27;Max&\#x27; tier denotes the flagship, largest, and most capable models in each generation. The model employs a Mixture-of-Experts \(MoE\) architecture, which activates only a subset of parameters per token \(in this case 95B out of 2.4T\) to improve efficiency. Previously, Max-level weights were only accessible through paid APIs, making this open-source release a major shift in how Qwen distributes its most advanced technology.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://empiriolabs.ai/blog/qwen3-8-max-api">How to Use the Qwen 3.8 Max API | EmpirioLabs AI</a></li>
<li><a href="https://apidog.com/blog/qwen-3-8-vs-qwen-3-7/">Qwen 3.8 vs Qwen 3.7 Max : What Actually Changed</a></li>

</ul>
</details>

**Tags**: `#Qwen`, `#LLM`, `#Open-Source`, `#AI`, `#Model Release`

---

<a id="item-2"></a>
## [Apple sues UK government over iCloud backdoor demand](https://www.ft.com/content/2cc9c96a-0e5b-4c33-a95a-3d11072a145c?syn-25a6b1a6=1) ⭐️ 9.0/10

Apple has filed a legal challenge with the UK Investigatory Powers Tribunal against the government&\#x27;s Technical Capability Notice requiring a backdoor into encrypted iCloud backups. The case continues a long-running dispute over encryption and privacy. This case could set a precedent for whether governments can compel tech companies to weaken encryption, affecting user privacy and security worldwide. It also tests the limits of UK surveillance powers against global tech firms. The UK initially withdrew a broader notice after a dispute with the US, then issued a new notice limited to UK users. Apple removed iCloud Advanced Data Protection in the UK in February 2025; privacy groups Privacy International and Liberty have also challenged the notice, with a case management hearing scheduled next month.

telegram · zaihuapd · Aug 3, 15:40

**Background**: A Technical Capability Notice \(TCN\) is a legal order under UK law that can require companies to remove electronic protection or provide access to data. The Investigatory Powers Tribunal is the UK court that hears complaints about surveillance powers. iCloud Advanced Data Protection is an optional Apple setting that provides end-to-end encryption for most iCloud data, meaning Apple cannot access the content.

<details><summary>References</summary>
<ul>
<li><a href="https://support.apple.com/zh-cn/guide/security/sec973254c5f/web">iCloud 高 级 数 据 保 护 - 官方 Apple 支持 (中国)</a></li>
<li><a href="https://support.apple.com/zh-cn/108756">如何打开 iCloud 高 级 数 据 保 护 - 官方 Apple 支持 (中国)</a></li>

</ul>
</details>

**Tags**: `#Apple`, `#encryption`, `#UK law`, `#privacy`, `#iCloud`

---

<a id="item-3"></a>
## [DNA Analysis Equipment Flaw Exposes 30 Years of Evidence to Tampering](https://www.wsj.com/tech/cybersecurity/security-flaw-placed-30-years-of-dna-evidence-at-risk-of-hacking-1932775a) ⭐️ 8.0/10

Researchers discovered security vulnerabilities in DNA analysis equipment made by Thermo Fisher Scientific and used by most U.S. crime labs, allowing undetectable tampering of evidence files dating back to 1995. A software update adding digital signatures has been released. This flaw threatens the integrity of decades of forensic DNA evidence, potentially affecting current and past criminal cases. It also highlights the lack of uniform cybersecurity oversight across the more than 200 U.S. crime labs using such equipment. Researchers used AI-generated code from Anthropic&\#x27;s Claude to modify DNA scan data without triggering alerts, completing the first tampering attempt in about 45 minutes. Thermo Fisher privately acknowledged the flaw in July and issued a high-severity advisory, while stating no real-world exploits have been confirmed.

telegram · zaihuapd · Aug 3, 05:15

**Background**: Forensic DNA analysis determines DNA profiles from biological samples for legal and investigative purposes, and its results are heavily relied upon in court. A digital signature is a cryptographic scheme that verifies the authenticity and integrity of digital data, making tampering detectable. In this case, AI tools like Anthropic&\#x27;s Claude were used to generate exploit code, demonstrating how large language models can assist in cybersecurity research.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Forensic_DNA_analysis">Forensic DNA analysis</a></li>
<li><a href="https://en.wikipedia.org/wiki/Digital_signature">Digital signature</a></li>
<li><a href="https://en.wikipedia.org/wiki/Anthropic_Claude">Anthropic Claude</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#DNA analysis`, `#forensics`, `#vulnerability`, `#AI`

---

<a id="item-4"></a>
## [Police Misused License Plate Cameras to Spy on Exes, Investigation Finds](https://www.washingtonpost.com/technology/2026/08/02/how-police-officers-used-vast-network-cameras-spy-their-exes/) ⭐️ 8.0/10

The Washington Post published an investigation on August 2, 2026 revealing that at least 50 U.S. law enforcement officers have been accused or prosecuted for misusing automated license plate recognition \(ALPR\) systems, including 26 cases involving spying on wives, girlfriends, ex-partners, or women they were interested in. Of these, 46 cases involved Flock Safety cameras, and one Georgia police chief who allegedly conducted about 600 searches on his ex-girlfriend&\#x27;s license plate died by suicide before his trial. This investigation exposes systemic privacy and accountability failures in the deployment of surveillance technology by law enforcement, revealing how tools meant for public safety can be weaponized for personal harassment. It underscores the urgent need for stronger oversight, mandatory audit trails, and legal consequences for misuse, affecting public trust in both police and surveillance vendors. Flock Safety operates more than 120,000 cameras across over 6,000 communities, recording about 20 billion license plate scans per month. The company&\#x27;s CEO acknowledged that misuse is hard to completely avoid and has launched an optional &\#x27;audit assistance&\#x27; feature, but currently only 13 states require audits and at least 8 states criminalize misuse of ALPR systems.

telegram · zaihuapd · Aug 3, 09:03

**Background**: Automated license plate recognition \(ALPR\) systems use high-speed cameras to capture and record every passing vehicle&\#x27;s license plate, along with make, model, and distinguishing features. Flock Safety is one of the largest ALPR vendors in the U.S., selling cameras to police departments, businesses, and homeowners&\#x27; associations. Privacy advocates have long warned that ALPR systems create vast, searchable databases of innocent people&\#x27;s movements, posing serious risks to civil liberties with little evidence of crime prevention.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ajc.com/news/2026/07/3-more-georgia-police-officers-fired-over-alleged-flock-camera-misuse/">Officers fired for alleged Flock camera misuse in DeKalb, Henry...</a></li>
<li><a href="https://www.eff.org/deeplinks/2019/06/victory-california-orders-state-audit-automated-license-plate-readers">Victory: California Orders State Audit of Automated License Plate...</a></li>
<li><a href="https://deflock.org/">Find Nearby ALPRs | DeFlock</a></li>

</ul>
</details>

**Tags**: `#surveillance`, `#privacy`, `#law enforcement`, `#license plate recognition`, `#technology ethics`

---

<a id="item-5"></a>
## [Nvidia CMP 170HX Cracked: 80GB VRAM Unlocked, Second-Hand Prices Surge](https://finance.sina.com.cn/tech/roll/2026-08-03/doc-inikzqsf4659769.shtml) ⭐️ 8.0/10

Researchers at Arizona State University published a method to crack Nvidia&\#x27;s CMP 170HX mining GPU by exploiting a stack overflow in its Falcon security coprocessor, bypassing OTP fuse locks. The hack unlocks up to 80GB of VRAM and boosts FP32 compute from 0.39 to 94 TFLOPS, sending second-hand prices from 300–500 yuan to 3000–4000 yuan. This turns a cheap, crippled mining card into a capable AI inference GPU, making high-end AI hardware far more accessible to hobbyists and researchers. It also highlights that physical fuse-based hardware locks are not irreversible, with potential implications for GPU security and the second-hand market. The exploit uses an unbounded DMA overflow in the Falcon security coprocessor to hijack privileges and modify registers, unlocking limits set by one-time-programmable \(OTP\) fuses. Chinese communities have verified unlocked cards running AI image generation and LLM inference on Windows and Linux, though long-term stability and unlock ceilings vary by batch.

telegram · zaihuapd · Aug 3, 11:29

**Background**: The CMP 170HX is a dedicated cryptocurrency mining GPU launched by Nvidia in 2021, built on the same GA100 die as the A100 data-center GPU. To keep it from cannibalizing AI sales, Nvidia physically crippled it with OTP fuses that cap compute, memory, and PCIe bandwidth; OTP fuses are one-time programmable hardware settings that cannot normally be reversed.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ebay.com/itm/158128978889">NVIDIA CMP 170 HX 8GB - 64GB Unlock Tested | eBay</a></li>
<li><a href="https://www.topcpu.net/en/gpu-c/cmp-170hx-vs-geforce-gtx-1070">NVIDIA CMP 170 HX vs NVIDIA GeForce GTX 1070 - GPU Comparison</a></li>
<li><a href="https://electronics.stackexchange.com/questions/455756/how-are-otp-fuses-in-ics-implemented">integrated circuit - How are OTP fuses in ICs implemented? - Electrical...</a></li>

</ul>
</details>

**Tags**: `#hardware-security`, `#GPU`, `#Nvidia`, `#AI-inference`, `#exploit`

---

<a id="item-6"></a>
## [CXMT Plans Beijing DRAM Fab Expansion Amid AI Chip Demand](https://www.reuters.com/world/asia-pacific/cxmt-plans-second-chip-plant-beijing-is-talks-its-funding-sources-say-2026-08-03/) ⭐️ 7.0/10

CXMT is planning to build a second 12-inch DRAM wafer fab in Beijing&\#x27;s Yizhuang area, next to its existing plant, and is in early talks with the Beijing Economic-Technological Development Area for at least 60 million yuan in funding. The company has not commented publicly on the reports. As AI infrastructure drives a global chip shortage, CXMT—the world&\#x27;s fourth-largest DRAM maker—is expanding to narrow the huge gap with Samsung, SK Hynix, and Micron, which together control nearly 90% of the market. The move could reshape DRAM supply dynamics and bolster China&\#x27;s semiconductor self-sufficiency. The new fab would be built in Yizhuang, adjacent to CXMT&\#x27;s existing DRAM plant, and negotiations are still at an early stage. CXMT currently operates three 12-inch DRAM fabs in Hefei and Beijing with monthly capacity of about 100,000 wafers each; planned plants in Shanghai and Hefei could roughly double total capacity to more than 600,000 wafers per month.

telegram · zaihuapd · Aug 3, 09:38

**Background**: DRAM \(Dynamic Random Access Memory\) is a type of volatile memory widely used in computers and servers to store data temporarily. A 12-inch \(300mm\) wafer fab is the industry-standard scale for advanced memory production, offering better cost efficiency and higher yields than older 8-inch lines. CXMT is a Chinese integrated memory manufacturer founded in 2016, focused on the design, R&amp;D, production, and sales of DRAM chips.

<details><summary>References</summary>
<ul>
<li><a href="https://zh.wikipedia.org/zh-cn/%E9%95%BF%E9%91%AB%E5%AD%98%E5%82%A8">长 鑫 存 储 - 维基百科，自由 的 百科全书</a></li>
<li><a href="https://m.elecfans.com/article/2067316.html">什 么 是 DRAM ？ DRAM 存储单元电路读写原理-电子发烧友网</a></li>
<li><a href="https://www.htsemi.com/shows/18/92.html">htsemi.com/shows/18/92.html</a></li>

</ul>
</details>

**Tags**: `#semiconductor`, `#DRAM`, `#China`, `#chip manufacturing`, `#funding`

---

<a id="item-7"></a>
## [Apple Photos faces $32.5B class action over facial data in Illinois](https://appleinsider.com/articles/26/08/03/apple-photos-facial-features-prompt-a-325b-class-action-lawsuit) ⭐️ 7.0/10

A $32.5 billion class action lawsuit against Apple Photos has been cleared to proceed in Illinois, alleging the app collects facial biometric data without users&\#x27; informed consent. The U.S. Seventh Circuit Court of Appeals rejected Apple&\#x27;s appeal on June 30, allowing the case to move forward. This case tests how U.S. state biometric privacy laws apply to consumer photo apps and could shape facial-recognition practices across the tech industry. Because BIPA allows penalties of $1,000 to $5,000 per violation without proof of actual harm, the financial exposure for companies can be enormous. The suit covers roughly 6.5 million Illinois consumers and claims Apple creates &\#x27;face features&\#x27; for people in photos, identifies iPhone users via algorithms, and syncs data through iCloud. Apple had argued the process does not create biometric identifiers, but the court found the case suitable for class-action status.

telegram · zaihuapd · Aug 3, 14:33

**Background**: Illinois&\#x27;s Biometric Information Privacy Act \(BIPA\), enacted in 2008, was the first U.S. state law to regulate the collection, use, and handling of biometric identifiers and information by private entities. BIPA is notable for allowing plaintiffs to recover statutory damages of $1,000 to $5,000 per violation without alleging actual injury, making it a powerful tool for class action lawsuits. Facial recognition in photo apps typically works by extracting features such as eyes, nose, mouth, and their relative positions to identify or tag individuals.

<details><summary>References</summary>
<ul>
<li><a href="https://www.kelleydrye.com/trending/the-illinois-biometric-information-privacy-act-bipa">The Illinois Biometric Information Privacy …</a></li>
<li><a href="https://www.wikiwand.com/en/articles/Biometric_Information_Privacy_Act">Biometric Information Privacy Act - Wikiwand</a></li>

</ul>
</details>

**Tags**: `#Apple`, `#Privacy`, `#Biometric Data`, `#Facial Recognition`, `#Lawsuit`

---

<a id="item-8"></a>
## [US States Reconsider Data Center Tax Breaks, Raising AI Infrastructure Costs](https://theinformation.com/articles/exclusive-data-center-costs-set-rise-u-s-states-move-repeal-tax-breaks) ⭐️ 6.0/10

Several U.S. states are considering repealing or tightening tax exemptions previously offered to data centers. The policy shift could raise the cost of building and operating AI infrastructure, according to a report from The Information. This matters because data centers are the physical backbone of AI development, and higher costs could ripple through cloud pricing and AI deployment. State-level tax policy is becoming a key battleground as AI-driven electricity demand and fiscal pressures collide. The report notes that states previously waived taxes on servers and electricity to attract data center investment, but now face pressure from rising power demand and infrastructure costs. Analysts say the change may affect where and how quickly future AI data centers are built in the U.S.

telegram · zaihuapd · Aug 3, 00:42

**Background**: Data center tax incentives have long been used by U.S. states to lure large-scale computing facilities, which bring jobs and investment. However, AI workloads consume far more electricity and land than earlier cloud computing, and local governments are increasingly asked to pay for grid upgrades and other public infrastructure while tax revenue shrinks. This has led to a policy rethink across several states.

<details><summary>References</summary>
<ul>
<li><a href="https://commerce.maryland.gov/fund/data-center-maryland-sales-and-use-tax-exemption-incentive-program">Funding &amp; Incentives Data Center Maryland Sales and Use Tax Exemption Incentive Program</a></li>
<li><a href="https://ded.mo.gov/programs/business/data-center-sales-tax-exemption-program">Data Center Sales Tax Exemption Program | Department of Economic Development</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_infrastructure">AI infrastructure</a></li>

</ul>
</details>

**Tags**: `#AI infrastructure`, `#data centers`, `#tax policy`, `#cloud computing`, `#economics`

---