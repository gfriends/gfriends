<img src="https://avatars.githubusercontent.com/u/109220009?s=200" alt="logo" width="140" height="140" align="right">

# Gfriends 女友头像仓库
![TotalNumber](https://img.shields.io/badge/TotalNum-103,003-blueviolet.svg)  ![AutoUpdate](https://img.shields.io/badge/AutoUpdate-2024--6--22-brightgreen.svg)  ![GfriendBot](https://img.shields.io/badge/GfriendBot-Working-blue.svg?logo=Dependabot)<br>
媒体服务器演员头像仓库。<br>旨在满足数量需求前提下，尽可能收集和处理高质量女友头像，并提供导入媒体服务器方案。<br>
> *There is no correlation between this repo and Korean girl group GFRIEND.*

## 目录
* [快速开始](#快速开始)
   * [Emby / Jellyfin](#emby--jellyfin)
   * [Plex](#plex)
* [进阶玩法](#进阶说明)
   * [手动搜索头像](https://github.com/xinxin8816/gfriends/find/master) (日文姓名)
   * 成为 Gfriends 女友头像仓库的贡献者
      * [上传新的头像到仓库](#上传新的头像图片到仓库)
      * [开发及调用](#对女友仓库的开发及调用)
   * 衍生项目
     * [Gfriends Inputer](https://github.com/gfriends/gfriends-inputer)
     * [PornChecker](https://github.com/gfriends/pornchecker)
* [更新计划](#更新计划)
* [图片来源](#图片来源)
   * [第三方内容商](#第三方内容商)
   * [经纪公司](#经纪公司)
   * [品牌官方](#品牌官方)
* [法律信息](#法律信息及免责声明)

## 快速开始
已有多款软件使用女友仓库作为数据源。对于一般用户来说，无需手动下载头像，即可通过以下方案导入头像。

### Emby / Jellyfin
**1. [Gfriends Inputer](https://github.com/gfriends/gfriends-inputer)**<br>*由 Gfriends 提供*

> 官方维护的 Jellyfin/Emby 头像导入工具，兼容女友仓库所有特性，全平台支持。

**2. [MDCx](https://github.com/anyabc/something)**<br>*由 Hermit 提供*

> 演化自 MDC 的图形化刮削软件，支持带桌面的 Windows 和 MacOS。

<details>
<summary>或者试试安装插件导入？</summary>

**3. [JavScraper](https://github.com/JavScraper/Emby.Plugins.JavScraper)**<br>*由 JavScraper 提供*

> 一个 Jellyfin/Emby 的日本电影刮削器插件，Emby JAV 刮削器元老。

**4. [MetaTube](https://github.com/javtube/jellyfin-plugin-javtube)**<br>*由 MetaTube 提供*

> 另一个为 Jellyfin/Emby 开发的好用插件，插件前端与刮削器后端分离，上手稍难。

</details>

### Plex
**1. [JAVnfoMoviesImporter](https://github.com/ddd354/JAVnfoMoviesImporter.bundle)**<br>*由 ddd354 提供*

> 基于 XBMCnfoMoviesImporter 修改的插件，增加了女友头像功能。

**2. [JAV.bundle](https://github.com/Xavier-Lam/JAV.bundle)**<br>*由 Xavier-Lam 提供*

> 受 JAVLibrary.bundle 启发而开发的新插件，亦提供了 JAV 元数据刮削功能。

### 更多工具
推荐与 Gfriends Inputer 搭配刮削整理项目，神兵利器助您事半功倍。

[Movie Data Capture](https://github.com/yoshiko2/AV_Data_Capture "AV Data Capture")、
[AVDC GUI](https://github.com/moyy996/AVDC "AVDC GUI")、
[JAVSDT](https://github.com/junerain123/javsdt "JAVSDT")、
[JAVOneStop](https://github.com/ddd354/JAVOneStop "JAVOneStop")、
[Avutil](https://github.com/Lqlsoftware/Avutil "Avutil")

*您知道其他相似的开源工具？欢迎提交 issues 告诉我。*

## 进阶说明
本项目以抓取官方高质量大图为主要目标，头像图片为自动化抓取，部分人工筛选。

### 上传新的头像图片到仓库
欢迎提交优质的演员头像图片或写真。以下条件应 **尽可能** 满足：

1. 对应演员头像缺失或现有头像不堪入目。
2. 新头像是以女友为主体的特写或近景、近似 3:2 的长宽比，且宽度宜在 300px 以上。

如果您的图片符合上述要求，则可以通过如下步骤上传图片：

1. 轻击主仓库右上角 `Fork` 按钮，然后会自动克隆主仓库，并跳转到属于您的个人仓库。
2. 移步至个人仓库 `Content` 下的 `人工存储 HandStorage` 目录，该目录拥有最高优先级，能保证上传的图片被优先使用。
3. 轻击 `Add files` 菜单下的 `Upload files` 按钮，然后上传头像图片到仓库，图片应该以`演员日文姓名.jpg`来命名（请注意，仅支持*jpg*），女友仓库会自动匹配多语种姓名。在上传等待过程中，可以随便写一点 `Commit Changes` 说明，比如上传了哪些女友的图片。上传完成后轻击 `Commit` 提交。
4. 进入 `Pull Requests` 板块下，点击 `New Pull Requests` 发起新的合并请求。稍等片刻，待仓库自动检查完成后，点击 `Create Pull Requests` 并轻击 `Commit`提交，请同时勾选 `Allow edits by maintainers`。
5. 至此，在经过人工审核和文件树自动刷新后，您的美图就可以和大家分享了。

P.S. 如果您发现某些女友未自动匹配别名，请提交 issue 告诉我她的日文姓名和别名。<br>
您可以使用 [文件检索](https://github.com/xinxin8816/gfriends/find/master) 来搜索仓库中存储的头像文件，该功能仅支持日文名。

### 对女友仓库的开发及调用
请务必先阅读 [法律信息及免责声明](#%E6%B3%95%E5%BE%8B%E4%BF%A1%E6%81%AF%E5%8F%8A%E5%85%8D%E8%B4%A3%E5%A3%B0%E6%98%8E)；[快速开始](#快速开始) 所列出的工具均已开源，可供阁下在开发时参考。

#### 【Json 文件树】

位于根目录的`Filetree.json`，是 [内容 Content](https://github.com/xinxin8816/gfriends/tree/master/Content) 文件夹的文件树，在头像图片变化时自动更新，可供程序调用搜索。
*P.S. 在请求头中开启 Gzip 压缩可以大幅减少下载文件树所需的流量*

以下是文件树格式示例：

```json
{
  "Information": {
    "TotalNum": "TotalNum",
    "TotalSize": "TotalSize",
    "Timestamp": "Timestamp"
  },
  "Content": {
    "CompanyNameA": {
      "ActorNameA.jpg": "ActorNameA.jpg?t=FileATimestamp",
      "ActorNameB.jpg": "ActorNameB.jpg?t=FileBTimestamp",
    },
    "CompanyNameB": {
      "ActorNameA.jpg": "ActorNameA.jpg?t=FileATimestamp",
      "ActorNameB.jpg": "ActorNameB.jpg?t=FileBTimestamp",
    },
}
```

通过拼接 URL，您可以获得对应女友头像的下载链接。

这些值得留意：
1. `Information` 对象内字段依次为：头像总数量 `TotalNum`、头像大小之和 `TotalSize`、文件树完成生成的微秒级时间戳 `Timestamp`。
2. `Content` 对象内字段按头像图片 **质量升序** 排列，参数 `t` 为头像文件更新时间的秒级时间戳 `FileTimestamp`。更多细节请继续往下阅读。

**1. 多头像匹配**

部分女友可能在多个厂牌下任职，亦或者参与过写真拍摄等，不排除同一位女友在仓库中存储了多张图片的情况。

```json
{
  "Content": {
    "CompanyNameA": {
      "三上悠亚.jpg": "三上悠亚.jpg",
      "三上悠亚-1.jpg": "三上悠亚-1.jpg",
      "三上悠亚-2.jpg": "三上悠亚-2.jpg",
    },
    "CompanyNameB": {
      "三上悠亚.jpg": "三上悠亚.jpg",
      "三上悠亚-1.jpg": "三上悠亚-1.jpg",
    },
    "CompanyNameC": {
      "三上悠亚.jpg": "三上悠亚.jpg",
    },
}
```

**2. 多姓名匹配**

仓库已匹配女友的多语种姓名、艺名、片假名，甚至是素人佚名等别名。

但提请注意：无论何时，都应首先使用 **主流艺名** 为关键词进行搜索。

```
艺    名：妃月るい
简中译名：妃月由衣
繁中译名：紀月留衣
片 假 名：るいぺち
罗马拼音：Hiduki Rui、Rui Hiduki
素人佚名：Rui
曾 用 名：川島今日子、如月るい、日向美月、森平みさき、石原美紀、紀月るい
```
```json
{
  "Content": {
    "CompanyNameA": {
      "妃月るい.jpg": "妃月るい.jpg",
      "妃月由衣.jpg": "妃月るい.jpg",
      "紀月留衣.jpg": "妃月るい.jpg",
      "るいぺち.jpg": "妃月るい.jpg",
      "Hiduki Rui.jpg": "妃月るい.jpg",
      "Rui Hiduki.jpg": "妃月るい.jpg",
      "川島今日子.jpg": "妃月るい.jpg",
      "如月るい.jpg": "妃月るい.jpg",
      "日向美月.jpg": "妃月るい.jpg",
      "森平みさき.jpg": "妃月るい.jpg",
      "石原美紀.jpg": "妃月るい.jpg",
      "紀月るい.jpg": "妃月るい.jpg",
}
```

**3. AI 技术的应用**

女友仓库通过 AI 鉴别并移除的违法头像，还会借助 AI 无损放大并优化的低质量头像图片、去除图片中的水印（如果有）。

```json
{
  "Content": {
    "CompanyNameA": {
      "吉高寧々.jpg": "AI-Fix-吉高寧々.jpg",
}
```
女友仓库无法保证这些经优化的头像完美无瑕。若您不想调用获取到这些经 AI 优化的图片，只需删除文件树中的 `AI-Fix-` 前缀即可，仓库存储着未经 AI 处理的原始图片副本。
```json
{
  "Content": {
    "CompanyNameA": {
      "吉高寧々.jpg": "吉高寧々.jpg",
}
```

#### 【Recycled 回收站】
[回收站 Recycled](https://github.com/xinxin8816/gfriends/tree/master/.Recycled) 目录是通过 AI 鉴别并移除的违法头像（基于中国大陆法律）。

文件树中不包含该目录，如有调用该目录需求请自行遍历。

#### 【CDN 加速的镜像仓库】
鉴于 GitHub 在全球网络中的连通性不一，此全球可达的仓库镜像供阁下备用：https://cdn.jsdelivr.net/gh/xinxin8816/gfriends/

该链接仅供调用，无法使用浏览器直接访问

## 更新计划
女友仓库目前已趋于稳定，一段时间内不会有大型更新迭代。GfriendBot 将自动定期更新仓库内容。

✔ 自动定期抓取新入职女友头像至仓库（仅后述标注 🌟）<br>
✔ 匹配多语种姓名（简体中文 / 繁体中文 / 日文）<br>
✔ 匹配女友的多个艺名<br>
✔ AI 放大并优化低分辨率头像（仅后述标注 ➡）<br>
✔ AI 鉴别并移除违法违规头像<br>
✔ AI 移除头像水印

## 图片来源
排序不分前后，表格更新可能滞后。<br>
标注🌟的图片为原生高质量大图，标注➡的图片为经过 AI 算法放大优化的图片。<br>
除下表外，仓库中还收录了热心网友提供或上传的头像，位于 `人工存储 HandStorage` 目录，后述法律信息同样适用于此。

### 第三方内容商
| 品牌 | 尺寸 |数量|简介|备注|
| :----: | :----: | :----: | :----: | :----: |
| [GRAPHIS](http://graphis.ne.jp/ "GRAPHIS") | 360×508 | 600+ | 知名的美女摄影写真机构 | 🌟 |
| [Juicy Honey](http://juicy-honey.com/ "Juicy Honey") | 640×960 | 30+ | X-City 旗下的写真分支 | 🌟 |
| [LovePop](https://lovepop.net/ "Lovepop") | 384×576 | 70+ | 美少女写真摄影机构 | 🌟 |
| [FANZA](http://dmm.co.jp/ "FANZA") | *inconsistent* | 15,000+ | FANZA 官方（原DMM） | ➡ |
| [Warashi](http://warashi-asian-pornstars.fr/ "Warashi") | 250×300 | 2800+ | 来自法国的演员数据库 | ➡ |
| [Javrave](https://javrave.club/ "Javrave") | *inconsistent* | 6800+ | 知名的演员资料数据库 | ➡ |
| [Nanairo](https://nanairo.co/ "Nanairo") | 400×400 | 700+ | S-cute 旗下流媒体 | 🌟 |
| [AVDBS](https://www.avdbs.com/ "AVDBS") | 380×460 | 800+ | 来自韩国的演员数据库 | ➡ |
| [Derekhsu](http://wiki.derekhsu.net/ "Derekhsu") | *inconsistent* | 3700+ | 来自中国台湾的演员维基 | |
| [Minnano](http://www.minnano-av.com/ "Minnano") | *inconsistent* | 19,000+ | 来自日本的信息交流站 | ➡ *New Add!* |
| [DigiGra](https://digi-gra.net/ "DigiGra") | 380x576 | 750+ | ImageBox 旗下流媒体 | 🌟 *New Add!* |

### 经纪公司
| 品牌 | 尺寸 |数量|旗下知名小姐姐|备注|
| :----: | :----: | :----: | :----: | :----: |
| [Diaz Group](http://diaz-g.com/ "Diaz-z") | 2880×1800 | 10+ | 友田彩也香、東凛、卯水咲流、長瀬麻美 | 🌟 *New Add!*|
| [T-powers](https://www.t-powers.co.jp/ "T-powers") | 948×948 | 130+ | 天海つばさ、野々浦暖、河合あすな、结城のの | 🌟 *New Add!* <br> 最大的女友经纪公司|
| [Bambi](https://bambi.ne.jp/ "Bambi") | 500×500 | 30+ | 星奈あい、藍芽みずき、西村ニーナ、天音ゆい | 🌟 *New Add!*|
| [Eightman](http://www.8man.jp/ "Eightman") | 600×800 | 50+ | 葵つかさ、吉高寧々、七海ティナ、つばさ舞 | 🌟 *New Add!* <br> 位于关西的事务所|
| [Mine's](https://mines-pro.jp/ "Mine's") | 300×300 | 40+ | 明里ともか、朝倉ここな、あさみ潤、幾田まち | 🌟 *New Add!*|
| [C-more](https://cmore.jp/ "C-more") | 1920×1080 | 30+ | JULIA、明里つむぎ、本庄鈴、桐谷まつり | 🌟 *New Add!*|
| [Arrows](https://arrowsweb.net/ "Arrows") | 720×1000 | 10+ | 松本いちか、七嶋舞、今井夏帆、月野かすみ | 🌟 *New Add!*|
| [Capsule](https://capsule.bz/ "Capsule") | 1920×2560 | 30+ | 七沢みあ、香坂紗梨、稲森美優、結菜さき | 🌟 *New Add!*|
| [AllPro](https://all-p.jp/ "AllPro") | *inconsistent* | 30+ | 佐知子、八乃つばさ、加藤ツバキ、夏川うみ | 🌟 *New Add!* <br> [AllGroup](https://all-grp.com/ "AllGroup") 旗下企业|
| [Attractive](https://attractive-llc.net/ "Attractive") | *inconsistent* | 20+ | 永瀬ゆい、楓ふうあ、葵いぶき、皆瀬あかり | 🌟 *New Add!*|

### 品牌官方
| 品牌 | 尺寸 |数量|旗下知名小姐姐|备注|
| :----: | :----: | :----: | :----: | :----: |
| [S1 No. 1 Style](https://www.s1s1s1.com/ "S1 No. 1 Style") | 470×600 |300+|三上悠亜、羽咲みはる、桜羽のどか、架乃ゆら|🌟<br>人气与美形著称|
| [MUTEKI](https://www.mutekimuteki.com/ "MUTEKI") | 640×906|50+|深山あすか、水瀬ちあき、松本菜奈実、夢川エマ|🌟|
| [FaleNO](https://faleno.jp/ "FaleNO") | 1500×2125 |10+|桥本有菜、吉高寧々、美乃すずめ、佐藤ゆか|🌟 <br> AllPro 旗下公司|
| [Dahlia](https://dahlia-av.jp/ "Dahlia") | 1500×2125 |10+|水川潤、徳永しおり、月見伊織、本田もも|🌟 *New Add!* <br> FaleNO 旗下品牌|
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
| [kira☆kira](https://www.kirakira-av.com/ "kira☆kira") |180×180|170+|加瀬エリナ、水谷心音、霧嶋りお、有村リア|➡360×360|
| [BeFree](https://www.befreebe.com/ "BeFree") | 215×215|100+|つぼみ、浜崎真緒、安藤美奈子、坂口れな|➡430×430|
| [痴女天堂](https://www.bi-av.com/ "痴女天堂") | 300×300|300+|大槻ひびき、沖田杏梨、大浦真奈美、渚みつき|➡600×600|
| [Fitch](https://www.fitch-av.com/ "Fitch") | 300×392|500+|春菜はな、美園和花、月森ゆの、河北はるな|➡600×786|
| [Madonna](https://www.madonna-av.com/ "Madonna") | 230×420|1700+|美森けい、谷花紗耶、桜井ゆみ、今井ひまり|🌟|
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
