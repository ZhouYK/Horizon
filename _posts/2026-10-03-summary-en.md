---
layout: default
title: "Horizon Summary: 2026-10-03 (EN)"
date: 2026-10-03 23:03:06 +0000
lang: en
report: default
---

> From 138 items, 5 important content pieces were selected

---

1. [Qt 6.12 LTS Released With 5-Year Support, Adds HarmonyOS](#item-1) ⭐️ 7.0/10
2. [Google Bans Fake Author Bylines and AI Headshots in Search Guidelines](#item-2) ⭐️ 7.0/10
3. [Google restricts free Gemini users to Flash-Lite model from October 9](#item-3) ⭐️ 6.0/10
4. [Google Antigravity Adds Opus 5.5 and Sonnet 5.5, Paywalls Third-Party Models](#item-4) ⭐️ 6.0/10
5. [US Stock Markets to Enter 23-Hour Trading Era on December 6](#item-5) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Qt 6.12 LTS Released With 5-Year Support, Adds HarmonyOS](https://www.qt.io/blog/qt-6.12-released) ⭐️ 7.0/10

Qt 6.12 LTS was released on September 30, 2026, and will receive five years of maintenance support. For the first time, Huawei&\#x27;s HarmonyOS has been added to Qt&\#x27;s list of officially supported LTS platforms. Because LTS releases are the versions enterprises and device makers standardize on, adding HarmonyOS to that tier gives Qt developers a supported, long-term path to target Huawei&\#x27;s ecosystem without relying on community ports. It also reflects Huawei&\#x27;s push to build out a self-contained app ecosystem, and could matter to anyone shipping desktop, embedded, or mobile products in the Chinese market. The headline commitment is the five-year maintenance window attached to an LTS release, which is what makes it suitable for products with long lifecycles. The notable caveat is that HarmonyOS support arrives at the LTS tier, so the practical value depends on which Qt modules and tooling are covered for that target rather than on the platform being listed alone.

telegram · zaihuapd · Oct 3, 04:52

**Background**: Qt is a cross-platform C++ application development framework, maintained by Qt Group and the open-source Qt Project, that lets developers build native applications for Windows, macOS, Linux, Android, embedded systems and more from a largely shared codebase; it is dual-licensed under commercial terms and open-source GPL/LGPL licenses. An LTS \(long-term support\) release is a version Qt commits to maintaining with fixes over a multi-year period, which is why companies build products on it rather than on short-lived feature releases. HarmonyOS is Huawei&\#x27;s distributed operating system for phones, tablets, PCs, wearables and other devices; since HarmonyOS 5 \(formerly HarmonyOS NEXT\), it has dropped Android/AOSP compatibility and runs only native HarmonyOS apps on Huawei&\#x27;s own microkernel.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Qt_framework">Qt framework</a></li>
<li><a href="https://en.wikipedia.org/wiki/HarmonyOS">HarmonyOS</a></li>
<li><a href="https://www.qt.io/development/qt-framework">Qt Framework – Build Fast, Scalable Cross-Platform Software | Qt</a></li>

</ul>
</details>

**Tags**: `#Qt`, `#HarmonyOS`, `#C++`, `#Cross-Platform`, `#Release`

---

<a id="item-2"></a>
## [Google Bans Fake Author Bylines and AI Headshots in Search Guidelines](https://futurism.com/artificial-intelligence/google-updates-guidelines-fake-bylines-ai-generated-headshots) ⭐️ 7.0/10

Google has updated its search quality and people-first content guidance to explicitly classify fabricated author identities as deception, adding that AI-generated headshots, invented names and fake credentials used to make content appear expert-written are a signal of low-quality pages. The change follows Futurism&\#x27;s investigation into the AI content farm Brown Brothers Media, which acquired struggling news outlets and mass-produced SEO articles under fictitious reporters; Google subsequently suppressed the network in search and news results. This is a direct policy signal for the SEO and publishing industry: sites that fabricate expertise now risk ranking suppression rather than merely missing out on a recommendation, which affects affiliate marketers, programmatic content operations and legitimate small publishers alike. It also marks Google formally extending its long-standing rater guidelines on deception into the site-owner-facing documentation that publishers actually read. Previously Google only encouraged accurate attribution without prohibiting fabrication, so this wording converts a soft recommendation into an explicit quality violation; the existing rater guidelines already described such deception, and the new text links fake authorship to damaged trust for both users and automated quality systems.

telegram · zaihuapd · Oct 3, 16:31

**Background**: Google&\#x27;s search ranking is governed partly by publicly documented guidance for site owners, which tells publishers what constitutes helpful, people-first content versus content created mainly to manipulate rankings. &quot;AI slop&quot; refers to low-effort, mass-produced generative AI content, and content farms are operations that churn out huge volumes of such pages to harvest ad clicks. The investigation into Brown Brothers Media showed a related pattern of &quot;pink slime&quot; journalism, in which AI-generated outlets impersonate or buy up real local news brands; similar operations were also found in Canada, Florida and Rhode Island.

<details><summary>References</summary>
<ul>
<li><a href="https://www.searchenginejournal.com/google-fake-author-warning-site-owner-guidance/591806/">Google Adds Fake Author Warning To Helpful Content Guidance</a></li>
<li><a href="https://futurism.com/artificial-intelligence/google-updates-guidelines-fake-bylines-ai-generated-headshots">Google Updates Guidelines to Punish Sites That Use Fake ...</a></li>

</ul>
</details>

**Tags**: `#Google Search`, `#SEO`, `#AI Content`, `#Misinformation`, `#Content Farms`

---

<a id="item-3"></a>
## [Google restricts free Gemini users to Flash-Lite model from October 9](https://support.google.com/gemini/answer/17004136) ⭐️ 6.0/10

Starting October 9, Google will limit individual users who have not subscribed to a Google AI plan to the Gemini Flash-Lite model, as Flash and Pro will no longer be available to free users. Paid tiers keep the higher-end models: AI Plus gets Flash-Lite and Flash, while AI Pro and AI Ultra get Flash-Lite, Flash, and Pro. This turns Gemini&\#x27;s free tier from a fairly open full-model offering into a slimmed-down entry point, pushing heavy users toward paid subscriptions and aligning Google with competitors that reserve their strongest models for paying customers. It also makes model choice, rather than raw usage volume, the main lever Google uses to differentiate its subscription tiers. Usage quotas will now be calculated based on the model, prompt complexity, and the features used, refreshing every 5 hours with an additional weekly cap in place. Features such as image and video generation and Deep Research consume noticeably more quota than plain text chats.

telegram · zaihuapd · Oct 3, 06:09

**Background**: Gemini is Google&\#x27;s family of multimodal AI models, split into tiers by cost and capability: Flash-Lite \(the lightest, cheapest and lowest-latency\), Flash \(a balanced mid-tier\), and Pro \(the most capable\). Google monetizes access through Google AI Plus, Pro, and Ultra subscription plans, which are available in more than 140 countries and bundle higher model access with features like video generation and Deep Research — an agentic tool that browses many websites and produces multi-page reports. Restricting free users to Flash-Lite is therefore a way to control compute costs while giving subscribers a concrete reason to pay.

<details><summary>References</summary>
<ul>
<li><a href="https://gemini.google/us/subscriptions/?hl=en">Google AI Pro &amp; Ultra — get access to Gemini 3.1 Pro &amp; more</a></li>
<li><a href="https://blog.google/products-and-platforms/products/google-one/google-ai-subscriptions/">Google AI subscription updates from Google I/O 2026</a></li>
<li><a href="https://gemini.google/us/overview/deep-research/?hl=en">Gemini Deep Research — your personal research assistant</a></li>

</ul>
</details>

**Tags**: `#Google Gemini`, `#AI pricing`, `#LLM access`, `#product policy`, `#AI subscriptions`

---

<a id="item-4"></a>
## [Google Antigravity Adds Opus 5.5 and Sonnet 5.5, Paywalls Third-Party Models](https://www.reddit.com/r/google_antigravity/comments/1wwfcav/google_finally_added_opus_55_and_sonnet_55_on) ⭐️ 6.0/10

Google Antigravity has added Anthropic&\#x27;s Claude Opus 5.5 and Sonnet 5.5 models to its model lineup, and announced that after November 2 all third-party models on the platform will be restricted to paid Pro and Ultra subscription tiers. The move lets developers driving agents inside Google&\#x27;s own IDE call Anthropic&\#x27;s frontier models directly, but the concurrent paywall shrinks what free users can access, showing how multi-vendor model choice is becoming a monetization lever for AI coding platforms rather than just a convenience feature. Antigravity already runs Google&\#x27;s own Gemini models, so the third-party restriction applies specifically to non-Google models such as Anthropic&\#x27;s; Opus 5.5 is positioned by Anthropic for long-running agentic coding at $4/$20 per million input/output tokens, while Sonnet 5.5 sits at a lower Sonnet-level price point with a large context window.

telegram · zaihuapd · Oct 3, 06:32

**Background**: Google Antigravity is Google&\#x27;s software development platform, combining a chat-oriented development environment, an IDE, a command-line interface and an SDK, all designed to orchestrate autonomous AI agents that generate, run and test code. Rather than being tied to a single model family, such platforms increasingly let users swap in models from different vendors, which is why a decision about third-party model access is a notable policy change for its user base.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Google_Antigravity">Google Antigravity</a></li>
<li><a href="https://antigravity.google/">Google Antigravity</a></li>
<li><a href="https://grokipedia.com/page/Google_Antigravity">Google Antigravity</a></li>

</ul>
</details>

**Tags**: `#Google Antigravity`, `#Anthropic Claude`, `#AI models`, `#pricing`, `#platform update`

---

<a id="item-5"></a>
## [US Stock Markets to Enter 23-Hour Trading Era on December 6](https://wallstreetcn.com/articles/3782956) ⭐️ 6.0/10

Starting December 6, four core US exchanges including Nasdaq and NYSE Arca will add a night session, extending daily US equity trading to 23 hours with only a one-hour maintenance break from 8 p.m. to 9 p.m. Eastern Time. This marks the formal arrival of near-round-the-clock trading for major US stock venues. This reshapes the structure of the US equity market by giving global investors near-24/7 access to US stocks and could shift volume away from the traditional cash session. It also puts pressure on brokers, market makers, clearing and market-data infrastructure to operate across extended hours, while raising concerns about thinner liquidity outside regular hours. SEC data show night-session trading currently accounts for only about 1% of total volume, but it has grown 358% year over year. Institutions are worried about liquidity and bid-ask spreads, while overseas funds and retail traders remain the main participants in the night session.

telegram · zaihuapd · Oct 3, 07:29

**Background**: NYSE Arca is an all-electronic exchange and a wholly owned subsidiary of NYSE Group \(part of Intercontinental Exchange\), best known as the leading US venue for listing and trading exchange-traded products while also trading all NMS securities. US equities normally trade from 9:30 a.m. to 4 p.m. Eastern Time, with pre-market and after-hours sessions that are far less liquid than the regular session. The bid-ask spread — the gap between the best quoted buy and sell prices — is a standard measure of liquidity and transaction cost, which is why widening spreads in a thin night session worry institutions. The new night session extends this fragmented extended-hours landscape toward a nearly continuous 23-hour trading day.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/NYSE_Arca">NYSE Arca</a></li>
<li><a href="https://en.wikipedia.org/wiki/Bid-ask_spread">Bid-ask spread</a></li>
<li><a href="https://www.kiplinger.com/investing/602886/stock-market-trading-hours">When Does the Market Open? Today&#x27;s Stock Market Hours | Kiplinger</a></li>

</ul>
</details>

**Tags**: `#US stock market`, `#23-hour trading`, `#Nasdaq`, `#NYSE`, `#market infrastructure`

---