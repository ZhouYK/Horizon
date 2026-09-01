---
layout: default
title: "Horizon Summary: 2026-09-01 (EN)"
date: 2026-09-01 23:07:39 +0000
lang: en
report: default
---

> From 301 items, 8 important content pieces were selected

---

1. [BGP hijack hits Virtualizor updates, plants root backdoor](#item-1) ⭐️ 8.0/10
2. [Claude Fable 5.1 Launches with 1M Context, Cheaper Cache Reads](#item-2) ⭐️ 8.0/10
3. [Qualcomm to Raise Chip Prices by Double Digits Starting September 1, 2026](#item-3) ⭐️ 7.0/10
4. [Takeaway Cups Release Microplastics; PLA Liners Shed 12x More Than PE](#item-4) ⭐️ 6.0/10
5. [VLC Hits 7 Billion Downloads, Ports to Amazon Vega OS](#item-5) ⭐️ 6.0/10
6. [Nubia&\#x27;s AI Agent Phone &\#x27;Doubao Phone 2&\#x27; Cleared for Network Access, Launching in September](#item-6) ⭐️ 6.0/10
7. [Japan Relaxes Overtime Cap, Ending 45-Hour Limit](#item-7) ⭐️ 6.0/10
8. [UBS Says China Decade Behind ASML in EUV, DUV in 2-5 Years](#item-8) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [BGP hijack hits Virtualizor updates, plants root backdoor](https://www.virtualizor.com/blog/security-incident-bgp-hijacking/) ⭐️ 8.0/10

On August 28–30, 2026, attackers hijacked BGP routes for Virtualizor&\#x27;s update infrastructure and used valid TLS certificates to serve malicious update packages that installed a root backdoor on affected hypervisors. The vendor confirmed only a small number of installations that updated during the window were impacted. This incident demonstrates how BGP hijacking can transform a trusted update channel into a supply-chain attack vector, affecting even software without inherent vulnerabilities. Hosting providers and VPS users who rely on Virtualizor could face full compromise of hypervisors and all hosted virtual machines. The malicious update wrote root SSH keys, installed a Java payload, and created persistent services. Independent analysis found indicators on 5 of 34 hypervisors at AlbaHost, while Softaculous said there is no evidence other products were affected.

telegram · zaihuapd · Sep 1, 06:05

**Background**: BGP \(Border Gateway Protocol\) is the routing protocol that directs traffic between autonomous systems on the internet; attackers can hijack routes to redirect traffic destined for a specific IP range to their own servers. Virtualizor is a web-based VPS control panel developed by Softaculous that is widely used by hosting providers to manage virtual machines and hypervisors. In this incident, the attackers impersonated the update server and used a valid TLS certificate to make malicious updates appear authentic, a classic supply-chain attack where malicious code is delivered through the vendor&\#x27;s own trusted update mechanism.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/BGP_hijacking">BGP hijacking</a></li>
<li><a href="https://www.cloudflare.com/learning/security/glossary/bgp-hijacking/">What Is BGP Hijacking ?</a></li>
<li><a href="https://cybersecuritynews.com/virtualizor-compromise/">BGP Hijack Diverts Softaculous Traffic to Deliver Malicious Virtualizor ...</a></li>

</ul>
</details>

**Tags**: `#security`, `#BGP hijacking`, `#supply chain attack`, `#Virtualizor`, `#rootkit`

---

<a id="item-2"></a>
## [Claude Fable 5.1 Launches with 1M Context, Cheaper Cache Reads](https://platform.claude.com/docs/en/models/fable-5-1/overview) ⭐️ 8.0/10

Anthropic released Claude Fable 5.1 on September 1, 2026, supporting a 1M-token context window and 128K-token maximum output, with pricing unchanged from Fable 5 and cache-read costs cut to one-quarter. This release matters because a 1M-token context window and reduced cache-read costs make long-horizon agentic and complex reasoning workloads significantly more economical for AI/ML practitioners and enterprises. It also signals intensifying competition in frontier-model pricing and capabilities. Claude Mythos 5.1 is functionally identical to Fable 5.1 but features more permissive safeguards and is restricted to vetted Project Glasswing participants. The cache-read price cut applies to prompt caching, which reduces repeated-input costs by up to 90%.

telegram · zaihuapd · Sep 1, 17:54

**Background**: Claude is Anthropic&\#x27;s family of large language models. A context window defines how many tokens the model can process at once; 1M tokens accommodates very long documents or multi-step agent runs. Prompt caching lets developers store and reuse prompt prefixes, reducing latency and cost, with cache reads typically priced at a small fraction of base input. Project Glasswing, launched April 7, 2026, is Anthropic&\#x27;s $100M defensive cybersecurity initiative built around a restricted frontier model called Claude Mythos.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/claude-fable-and-mythos-5-1">Introducing Claude Fable 5 . 1 and Claude Mythos 5 . 1 \ Anthropic</a></li>
<li><a href="https://platform.claude.com/cookbook/misc-prompt-caching">Prompt caching through the Claude API | Claude Cookbook</a></li>
<li><a href="https://www.anthropic.com/glasswing">Project Glasswing : Securing critical software for the AI era \ Anthropic</a></li>

</ul>
</details>

**Tags**: `#Claude`, `#AI model`, `#context window`, `#pricing`, `#release`

---

<a id="item-3"></a>
## [Qualcomm to Raise Chip Prices by Double Digits Starting September 1, 2026](https://www.macrumors.com/2026/08/31/qualcomm-chip-price-increase/) ⭐️ 7.0/10

Qualcomm will increase prices across its entire chip lineup for shipments after September 1, 2026, with double-digit percentage hikes negotiated individually with each customer. CEO Cristiano Amon said the company can no longer absorb rising supplier costs alone. The hike will raise costs for major customers like Apple, which continues to buy Qualcomm modem chips for the iPhone 17 series, and likely trickle down to hardware pricing. It signals broader inflationary pressure in the semiconductor supply chain. The exact percentage varies by customer and will be negotiated bilaterally. Apple still relies on Qualcomm for modem chips in iPhone 17, despite its long-term efforts to develop in-house modems.

telegram · zaihuapd · Sep 1, 04:10

**Background**: Qualcomm is a leading supplier of mobile processors and modem chips used in most smartphones, including iPhones. Chipmakers are raising prices as manufacturing costs, materials, and R&amp;D expenses climb. This price increase could affect not only Apple but the wider Android smartphone market as well.

<details><summary>References</summary>
<ul>
<li><a href="https://tech.sina.cn/csj/2018-11-05/doc-ihmutuea7064783.d.html?oid=5_iqq&amp;vt=4">高通与苹果决裂背后， 基 带 芯 片 到底是啥？_ 手机新浪网</a></li>
<li><a href="https://www.21ic.com/a/974018.html">最强梳理！ 基 带 与射频到底干什么用的？ - 21ic电子网</a></li>

</ul>
</details>

**Tags**: `#Qualcomm`, `#chip pricing`, `#hardware`, `#supply chain`, `#Apple`

---

<a id="item-4"></a>
## [Takeaway Cups Release Microplastics; PLA Liners Shed 12x More Than PE](https://news.uq.edu.au/2026-08-takeaway-cups-release-microplastics-your-coffee) ⭐️ 6.0/10

A University of Queensland study found that takeaway paper cups release millions of microplastic particles into hot beverages. PLA-lined cups released about 12 times more total particle mass than conventional PE-lined cups, with roughly 4.3 million versus 2.7 million nanoparticles per milliliter. The findings raise questions about the safety of &\#x27;eco-friendly&\#x27; biodegradable coatings and highlight a previously underappreciated source of microplastic and nanoplastic exposure in everyday life. Regulators may need to consider safety guidelines or labeling for single-use paper cups. Both PE and PLA cups shed particles, but by total particle mass, PLA released roughly 12 times more than PE. The researchers stressed that the findings do not mean PLA is unsafe per se and that health effects remain unclear, but they urged regulators to consider precautionary guidelines.

telegram · zaihuapd · Sep 1, 00:45

**Background**: Microplastics are plastic fragments smaller than 5 millimeters, while nanoplastics are smaller than 1 micrometer and invisible to the human eye. PLA \(polylactic acid\) is a biodegradable thermoplastic often used as a &\#x27;green&\#x27; coating for paper cups, whereas PE is conventional polyethylene. This study compared the two liner materials when exposed to hot liquid.

<details><summary>References</summary>
<ul>
<li><a href="https://ru.wikipedia.org/wiki/%D0%9F%D0%BE%D0%BB%D0%B8%D0%BB%D0%B0%D0%BA%D1%82%D0%B8%D0%B4">Полилактид — Википедия</a></li>
<li><a href="https://en.wikipedia.org/wiki/Nanoplastics">Nanoplastics</a></li>

</ul>
</details>

**Tags**: `#microplastics`, `#environment`, `#PLA`, `#food safety`, `#research`

---

<a id="item-5"></a>
## [VLC Hits 7 Billion Downloads, Ports to Amazon Vega OS](https://techcrunch.com/2026/08/31/vlc-crosses-7-billion-downloads/) ⭐️ 6.0/10

VideoLAN&\#x27;s VLC media player has surpassed 7 billion cumulative downloads across all platforms, approximately 18 months after reaching 6 billion in January 2025. The nonprofit also announced VLC is being ported to Amazon&\#x27;s Vega OS television system, while VLC 4 remains in development. Passing 7 billion downloads underscores VLC&\#x27;s enduring dominance as a free, open-source media player in an era of streaming services. Porting to Amazon&\#x27;s Vega OS could bring VLC&\#x27;s format support to a new generation of smart TVs, expanding its reach into living-room devices. The 7-billion mark was reached about 18 months after the 6-billion milestone in January 2025. VLC 4.0 is still in development, and no release date has been announced for the Vega OS port.

telegram · zaihuapd · Sep 1, 03:43

**Background**: VLC is a free, open-source media player developed by the nonprofit organization VideoLAN. It is known for playing virtually any video or audio format without needing additional codecs, and it runs on desktop, mobile, and now TV platforms. Amazon&\#x27;s Vega OS is a newer operating system for Amazon&\#x27;s television hardware, making smart TVs a new target for VLC&\#x27;s cross-platform support.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/VLC_media_player">VLC media player</a></li>
<li><a href="https://www.oxagile.com/article/vega-os-overview/">What is Amazon Vega OS ( Operating System )? Vega OS Release...</a></li>
<li><a href="https://www.stork.ai/blog/amazons-secret-os-is-replacing-android">Amazon &#x27;s Vega OS : The Post-Android Future for Fire TV... | Stork.AI</a></li>

</ul>
</details>

**Discussion**: No community discussion was provided for this news item.

**Tags**: `#VLC`, `#VideoLAN`, `#open-source`, `#media-player`, `#milestone`

---

<a id="item-6"></a>
## [Nubia&\#x27;s AI Agent Phone &\#x27;Doubao Phone 2&\#x27; Cleared for Network Access, Launching in September](https://mp.weixin.qq.com/s/u7KXxdvmh8hjf8cVbQZOKg) ⭐️ 6.0/10

Nubia&\#x27;s AI agent phone, the Nubia NaviX Ultra \(also called Doubao Phone 2\), has received China&\#x27;s network access license and will hit the market in September. Co-developed with ByteDance, its &\#x27;Nubia Doubao Phone Large Model&\#x27; completed generative AI service filing on July 8, making it among the first terminal products with an on-device model to be filed. This marks one of the first phones to pass both network access certification and generative AI service filing in China, giving the industry a compliance template for AI-powered handsets. It also shows how smartphone makers are teaming up with AI companies to push on-device intelligence into mainstream devices. The phone is billed as the world&\#x27;s first AI agent phone, comes in four colors — Lanyu \(blue\), Huamong \(dream\), black, and white — and ships with ByteDance&\#x27;s Doubao phone assistant. The network access license is required for legal sales through official or retail channels; devices without it cannot be sold through formal channels and have no after-sales support.

telegram · zaihuapd · Sep 1, 11:18

**Background**: In China, cell phones must obtain a network access license before they can be legally sold through official channels; this certification means the device passed network testing and compliance checks. Separately, Chinese rules require providers of generative AI services to file with internet authorities under the Interim Measures for the Management of Generative AI Services. An on-device large language model runs locally on the phone instead of relying solely on cloud servers, which improves privacy, latency, and offline availability, though it also faces constraints from model size and device computing power. ByteDance&\#x27;s Doubao is a popular AI assistant ecosystem, and this device integrates it directly into the smartphone.

<details><summary>References</summary>
<ul>
<li><a href="https://www.jwview.com/jingwei/html/06-09/405701.shtml">让没有 入 网 许 可 的山寨 机 “顺利 入 网 ”，谁该出来走两步？ -中新经纬</a></li>
<li><a href="https://www.cnnic.net.cn/NMediaFile/2025/1021/MAIN1761038973801E6DI0GFPDE.pdf">cnnic.net.cn/NMediaFile/2025/1021/MAIN1761038973801E6DI...</a></li>
<li><a href="https://www.infoq.cn/article/atf5mzkswcxk2lgfdhlr">“像把 大 象塞进冰箱一样困难”， 端 侧 大 模 型 是 噱头还 是 未来？ - InfoQ</a></li>

</ul>
</details>

**Tags**: `#AI`, `#smartphone`, `#Nubia`, `#Doubao`, `#edge AI`

---

<a id="item-7"></a>
## [Japan Relaxes Overtime Cap, Ending 45-Hour Limit](https://www.orientaldaily.com.my/news/international/2026/09/01/844683) ⭐️ 6.0/10

Effective September 1, Japan has relaxed its overtime rules, making the mandatory 45-hour monthly cap non-binding. The change, part of Prime Minister Takaichi Sanae&\#x27;s growth strategy passed in July, allows about 40% of companies to permit up to 100 hours of monthly overtime. This policy could normalize excessive overtime and increase the risk of karoshi, affecting millions of Japanese workers. Critics see it as a reversal of work-style reforms, potentially influencing labor policies elsewhere. Officials warn that exceeding 45 hours of monthly overtime raises the risk of death from overwork. The relaxation stems from Prime Minister Takaichi Sanae&\#x27;s government, and labor standard inspectors will no longer enforce the cap.

telegram · zaihuapd · Sep 1, 12:56

**Background**: Japan introduced the 45-hour monthly overtime cap as part of work-style reforms aimed at curbing its notorious overwork culture. The new policy, effective September 1, removes mandatory enforcement, drawing criticism from unions who say it abandons the reform agenda and endangers worker health.

**Tags**: `#Japan`, `#labor policy`, `#overtime`, `#work culture`, `#policy change`

---

<a id="item-8"></a>
## [UBS Says China Decade Behind ASML in EUV, DUV in 2-5 Years](https://thenextweb.com/news/ubs-china-asml-euv-decade-immersion-duv-dutch-export-licence) ⭐️ 6.0/10

UBS analysts estimate that China&\#x27;s lithography capability is roughly at ASML&\#x27;s 2004 level, so a viable EUV replacement is unlikely within a decade. They expect China to mass-produce immersion DUV lithography machines within two to five years. The forecast suggests ASML&\#x27;s near-monopoly on EUV will remain unchallenged for at least a decade, while China may focus on DUV to circumvent export controls. This shapes the competitive landscape of global semiconductor manufacturing and the effectiveness of Dutch export restrictions. Immersion DUV systems sell for nearly $90 million, while EUV systems cost more than $200 million. In the third quarter of 2025, China accounted for 42% of ASML&\#x27;s net sales, and immersion DUV tools are currently subject to Dutch export license controls.

telegram · zaihuapd · Sep 1, 13:58

**Background**: EUV \(extreme ultraviolet\) lithography uses 13.5 nm wavelength light to pattern the most advanced chips and is currently unique to ASML, while DUV \(deep ultraviolet\) lithography uses longer wavelengths for less advanced nodes. Immersion DUV is an enhanced DUV technique that uses a liquid layer to improve resolution, making it relevant for mature and mid-range chips. The comparison to ASML&\#x27;s 2004 level reflects the gap between current Chinese lithography prototypes and the Dutch company&\#x27;s historical roadmap.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Extreme_ultraviolet_lithography">EUV lithography - Wikipedia</a></li>
<li><a href="https://www.asml.com/en/products/euv-lithography-systems">EUV lithography systems – Products | ASML</a></li>
<li><a href="https://www.zeiss.com/semiconductor-manufacturing-technology/inspiring-technology/duv-lithography.html">DUV lithography for chip manufacturing | ZEISS SMT</a></li>

</ul>
</details>

**Tags**: `#semiconductor`, `#lithography`, `#ASML`, `#China`, `#EUV`

---