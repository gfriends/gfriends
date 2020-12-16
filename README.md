# 女友头像仓库
![TotalNumber](https://img.shields.io/badge/TotalNum-3.20w-Blue.svg)  ![AutoUpdate](https://img.shields.io/badge/AutoUpdate-2020--12--16-green.svg)<br>
媒体服务器演员头像仓库。<br>旨在满足数量需求前提下，尽可能收集和处理高质量女友头像，并提供导入媒体服务器方案。

## 目录
* [快速开始](#快速开始)
   * [Emby / Jellyfin](#emby--jellyfimn)
   * [Plex](#plex)
* [进阶说明](#进阶说明)
   * Gfriends Inputer 进阶玩法
      * [导入本地头像图片到媒体服务器](#导入本地头像图片到媒体服务器)
      * [使用百度AI精准裁剪头像](#使用百度AI精准裁剪头像)
      * [自定义头像来源](#自定义头像来源不导入某些来源的头像)
   * 为女友头像仓库做贡献
      * [上传新的头像图片到仓库](#上传新的头像图片到仓库)
      * [共享头像图片来源网站](#共享头像图片来源网站)
      * [对女友仓库的开发及调用](#对女友仓库的开发及调用)
   * [仓库更新计划](#仓库更新计划)
* [图片来源](#图片来源)
* [法律信息](#法律信息及免责声明)

## 快速开始
对于一般用户来说，可以通过以下方案导入头像。

### Emby / Jellyfin

无需下载本仓库的女友头像，仅需下载 [Gfriends Inputer 一键导入工具](https://github.com/xinxin8816/gfriends/releases)，编辑 `Config.ini` 文件并运行程序。<br>该工具将自动从本仓库搜索头像并导入你的服务器。

<details>

<summary>或者试试安装插件导入？</summary>
<p>由 JavScraper 提供<p>

无需下载本仓库的女友头像，仅需为你的 Emby / Jellyfin 服务器安装 [JavScraper](https://github.com/JavScraper/Emby.Plugins.JavScraper) 插件。<br>该插件将自动从本仓库搜索头像并导入你的服务器，亦提供了元数据刮削功能。

</details>

### Plex
由 ddd354 提供

无需下载本仓库的女友头像，仅需为你的 Plex 服务器安装 [JAVnfoMoviesImporter](https://github.com/ddd354/JAVnfoMoviesImporter.bundle) 插件。<br>该插件将自动从本仓库搜索头像并导入你的服务器，亦提供了元数据刮削功能。

## 进阶说明
本项目以抓取官方高质量大图为主要目标，头像图片为自动化抓取，部分人工筛选。

推荐搭配任一刮削整理项目 [AVDC](https://github.com/yoshiko2/AV_Data_Capture "AV Data Capture")([GUI](https://github.com/moyy996/AVDC "AVDC GUI"))、[JavScraper](https://github.com/JavScraper/Emby.Plugins.JavScraper "JavScraper")、[JAVSDT](https://github.com/junerain123/javsdt "JAVSDT")、[JAVOneStop](https://github.com/ddd354/JAVOneStop "JAVOneStop")。

### 导入本地头像图片到媒体服务器
Gfriends Inputer v2.5 及后续版本支持导入本地头像到媒体服务器。

程序首次启动时会自动创建 `Avatar` 文件夹（可在配置文件中修改）。将本地头像图片重命名为`演员姓名.jpg`，或将第三方头像包移动至该文件夹。此后，导入工具优先从该文件夹查找并导入头像，本地路径中不存在的则会尝试从本仓库搜索并导入。

### 使用百度AI精准裁剪头像
Gfriends Inputer v2.7 及后续版本支持使用百度AI精准裁剪头像。

您可以在通过如下途径申请相关 API：
1. 访问 https://ai.baidu.com 百度 AI 开放平台，登录并进入控制台。
2. 进入 “人体分析” —— “创建应用”，按要求填写表单，并勾选 “人体分析” 接口。
3. 进入 “人体分析” —— “管理应用”，得到 “BD_App_ID”、“BD_API_Key”、“BD_Secret_Key” 参数。编辑 `Config.ini` 文件 “百度AI API” 并运行程序。

该 API 对免费用户的限制为 QPS=2，可满足正常使用需求。百度 AI 付费用户可选使用高速通道。

### 自定义头像来源（不导入某些来源的头像）
Gfriends Inputer v2.73 及后续版本支持自定义头像来源。

在仓库中，可能收录了多张不同来源的同一女友头像。这时，默认根据头像质量及尺寸，自动选优后导入头像。<br>
但是，每个人的主观意识不同。比如，有的人可能不喜欢 Graphis 的头像，因为上面有标记女友名。有些人可能不喜欢 EBODY 的头像，因为女友衣着太暴露了。

编辑 `Config.ini` 文件 “厂牌黑名单”，填入厂牌的头像将不会被获取。

### 上传新的头像图片到仓库
欢迎提交优质的演员头像图片或写真。以下条件应 **尽可能** 满足：

1. 对应演员头像缺失或现有头像不堪入目。
2. 新头像是以女友为主体的特写或近景、近似 3:2 的长宽比，且宽度宜在 300px 以上。

如果您的图片符合上述要求，则可以通过如下步骤上传图片：

1. 轻击主仓库右上角 `Fork` 按钮，然后会自动克隆主仓库，并跳转到属于您的个人仓库。
2. 移步至个人仓库 `Content` 下的 `人工存储 HandStorage` 目录，该目录拥有最高优先级，能保证上传的图片被优先使用。
3. 轻击 `Add files` 菜单下的 `Upload files` 按钮，然后上传头像图片到仓库，图片应该以`演员日文姓名.jpg`来命名，女友仓库会自动匹配多语种姓名。在上传等待过程中，可以随便写一点 `Commit Changes` 说明，比如上传了哪些女友的图片。上传完成后轻击 `Commit` 提交。
4. 进入 `Pull Requests` 发起新的合并请求，请同时勾选 `Allow edits by maintainers`。在经过审核后，您的美图就可以和大家分享了。

P.S. 如果您发现某些女友未自动匹配多语种姓名，请提交 issue 告诉我她的日文姓名和译名。

### 共享头像图片来源网站

首先，该优质网站上的图片除了满足上述条件，还应尽可能满足：每位女友只有一张或少量的图片，以避免二次人工筛选。

如果您有这样的来源网站，那就太完美了~ 您只需提交一个 issue 告诉我地址即可。

### 对女友仓库的开发及调用
请务必先阅读 [法律信息及免责声明](#%E6%B3%95%E5%BE%8B%E4%BF%A1%E6%81%AF%E5%8F%8A%E5%85%8D%E8%B4%A3%E5%A3%B0%E6%98%8E)

1. `Filetree.json` 为 [内容 Content](https://github.com/xinxin8816/gfriends/tree/master/Content) 目录的 Json 文件树，在头像图片变化时将自动更新。该文件已按头像质量降序排列且已匹配多语言女友姓名，可供程序调用搜索。

2. 女友仓库通过 AI 移除违法头像（基于中国大陆法律）至 [回收站 Recycled](https://github.com/xinxin8816/gfriends/tree/master/.Recycled) 目录，如果想调用该目录的头像请自行遍历。下述仓库镜像中不包含此回收站目录。

3. 女友仓库通过 AI 放大并优化的低质量头像图片，但不能保证经优化的头像完美无瑕。若您不想调用获取到这些经 AI 优化的图片，只需删除文件树中的 `AI-Fix-` 前缀即可，仓库存储着未经 AI 处理的原始图片副本。

4. ~鉴于 GitHub 在全球网络中的连通性不一，此全球可达的仓库镜像供阁下备用：https://gfriends.imfast.io/~ 受服务提供商业务调整影响，镜像仓库将于 2020/12/31 关闭。

### 仓库更新计划
✔ 自动定期抓取新入职女友头像至仓库（仅后述标注 🌟）<br>
✔ 匹配多语种姓名（简体中文 / 繁体中文 / 日文）<br>
✔ AI 放大并优化低分辨率头像（仅后述标注 ➡）<br>
✔ AI 鉴别并移除违法违规头像

## 图片来源
排序不分前后 表格非即时更新<br>
标注🌟的图片为原生高质量大图，标注➡的图片为经过 AI 算法放大优化的图片。

### 第三方内容商
| 品牌 | 尺寸 |数量|简介|备注|
| :----: | :----: | :----: | :----: | :----: |
| [GRAPHIS](http://graphis.ne.jp/ "GRAPHIS") | 360×508 | 600+ | 著名的美女摄影写真机构 | 🌟 |
| [Juicy Honey](http://juicy-honey.com/ "Juicy Honey") | 640×960 | 30+ | X-City 旗下的写真分支 | 🌟 |
| [LovePop](https://lovepop.net/ "Lovepop") | 384×576 | 70+ | 美少女写真摄影机构 | 🌟 |
| [FANZA](http://dmm.co.jp/ "FANZA") | *inconsistent* | 1.5W+ | DMM官方 | ➡ |
| [Warashi](http://warashi-asian-pornstars.fr/ "Warashi") | 250×300 | 2800+ | 知名演员资料数据库 | ➡ *New Add!* |

### 品牌官方
| 品牌 | 尺寸 |数量|旗下知名小姐姐|备注|
| :----: | :----: | :----: | :----: | :----: |
| [S1 No. 1 Style](https://www.s1s1s1.com/ "S1 No. 1 Style") | 470×600 |300+|三上悠亜、羽咲みはる、桜羽のどか、架乃ゆら|🌟<br>人气与美形著称|
| [MUTEKI](https://www.mutekimuteki.com/ "MUTEKI") | 640×906|50+|深山あすか、水瀬ちあき、松本菜奈実、夢川エマ|🌟|
| [FaleNO](https://faleno.jp/ "FaleNO") | 1500×2125 |10+|桥本有菜、吉高寧々、美乃すずめ、佐藤ゆか|🌟 <br> U-next 旗下公司|
| [Attackers](https://www.attackers.net/ "Attackers") | 216×270|1000+|明里つむぎ、岬ななみ、二宮ひかり、結城のの|➡432×540|
| [Moodyz](https://www.moodyz.com/ "MOODYZ") | 600x783 |1300+|高桥しょう子、西宫このみ、伊东ちなみ、千早希|🌟|
| [Premium](http://www.premium-beauty.com/ "Premium") | 544x724 |100+|樱木凛、星野美优、冬月枫、二宫沙树|🌟|
| [Idea Pocket](https://www.ideapocket.com/ "Idea Pocket") | 300×300 |100+|天海つばさ、相沢みなみ、桃乃木かな、希崎ジェシカ|➡600×600|
| [KM Produce](https://www.km-produce.com/ "KM Produce") | 330×330|10+|川上优、麻生岬、麻仓忧、神咲诗织|➡660×660|
| [kawaii*](https://www.kawaiikawaii.jp/ "kawaii*") | 640×896|300+|ひなみちゃん、伊藤舞雪、宇佐木あいか、有栖るる|🌟|
| [Prestige<br>蚊香社](https://www.prestige-av.com/ "Prestige<br>蚊香社") | 119×170|200+|永瀬みなも、有村のぞみ、園田みおん、藤江史帆|绝对美少女制造商<br>➡476×680|
| [未満](http://www.miman.jp/ "未満") |290×390|100+|あやみ旬果、さくらゆら、高岡美鈴、高梨ゆあ|➡580×780|
| [无垢](http://www.muku.tv/ "无垢") |110×70|300+|河南実里、高杉麻里、本橋実来、大島美緒|➡440×280|
| [桃太郎映像](http://www.indies-av.co.jp/ "桃太郎映像") |451×600 | 200+ |宝生リリー、泉りおん、入江愛美、阿部乃みく|🌟<br>专业企划制造商|
| [えむっ娘ラボ](http://www.mko-labo.net/ "えむっ娘ラボ") | 168×191 |200+|有坂深雪、有村のぞみ、笹倉杏、上原亜衣|➡336×382|
| [OPPAI](http://www.oppai-av.com/ "OPPAI") | 312×364 |100+|浜崎真緒、成海さやか、美緒みくる、柊るい|➡624×728|
| [E-BODY](http://www.av-e-body.com/ "E-BODY") | 702x900|500+|Julia、红城まゆ、羽野理沙、蒂亚|🌟|
| [Wanz Factory](https://www.wanz-factory.com/ "Wanz Factory") | 280×280 |200+|椎名そら、つぼみ、水野朝陽、浅井ルリ子|➡560×560|
| [Honnaka<br>本中](https://www.honnaka.jp/ "Honnaka<br>本中") | 335×375 |300+|さわきりほ、さくらみゆき、つくしみか、あいだ飛鳥|➡670×750|
| [kira☆kira](https://www.kirakira-av.com/ "kira☆kira") |180×180|10+|加瀬エリナ、水谷心音、霧嶋りお、有村リア|➡360×360|
| [BeFree](https://www.befreebe.com/ "BeFree") | 215×215|100+|つぼみ、浜崎真緒、安藤美奈子、坂口れな|➡430×430|
| [痴女天堂](https://www.bi-av.com/ "痴女天堂") | 300×300|300+|大槻ひびき、沖田杏梨、大浦真奈美、渚みつき|➡600×600|
| [Fitch](https://www.fitch-av.com/ "Fitch") | 300×392|500+|春菜はな、美園和花、月森ゆの、河北はるな|➡600×786|
| [Madonna](https://www.madonna-av.com/ "Madonna") | 230×300|30+|美森けい、谷花紗耶、桜井ゆみ、今井ひまり|➡792×800|
| [溜池ゴロー](http://www.tameikegoro.jp/ "溜池ゴロー") |100×100|500+|めぐり、本田岬、かすみ果穂、さとう遥希|MOODYZ 旗下公司<br>➡400×400|
| [Das!](http://www.dasdas.jp/ "Das!") |280×280|300+|あべみかこ、冴月りん、跡美しゅり、一ノ瀬梓|➡560×560|
| [ラグジュTV](https://seesaawiki.jp/av_neme/d/%A5%E9%A5%B0%A5%B8%A5%E5TV/ "ラグジュTV") |116×236|900+|藤本ゆうり、美園和花、浜崎真緒、あやみ旬果|➡332×472|

## 扫黄打非 · 净网行动
鉴于女友仓库目前受众多为中国大陆地区用户，为积极配合中国大陆地区相关部门开展专项行动，女友仓库将依托于 AI 技术，尽最大可能鉴别和删除违规头像。在此呼吁广大用户自觉守法、相互监督，共同打造绿色健康的网络环境。

投诉邮箱：Gfriends#keemail.me

## 法律信息及免责声明
1. 本项目作者旨在学习 Python 后端，提高编程水平。
2. 项目仅用于技术、学术交流，严禁用于商业和其他盈利目的。
3. 请自觉遵守当地法律法规，产生的一切后果由用户自行承担。
4. 头像图片版权归相应网站及演员所属经纪公司所有。
5. 作者保留最终决定权和最终解释权。

若您不同意上述任一条款，请勿直接或间接使用本项目。
