---
layout: default
title: "Horizon Summary: 2026-11-14 (EN)"
date: 2026-11-14 23:03:16 +0000
lang: en
report: ai
---

> From 143 items, 6 important content pieces were selected

---

1. [Researchers allege DeepSeek, Kimi trained on banned Nvidia Blackwell GPUs via new fingerprinting](#item-1) ⭐️ 8.0/10
2. [AI Chatbots Keep Recommending Scam Websites to Shoppers](#item-2) ⭐️ 6.0/10
3. [Taipei Times: World Nearing an Autonomous Weapons Revolution](#item-3) ⭐️ 6.0/10
4. [UN set to debate curbs on AI-powered autonomous weapons](#item-4) ⭐️ 6.0/10
5. [Anthropic Accused of Infringing Neural Network Patents](#item-5) ⭐️ 6.0/10
6. [AI Models Reportedly Predict Alzheimer&\#x27;s Progression Years Before Symptoms](#item-6) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Researchers allege DeepSeek, Kimi trained on banned Nvidia Blackwell GPUs via new fingerprinting](https://news.google.com/rss/articles/CBMi_wJBVV95cUxQR0JoRXdycDVWakNINktZeHpUS1pLN2xxS0p1dVhFODJ1bkpPMEExZG9yb0dGSlRTMkhzbkNVYTlkWXl4OWk4Ujc4dEtJU0stNG5fT2JpdjJHNTRfZUxjSmk3cXEwa0F0YmNsRGtFMml0NWdzSjB4NnBaNS1vMFp4MWhsdDFBUlM4OEd6dlh1MGZBOUloRFlsam11dUh3WHJVSWVUWElwajhZWk9kS1hQbU54U2dlQy1EWHhsa1oyN0pDNElRd0hBdmY5bG1KeFlzSkhKNXg1dkxYNmFBVTJld3M5UkZDbHRsLTU0Y0J5TjFNQlp3Tl9DVnU1d1VTTGV6VGVzaTA2YXlPUGNHNXZIMXlsQ0xLVGtycVBzQzB4RHNHRDkzY08wMDJUcmtKb29TU1NuaktQYkw4WEJJNndJQVdPbU1WVC1WT3RudVJXM3VDM3Mwd3N5THZEcnBvOVBvZXE5UV9IbzhSbGM1Z2djcGI0Ym9hS0xjUHZQZ09lQQ?oc=5) ⭐️ 8.0/10

Researchers used a new GPU &quot;fingerprinting&quot; technique that analyzes published open model weights to identify the GPUs used during training, and report finding traces of Blackwell-generation hardware in six models from four Chinese organizations, including DeepSeek V4, Kimi K3 and MiniMax M3. Because Blackwell GPUs are banned from export to China or Chinese-owned firms, the findings have been framed as evidence that export controls were circumvented. If the technique holds up, it gives regulators and auditors a hardware-provenance tool that works on open-weight models alone, potentially reshaping how AI compute governance and export controls are enforced. It also puts major Chinese labs such as DeepSeek and Moonshot AI under scrutiny and could trigger tighter rules around remote access to restricted compute. The method reportedly infers the initialization GPUs from statistical signatures and SM-count-related traits left in model weights, achieving up to 100% re-identification accuracy only in small-scale tests; the researchers themselves note the findings do not prove export-control violations, since chips could have been accessed via overseas or remote servers.

google\_news · Tom&\#x27;s Hardware · Nov 14, 14:50

**Background**: Blackwell is Nvidia&\#x27;s current high-end data-center GPU family, and Washington bans its export to China and Chinese-owned companies on national-security grounds, permitting only weaker chips like the H200 under certain conditions. Demand has pushed banned Blackwell parts onto Chinese black markets at roughly double their normal price. &quot;GPU fingerprinting&quot; is an emerging research area that identifies individual accelerators from hardware-level characteristics rather than software keys, and this work applies that idea to model weights so that a released open model can be audited for the hardware that trained it.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.01930">[2605.01930] GPU Fingerprinting for Location Verification Researchers allege DeepSeek, Kimi, and other Chinese AI ... Blackwell GPU Fingerprints in DeepSeek &amp; Kimi Weights (2026 ... GPU Fingerprints in AI Model Weights Reveal Blackwell Traces ... GPU Fingerprinting for Location Verification | OpenReview</a></li>
<li><a href="https://techcrunch.com/2026/11/13/export-banned-nvidia-chips-are-behind-chinas-most-powerful-ai-models-uh-oh-jensen/">Export-banned Nvidia chips are behind China&#x27;s most powerful ...</a></li>
<li><a href="https://wccftech.com/china-fails-to-stop-tech-firms-from-using-nvidia-chips-banned-blackwell-gpus-hit-2x-price-on-black-market/">China Fails To Stop Tech Firms From Using NVIDIA Chips, As ...</a></li>

</ul>
</details>

**Tags**: `#AI regulation`, `#GPU fingerprinting`, `#Nvidia Blackwell`, `#DeepSeek`, `#China AI`

---

<a id="item-2"></a>
## [AI Chatbots Keep Recommending Scam Websites to Shoppers](https://news.google.com/rss/articles/CBMie0FVX3lxTE5aSHlZX2RZQmFWSnF1S25wUHlTb1ZvdURmZ3VMcjV4b3kzRE1oVW4wRHdLVmR5QzN4Umx1a1pwbXRxc3dpTE9fUkxlUFk1WTRHRVdiUE82N2RsYkJFaGM3ZEZzN1dBUmNOc3pWZ2hzTUt4YWJpdnVmemg5TQ?oc=5) ⭐️ 6.0/10

Futurism reported that consumer-facing AI chatbots continue to recommend scam websites to people asking for shopping advice, even as these assistants are increasingly used as product-research tools. The report frames this as a recurring, unresolved failure rather than a one-off glitch, with no indication that the problem has been fixed. Consumers increasingly treat chatbots as a substitute for search engines when deciding what to buy, so a recommendation carries implicit trust that scammers can exploit for fraud and financial loss. This exposes a real trust-and-safety gap in deployed LLM products and puts pressure on vendors to add link vetting and clearer warnings. The item is a headline-level news link with no published methodology, so it is unclear which chatbots were tested, how many prompts were used, or how the scam sites were identified. The underlying failure mode is well known: models generate plausible-sounding links from training data and pattern matching rather than verifying that a domain is legitimate or currently active.

google\_news · Futurism · Nov 14, 18:02

**Background**: Large language models generate text by predicting likely continuations rather than looking up verified facts, so a URL they produce can look convincing while pointing to a dead or malicious domain. Shopping-related queries are a popular target for scammers because purchase intent makes people more likely to click and enter payment details. Retrieval-augmented generation and real-time web grounding can reduce the risk, but only if the vendor applies reputation checks and filters to the links returned.

**Tags**: `#AI Safety`, `#LLM Reliability`, `#Chatbots`, `#Consumer Protection`, `#E-commerce`

---

<a id="item-3"></a>
## [Taipei Times: World Nearing an Autonomous Weapons Revolution](https://news.google.com/rss/articles/CBMieEFVX3lxTE5UbDUxN0dlazNyUXZWakZ5OGVSRTFWMGhpbkd0NTRUWE84aFdRbFU2aF9CVzJ6ZzBmQkZwX2lobUoyU1RRS19LOXV4REtXcnk2SWUyUFJCbks5WWV4bWxIcnZ4cWZFRUQ1WURmZ3BqYnVRVDA4TVFETA?oc=5) ⭐️ 6.0/10

The Taipei Times published a headline article arguing that the world is on the cusp of an autonomous weapons revolution, framing lethal autonomous weapon systems \(LAWS\) as an emerging military-technological shift rather than a distant prospect. No article body, technical specifications, or specific program names were available in the supplied material, so the claim rests on the headline framing alone. Autonomous weapons sit at the intersection of military AI, international humanitarian law, and arms control, so any perceived acceleration toward fielding them affects defense procurement, ethical debates, and ongoing UN talks on regulating LAWS. If the shift is real, it would reshape how states conduct targeting decisions and how much human judgment remains in the kill chain. LAWS are typically defined as systems that use sensor suites and computer algorithms to identify and engage targets without manual human control, which is precisely what makes the &\#x27;human-in-the-loop&\#x27; safeguard so contested. Public reporting on autonomy levels is difficult to verify, and the current regulatory discussion is anchored in draft texts at the UN GGE on LAWS rather than any binding treaty.

google\_news · Taipei Times · Nov 14, 16:00

**Background**: Lethal autonomous weapon systems \(LAWS\) are a class of weapons that can select and engage targets using onboard sensors and algorithms, without a human operator manually controlling each engagement. International Humanitarian Law requires distinctions between combatants and civilians and proportional use of force, which critics argue algorithms cannot reliably guarantee. The UN has convened a Group of Governmental Experts \(GGE\) on LAWS for years, and the ICRC has circulated draft regulatory text, but no binding international agreement exists. The &\#x27;human-in-the-loop&\#x27; concept has long been promoted as a safeguard, though the war in Ukraine has prompted analysts to question whether it is practical under real battlefield conditions.

<details><summary>References</summary>
<ul>
<li><a href="https://www.congress.gov/crs_external_products/IF/HTML/IF11150.web.html">Defense Primer: U.S. Policy on Lethal Autonomous Weapon Systems</a></li>
<li><a href="https://www.icrc.org/sites/default/files/2026-08/ICRC_working_paper_GGE_LAWS_August-2026-ICRC.pdf">ICRC_working_paper_GGE_LAWS_August-2026-ICRC</a></li>
<li><a href="https://www.foresightnavigator.com/p/rethinking-human-in-the-loop-in-modern">Rethinking &quot;Human in the Loop&quot; in Modern Warfare</a></li>

</ul>
</details>

**Tags**: `#autonomous weapons`, `#military AI`, `#AI ethics`, `#defense technology`, `#policy`

---

<a id="item-4"></a>
## [UN set to debate curbs on AI-powered autonomous weapons](https://news.google.com/rss/articles/CBMisgFBVV95cUxOcloza1U3a1BwWGxhREpyVnVOVHhmQ2lURlA2Q0pUekUtd3VPOTRza2k3b3dYc010eWt1cW5NUXQ1ck5ybUdrbDRnUXR0R21PWnY1QnJxWWhWbEUzU3NmSnliLWF0X290alpKZkZPQVBhdWtzTGpPaXhFTnJoQVpETHVrZ2xXM2ZjNVB4YjZCQ1BVOVVscHNNX20zTzlCbnI5Z0JGYzVTMGZEMG9DZTVtQjVB0gG3AUFVX3lxTFBaanBpUmhROS1KSExhaHBUZUpvU2hlQU53ZDEyb0V2WXktUDdoQ3lpTDlpMnhCVTNPOTRCRWN5aUJ4OHZ4UzJXWG9KbjhxTk1haERldjAxT0Q3Zno1NnExVFlPR1dkVWdCZlhsRzhZT1lxNVgwdWdKX0tHakxCZmY3Ym8wWnlWTGVpRnllYjVNWXFMbDJ6amZHUFBDd0pMcjRVNXF1ZGpOaDJGY0hVRlNPWExEV2YwMA?oc=5) ⭐️ 6.0/10

According to Ukraine&\#x27;s state news agency Ukrinform, the United Nations is reportedly set to hold discussions on restricting AI-powered autonomous weapons, keeping the issue on the international policy agenda. The report is a headline-level item and does not yet specify which UN body, session date, or concrete proposals are involved. If meaningful restrictions advance, they would directly shape how states and defense contractors can develop and deploy AI-enabled targeting systems, affecting military procurement and AI governance norms worldwide. Even without a binding treaty, UN-level debate sets the vocabulary and expectations that national regulators and AI labs will eventually be measured against. The term of art in these negotiations is lethal autonomous weapons systems \(LAWS\), meaning weapons that can search for and engage targets based on programmed constraints without human intervention; as of 2025 most military drones and robots still require human control and are not truly autonomous. A central fault line is whether any agreement should be a legally binding treaty or a non-binding set of political commitments, and major military AI powers have historically resisted binding limits.

google\_news · Ukrinform · Nov 14, 21:27

**Background**: Lethal autonomous weapons systems \(LAWS\) — often called &quot;killer robots&quot; — are military drones, robots or uncrewed vehicles that can independently search for and engage targets based on programmed constraints and descriptions, rather than being steered by a human operator. They come in several forms, including unmanned aerial vehicles \(UAVs\), unmanned underwater vehicles \(UUVs\) and unmanned ground vehicles \(UGVs\), though most alleged examples today are aerial. Because such systems raise unresolved questions about accountability when a machine selects a human target, the topic has been debated for years in UN disarmament forums in Geneva, and the current discussion is another round in that long-running process rather than a new initiative.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Lethal_autonomous_weapons_systems">Lethal autonomous weapons systems</a></li>
<li><a href="https://fsi.stanford.edu/sipr/content/lethal-autonomous-weapons-next-frontier-international-security-and-arms-control">Lethal Autonomous Weapons: The Next Frontier in International ...</a></li>

</ul>
</details>

**Tags**: `#AI governance`, `#autonomous weapons`, `#UN policy`, `#AI ethics`, `#military AI`

---

<a id="item-5"></a>
## [Anthropic Accused of Infringing Neural Network Patents](https://news.google.com/rss/articles/CBMi_AFBVV95cUxQa09ZQllGRFA4eTctdzhDMFk4VmkxeGhZcTNpcWQ5SXhSVU83akhfT3lTMDZoMG00U3NTNHl4amhsTjBTYjhmbi1hZGtVZF8xSTFqZ29aZE02WEZvcXpzbW9Zb2s0azROS25sZHpCUlNGbFQ5WHhBRlpja3ZwcktkREZmMDNFbGVDcnlvdHdkeTNFRVV6N21rc3hlQTJUSUk1WFFiM1FidlRfT2RpWVByR2ZYN2lUVU1EUXB1R0JGQkdWaWRzQXFhaERnaTljZDN3QUN0V05WOWtnbkl2ZElqYTAtcVE5TU5NaGItcEctQ0x0SnhBUnBuU2tUdUw?oc=5) ⭐️ 6.0/10

A VitalLaw.com patent news report states that Anthropic&\#x27;s AI systems are accused of infringing neural network patents, though the available excerpt provides only the headline and no further details on the plaintiff, patents, or filing venue. If the claim proceeds, it would add to growing intellectual-property friction around generative AI, where patent holders are testing whether neural network training and inference methods fall within existing claims. The excerpt does not name the plaintiff, identify the patents-in-suit, or specify the court, so the scope and strength of the allegations cannot yet be assessed.

google\_news · VitalLaw.com · Nov 13, 23:03

**Background**: Neural networks are the core computational architecture behind modern machine learning, and patents in this area can cover training techniques, model architectures, and inference methods. Patent disputes in AI have been growing as companies seek to monetize early inventions and defend commercial products. Anthropic is an AI company whose systems are the subject of the accusation; the report, however, provides no information about the specific patents or legal claims involved.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Anthropic">Anthropic - Wikipedia</a></li>
<li><a href="https://patents.google.com/patent/US20210019618A1/en">US20210019618A1 - Neural Network Processor - Google Patents</a></li>
<li><a href="https://patents.justia.com/patents-by-us-classification/706/15">Neural Network Patents (Class 706/15)</a></li>

</ul>
</details>

**Tags**: `#AI patents`, `#Anthropic`, `#litigation`, `#intellectual property`, `#neural networks`

---

<a id="item-6"></a>
## [AI Models Reportedly Predict Alzheimer&\#x27;s Progression Years Before Symptoms](https://news.google.com/rss/articles/CBMiwgFBVV95cUxPTTdOQjdpalh3dThBa2c0Um5PVElVbnFmTGNGaGxNQjdVenlKbzFoQzJRTUJCVXg3S0hBNEh5ekNoMlNJRW9YN2N6eUZiU1pUNHo1dGx6d0NjUmpzcEFDWnRldXJlVGVYVDBmZ3FnY3RYY0xVV1FQUWFGcUhnb0tObVpLQUs5UHo0RTNVOXllMjByWHRaMUx1enRSN0ZncWV2RC05SGtBQzBjT0xtZkdwUG1aWk1UVjRSWG1aQUVWQkVVQQ?oc=5) ⭐️ 6.0/10

Bioengineer.org published a headline stating that artificial intelligence models can predict the progression of Alzheimer&\#x27;s disease years before clinical symptoms emerge. However, the item as circulated is essentially a headline and link, with no information on the study&\#x27;s authors, model architecture, dataset size, prediction horizon, or validation results. If the underlying work holds up, reliable early prediction would widen the window for intervention, since Alzheimer&\#x27;s pathology begins accumulating in the brain years or even decades before memory loss becomes apparent. It could also sharpen patient selection for clinical trials and help distinguish those with mild cognitive impairment who will convert to dementia from those who will not. Because only the headline is available, key specifics such as the model type, the training cohort, the reported accuracy or AUC, and whether predictions were validated in an independent external cohort cannot be confirmed. The claim itself sits within an active research area where deep learning models trained on multimodal data, typically MRI, PET and cerebrospinal fluid or blood biomarkers, are used to forecast conversion from mild cognitive impairment to Alzheimer&\#x27;s dementia.

google\_news · Bioengineer.org · Nov 14, 01:37

**Background**: Alzheimer&\#x27;s disease is a progressive neurodegenerative disorder and the leading cause of dementia, and today diagnosis still largely rests on clinical symptoms that appear only after substantial brain damage has occurred. The intermediate stage known as mild cognitive impairment \(MCI\) is often treated as prodromal Alzheimer&\#x27;s, but not everyone with MCI progresses to dementia, which makes conversion prediction a central goal. Much of this research relies on datasets such as the Alzheimer&\#x27;s Disease Neuroimaging Initiative \(ADNI\), which pairs neuroimaging with biomarkers like amyloid and tau, and machine learning models are trained to detect patterns that precede overt symptoms.

<details><summary>References</summary>
<ul>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC13275144/">Use of Artificial Intelligence for the Early Detection and Prediction of...</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC11353639/">Early Alzheimer’s Disease Detection: A Review of Machine ...</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S1568163726003648">Predicting conversion from mild cognitive impairment to ...</a></li>

</ul>
</details>

**Tags**: `#AI in healthcare`, `#Alzheimer&\#x27;s disease`, `#medical AI`, `#predictive modeling`, `#biomedical research`

---