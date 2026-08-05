---
layout: default
title: "Horizon Summary: 2026-08-05 (ZH)"
date: 2026-08-05
lang: zh
report: default
---

> 从 281 条内容中筛选出 13 条重要资讯。

---

1. [ChainDrop 蠕虫攻陷 npm 逾 1300 个包](#item-1) ⭐️ 9.0/10
2. [马斯克宣布 SpaceX 将独家采用英伟达 AI 系统](#item-2) ⭐️ 8.0/10
3. [豆包上线原生音视频全双工模型 SeedRealtime](#item-3) ⭐️ 8.0/10
4. [宇树科技科创板 IPO 启动询价](#item-4) ⭐️ 8.0/10
5. [FFmpeg 9.0 发布：新增动画 WebP 支持与 AI 辅助开发](#item-5) ⭐️ 8.0/10
6. [交易所关闭局域网线路，周边机房租金跳涨](#item-6) ⭐️ 8.0/10
7. [DeepSeek 重启第二轮融资 投前估值 5000 亿元](#item-7) ⭐️ 7.0/10
8. [三星与 SK 海力士测试中微刻蚀设备，以对冲美国出口管制风险](#item-8) ⭐️ 7.0/10
9. [国产扫地机器人占全球七成市场](#item-9) ⭐️ 7.0/10
10. [甲骨文云将于 2026 年 8 月 18 日强制执行新版 Always-Free 限制](#item-10) ⭐️ 6.0/10
11. [酷安小编称收到上万封下架函，唯独苹果从未发过](#item-11) ⭐️ 6.0/10
12. [删 89TB 数据获刑五年十个月](#item-12) ⭐️ 6.0/10
13. [苹果压价策略失效，长鑫存储拒绝降价](#item-13) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [ChainDrop 蠕虫攻陷 npm 逾 1300 个包](https://www.bleepingcomputer.com/news/security/massive-chaindrop-npm-supply-chain-attack-infects-hundreds-of-packages/) ⭐️ 9.0/10

名为 ChainDrop 的自我传播蠕虫已入侵 npm 上超过 1300 个包，包括 Keyv、Cacheable 等热门缓存库，合计月下载量达 20 亿次。攻击始于黑客攻破 Keyv 维护者的 GitHub 账号，并通过正常的 GitHub Actions 流程扩散。 这是一次严重的供应链攻击，影响的是下载量极高的库，任何执行 npm install 的系统都可能被安装窃密恶意软件，导致 GitHub、npm、AWS、Kubernetes 等凭证泄露。开发者和企业应立即将受感染系统视为已被彻底攻破，并轮换所有令牌。 恶意包包含 setup.mjs 投放器（可定位或下载 Bun 运行时）和 Math\_Symbol.js（部分版本改名为 math\_init.js）窃密脚本，后者是 Mini Shai-Hulud 变体。该恶意软件利用窃取的 npm 发布凭证自我传播，npm-cache\[.\]com 域名可作为失陷指标。

telegram · zaihuapd · 8月5日 03:04

**背景**: npm 是 Node.js 的默认包管理器，针对开源软件仓库的供应链攻击日益猖獗，因为一个被攻破的依赖可能影响成千上万的下游项目。ChainDrop 基于开源 Mini Shai-Hulud 蠕虫，利用正常开发流程：恶意 preinstall 钩子在开发者安装包时自动执行。StepSecurity 研究人员曾在不到 4 小时内观察到 444 个包被投毒，目前总数已超过 1300。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.csoonline.com/article/4205276/chaindrop-credential-stealing-worm-infects-over-400-npm-packages.html">ChainDrop credential stealing worm infects over 400 npm ...</a></li>
<li><a href="https://www.stepsecurity.io/blog/chaindrop-npm-worm">ChainDrop npm Worm : Bun-loaded CI/CD credential... - StepSecurity</a></li>
<li><a href="https://www.endorlabs.com/learn/npm-malware-compromises-keyv-and-cacheable-with-500m-weekly-downloads-and-spreads-to-hundreds-of-packages">NPM Malware Compromises keyv and cacheable with... | Endor Labs</a></li>

</ul>
</details>

**标签**: `#security`, `#supply-chain`, `#npm`, `#malware`, `#credential-theft`

---

<a id="item-2"></a>
## [马斯克宣布 SpaceX 将独家采用英伟达 AI 系统](https://wccftech.com/elon-musk-commits-spacex-exclusively-to-nvidia-gpus-citing-theyre-the-best/) ⭐️ 8.0/10

8 月 4 日，马斯克在 SpaceX 首次财报电话会议上宣布，SpaceX 的 AI 服务将独家基于英伟达系统运行，并称英伟达 Vera Rubin 架构是“最佳 AI 计算架构”。SpaceX 计划在地面数据中心及太空部署 Vera Rubin NVL72 机架系统，预计今年年底 AI 算力超过 2 吉瓦，2027 年底接近 10 吉瓦。 这标志着 SpaceX 与英伟达之间的重大战略结盟，并预示着 AI 基础设施正向太空部署转变。通过 Starmind 等项目，高性能 AI 计算有望延展到轨道上，可能重塑 AI 数据中心的部署方式。 SpaceX 将在地面和轨道部署 Vera Rubin NVL72 机架系统——这是一种 72 GPU 液冷机架级架构。公司计划明年开始发射 Starmind 卫星，以打造轨道 AI 数据中心；此前英伟达已推出太空级 Space-1 Vera Rubin 模块，支持卫星与在轨飞行器的高性能 AI 推理。

telegram · zaihuapd · 8月5日 02:04

**背景**: 英伟达 Vera Rubin 平台于 2026 年初发布，代表从单一芯片向完全集成、协同设计的 AI 工厂转变，其 6 款协同设计芯片可将推理成本比 Blackwell 降低 10 倍。NVL72 机架系统集成 72 颗 GPU 与 AI 原生存储，采用液冷设计，面向大规模 AI 训练和实时推理。SpaceX 的 Starmind 项目于 2026 年 6 月 23 日由马斯克确认，是从拥有 1 万多颗互联网卫星的 Starlink 网络向 AI 卫星星座的转折。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://memo-daily.beehiiv.com/p/7-january-2025">Nvidia Unveils Vera Rubin AI Platform</a></li>
<li><a href="https://www.nextpcb.com/blog/nvidia-gb200-nvl72-architecture">NVIDIA GB200 NVL 72 : PCB &amp; System Architecture Explained</a></li>
<li><a href="https://cryptobriefing.com/spacex-starmind-ai-satellite-network/">SpaceX plans Starmind , an AI network powered by satellites in orbit</a></li>

</ul>
</details>

**标签**: `#AI Infrastructure`, `#SpaceX`, `#Nvidia`, `#Space Computing`, `#AI`

---

<a id="item-3"></a>
## [豆包上线原生音视频全双工模型 SeedRealtime](https://seed.bytedance.com/zh/blog/seedrealtime-%E9%9F%B3%E8%A7%86%E9%A2%91%E5%85%A8%E5%8F%8C%E5%B7%A5%E5%A4%A7%E6%A8%A1%E5%9E%8B%E5%8F%91%E5%B8%83-%E8%B5%B0%E5%90%91%E5%85%A8%E6%A8%A1%E6%80%81%E8%87%AA%E7%84%B6%E4%BA%A4%E4%BA%92) ⭐️ 8.0/10

8 月 5 日，字节跳动发布了原生音视频全双工大模型 SeedRealtime，该模型以统一架构融合音频、视频与文本，支持实时多模态交互。目前该模型已在豆包 App 全量上线，端到端人工评测显示，其对话节奏问题较级联模型减少一半。 这标志着从传统的级联模块（ASR、VLM、TTS）向原生端到端全双工架构的转变，降低了延迟和信息损耗，实现了更自然、可打断的对话。该模型为实时多模态 AI 助手设立了新基准，可能加速全双工交互在整个行业的普及。 SeedRealtime 将感知、理解、决策与表达整合进同一个端到端模型，无需外置 VAD（语音活动检测）模块来判断对话轮次。它支持音视频联合理解、主动环境感知和流畅的对话节奏，显著减少了“话未说完被抢断”等卡壳现象。

telegram · zaihuapd · 8月5日 04:42

**背景**: 传统的实时语音 AI 系统采用级联流水线：语音转文字（ASR）、大型语言/视觉模型（VLM）和文字转语音（TTS）串联工作。这种模块化方式在每一步转换中都会增加延迟并损失副语言信息。全双工模型能够同时进行说话、聆听和推理，使交互更像自然的人类对话，而不再是轮流发言式的交流。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://clova.ai/en/tech-blog/conversation-doesnt-wait-its-turn-sommelier-a-data-pipeline-for-real-time-conversational-voice-ai">Conversation doesn’t wait its turn: Sommelier, a data... | CLOVA</a></li>
<li><a href="https://en.wikipedia.org/wiki/Voice_activity_detection">Voice activity detection - Wikipedia</a></li>
<li><a href="https://inworld.ai/resources/cascaded-vs-speech-to-speech-voice-architecture">Cascaded vs Speech-to-Speech Voice Architecture - Inworld AI</a></li>

</ul>
</details>

**标签**: `#AI`, `#multimodal`, `#real-time conversation`, `#ByteDance`, `#full-duplex model`

---

<a id="item-4"></a>
## [宇树科技科创板 IPO 启动询价](https://m.jrj.com.cn/madapter/stock/2026/08/05141758022724.shtml) ⭐️ 8.0/10

2026 年 8 月 5 日，宇树科技科创板 IPO 进入初步询价阶段，拟发行新股 4044.64 万股，募资 42.02 亿元。市场预估发行价约 104 元/股，对应市值超过 400 亿元。 此次 IPO 是中国人形机器人领军企业的重要里程碑，高估值反映了市场对人形机器人赛道的信心。募资或将加速宇树的研发与全球扩张，也可能成为科创板 AI 与机器人企业上市的标杆。 宇树科技 2025 年营收 16.99 亿元，净利润 2.78 亿元；预计 2026 年上半年营收为 10.52 亿至 11.28 亿元，同比增长 35.62%至 45.41%。网上、网下申购将于 8 月 10 日启动，8 月 12 日为缴款截止日。

telegram · zaihuapd · 8月5日 07:40

**背景**: 宇树科技是中国知名的机器人公司，专注于四足机器人和人形机器人。科创板是上交所为高科技和创新企业设立的板块，而初步询价阶段是机构投资者进行簿记建档、最终确定发行价的流程。

**标签**: `#IPO`, `#robotics`, `#Unitree`, `#STAR Market`, `#funding`

---

<a id="item-5"></a>
## [FFmpeg 9.0 发布：新增动画 WebP 支持与 AI 辅助开发](https://news.ycombinator.com/item?id=49166202) ⭐️ 8.0/10

FFmpeg 9.0 正式发布，新增动画 WebP 解码器和分离器、v360\_vulkan 滤镜、Playdate 视频编码器和封装器、HE-AAC 960 解码（DAB+）、transpose\_cuda 滤镜、AMF 帧率转换滤镜以及 ONNX Runtime DNN 后端。开发团队还通过 Anthropic 的项目使用 Claude 来帮助查找缺失的向后移植。 作为使用最广泛的多媒体框架的重大版本发布，FFmpeg 9.0 扩展了格式支持和硬件加速选项，影响了无数的音视频处理流水线。使用 Claude 进行 AI 辅助开发也标志着开源项目可能利用 AI 工具的一种转变。 动画 WebP 支持是解码器和分离器，而不是编码器。v360\_vulkan 滤镜是由 Lynne 实现的基于 Vulkan 计算的 360 度视频转换滤镜。ONNX Runtime DNN 后端由 AMD 贡献，增强了视频流程中的 AI 模型执行能力。

telegram · zaihuapd · 8月5日 10:32

**背景**: FFmpeg 是领先的开源多媒体框架，用于音频和视频的编码、解码、转码和流媒体传输。该项目持续开发，9.0 版本大约在 FFmpeg 8.1 发布五个月后到来。值得关注的新功能还包括 APV Vulkan 硬件加速路径和四项 AMD AMF 新增功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://peoplearegeek.com/articles/ffmpeg-9-0-animated-webp-vulkan/">FFmpeg 9.0 Adds Animated WebP and Drops CELT... | PeopleAreGeek</a></li>
<li><a href="https://code.ffmpeg.org/FFmpeg/FFmpeg/pulls/22725">#22725 - lavfi/v360: add a Vulkan-compute based filter ...</a></li>
<li><a href="https://thelinuxcamp.com/news/amd-introduces-onnx-runtime-backend-for-ffmpeg-s-dnn-filter-mqte6kmz">AMD Introduces ONNX Runtime Backend for FFmpeg &#x27;s DNN Filter</a></li>

</ul>
</details>

**社区讨论**: 部分社区成员对 AI 辅助开发的安全审查流程表达了担忧。使用 Claude 查找缺失的向后移植值得关注，但关于 AI 在开源开发中的影响，总体情绪较为复杂。

**标签**: `#FFmpeg`, `#release`, `#multimedia`, `#AI`, `#open source`

---

<a id="item-6"></a>
## [交易所关闭局域网线路，周边机房租金跳涨](https://mp.weixin.qq.com/s/lH2IAcm1uX33Hw1H_EfPDg) ⭐️ 8.0/10

7 月 31 日晚起，沪深北交易所关闭了机房内的局域网交易行情线路，机构统一改为通过广域网接入，且双向时延不得低于 2 毫秒，服务器必须迁出交易所机房。上海金桥、外高桥、张江等邻近区域的机房租金随即上涨，标准 4000 瓦金融机柜月租金从年初约 7000 元涨至万元上下，部分黄金区位报价翻倍。 这一监管变化消除了机房托管为高频交易（HFT）带来的超低延迟优势，实际上拉平了订单速度的竞争条件。它同时扰乱了托管机柜的定价格局，迫使机构投资者、量化私募和数据中心运营商重新考虑其基础设施策略。 标准 4000 瓦金融机柜月租金从今年初约 7000 元涨至万元上下，而金桥周边金融级第三方机柜仅有数千个。业内人士指出，真正依赖速度竞争的只是少数超高频策略，多家量化私募表示将“跟着券商走”。

telegram · zaihuapd · 8月5日 14:44

**背景**: 机房托管是交易所提供的一项服务，允许交易机构把服务器放在交易所数据中心内部，以缩短到撮合引擎的物理距离，将执行延迟降低到微秒级。撮合引擎按“价格优先、时间优先”原则撮合买卖订单，因此到达时间的微小差异都可能决定哪个订单先成交。通过强制机构改用双向时延不低于 2 毫秒的广域网线路，交易所实际上抵消了此前机房托管所带来的邻近优势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://questdb.com/glossary/exchange-co-location-strategies/">Exchange Co-Location Strategies - QuestDB</a></li>
<li><a href="https://www.tradealgo.com/trading-guides/tools/co-location">Co-location | TradeAlgo</a></li>
<li><a href="https://devexperts.com/matching-engine/">Matching Engine for Crypto and Stock Exchanges - Devexperts</a></li>

</ul>
</details>

**标签**: `#trading infrastructure`, `#low latency`, `#exchanges`, `#regulatory change`, `#HFT`

---

<a id="item-7"></a>
## [DeepSeek 重启第二轮融资 投前估值 5000 亿元](https://finance.sina.com.cn/wm/2026-08-05/doc-inimfmyv1554159.shtml) ⭐️ 7.0/10

DeepSeek 已重启第二轮融资，计划募资 500 亿元，投前估值约 5000 亿元，预计 8 月下旬完成签约。该轮融资曾在 7 月底暂停，原因是创始人梁文锋对疑似泄露的投资者会议实录不满。 本轮融资显示了市场对 DeepSeek 的高度认可，并为中国竞争激烈的人工智能大模型赛道注入巨额资金。若顺利完成，两轮合计募资将超过 1000 亿元，增强 DeepSeek 在 AI 初创公司及科技巨头中的竞争地位。 本轮投前估值较今年 6 月完成交割的首轮估值（超 3500 亿元）提升约 43%。不过，部分此前积极接触的机构表示尚未接到重启消息，通道仍处暂缓状态。

telegram · zaihuapd · 8月5日 02:46

**背景**: DeepSeek 是一家专注于开发大语言模型的中国人工智能初创公司。该公司于 2025 年 4 月开启首轮融资，并于 2025 年 6 月完成 500 亿元募资。第二轮融资期间的暂停反映了创始人对信息泄露的敏感，以及希望融资过程保持低调的意愿。

**标签**: `#DeepSeek`, `#AI funding`, `#startup valuation`, `#LLM industry`

---

<a id="item-8"></a>
## [三星与 SK 海力士测试中微刻蚀设备，以对冲美国出口管制风险](https://www.reuters.com/world/china/samsung-sk-hynix-test-chinese-chip-tools-hedge-against-us-risks-2026-08-05/) ⭐️ 7.0/10

据路透社报道，三星电子与 SK 海力士正在测试中国中微公司（AMEC）的等离子体刻蚀设备，考虑用于其在华工厂。测试约两年前已开始，但大规模部署尚未决定。 这标志着主要存储芯片制造商可能转向采用中国半导体设备，以对冲美国对芯片工具收紧的出口管制。若获采用，可能重塑供应链，并为中国设备厂商提供强有力的国际背书。 三星否认了相关测试，SK 海力士则拒绝置评。美国于 2025 年撤销了两家公司中国工厂的“经验证最终用户”资格，改为年度许可；中国设备价格通常比西方同类产品低 20%至 30%，德意志银行预计中国本土设备商今年将占据中国约 280 亿美元晶圆制造设备市场的 25%至 30%。

telegram · zaihuapd · 8月5日 04:32

**背景**: 刻蚀是半导体制造中的关键工序，用于在晶圆上选择性地去除材料，形成微观电路图案。中微公司是一家总部位于中国的等离子体刻蚀设备厂商，其设备应用于 65 纳米至 5 纳米及更先进工艺。美国出口管制限制先进芯片制造设备对华出口，而“经验证最终用户”（VEU）计划曾允许合格企业无需单独许可即可进口部分受管制设备。韩国芯片制造商在华运营大型工厂，且高度依赖美国和西方设备，因此易受管制收紧影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.amec-inc.com/index/Lists/index/catid/27.html">产品技术-刻蚀设备-中微公司 - amec-inc.com</a></li>
<li><a href="https://sputniknews.cn/20260805/1072640842.html">媒 体 ：三星、SK海力士在测试中国芯片 制 造设备，以规避美国风险</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/348315252">[初探半导体产业]“光刻”和“刻蚀”区别大揭秘 - 知乎</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#supply chain`, `#export controls`, `#China`, `#chip equipment`

---

<a id="item-9"></a>
## [国产扫地机器人占全球七成市场](https://cn.nikkei.com/china/ccompany/63358-2026-08-05-08-31-00.html?start=0) ⭐️ 7.0/10

IDC 统计显示，2025 年下半年，石头科技、科沃斯等五家主要中国厂商合计占据全球扫地机器人市场超过 70% 的份额，其中石头科技以 27% 的份额位居首位，在美国、德国、韩国等市场排名第一。石头科技还在开发能上楼梯的扫地机器人 Saros Rover，力争数年内量产；而曾经的行业开创者 iRobot 已于 2025 年末破产。 中国扫地机器人厂商凭借自主技术而非价格战取得主导地位，正在重塑全球消费机器人格局。可上楼梯机器人的问世和 iRobot 的破产标志着行业竞争的重大转折，将影响全球竞争对手、投资者和消费者。 Saros Rover 在 2026 年 CES 上发布，是全球首款采用 AI 驱动轮腿架构、可爬楼梯和坡道并清洁的扫地机器人。文章还提到安克、大疆已跨界入局，iRobot 破产后被中国企业收归旗下。

telegram · zaihuapd · 8月5日 11:32

**背景**: 扫地机器人是智能家居中广泛使用的自主清洁设备。此前它们只能清扫单一楼层，无法上下楼梯，因此仅限于平坦的单层空间。Saros Rover 的轮腿架构模拟人类移动方式，可实现跨层清洁，是家用机器人领域的突破。iRobot 的 Roomba 系列曾开创消费级扫地机器人品类，但因落后于中国竞争对手，于 2025 年末申请破产。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://newsroom.roborock.com/gl/news/ces-2026-roborock-releases-the-world-s-first-robotic-vacuum-with-wheel-leg-architecture-as-it-joins-hands-with-real-madrid-football-club-">CES 2026: Roborock releases the world&#x27;s first robotic vacuum ...</a></li>
<li><a href="https://robohorizon.com/en-us/news/2026/01/roborock-saros-rover-the-robot-vacuum-that-finally-grew-legs/">Roborock Saros Rover: The Robot Vacuum That Finally … | …</a></li>
<li><a href="https://ca.dreametech.com/blogs/blog/robot-vacuum-stairs-climbing-guide">Can Robot Vacuums Climb Stairs ? A Look at the Future of...</a></li>

</ul>
</details>

**标签**: `#robotics`, `#smart home`, `#China tech`, `#market analysis`, `#consumer electronics`

---

<a id="item-10"></a>
## [甲骨文云将于 2026 年 8 月 18 日强制执行新版 Always-Free 限制](https://telegram.me/zaihuapd/42978) ⭐️ 6.0/10

甲骨文云已通过邮件通知用户，其 Always Free 计算限制即将更新，超配额租户须在 2026 年 8 月 18 日前降低用量。此后甲骨文将自动终止超出新限制的计算实例。 这将把免费 Ampere A1 配额从 4 个 OCPU/24GB 减半至 2 个 OCPU/12GB，影响大量依赖甲骨文 ARM 实例托管服务的免费用户。这也表明“始终免费”云资源也可能被缩减，用户需提前规划迁移或付费方案。 新限制规定 Always Free 计算最多为 2 个 Ampere A1 OCPU 和 12GB 内存。甲骨文将于 2026 年 8 月 18 日自动终止超配额实例，用户必须在截止日期前自行减少用量。

telegram · zaihuapd · 8月4日 23:51

**背景**: 甲骨文云基础设施（OCI）提供 Always Free 免费套餐，包含基于 ARM 的 Ampere A1 计算实例，此前最多提供 4 个 OCPU 和 24GB 内存，可拆分为多个虚拟机使用。许多用户在这些免费实例上运行轻量服务、代理或数据库。新政策降低了这一配额，并增设自动执行期限，反映甲骨文在控制免费层资源使用上的调整。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.oracle.com/en-us/iaas/Content/FreeTier/freetier_topic-Always_Free_Resources.htm">Learn what Always Free resources are available to all Oracle Cloud ...</a></li>
<li><a href="https://www.cnx-software.com/2021/08/25/oracle-cloud-always-free-services-include-ampere-a1-arm-compute-instances/">Oracle Cloud &quot;Always Free&quot; services include Ampere ... - CNX Software</a></li>
<li><a href="https://space-node.net/blog/oracle-cloud-always-free-limits-2026">Oracle Cloud Always Free Limits 2026: Real Caps and Alternatives</a></li>

</ul>
</details>

**标签**: `#Oracle Cloud`, `#Free Tier`, `#Cloud Computing`, `#Policy Change`, `#Infrastructure`

---

<a id="item-11"></a>
## [酷安小编称收到上万封下架函，唯独苹果从未发过](https://www.coolapk.com/feed/73075082?s=YmVlMmRhZjBiN2YxOWFnNmE3MmFmYjR6i1653) ⭐️ 6.0/10

酷安小编发文称，酷安多年来累计收到厂商发来的内容下架函估计有上万封，几乎每天都有，其中只有苹果从未发过函。文章还建议用户表达产品缺点时用词平和客观、有理有据。 这一说法从一个侧面揭示了国内品牌对科技社区施加的删帖压力，可能扭曲消费者评价生态。它也凸显苹果在此类做法上的例外，以及过度“捂嘴”可能反而把用户推向竞品的风险。 小编估计厂商下架函总数超过一万封，并称一些厂商态度强硬到“捂嘴”程度，不允许任何负面品牌信息出现。文章认为，完全没有负面评价的产品反而显得假，而遭遇此类处理的用户往往容易转投其他品牌。

telegram · zaihuapd · 8月5日 03:43

**背景**: 酷安是中国最大的安卓应用市场之一，也是技术爱好者的热门社区，用户在这里分享应用、发表评测和讨论。在中国，类似酷安的平台经常收到企业发来的要求删除不利内容的“下架函”，这反映了科技行业普遍存在的内容审核现象。据小编说法，苹果是唯一从未向酷安发过此类函件的厂商。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.yimenapp.com/kb-yimen/29446/">app怎 么 上架 酷 安 ？ -APP开发</a></li>

</ul>
</details>

**标签**: `#content moderation`, `#tech industry`, `#censorship`, `#Coolapk`, `#Apple`

---

<a id="item-12"></a>
## [删 89TB 数据获刑五年十个月](https://xinwen.bjd.com.cn/content/s6a728509e4b0e45f3fd5a25b.html) ⭐️ 6.0/10

北京市第二审法院驳回上诉，维持原判，算法工程师王某因删除公司 89 TB 模型及训练数据，被以破坏计算机信息系统罪判处有期徒刑五年十个月，并赔偿经济损失 20.4 万余元。 此案是北京首例将 AI 模型训练系统认定为刑法意义上&\#x27;计算机信息系统&\#x27;的刑事案件，标志着恶意删除 AI 训练数据将承担刑事责任，对 AI 企业的数据治理和内部风险管理具有重要警示意义。 王某使用最高管理员权限运行删除代码超过 17 小时，删除了公司的模型及训练数据。检察机关邀请专家参与证据审查，认定该模型训练系统属于刑法保护的&\#x27;计算机信息系统&\#x27;，并将数据恢复期间产生的人工和算力支出计入经济损失。

telegram · zaihuapd · 8月5日 06:17

**背景**: 根据中国《刑法》第二百八十六条，破坏计算机信息系统罪是指违反国家规定，对计算机信息系统功能进行删除、修改、增加、干扰，造成计算机信息系统不能正常运行，后果严重的行为。本案的办理将 AI 模型训练系统纳入刑法保护的&\#x27;计算机信息系统&\#x27;范围。2024 年 9 月，王某在北京市东城区某科技公司使用最高管理员权限输入删除代码，导致研发项目停摆。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://baike.baidu.com/item/%E9%9D%9E%E6%B3%95%E5%88%A0%E9%99%A4%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%E6%A8%A1%E5%9E%8B%E8%AE%AD%E7%BB%83%E6%95%B0%E6%8D%AE%E6%A1%88/67654528">非法删除人工智能模型训练数据案_百度百科</a></li>
<li><a href="https://www.sohu.com/a/1059062485_479806">离谱！员工 17 小时删光公司 89TB AI 数据，成北京首例破坏 AI 模型刑...</a></li>
<li><a href="https://www.163.com/dy/article/JE8RU4FO05568RYX.html">163.com/dy/article/JE8RU4FO05568RYX.html</a></li>

</ul>
</details>

**标签**: `#AI`, `#legal`, `#data-management`, `#cybercrime`, `#machine-learning`

---

<a id="item-13"></a>
## [苹果压价策略失效，长鑫存储拒绝降价](https://m.ddaily.co.kr/page/view/2026080513445474844) ⭐️ 6.0/10

据韩国《Digital Daily》报道，苹果近期与长鑫存储就 LPDDR5X 等移动 DRAM 供应展开谈判，试图压低成本，但长鑫存储拒绝降价，报价甚至与三星、SK 海力士持平或更高。这标志着苹果惯用的中国低价替代策略在 DRAM 短缺背景下失效。 这表明长鑫存储在内存市场获得了罕见的定价权，底气来自华为、小米等中国厂商的大规模采购。同时，三星和 SK 海力士将产线集中于 HBM 等高附加值 AI 内存，通用 DRAM 供给持续收紧，使存储厂商在下半年与全球大厂的长期价格谈判中占据更强主导权。 长鑫存储目前是中国最大、全球第四大 DRAM 厂商，截至 2025 年底每季度产能约为 72 万片晶圆。据报道，苹果此次谈判主要围绕 LPDDR5X 等移动 DRAM，而三星和 SK 海力士将产能转向 HBM，导致通用 DRAM 供应收紧。

telegram · zaihuapd · 8月5日 08:27

**背景**: LPDDR5X 是 JEDEC 制定的低功耗 DRAM 标准，主要用于智能手机和笔记本电脑，三星于 2021 年推出业界首款 LPDDR5X DRAM。HBM（高带宽内存）是 AI 加速器必需的 3D 堆叠存储器技术，因此三星和 SK 海力士将产能转向该领域。长鑫存储于 2016 年在合肥成立，现已成长为中国最大、全球第四大 DRAM 供应商，华为、小米等国内厂商的大规模采购已能消化其大部分产能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/LPDDR">LPDDR - Wikipedia</a></li>
<li><a href="https://semiconductor.samsung.com/dram/lpddr/lpddr5x/">LPDDR5X | DRAM | Samsung Semiconductor Global</a></li>
<li><a href="https://en.wikipedia.org/wiki/ChangXin_Memory_Technologies">ChangXin Memory Technologies</a></li>

</ul>
</details>

**标签**: `#semiconductor`, `#DRAM`, `#Apple`, `#supply-chain`, `#memory`

---