---
layout: default
title: "Horizon Summary: 2026-08-25 (EN)"
date: 2026-08-25 23:35:50 +0000
lang: en
report: default
---

> From 285 items, 11 important content pieces were selected

---

1. [NVIDIA Vera Rubin NVL72 Boosts DeepSeek Throughput 30x](#item-1) ⭐️ 9.0/10
2. [OpenAI&\#x27;s Custom Jalapeño Chip Beats Nvidia GB300 in Inference Tests](#item-2) ⭐️ 9.0/10
3. [SpaceX plans to launch NVIDIA Vera Rubin NVL72 into orbit by 2027](#item-3) ⭐️ 8.0/10
4. [Apple Unveils M6 and M5 Ultra Chips, M6 Debuts with 2nm Process](#item-4) ⭐️ 8.0/10
5. [GPT-5.6 Sol Designs Custom CPU That Runs Doom in Turing Complete](#item-5) ⭐️ 8.0/10
6. [Anthropic Projects Over $30 Trillion in Potential Revenue, Topping SpaceX&\#x27;s Record](#item-6) ⭐️ 8.0/10
7. [Leaked Project Aion: Microsoft&\#x27;s Experimental Copilot-Centric OS](#item-7) ⭐️ 6.0/10
8. [Linux Marks 35 Years Since Its First Public Release](#item-8) ⭐️ 6.0/10
9. [Unitree Stock Slides 45% From IPO Peak, Wiping Out 200 Billion Yuan](#item-9) ⭐️ 6.0/10
10. [Qwen Teases August 2026 Open-Source Release of Qwen3.8-Flash-Next](#item-10) ⭐️ 6.0/10
11. [Nvidia Unveils Jetson Orin Nano 2, Doubling Edge AI Inference Performance](#item-11) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [NVIDIA Vera Rubin NVL72 Boosts DeepSeek Throughput 30x](https://blogs.nvidia.com/blog/vera-rubin-nvl72-efficiency-ai-agents/) ⭐️ 9.0/10

NVIDIA announced first on-chip benchmark results for its Vera Rubin NVL72 rack-scale system, showing up to 30x higher throughput per megawatt and 35x lower cost per million tokens for DeepSeek-V4-Pro agentic coding tasks compared to GB300. The company also unveiled Groq 3 LPX inference accelerators and the Vera CPU for agents. This marks a major leap in AI inference efficiency, significantly lowering the cost of running large language models and enabling more scalable agentic AI workloads. The announcement signals intensifying competition in AI infrastructure, with implications for cloud providers, enterprises, and the broader AI ecosystem. Vera Rubin NVL72 combines 72 Rubin GPUs and 36 Vera CPUs in a single liquid-cooled rack interconnected via NVLink 6, featuring a new Transformer Engine with adaptive compression for NVFP4 inference performance. Groq 3 LPX, benchmarked running Gemma 4 31B at 3,400 output tokens per second, enters full production and supports up to 256 LP30 accelerators per rack deployment.

telegram · zaihuapd · Aug 25, 14:48

**Background**: Rack-scale systems package multiple GPUs, CPUs, and high-bandwidth interconnects into a single unit to act as one giant computer, delivering far higher performance and efficiency than traditional server racks. AI inference—running trained models to generate outputs—has become a key bottleneck for applications like AI agents, which require low latency and high throughput at scale. NVIDIA&\#x27;s Vera Rubin platform targets these workloads with new GPU, CPU, and inference accelerator designs.

<details><summary>References</summary>
<ul>
<li><a href="https://blogs.nvidia.com/blog/vera-rubin-lpx-spectrum-x-nvlink-fusion/">NVIDIA Advances Vera Rubin Inference With New LPX ... | NVIDIA Blog</a></li>
<li><a href="https://www.nvidia.com/en-us/data-center/technologies/rubin/">Infrastructure for Scalable AI Reasoning | NVIDIA Vera Rubin Platform</a></li>
<li><a href="https://siliconangle.com/2026/08/24/nvidias-dedicated-inference-accelerator-groq-3-lpx-enters-full-production-to-supercharge-ai-agents/">Nvidia&#x27;s dedicated inference accelerator Groq 3 LPX ... - SiliconANGLE</a></li>

</ul>
</details>

**Tags**: `#NVIDIA`, `#Vera Rubin`, `#AI inference`, `#hardware`, `#DeepSeek`

---

<a id="item-2"></a>
## [OpenAI&\#x27;s Custom Jalapeño Chip Beats Nvidia GB300 in Inference Tests](https://openai.com/index/jalapeno-first-results/) ⭐️ 9.0/10

OpenAI published first benchmark results for Jalapeño, its custom inference chip co-developed with Broadcom. Against Nvidia&\#x27;s GB300, it delivers 1.5–1.9x better power efficiency and 1.7–3.6x lower latency across three large models, with deployment planned by end of year. This marks OpenAI&\#x27;s push to reduce reliance on Nvidia and could reshape the AI hardware landscape. However, the results are self-reported and do not compare against Nvidia&\#x27;s newly shipping Vera Rubin platform. The chip is rated at 700W but sustained real-world power draw stays under 550W. It is designed only for inference—not training—and a second-generation chip is already in development, with a third in design.

telegram · zaihuapd · Aug 25, 16:08

**Background**: OpenAI has historically depended on Nvidia GPUs for both training and inference. Custom inference ASICs can cut costs and latency by specializing in running already-trained models; Nvidia&\#x27;s GB300 is the current Blackwell-based system, while Vera Rubin is Nvidia&\#x27;s next-generation platform that has just begun shipping.

<details><summary>References</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/openais-jalape%C3%B1o-chip-what-developers-need-know-its-move-ashish-jain-9uoof">OpenAI ’s Jalapeño Chip : What Developers Need to Know About Its...</a></li>
<li><a href="https://www.spheron.network/blog/openai-jalapeno-chip-gpu-cloud-inference-2026/">OpenAI Jalapeño Chip Explained: What... | Spheron Blog</a></li>
<li><a href="https://blogs.nvidia.com/blog/vera-rubin-nvl72-efficiency-ai-agents/">NVIDIA Vera Rubin NVL72 Sets a New Efficiency... | NVIDIA Blog</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#custom silicon`, `#AI hardware`, `#inference`, `#Nvidia`

---

<a id="item-3"></a>
## [SpaceX plans to launch NVIDIA Vera Rubin NVL72 into orbit by 2027](https://www.theregister.com/off-prem/2026/08/25/spacex-claims-it-will-put-a-vera-rubin-nvl72-rack-scale-system-into-orbit-next-year/5292067) ⭐️ 8.0/10

SpaceX announced plans to launch an NVIDIA Vera Rubin NVL72 rack-scale AI system into orbit in 2027 to test space-based AI computing. This would be the first deployment of a full rack-scale AI supercomputer in space. This is a significant milestone in the growing push toward orbital data centers and space-based AI infrastructure. If successful, it could enable on-orbit data processing for satellite constellations, defense programs, and low-latency edge computing, reducing reliance on ground-based systems. The NVL72 consists of 72 Rubin GPUs and 36 Vera CPUs, with total power consumption exceeding 100 kW and requiring complex liquid cooling and power delivery. SpaceX has not yet disclosed the exact launch date, orbital altitude, or how the system will be powered and cooled in space.

telegram · zaihuapd · Aug 25, 08:03

**Background**: Orbital data centers and space-based AI infrastructure are long-proposed concepts that would use space-based solar power and on-orbit processing. The idea has historical roots in military architectures, such as the 1980s Brilliant Pebbles program, and has been revived by the Space Development Agency&\#x27;s Proliferated Warfighter Space Architecture. Launching a rack-scale GPU system like the Vera Rubin NVL72 would be a concrete step toward making such orbital computing a reality.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/data-center/technologies/rubin/">Infrastructure for Scalable AI Reasoning | NVIDIA Vera Rubin Platform</a></li>
<li><a href="https://en.wikipedia.org/wiki/Orbital_data_center">Orbital data center</a></li>
<li><a href="https://grokipedia.com/page/nvidia-vera-rubin-nvl72">NVIDIA Vera Rubin NVL72</a></li>

</ul>
</details>

**Tags**: `#SpaceX`, `#NVIDIA`, `#AI`, `#Space Computing`, `#Orbital Data Center`

---

<a id="item-4"></a>
## [Apple Unveils M6 and M5 Ultra Chips, M6 Debuts with 2nm Process](https://www.apple.com/newsroom/2026/08/apple-introduces-m6-and-m5-ultra-for-a-big-leap-in-performance-and-ai-compute/) ⭐️ 8.0/10

Apple announced the M6 chip in the new Mac mini and the M5 Ultra in the new Mac Studio. The M6 is Apple&\#x27;s first 2nm chip, while the M5 Ultra is the first M-series chip to use a quad-die architecture. This marks a major leap in Apple Silicon performance and AI compute, directly impacting developers and systems researchers working on high-performance and machine-learning workloads. The 2nm process and quad-die design set new benchmarks for the industry. The M6 features a 12-core CPU, 12-core GPU, and dual 16-core Neural Engines, with up to 170GB/s unified memory bandwidth. The M5 Ultra offers up to 36 CPU cores, 80 GPU cores, up to 512GB memory, and 1.2TB/s bandwidth, a 50% increase over the M3 Ultra.

telegram · zaihuapd · Aug 25, 13:06

**Background**: Unified memory bandwidth measures how fast the CPU and GPU can access the same shared memory pool, which is crucial for AI inference and large model workloads. The 2nm process refers to a chip manufacturing node that packs more transistors, improving performance and energy efficiency compared to current 3nm technology.

<details><summary>References</summary>
<ul>
<li><a href="https://www.shuzhipunk.com/articles/0hJ3ur8LMTR">M 5 Ultra ... | 数智朋克</a></li>
<li><a href="https://agihunt.info/story/1a0374c13676b3f5f7fc2aa1885">苹果 M 5 /M6 芯 片 新品：从爆料到发布 · AGI Hunt 专题</a></li>
<li><a href="https://ljmeat.com/article/2-96/">ljmeat.com/article/ 2 -96</a></li>

</ul>
</details>

**Tags**: `#Apple Silicon`, `#M6`, `#M5 Ultra`, `#2nm`, `#Hardware`

---

<a id="item-5"></a>
## [GPT-5.6 Sol Designs Custom CPU That Runs Doom in Turing Complete](https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-coder-gets-doom-running-on-a-custom-cpu-designed-by-gpt-5-6-sol-game-viewport-is-overlaid-on-a-pulsing-schematic-of-the-cpu-in-turing-completes-sandbox-environment) ⭐️ 8.0/10

AI enthusiast Angel showed GPT-5.6 Sol designing a custom CPU called Codex-R32 inside the game Turing Complete, which successfully booted and ran the 1993 classic Doom. The CPU was built from basic logic gates and executed RV32IM machine code compiled from C. This marks a notable AI milestone: a model autonomously designing a complete, working CPU from logic gates to run a real game, demonstrating advanced hardware design and code generation capability. It showcases potential for AI-assisted chip design, though it is a sandbox demonstration rather than a production breakthrough. The CPU runs PureDOOM, a single-header Doom source port, compiled to RV32IM RISC-V instructions and executed natively on the simulated hardware. In the demo, the game viewport is overlaid on a real-time pulsing schematic of the processor&\#x27;s gate-level circuit.

telegram · zaihuapd · Aug 25, 15:23

**Background**: Turing Complete is a Steam game that teaches computer architecture: starting from a single NAND gate, players build logic gates, components, and eventually a full CPU. RV32IM is a common RISC-V instruction set variant. PureDOOM is a dependency-free single-header port of Doom that can run without graphics, input, sound, or music. These pieces together let an AI construct and test a complete CPU in a simulated environment.

<details><summary>References</summary>
<ul>
<li><a href="https://turingcomplete.game/">Turing Complete</a></li>
<li><a href="https://github.com/Daivuk/PureDOOM">Daivuk/ PureDOOM : Pure DOOM - Single Header Doom Source Port ...</a></li>
<li><a href="https://projectf.io/posts/riscv-cheat-sheet/">RISC - V Assembler Cheat Sheet - Project F</a></li>

</ul>
</details>

**Discussion**: Commenters jokingly asked whether the AI could run Crysis next. The AI&\#x27;s reply, delivered via Angel, was to first build a GPU, add several gigabytes of RAM, and draw a circuit diagram visible from space.

**Tags**: `#AI`, `#CPU Design`, `#GPT-5.6`, `#Doom`, `#Turing Complete`

---

<a id="item-6"></a>
## [Anthropic Projects Over $30 Trillion in Potential Revenue, Topping SpaceX&\#x27;s Record](https://www.wsj.com/tech/ai/anthropic-expected-to-tell-investors-it-sees-over-30-trillion-in-potential-revenue-a611efea) ⭐️ 8.0/10

Anthropic, the developer of Claude, is reportedly preparing to tell investors that its potential revenue opportunity exceeds $30 trillion, a figure that would surpass SpaceX&\#x27;s record $28.5 trillion estimate. The Wall Street Journal reported the projection, citing people familiar with the matter. This staggering projection signals enormous market expectations for artificial intelligence and could significantly influence AI investment trends, setting a new benchmark for startup valuations. As a leading AI company, Anthropic&\#x27;s estimate may reshape how investors assess the growth potential of AI startups across the industry. The figure refers to total addressable market \(TAM\)—the potential revenue opportunity for a product or service—not actual revenue or profit. Anthropic&\#x27;s $30 trillion estimate would exceed SpaceX&\#x27;s $28.5 trillion claim, pushing the limits of this often-criticized financial metric even further.

telegram · zaihuapd · Aug 25, 17:32

**Background**: Total addressable market \(TAM\) is a metric used to measure the revenue opportunity for a product or service and helps prioritize business opportunities. It is often used by startups to justify large valuations by showing investors how big the opportunity could become. TAM is typically calculated using top-down, bottom-up, or value theory methods. SpaceX&\#x27;s IPO had previously tested the limits of this metric, and Anthropic&\#x27;s projection would push it to a new level.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Total_addressable_market">Total addressable market - Wikipedia</a></li>
<li><a href="https://corporatefinanceinstitute.com/resources/management/total-addressable-market-tam/">Total Addressable Market - Learn How to Calculate the TAM</a></li>
<li><a href="https://hellopm.co/what-is-tam/">TAM ( Total Addressable Market ): Definition , Examples &amp; How to...</a></li>

</ul>
</details>

**Tags**: `#Anthropic`, `#AI`, `#Finance`, `#Revenue`, `#Market`

---

<a id="item-7"></a>
## [Leaked Project Aion: Microsoft&\#x27;s Experimental Copilot-Centric OS](https://www.windowslatest.com/2026/08/24/microsofts-leaked-new-os-is-one-youll-hope-stays-buried-and-its-not-windows/) ⭐️ 6.0/10

Leaked documents reveal Project Aion \(also called Copilot OS\), a 2024 Microsoft experimental system with no start menu or desktop icons, where Copilot handles everything. It is built on a custom Edge browser and a lightweight Windows kernel called Win3, and relies on Windows 365 cloud PCs. This leak showcases Microsoft&\#x27;s internal exploration of an AI-first operating system where Copilot is the central interface, hinting at a possible future direction for Windows. However, because it is unlikely to be released, its immediate impact on users and developers is limited. Project Aion is a 2024 internal prototype, not a shipping product or Windows replacement, and it describes a cross-device &\#x27;agentic OS&\#x27; supporting AOSP and Windows 11, where each conversation generates its own window and icons. Microsoft is already removing some Copilot features from Windows 11, which suggests the project will likely remain buried.

telegram · zaihuapd · Aug 25, 03:41

**Background**: Project Aion uses a lightweight Windows codebase called Win3 and the Edge browser to create an AI-first desktop interface centered on Copilot. The concept of an agentic OS, where an AI assistant manages tasks across devices, is part of a broader industry trend. Windows 365 is a cloud PC service that streams a full Windows experience, which would complement the limited local capabilities of such a system.

<details><summary>References</summary>
<ul>
<li><a href="https://pureinfotech.com/project-aion-microsoft-ai-desktop-leak-explained/">Microsoft ’s leaked Project Aion isn’t Windows 12... - Pureinfotech</a></li>
<li><a href="https://winaero.com/project-aion-an-experimental-microsoft-os-with-a-focus-on-ai/">Project Aion , an experimental Microsoft OS with a focus on AI</a></li>

</ul>
</details>

**Tags**: `#Microsoft`, `#Copilot`, `#Windows`, `#OS leak`, `#experimental`

---

<a id="item-8"></a>
## [Linux Marks 35 Years Since Its First Public Release](https://9to5linux.com/happy-35th-birthday-linux) ⭐️ 6.0/10

On August 25, the Linux community observes the 35th anniversary of Linux&\#x27;s initial public release. 9to5Linux published a commemorative post marking this milestone in operating system history. Linux has grown from a student&\#x27;s hobby project into the world&\#x27;s most widely used operating system kernel, powering Android devices, cloud servers, and supercomputers. This anniversary highlights the enduring impact of open-source collaboration on the technology industry. Linus Torvalds, then a student at the University of Helsinki, first announced Linux in a Usenet post to the comp.os.minix newsgroup on August 25, 1991. He described the project as a free operating system created merely as a hobby, which he said would not be as large or professional as GNU.

telegram · zaihuapd · Aug 25, 07:29

**Background**: Linux is a free and open-source operating system kernel, later distributed under the GNU General Public License, and developed collaboratively by thousands of contributors around the world. It initially served as a Unix-like alternative for personal computers, and today it underpins everything from smartphones and embedded devices to the vast majority of cloud infrastructure and the fastest supercomputers. The August 25 anniversary marks the date of Torvalds&\#x27;s original announcement, which effectively started the Linux project.

**Tags**: `#Linux`, `#anniversary`, `#open source`, `#history`, `#milestone`

---

<a id="item-9"></a>
## [Unitree Stock Slides 45% From IPO Peak, Wiping Out 200 Billion Yuan](https://www.reuters.com/business/finance/china-robot-maker-unitrees-post-listing-slump-sparks-bubble-fears-2026-08-25/) ⭐️ 6.0/10

After surging 629.44% on its STAR Market debut, Chinese humanoid robot maker Unitree&\#x27;s stock fell for three consecutive sessions, dropping about 45% from its first-day peak and erasing roughly 200.8 billion yuan in market value. Founder Wang Xingxing also said at the 2026 World Robot Conference that the &\#x27;ChatGPT moment&\#x27; for embodied AI is still 2-3 years away at best and 5-10 years away at worst. The sharp reversal has fueled concerns about a bubble in China&\#x27;s humanoid robotics sector and raised questions about IPO pricing and retail investor losses. It also provides a notable reality check from a leading founder on how far embodied AI still is from a mainstream breakthrough. Unitree opened at 1,100 yuan on its first day, giving it a market value of 444.9 billion yuan before the subsequent slump. Wang Xingxing acknowledged that embodied AI still faces industry-level challenges with generalization, meaning robots struggle to handle unfamiliar tasks and environments reliably.

telegram · zaihuapd · Aug 25, 12:38

**Background**: Embodied AI refers to the integration of artificial intelligence into physical systems, enabling them to sense and interact with the real world, such as humanoid robots. A &\#x27;ChatGPT moment&\#x27; is a breakthrough where a technology suddenly becomes broadly practical, as ChatGPT did for conversational AI. Generalization — the ability to apply learned skills to new situations — remains one of the biggest technical hurdles for embodied AI. Unitree is a leading Chinese maker of humanoid robots, and its stock listing was seen as a test of investor appetite for robotics companies.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/glossary/embodied-ai/">What is Embodied AI ? | NVIDIA Glossary</a></li>
<li><a href="https://logicity.in/en/blog/unitree-ceo-robots-near-chatgpt-moment-but-2-10-years-out">Unitree CEO: robots near &#x27; ChatGPT moment ,&#x27; but 2-10 years... | Logicit...</a></li>

</ul>
</details>

**Tags**: `#Unitree`, `#humanoid robots`, `#embodied AI`, `#IPO`, `#market sentiment`

---

<a id="item-10"></a>
## [Qwen Teases August 2026 Open-Source Release of Qwen3.8-Flash-Next](https://www.modelscope.cn/models/Qwen/Qwen3.8-Flash-Next) ⭐️ 6.0/10

Qwen posted a teaser page on ModelScope for the upcoming open-source release of Qwen3.8-Flash-Next, a multimodal MoE model, scheduled for August 26, 2026 at 23:00 UTC+8. The release will include both a standard version and an FP8 version, and is positioned as an early look at the next-generation Qwen4 architecture. This release gives the open-source community an early opportunity to explore the architectural changes that will define the upcoming Qwen4 series. Since Qwen models are widely used, this preview could influence developer adoption, fine-tuning practices, and inference stack support well before Qwen4 officially launches. The model is a multimodal Mixture-of-Experts design, and the teaser confirms two release variants: a standard version and an FP8 quantized version. Official release timing is set for August 26, 2026 at 23:00 \(UTC+8\); further technical specifications such as parameter count, context length, and expert configuration have not yet been announced.

telegram · zaihuapd · Aug 25, 12:59

**Background**: Qwen is a family of large language and multimodal models developed by Alibaba, with multiple generations and sizes released both commercially and as open weights. MoE \(Mixture of Experts\) is an architecture that activates only a subset of specialized sub-networks for each input, which improves efficiency and performance compared to dense models that activate all parameters for every token. FP8 is an 8-bit floating-point precision format used to reduce memory footprint and speed up inference, often at a small cost in quality. This teaser indicates that Qwen3.8-Flash-Next is an early preview of the Qwen4 architecture, giving the community a head start in adapting tools and workflows.

<details><summary>References</summary>
<ul>
<li><a href="https://www.youtube.com/watch?v=EM08mb4sqQs">Qwen 4 Is Coming! Qwen3.8 MoE Reveals the Next Architecture</a></li>
<li><a href="https://www.linkedin.com/pulse/mixture-experts-moe-ai-breakthrough-making-large-language-banafa-xk01c">Mixture of Experts ( MoE ): The AI Breakthrough Making Large ...</a></li>
<li><a href="https://qwen-ai.chat/blog/what-is-qwen-ai/">What Is Qwen AI? Owner, Models, Access &amp; Open Weights</a></li>

</ul>
</details>

**Tags**: `#AI`, `#LLM`, `#Qwen`, `#open-source`, `#model architecture`

---

<a id="item-11"></a>
## [Nvidia Unveils Jetson Orin Nano 2, Doubling Edge AI Inference Performance](https://www.therobotreport.com/jetson-orin-nano-2-doubles-inference-performance-robotics-edge-says-nvidia/) ⭐️ 6.0/10

Nvidia announced the Jetson Orin Nano 2 edge computing module on August 25, delivering 78 TOPS and 8 GB of memory. It doubles inference performance compared to the Orin Nano Super while cutting power consumption by 40% at the same performance level. This gives robotics and edge AI developers a significantly faster and more power-efficient entry-level platform for running large models locally. It could accelerate real-time on-device AI applications and broaden Nvidia&\#x27;s robotics ecosystem, which already has over 3 million developers. The module and developer kit are scheduled to launch in the first half of 2027. Nvidia says it can run Cosmos and Qwen 3 large models in real time at the edge, and companies such as Wing and Matic are evaluating or adopting the product.

telegram · zaihuapd · Aug 25, 16:54

**Background**: The Jetson line is Nvidia&\#x27;s family of systems-on-module \(SoMs\) designed for edge AI and robotics applications, and &quot;TOPS&quot; \(trillions of operations per second\) is a common metric for AI inference throughput. Cosmos is Nvidia&\#x27;s platform for generative world foundation models aimed at physical AI, while Qwen 3 is a series of large language models developed by Alibaba that excel in reasoning, coding, and multimodal understanding. These tools help developers build autonomous machines that perceive and interact with the real world.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/ai/cosmos/">Physical AI with World Foundation Models | NVIDIA Cosmos</a></li>
<li><a href="https://www.siliconflow.com/articles/en/the-best-qwen-models-in-2025">Ultimate Guide - The Best Qwen Models in 2026</a></li>
<li><a href="https://huggingface.co/Qwen/Qwen3-0.6B">Qwen / Qwen 3 -0.6B · Hugging Face</a></li>

</ul>
</details>

**Tags**: `#Nvidia`, `#Edge AI`, `#Hardware`, `#Jetson`, `#Robotics`

---