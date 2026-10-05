---
layout: default
title: "Horizon Summary: 2026-10-05 (EN)"
date: 2026-10-05 23:03:46 +0000
lang: en
report: ai
---

> From 159 items, 9 important content pieces were selected

---

1. [Qwen3.8 27B scores 23.6% on addition-in-words test](#item-1) ⭐️ 7.0/10
2. [RAND Report Explores AI Loss of Control Across Five Scenarios](#item-2) ⭐️ 7.0/10
3. [War on the Rocks: AI in the Kill Chain Risks a Strategic Own Goal](#item-3) ⭐️ 7.0/10
4. [Nvidia-backed Reflection unveils first AI model to compete with Chinese open models](#item-4) ⭐️ 6.0/10
5. [New York City Council Holds Landmark AI Oversight Hearing](#item-5) ⭐️ 6.0/10
6. [The Lancet Examines How AI Meets Evidence-Based Medicine](#item-6) ⭐️ 6.0/10
7. [Trump Announces &\#x27;Super Intelligence Force&\#x27; for AI Oversight](#item-7) ⭐️ 6.0/10
8. [Microsoft and Meta Push Staff Away From Anthropic&\#x27;s Claude Toward In-House AI](#item-8) ⭐️ 6.0/10
9. [Engineering Concerns About Anthropic&\#x27;s Invisible Watermarking](#item-9) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Qwen3.8 27B scores 23.6% on addition-in-words test](https://simonwillison.net/2026/Oct/4/qwen38-addition-in-words/) ⭐️ 7.0/10

Simon Willison re-ran an experiment first posted by Colin Frasier on Bluesky, testing whether LLMs can compute a sum and return the answer only in words rather than digits. Using Qwen3.8-27B-Q4\_K\_M.gguf on a local DGX Spark with reasoning disabled, the model answered just 1,195 of 5,070 prompts correctly — an overall numeric accuracy of 23.57%, far below the earlier GPT-4o results. The result shows that even a recent, well-regarded open-weight mid-size model collapses on multi-digit arithmetic when it is forced to express the answer in words, a task that removes the easy numeric-token path. It gives practitioners a reproducible, fully local benchmark angle for judging whether a model can be trusted with numeric reasoning without tool use or a calculator. Accuracy degraded sharply with operand length: Qwen3.8 27B was near 100% for single-digit operands but dropped to roughly 0% once both numbers reached ten or more digits, while GPT-4o&\#x27;s original chart retained strong scores in several large-digit cells. The run used 30 fixed pairs per ordered digit-length cell \(n = 5,070\), a colorblind-safe orange-to-blue heatmap, and a quantized Q4\_K\_M build with thinking disabled, so the numbers reflect a deliberately constrained setup rather than the model&\#x27;s best-case configuration.

rss · Simon Willison · Oct 4, 23:34

**Background**: Large language models do not perform arithmetic natively; they predict tokens, so multi-digit addition is handled through learned patterns rather than a real calculation step. Forcing the model to spell the answer out in words removes the convenient digit tokens and exposes how fragile that learned arithmetic really is. Qwen3.8 27B is Alibaba&\#x27;s open-weight mid-size model covering coding, reasoning and multimodal tasks, and the DGX Spark is a compact local AI machine used here to keep the experiment fully controlled and reproducible.

<details><summary>References</summary>
<ul>
<li><a href="https://www.university-365.com/post/qwen3-8-27b-alibaba-s-open-weight-mid-size-model">Qwen 3 . 8 27 B : Alibaba&#x27;s Open-Weight Mid-Size Model</a></li>
<li><a href="https://nano-gpt.com/models/text/qwen/qwen3.8-27b">Qwen 3 . 8 27 B model | NanoGPT</a></li>
<li><a href="https://stanford-cs324.github.io/winter2022/lectures/capabilities/">Understanding and developing large language models .</a></li>

</ul>
</details>

**Tags**: `#LLM evaluation`, `#arithmetic`, `#benchmarking`, `#Qwen`, `#GPT-4o`

---

<a id="item-2"></a>
## [RAND Report Explores AI Loss of Control Across Five Scenarios](https://news.google.com/rss/articles/CBMiaEFVX3lxTE90RXM2UDdrT3dvbE5oUl9pcGJETU5wWjR4ZkVaV25LVGpQdXc5T2VVbGc3T1luaWNXVnpySl9vXzlYeGUtem1neS1KS2ZMdW5QZ3VpNnlWYVJBUXhBSFkzVUVFa0x2TXRN?oc=5) ⭐️ 7.0/10

RAND, the nonprofit policy research organization, published a research report titled &quot;Infinite Potential—Insights on Artificial Intelligence Loss of Control Across Five Scenarios,&quot; which analyzes observations from structured &quot;Infinite Potential&quot; games involving AI loss of control to surface key issues, capabilities, and recommendations. The report frames loss of control as potential collapses of social legitimacy, economic stability, and technical control. As increasingly capable and autonomous AI systems are deployed, understanding how loss of control could unfold is central to AI safety and governance debates, and this report feeds directly into policy discussions where governments and standards bodies are building risk frameworks. It gives researchers and decision-makers a scenario-based vocabulary for anticipating failures that conventional, narrow risk assessments may miss. The report draws on the &quot;Infinite Potential&quot; games, a scenario-exercise format used to explore AI loss of control, and its scope spans social, economic, and technical dimensions rather than focusing only on engineering failures. In related safety literature, loss of control is typically defined as scenarios in which one or more general-purpose AI systems operate outside anyone&\#x27;s control and regaining control is extremely costly or impossible.

google\_news · RAND.org · Oct 5, 13:17

**Background**: RAND is a decades-old nonprofit, nonpartisan research organization that advises governments on policy, and it has increasingly turned its attention to AI risk. &quot;Loss of control&quot; is a specific term of art in AI safety: organizations such as Apollo Research have published taxonomies defining what it means and its different degrees, distinguishing it from ordinary bugs or misuse. This report sits alongside other governance efforts, such as the NIST AI Risk Management Framework, which encourages organizations to identify, classify, and mitigate risks across the AI lifecycle.

<details><summary>References</summary>
<ul>
<li><a href="https://www.rand.org/pubs/research_reports/RRA4767-3.html">Infinite Potential—Insights On Artificial Intelligence Loss of ... | RAND</a></li>
<li><a href="https://lossofcontrol.ai/chapter1">Chapter 1: A Taxonomy of Loss of Control | Apollo Research</a></li>
<li><a href="https://www.nist.gov/itl/ai-risk-management-framework">AI Risk Management Framework | NIST</a></li>

</ul>
</details>

**Tags**: `#AI Safety`, `#Loss of Control`, `#RAND`, `#AI Governance`, `#Risk Assessment`

---

<a id="item-3"></a>
## [War on the Rocks: AI in the Kill Chain Risks a Strategic Own Goal](https://news.google.com/rss/articles/CBMilgFBVV95cUxNdnByMUhsR0VkWFdmY0JCUkEta0FTUEpqMGxRcW53UnNIby1GQ1U3N3RnZTVWNlR3eUpEaUxTODBQaFlPd1BlQmhHSEJYNm1Sa2pkc0N4TkFjeG54d05EaTJWeWdGNjhWREhTLXVKVUxXanJNQXVTcUtOVXljbzRra0FJM3FVTF9DVVd6cVppWlhoMWR1SXc?oc=5) ⭐️ 7.0/10

War on the Rocks has published an analysis arguing that the race to automate the military &quot;kill chain&quot; with AI risks becoming a strategic own goal disguised as a tactical capability gain if Western militaries fail to implement it in line with their own values. Rather than treating AI-assisted targeting as a purely technical upgrade, the piece frames the speed-up of the sensor-to-shooter process as a values and legitimacy problem. As the Pentagon and allied militaries push to use AI to accelerate military decision-making, this analysis warns that battlefield and legal failures could cost more strategically than the speed gains are worth. It matters to defense policymakers, commanders, and AI vendors because it ties the technical design of targeting systems directly to public legitimacy, alliance cohesion, and long-term deterrence. The argument centers on process rather than algorithms: critics cited in related reporting note that a human &quot;approval button&quot; alone does not demonstrate meaningful control when AI compresses targeting timelines beyond what humans can realistically authenticate. Recent accounts of an AI-assisted kill chain linked to a strike in Iran likewise stress an interaction of flawed intelligence, automated data processing, and human decision-making, with the exact role of systems such as Maven remaining contested.

google\_news · War on the Rocks · Oct 5, 15:25

**Background**: The &quot;kill chain&quot; is a long-standing military concept, dating back to World War II, that describes the structure of an attack as a sequence of steps — typically find, fix, track, target, engage, and assess — used to decide which targets to strike and how. Modern militaries want to compress that sequence with AI so sensors and shooters can react faster than an adversary. The debate is whether speeding up that chain without commensurate human judgment and legal review trades short-term tactical advantage for long-term strategic harm.

<details><summary>References</summary>
<ul>
<li><a href="https://warontherocks.com/cogs-of-war/the-ai-assisted-strategic-own-goal-in-the-kill-chain/">The AI -Assisted Strategic Own Goal in the Kill Chain</a></li>
<li><a href="https://en.wikipedia.org/wiki/Kill_chain_%28military%29">Kill chain ( military ) - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI`, `#military`, `#kill chain`, `#national security`, `#strategy`

---

<a id="item-4"></a>
## [Nvidia-backed Reflection unveils first AI model to compete with Chinese open models](https://news.google.com/rss/articles/CBMiuwFBVV95cUxNQ2FQR2h6dGd0eThzSjRKNENDQV9YMnpIZlVfWTNVV2tlSTEzZDJyU09MZ2s1Sk9lWVRESzdwQmdfQjlsRzZPVmJuUzRLQkp5UXhVUHpia2pZWHVfRmQyR21COWx2dGZxR0pzUmxvT3RUUDVhX1JRWm1LQXRfVmV5bGpIMFYtRHFoNW1UMlV3Q3h5X19QaVAxMnJ1SkxrU0pKVnJYcW9LNTNENVJldFc1VTNoRHdRRmNkVFM4?oc=5) ⭐️ 6.0/10

Reflection AI, a startup backed by Nvidia, has unveiled its first AI model, which is aimed at competing with Chinese open models, according to Reuters. The announcement marks the company&\#x27;s entry into the competitive AI model space. This development highlights the growing competition between U.S. and Chinese AI firms in the open model arena, potentially influencing the global AI ecosystem and open-source AI development. It also underscores Nvidia&\#x27;s strategic investments in AI startups to counter Chinese open-source models. The model&\#x27;s name, architecture, size, and performance benchmarks have not been disclosed in the Reuters headline. Reflection AI was founded in 2024 by former Google DeepMind researchers Misha Laskin and Ioannis Antonoglou, and is reportedly in talks to raise $2.5 billion at a $25 billion valuation.

google\_news · Reuters · Oct 5, 20:54

**Background**: Reflection AI is an American AI startup founded in 2024 by former DeepMind researchers. It has received backing from Nvidia. Chinese open models, such as those from DeepSeek and Alibaba&\#x27;s Qwen, have gained global attention for their strong performance and open availability. Open models are AI systems whose weights or code are publicly released, allowing anyone to use or modify them.

<details><summary>References</summary>
<ul>
<li><a href="https://www.norgardx.com/company/reflection.ai">Reflection AI — NorgardX</a></li>
<li><a href="https://stockanalysis.com/private/reflection-ai/">Reflection AI Stock Price, Valuation &amp; News</a></li>

</ul>
</details>

**Tags**: `#AI models`, `#open models`, `#Nvidia`, `#startups`, `#Reuters`

---

<a id="item-5"></a>
## [New York City Council Holds Landmark AI Oversight Hearing](https://news.google.com/rss/articles/CBMihwFBVV95cUxOUEVTZmRJb1dHTFZ3MVFHdGt5ZUlBNks4ak0tT3pfTnNFb3M3TmUxVlZqaDBJdnQ0WTA4TDRURjVGMEhtcy04V05ZX2FLWS1rdWpUU080S0Qwd053OF9kMDFrOU1lbVBQcjRnczVRa1RYTjNUWkVNc2MtWmVhM1Biam9JU004Vmc?oc=5) ⭐️ 6.0/10

The New York City Council held what CBS News described as a landmark hearing on AI oversight, signalling a significant step in municipal-level regulation of artificial intelligence. The item is reported as a headline only, with no accompanying article body detailing the bills, witnesses or testimony involved. Cities are where AI actually touches people — hiring screens, policing tools, benefits eligibility, housing and permits — so municipal oversight can shape real-world deployment faster than slower-moving federal rules. Because New York City has often set the template that other US cities copy on tech policy, its hearings and ordinances tend to ripple outward to other municipalities and to vendors selling AI tools to government. The source provides only a headline, so no bill numbers, vote outcomes, named witnesses or specific proposed requirements are available from this item. It is also worth noting that a hearing itself creates no binding obligation: any new rules would still require actual legislation followed by agency rulemaking and enforcement by the relevant city bodies.

google\_news · CBS News · Oct 5, 17:05

**Background**: New York City is among the earliest US municipalities to write concrete AI rules. Local Law 144, which took effect in 2023, requires annual bias audits and candidate notification for automated employment decision tools used in hiring, while earlier legislation required city agencies to report on the automated decision systems they use. Cities generally lack the authority to regulate AI the way federal or state governments do, but they exercise substantial power through procurement contracts, local employment law and their own use of algorithmic tools in public services.

**Tags**: `#AI regulation`, `#AI policy`, `#AI governance`, `#NYC`, `#technology oversight`

---

<a id="item-6"></a>
## [The Lancet Examines How AI Meets Evidence-Based Medicine](https://news.google.com/rss/articles/CBMirgFBVV95cUxPRjRjNzY5S1U0YXQ5OXlTaUpabnFwYnd2azd4NlpReEswVHBEQXFWMVlqalRQeS1CNU0zYU9SX24zcFMwbG9qdmVabllxMUxJbkgyTlR3VnlIR3NUUThPajdwS3RCSUUxZm53dEhDLVlJQ1J4ZjJsNUhkektNeDFCWGJReHBLaFpIaE5mZHdiVU02dW1wU2NRT3B3LURoRzBobGZsbGU3UE9XbDZoekE?oc=5) ⭐️ 6.0/10

The Lancet has published a piece titled &quot;When evidence meets artificial intelligence,&quot; which examines the intersection of evidence-based medicine and AI-driven tools in clinical care. Only the headline and link were available from the feed, so the article&\#x27;s specific arguments, authors, and data could not be verified from the provided material. The Lancet is one of the world&\#x27;s most influential general medical journals, so its framing of AI within evidence-based medicine can shape how clinicians, regulators, and health systems judge when AI tools are trustworthy enough for patient care. As AI models proliferate in diagnostics and clinical decision support, the question of what counts as acceptable evidence for their approval is becoming a central policy battleground. A key tension the topic raises is that evidence-based medicine ranks study designs in a hierarchy — randomized controlled trials and systematic reviews at the top — while many AI models are trained and validated retrospectively on large datasets and can drift as data distributions change. Only the title and URL were accessible here, so this remains contextual framing rather than a summary of the article&\#x27;s own claims.

google\_news · The Lancet · Oct 5, 11:41

**Background**: Evidence-based medicine \(EBM\) is an approach in which clinicians combine the best available research evidence with their own expertise and the patient&\#x27;s values and preferences when making care decisions; it emerged as a formal movement in the 1990s. Artificial intelligence in medicine typically refers to machine learning systems that learn patterns from clinical data to support tasks such as diagnosis, risk prediction, or imaging interpretation. The friction between the two is structural: EBM was built around controlled trials and explicit evidence hierarchies, whereas many AI tools are developed through retrospective data-driven training and continuous updating.

<details><summary>References</summary>
<ul>
<li><a href="https://www.researchgate.net/publication/274042607_Evidence_Based_Medicine">(PDF) Evidence Based Medicine</a></li>
<li><a href="https://www.openaccessjournals.com/articles/the-power-of-evidencebased-medicine-advancing-healthcare-through-science-16448.html">The Power of Evidence - Based Medicine Advancing Healthcare through</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Healthcare`, `#Evidence-Based Medicine`, `#Medical AI`, `#The Lancet`

---

<a id="item-7"></a>
## [Trump Announces &\#x27;Super Intelligence Force&\#x27; for AI Oversight](https://news.google.com/rss/articles/CBMiiwFBVV95cUxQSnNjZGNSR1otY0JLdHBCbTdsY2xTTnl5dWtUajZmUkYyajVnRkpKTmRqc2VYTDM1bE53LVAydDdMTnNXRTJ3TWVoTExrOUxWWXpVTUl5MWhYd0FYSW9NcFNuZDNQai1IdlZIS2ozUGFfRUhMdGVDWmppc1BTM0tDNHRxZWtyMXA1SFFZ0gGQAUFVX3lxTE5GNTh3VlRJRF83YWNaMDRhaWQwcmlVaksxN0JpdUVsTDhQd2E4c29nUmw5YktjMWI2Njg2TkNncTI4Q0N3SnlEMmdsMTFyQkJzUWhNVXVZZk94em43Qlo1M2o4SzBVc1UxN1doVjV6QVNvSDdmdzFnSWNTdW9nOF9lZ25MYkMwbHUxTkl4ODJhcw?oc=5) ⭐️ 6.0/10

According to a NewsNation report, US President Donald Trump announced the creation of a new body called the &\#x27;Super Intelligence Force&\#x27; that would be responsible for overseeing artificial intelligence. The available report provides no further detail on the group&\#x27;s mandate, membership, legal authority, or timeline. Any new federal body dedicated to AI oversight signals how the current US administration intends to shape AI governance, which directly affects AI developers, cloud providers, and enterprises deploying models in the United States. Because Washington&\#x27;s approach to AI rules is closely watched globally, the announcement could influence regulatory thinking in the EU, UK, and other markets. The report offers no concrete information about the force&\#x27;s structure, budget, enforcement powers, or whether it is a new agency, a task force, or an advisory body. Without an executive order text or official White House statement, key questions about how it would interact with existing agencies such as the FTC, NIST, and the Commerce Department remain unanswered.

google\_news · NewsNation · Oct 5, 17:42

**Background**: AI oversight in the United States has been in flux: the Biden administration&\#x27;s 2023 executive order on AI was rescinded after Trump took office, and the current White House has instead emphasized an AI Action Plan aimed at speeding up development and reducing regulatory barriers. Against that backdrop, a body focused on &\#x27;super intelligence&\#x27; signals attention to frontier or highly capable AI systems rather than only consumer-facing AI applications. The term &\#x27;superintelligence&\#x27; generally refers to hypothetical AI systems that surpass human cognitive performance across most domains, and it is often raised in policy debates about long-term safety and control.

**Tags**: `#AI policy`, `#AI governance`, `#regulation`, `#Trump administration`, `#news`

---

<a id="item-8"></a>
## [Microsoft and Meta Push Staff Away From Anthropic&\#x27;s Claude Toward In-House AI](https://news.google.com/rss/articles/CBMiugFBVV95cUxNRG5VX3ZDVEZPNVFaYzBXaEh4N2hDWmdLRF9vNkVPRXl4NUZCaXVQNmFyRGZlVkFEVXQ4TGdEVmczcFZndGRTc3F0ZVhaMDZZa2JEeDE4S1EtOTAxZzdqWlNHXzF1SngzOGFURDkwVnVLQ2ViVXlQdmp2VVo2Q0dnWkxvRl9oN216eEJSV3Vva0l1cUItb0p1TUcxcUd5a0hDX255ZVU5c2ZBNWtVamk2SkpZMGswOWhnYUE?oc=5) ⭐️ 6.0/10

According to a PYMNTS.com report, Microsoft and Meta are reportedly steering their employees away from Anthropic&\#x27;s Claude and toward their own internally developed AI models. The shift is presented as a deliberate move by both companies to favor in-house tooling over a third-party frontier model. If major platform owners redirect their own workforces to in-house models, it reduces Anthropic&\#x27;s distribution reach inside two of the largest enterprise software ecosystems and signals that big tech increasingly sees frontier model access as a self-sufficiency question rather than a buy-versus-build one. This intensifies competition in enterprise AI, where model quality matters less than being embedded in the tools employees already use. The item is only a headline and RSS link with no article body, so the scope, timing, and whether these are formal mandates or informal guidance remain unverified. It also does not specify which internal models are being promoted, though Microsoft has been rolling out its in-house MAI model family and Meta has its own models such as Muse Image.

google\_news · PYMNTS.com · Oct 5, 22:00

**Background**: Claude is a family of large language models built by Anthropic, first released as a chatbot in March 2023 and offered in tiers named Haiku, Sonnet, and Opus since Claude 3. Microsoft had long relied on OpenAI&\#x27;s models to power its Copilot assistant, and has more recently launched its own MAI-branded in-house models, while Meta has built models such as Muse Image through Meta Superintelligence Labs. In enterprise AI, the choice of which model backs a product is often determined less by benchmark scores than by cost, data control, latency, and strategic independence from partners or competitors.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Anthropic_Claude">Anthropic Claude</a></li>
<li><a href="https://www.theverge.com/news/767809/microsoft-in-house-ai-models-launch-openai">Microsoft AI launches its first in - house models | The Verge</a></li>
<li><a href="https://promptslove.com/free-tools/meta-muse-image-prompt-generator/">Free Meta Muse Image Prompt Generator (2026) | Promptslove</a></li>

</ul>
</details>

**Tags**: `#AI Industry`, `#Enterprise AI`, `#Microsoft`, `#Meta`, `#Anthropic`

---

<a id="item-9"></a>
## [Engineering Concerns About Anthropic&\#x27;s Invisible Watermarking](https://news.google.com/rss/articles/CBMiswFBVV95cUxQUW0zYXlXTWoxSHM2a0cwMWJQY1Vxd2xLRXcwT0dBWjk2aU9CUEFObWRNMW0xa0Nici1hUkFKb3dJcGNKdkM3UjJEeGJnaW52OWxhUzUxS2ZVOG0ySUN4MnlnNVM1cm1kdnZQbDVIZXM2WDl0WTZBTkpjbE0wb2FpRDljazNGYnc5V3JLVnpwWVpxd2ZWZkw3SlBnQVNqQTlvdlFka3I3Mzg3REJaSXRuakF1OA?oc=5) ⭐️ 6.0/10

Design News has published an article examining engineering concerns surrounding Anthropic&\#x27;s invisible watermarking technology, which the company recently integrated into its Claude AI model&\#x27;s text outputs to make AI-generated content detectable. This matters because invisible watermarking is a key tool for AI content provenance and regulatory compliance, such as the EU AI Act, but engineering challenges could undermine its reliability and affect widespread adoption across the AI industry. Key engineering concerns include the watermark&\#x27;s robustness against paraphrasing or editing, the risk of false positives that misclassify human-written text, and potential trade-offs with model output quality or computational overhead.

google\_news · Design News · Oct 5, 22:49

**Background**: Invisible watermarking for AI-generated text involves embedding statistical patterns or subtle signals into the output so that it can later be identified as machine-generated. Anthropic, the company behind the Claude AI assistant, rolled out such a system for its text outputs, partly in response to transparency requirements under the European Union&\#x27;s AI Act. Content provenance—the documented record of a work&\#x27;s origin and modifications—is increasingly important as generative AI proliferates.

<details><summary>References</summary>
<ul>
<li><a href="https://yourstory.com/ai-story/anthropic-invisible-watermarks-ai-generated-text">Anthropic adds invisible watermarks to AI-generated text | YourStory</a></li>
<li><a href="https://www.linkedin.com/pulse/anthropic-rolls-out-invisible-watermarking-claude-text-lnqqf">Anthropic Rolls Out Invisible Watermarking for Claude Text Outputs</a></li>
<li><a href="https://enterprisedna.co/resources/ai-pulse/ai-pulse-2026-08-12-anthropic-starts-invisible-watermarking-of-claude-output-glo/">Anthropic starts invisible watermarking of Claude... — Enterprise DNA</a></li>

</ul>
</details>

**Tags**: `#AI watermarking`, `#Anthropic`, `#AI safety`, `#content provenance`, `#engineering`

---