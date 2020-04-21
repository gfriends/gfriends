# 女友头像仓库
![TotalNumber](https://img.shields.io/badge/TotalNum-1.20w-Blue.svg)  ![AutoUpdate](https://img.shields.io/badge/AutoUpdate-2020--4--21-green.svg)<br>
媒体服务器演员头像仓库<br>推荐搭配任一刮削整理项目 [JAVSDT](https://github.com/junerain123/javsdt "JAVSDT")、[JAVOneStop](https://github.com/ddd354/JAVOneStop "JAVOneStop")、[AVDC](https://github.com/moyy996/AVDC "AVDC") 及 Emby、Jellyfin、Plex 等媒体服务器使用。

## 使用说明
1. 本项目以抓取官方高质量大图为主要目标，满足数量需求为次要。
2. 头像图片为自动化抓取，部分人工筛选。
3. `Filetree.json` 为JSON格式的文件树，可供程序调用搜索。
4. 欢迎提交新来源网站和演员图片，图片版权归相应网站及演员所属经纪公司所有。

## 更新计划
✔ 自动定期抓取新入职女友头像至仓库（仅后述标注 ★ 官网）<br>
✔ 匹配简中/繁中/日文姓名<br>
✔ 移除低质量和重复头像<br>
✔ 裁剪以匹配 Emby 的特殊尺寸（需使用 Windows 导入工具）

此外后端进行了大量改写，文件树排序将更智能。

## 快速开始
可以通过这些工具方便的导入头像。

### Emby / Jellyfin

#### Windows
无需预先下载本仓库的女友头像，仅需下载 [Gfriends 一键导入工具](https://github.com/xinxin8816/gfriends/releases)，编辑 `Config.ini`文件并运行程序。<br>该工具将自动从本仓库搜索头像并导入你的服务器。

#### Linux / Mac
由 *JavScraper* 提供

1. 根据需求下载本仓库中的女友头像，并下载 [Linux / Mac 导入工具](https://github.com/JavScraper/Emby.Plugins.JavScraper/releases/download/v1.22.27.1109/Emby.Actress@20200202-dotnet_core.zip)，编辑 `Config.json`文件
- **url**：Emby / Jellyfin 服务器的地址
- **api_key**：Emby / Jellyfin 服务器的 API 密钥
- **dir**：女友头像所在文件夹，如果填入完整路径请使用 "/" 替换 "\\"
2. 运行 `dotnet Emby.Actress.dll`，若无法运行请安装依赖 [.NET Core 3.1 Runtime](https://dotnet.microsoft.com/download/dotnet-core/current/runtime)

### Plex
由 *ddd354* 提供

无需预先下载本仓库的女友头像，仅需为你的 Plex 服务器安装 [JAVnfoMoviesImporter](https://github.com/ddd354/JAVnfoMoviesImporter.bundle) 插件。<br>该插件将自动从本仓库搜索头像并导入你的服务器。

## 图片来源
标注☆的图片尺寸可直接用于媒体服务器。<br>标注★的图片为高质量大图，亦可直接用于媒体服务器。

### 第三方内容商
| 品牌 | 分辨率 |女友数量|简介|备注|
| :----: | :----: | :----: | :----: | :----: |
| [GRAPHIS](http://graphis.ne.jp/ "GRAPHIS") | 360*508 | 600+ | 著名的美女摄影写真机构 | ★ |
| [Juicy Honey](http://juicy-honey.com/ "Juicy Honey") | 640*960 | 30+ | X-City 旗下的写真分支 | ★ |
| [LovePop](https://lovepop.net/ "Lovepop") | 384*576 | 70+ | 美少女写真摄影机构 | *New Add!* ★ |

### 品牌官方
| 品牌 | 分辨率 |女友数量|旗下知名小姐姐|备注|
| :----: | :----: | :----: | :----: | :----: |
| [S1 No. 1 Style](https://www.s1s1s1.com/ "S1 No. 1 Style") | 470*600 |300+|三上悠亜、羽咲みはる、桜羽のどか、架乃ゆら|★<br>人气与美形著称|
| [MUTEKI](https://www.mutekimuteki.com/ "MUTEKI") | 640*906|50+|深山あすか、水瀬ちあき、松本菜奈実、夢川エマ|★ <br> “偶像艺人”系列|
| [FaleNO](https://faleno.jp/ "FaleNO") | 1500*2125 |10+|桥本有菜、吉高寧々、美乃すずめ、佐藤ゆか|★ <br> U-next 旗下公司|
| [Attackers](https://www.attackers.net/ "Attackers") | 216*270 |1000+|明里つむぎ、岬ななみ、二宮ひかり、結城のの|☆<br>“凌辱剧情”系列|
| [Moodyz](https://www.moodyz.com/ "MOODYZ") | 230*300 |1100+|高桥しょう子、西宫このみ、伊东ちなみ、千早希|☆|
| [Premium](http://www.premium-beauty.com/ "Premium") | 208*276 |100+|樱木凛、星野美优、冬月枫、二宫沙树|☆|
| [Idea Pocket](https://www.ideapocket.com/ "Idea Pocket") | 300*300 |100+|天海つばさ、相沢みなみ、桃乃木かな、希崎ジェシカ||
| [KM Produce](https://www.km-produce.com/ "KM Produce") | 330*330 |10+|川上优、麻生岬、麻仓忧、神咲诗织||
| [kawaii*](https://www.kawaiikawaii.jp/ "kawaii*") | 640*896|300+|ひなみちゃん、伊藤舞雪、宇佐木あいか、有栖るる|★<br>“女子大生”系列|
| [Prestige<br>蚊香社](https://www.prestige-av.com/ "Prestige<br>蚊香社") | 119*170|200+|永瀬みなも、有村のぞみ、園田みおん、藤江史帆|☆<br>自称绝对美少女制造商|
| [未満](http://www.miman.jp/ "未満") |290*390|100+|あやみ旬果、さくらゆら、高岡美鈴、高梨ゆあ|☆<br>“巨ru少女”系列|
| [无垢](http://www.muku.tv/ "无垢") |110*70|300+|河南実里、高杉麻里、本橋実来、大島美緒|“JK制服美少女”系列|
| [桃太郎映像](http://www.indies-av.co.jp/ "桃太郎映像") |451*600 | 200+ |宝生リリー、泉りおん、入江愛美、阿部乃みく|★<br>自称专业企划制造商|
| [えむっ娘ラボ](http://www.mko-labo.net/ "えむっ娘ラボ") | 168*191 |200+|有坂深雪、有村のぞみ、笹倉杏、上原亜衣|☆<br>“M女”系列|
| [OPPAI](http://www.oppai-av.com/ "OPPAI") | 312*364 |100+|浜崎真緒、成海さやか、美緒みくる、柊るい|☆<br>“欧派”系列|
| [E-BODY](http://www.av-e-body.com/ "E-BODY") | 312*400 |500+|Julia、红城まゆ、羽野理沙、蒂亚|☆|
| [Wanz Factory](https://www.wanz-factory.com/ "Wanz Factory") | 280*280 |200+|椎名そら、つぼみ、水野朝陽、浅井ルリ子||
| [Honnaka<br>本中](https://www.honnaka.jp/ "Honnaka<br>本中") | 335*375 |300+|さわきりほ、さくらみゆき、つくしみか、あいだ飛鳥|“中chu”系列|
| [kira☆kira](https://www.kirakira-av.com/ "kira☆kira") |180*180|10+|加瀬エリナ、水谷心音、霧嶋りお、有村リア|“辣妹”系列|
| [BeFree](https://www.befreebe.com/ "BeFree") | 215*215|100+|つぼみ、浜崎真緒、安藤美奈子、坂口れな|“Cosplay”系列|
| [痴女天堂](https://www.bi-av.com/ "痴女天堂") | 300*300|300+|大槻ひびき、沖田杏梨、大浦真奈美、渚みつき|“痴*女”系列|
| [Fitch](https://www.fitch-av.com/ "Fitch") | 300*392|500+|春菜はな、美園和花、月森ゆの、河北はるな|☆|
| [Madonna](https://www.madonna-av.com/ "Madonna") | 230*300|30+|美森けい、谷花紗耶、桜井ゆみ、今井ひまり|☆|
| [溜池ゴロー](http://www.tameikegoro.jp/ "溜池ゴロー") |100*100|500+|めぐり、本田岬、かすみ果穂、さとう遥希|MOODYZ 旗下公司|
| [Das!](http://www.dasdas.jp/ "Das!") |280*280|300+|あべみかこ、冴月りん、跡美しゅり、一ノ瀬梓|“强X”系列|
| [ラグジュTV](https://seesaawiki.jp/av_neme/d/%A5%E9%A5%B0%A5%B8%A5%E5TV/ "ラグジュTV") |116*236|900+|藤本ゆうり、美園和花、浜崎真緒、あやみ旬果| *New Add!* ☆|

## 免责声明
1. 本项目作者旨在学习 Python 后端，提高编程水平。
2. 项目仅用于技术、学术交流，严禁用于商业和其他盈利目的。
3. 请自觉遵守当地法律法规，产生一切违法后果由用户自行承担。
4. 作者保留最终决定权和最终解释权。

若您不同意上述任一条款，请勿直接或间接使用本项目。