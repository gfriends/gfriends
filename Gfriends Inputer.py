# -*- coding:utf-8 -*-
# Gfriends Inputer / 女友头像仓库导入工具
# Licensed under the MIT license.
# Designed by xinxin8816, many thanks for junerain123, ddd354, moyy996.
version = 'v2.72'

import requests, os, sys, time, re, threading
from configparser import RawConfigParser
from base64 import b64encode
from traceback import format_exc
from json import loads
from PIL import Image,ImageFilter
from aip import AipBodyAnalysis
from alive_progress import alive_bar

def fix_size(type,path):
	pic = Image.open(path)
	(wf,hf) = pic.size
	if not 2/3-0.02 <= wf/hf <= 2/3+0.02: #仅处理会过度拉伸的图片
		if type == '1':
			fixed_pic = pic.resize((int(wf),int(3/2*wf))) #拉伸图片
			fixed_pic = fixed_pic.filter(ImageFilter.GaussianBlur(radius=50)) #高斯平滑滤镜
			fixed_pic.paste(pic,(0,int((3/2*wf-hf)/2))) #粘贴原图
			fixed_pic.save(path, quality=95)
		elif type == '2':
			fixed_pic = pic.crop((int(wf/2-1/3*hf),0,int(wf/2+1/3*hf),int(hf))) #像素中线向两边扩展
			fixed_pic.save(path, quality=95)
		elif type == '3':
			try:
				with open(path, 'rb') as fp:
					image = fp.read()
					x_nose = int(BD_AI_client.bodyAnalysis(image)["person_info"][0]['body_parts']['nose']['x']) #返回鼻子横坐标
					if BD_VIP == '否':
						time.sleep(0.4) # 免费用户QPS=2
					else:
						time.sleep( 1/int(1.1*BD_VIP) )
					if x_nose + 1/3*hf > wf: #判断鼻子在图整体的位置
						x_left = wf-2/3*hf #以右为边
					elif x_nose - 1/3*hf < 0:
						x_left = 0 #以左为边
					else:
						x_left = x_nose-1/3*hf #以鼻子为中线向两边扩展
					fixed_pic = pic.crop((x_left,0,x_left+2/3*hf,hf))
					fixed_pic.save(path, quality=95)
			except:
				print('!! '+ str(path) +' AI 分析失败，跳过 AI 直接裁剪。\n')
				fix_size('2',path)
		else:
			print('× 头像处理功能配置错误，没有此选项：' + str(type))
			sys.exit()

def get_gfriends_map(repository_url):
	rewriteable_word('>> 下载头像仓库文件树...')
	if repository_url == '默认/': repository_url = 'https://raw.githubusercontent.com/xinxin8816/gfriends/master/'
	github_template = repository_url+'{}/{}/{}'
	if aifix:
		request_url = repository_url+'Filetree.json'
	else:
		request_url = repository_url+'Filetree-NonFix.json'
	try:
		if proxy == '不使用':
			response = session.get(request_url)
		else:
			response = session.get(request_url, proxies = proxies)
		# 修复部分服务端返回 header 未指明编码使后续解析错误
		response.encoding = 'utf-8' 
	except:
		if debug: print(format_exc())
		print('× 网络连接异常且重试 ' + str(max_retries) + ' 次失败')
		print('× 请尝试开启全局代理或配置 HTTP 局部代理；若已开启代理，请检查其可用性')
		sys.exit()
	if response.status_code != 200:
		print('× 女友仓库返回了一个错误： {}'.format(response.status_code))
		sys.exit()
	if aifix:
		map_json = loads(response.text)
	else:
		map_json = loads(response.text.replace('AI-Fix-',''))
	output = {}
	first_lvls = map_json.keys()
	for first in first_lvls:
		second_lvls = map_json[first].keys()
		for second in second_lvls:
			for k, v in map_json[first][second].items():
				output[k[:-4]] = github_template.format(first, second, v)
	print('√ 读取头像仓库文件树完成')
	print('   当前仓库头像数量：' + str(response.text.count('\n')) + '枚\n')
	return output

def asyncc(f):
    def wrapper(*args, **kwargs):
        thr = threading.Thread(target=f, args=args, kwargs=kwargs)
        thr.start()
    return wrapper
	
@asyncc
def download_avatar(url,actor_name):
	if proxy == '不使用':
		response = session.get(url)
	else:
		response = session.get(url, proxies = proxies)
	pic_path = download_path+actor_name+".jpg"
	with open(pic_path,"wb") as code:
		code.write(response.content)

@asyncc
def input_avatar(url,data):
	session.post(url, data=data, headers={"Content-Type": 'image/jpeg',"User-Agent": 'Gfriends_Inputer/'+version.replace('v','')})

def get_gfriends_link(name):
	if name in gfriends_map:
		output = gfriends_map[name]
		return output
	else:
		return None

def read_config():
	rewriteable_word('>> 读取配置...')
	if os.path.exists('config.ini'):
		config_settings = RawConfigParser()
		try:
			config_settings.read('config.ini', encoding='UTF-8-SIG') # UTF-8-SIG 适配 Windows 记事本
			repository_url = config_settings.get("下载设置", "Repository_Url")
			host_url = config_settings.get("媒体服务器", "Host_Url")
			api_key = config_settings.get("媒体服务器", "Host_API")
			max_download_connect = config_settings.get("下载设置", "MAX_DL")
			max_retries = config_settings.get("下载设置", "MAX_Retry")
			proxy = config_settings.get("下载设置", "Proxy")
			download_path = config_settings.get("下载设置", "Download_Path")
			max_upload_connect = config_settings.get("导入设置", "MAX_UL")
			local_path = config_settings.get("导入设置", "Local_Path")
			BD_App_ID = config_settings.get("导入设置", "BD_App_ID")
			BD_API_Key = config_settings.get("导入设置", "BD_API_Key")
			BD_Secret_Key = config_settings.get("导入设置", "BD_Secret_Key")
			BD_VIP = config_settings.get("导入设置", "BD_VIP")
			aifix = True if config_settings.get("下载设置", "AI_Fix") == '是' else False
			overwrite = True if config_settings.get("导入设置", "OverWrite") == '是' else False
			debug = True if config_settings.get("调试功能", "DeBug") == '是' else False
			deleteall = True if config_settings.get("调试功能", "DEL_ALL") == '是' else False
			fixsize = config_settings.get("导入设置", "Size_Fix")
			# 修正用户的URL
			if not host_url.endswith('/'): host_url += '/'
			if not repository_url.endswith('/'): repository_url += '/'
			# 创建文件夹
			if not os.path.exists(download_path):
				os.makedirs(download_path)
				write_txt(download_path+"/README.txt",'本目录自动生成，用于存放从仓库下载和处理过的头像。')
			if not os.path.exists(local_path):
				os.makedirs(local_path)
				write_txt(local_path+"/README.txt",'本目录自动生成，您可以存放自己收集的头像，这些头像将被优先导入服务器。\n\n请自行备份您收集头像的副本，根据个人配置不同，该目录文件可能会被程序修改。\n\n仅支持JPG格式，且请勿再创建子目录。\n\n如果您收集的头像位于子目录，可通过 Move To Here.bat（Only for Windows） 工具将其全部提取到根目录。')
				write_txt(local_path+"/Move To Here.bat",'@echo off\necho This tool will help you move all files which in the subdirectory to this root directory\npause\nfor /f "delims=" %%a in ("dir /a-d /b /s ") do (\nmove "%%~a" ./ 2>nul\n)\n')
			if fixsize == '3': BD_AI_client = AipBodyAnalysis(BD_App_ID, BD_API_Key, BD_Secret_Key)
			return (repository_url,host_url,api_key,overwrite,fixsize,int(max_retries),proxy,aifix,debug,deleteall,download_path,local_path,int(max_download_connect),int(max_upload_connect),BD_AI_client,BD_VIP)
		except:
			print(format_exc())
			print('× 无法读取 config.ini。如果这是旧版本的配置文件，请删除后重试。\n')
			print('按任意键退出程序...')
			os.system('pause>nul')
			sys.exit()
	else:
		content='''[媒体服务器]
# Emby / Jellyfin 服务器地址
Host_Url = http://localhost:8096/
	
# Emby / Jellyfin API 密钥
Host_API = 

[下载设置]
# 下载文件夹
Download_Path = ./Downloads/

# 下载线程数
# 若网络不稳定、丢包率或延迟较高，可适当减小下载线程数
MAX_DL = 5

# 下载失败重试数
# 若网络不稳定、丢包率或延迟较高，可适当增加失败重试数
MAX_Retry = 3

# 女友头像仓库源
# "默认"使用官方主仓库：https://raw.githubusercontent.com/xinxin8816/gfriends/master/
# 官方备用镜像（镜像下载线程数不允许大于5）：https://gfriends.imfast.io/，受服务提供商业务调整影响，镜像仓库将于 2020/12/31 关闭。
Repository_Url = 默认

# AI 优化（仅支持官方源）
# 在不可避免下载低质量头像时，自动挑选经 AI 算法放大优化的副本，质量更高但更占空间
AI_Fix = 是

# HTTP / Socks 局部代理
# 推荐开启全局代理而不是使用此局部代理
# HTTP 代理格式为 http://IP:端口 , 如 http://localhost:8088
# Socks 代理格式为 socks+协议版本://IP:端口 , 如 socks5://localhost:8087
Proxy = 不使用

[导入设置]
# 本地头像文件夹
# 将第三方头像包或自己收集的头像移动至该目录，可优先于仓库导入服务器。仅支持非子目录下的 jpg 格式。
Local_Path = ./Avatar/

# 覆盖已有头像
OverWrite = 是

# 导入线程数
# 导入至本地或内网服务器时，网络稳定可适当增大导入线程数（推荐：20-100）
# 导入至远程服务器时，可适当减小导入线程数（推荐：5-20）
MAX_UL = 20

# 头像尺寸优化
# 避免媒体服务器拉伸比例不符合 2:3 的头像
# 0 - 不处理直接导入
# 1 - 高斯平滑处理（填充毛玻璃样式）
# 2 - 直接裁剪处理（可能会裁剪到演员面部）
# 3 - AI检测并裁剪处理（需配置百度人体定位 AI，免费用户QPS=2，处理速度慢）
Size_Fix = 2

# 百度人体定位 AI
# 具体使用说明请参阅仓库项目 README
# 免费个人用户 QPS=2 处理速度慢。付费个人用户和企业用户请修改 BD_VIP 为您购买的 QPS 额度值，免费个人用户修改后会报错。
BD_VIP = 否
BD_App_ID = 
BD_API_Key = 
BD_Secret_Key = 

[调试功能]
# 删除所有头像
DEL_ALL = 否

# 输出详尽错误
DeBug = 否'''
		write_txt("config.ini",content)
		print('× 没有找到 config.ini。已为阁下生成，请修改配置后重新运行程序。\n')
		print('按任意键退出程序...')
		os.system('pause>nul')
		sys.exit()

def read_persons(host_url,api_key):
	rewriteable_word('>> 读取 Emby / Jellyfin 演员...')
	emby = True
	host_url_persons = host_url + 'emby/Persons?api_key=' + api_key	 # &PersonTypes=Actor
	try:
		rqs_emby = session.get(url=host_url_persons, headers={"User-Agent": 'Gfriends_Inputer/'+version.replace('v','')})
	except session.exceptions.ConnectionError:
		print('× 连接 Emby / Jellyfin 服务器失败，请检查：', host_url, '\n')
		sys.exit()
	except:
		if debug: print(format_exc())
		print('× 连接 Emby / Jellyfin 服务器未知错误：', host_url, '\n')
		sys.exit()
	if rqs_emby.status_code == 401:
		print('× 无权访问 Emby / Jellyfin 服务器，请检查 API 密匙\n')
		sys.exit()
	if rqs_emby.status_code == 404:
		try:
			rewriteable_word('>> 可能是新版 Jellyfin，尝试重新读取...')
			emby = False
			host_url_persons = host_url + 'jellyfin/Persons?api_key=' + api_key	 # &PersonTypes=Actor
			rqs_emby = session.get(url=host_url_persons, headers={"User-Agent": 'Gfriends_Inputer/'+version.replace('v','')})
		except:
			if debug: print(format_exc())
			print('× 读取 Emby / Jellyfin 演员列表返回 404，可能是未适配的版本：', host_url, '\n')
			sys.exit()
	output = loads(rqs_emby.text)['Items']
	print('√ 读取 Emby / Jellyfin 演员完成\n')
	return (output,emby)

def write_txt(filename,content):
	txt = open(filename, 'a', encoding="utf-8")
	txt.write(content)
	txt.close()
		
def rewriteable_word(word):
	for t in ['', word]: sys.stdout.write('\033[K' + t + '\r')
		
def del_all():
	print('【调试模式】删除所有头像\n')
	(list_persons,emby) = read_persons(host_url,api_key)
	rewriteable_word('按任意键开始...')
	os.system('pause>nul')
	for dic_each_actor in list_persons:
		if dic_each_actor['ImageTags']:
			actor_name = dic_each_actor['Name']
			print('>> 删除：', actor_name)
			if emby:
				url_post_img = host_url + 'emby/Items/' + dic_each_actor['Id'] + '/Images/Primary?api_key=' + api_key
			else:
				url_post_img = host_url + 'jellyfin/Items/' + dic_each_actor['Id'] + '/Images/Primary?api_key=' + api_key
			session.delete(url=url_post_img)
	print('√ 删除完成')
	print('按任意键退出程序...')
	os.system('pause>nul')
	sys.exit()

def check_update():
	rewriteable_word('>> 检查更新...')
	try:
		if proxy == '不使用':
			response = session.get('https://api.github.com/repos/xinxin8816/gfriends/releases')
		else:
			response = session.get('https://api.github.com/repos/xinxin8816/gfriends/releases', proxies = proxies)
		response.encoding = 'utf-8'
		if response.status_code != 200:
			print('× 检查更新失败！返回了一个错误： {}\n'.format(response.status_code))
			rewriteable_word('按任意键跳过...')
			os.system('pause>nul')	
		if version.replace('v','') < loads(response.text)[0]['tag_name'].replace('v',''):
			print(loads(response.text)[0]['tag_name']+' 新版本发布啦！\n')
			print(re.search('What\'s New?.*?(?=\r\n<details>)',loads(response.text)[0]['body'],flags=re.S).group(0).replace('*',''))
			print('请通过如下链接更新：\nhttps://github.com/xinxin8816/gfriends/releases\n')		
			rewriteable_word('按任意键跳过更新...')
			os.system('pause>nul')
			print('即将跳过更新。不推荐跳过更新，如遇问题请及时更新。')
			time.sleep(5)
	except:
		if debug: print(format_exc())
		print('× 检查更新失败！\n')
		rewriteable_word('按任意键跳过...')
		os.system('pause>nul')
	os.system('cls')

os.system('title Gfriends Inputer '+version)
(repository_url,host_url,api_key,overwrite,fixsize,max_retries,proxy,aifix,debug,deleteall,download_path,local_path,max_download_connect,max_upload_connect,BD_AI_client,BD_VIP) = read_config()


#持久会话
session = requests.Session()
session.mount('http://', requests.adapters.HTTPAdapter(max_retries=max_retries))
session.mount('https://', requests.adapters.HTTPAdapter(max_retries=max_retries))

#局部代理
if not proxy == '不使用': proxies={'http': proxy,'https': proxy}

#检查更新
check_update()
if deleteall: del_all()

num_suc = num_fail = num_skip = num_exist = 0
name_list = []
link_list = []
actor_dict = {}

print('Gfriends Inputer '+version)
print('https://github.com/xinxin8816/gfriends')
if proxy == '不使用':
	print('推荐开启全局代理以加快下载速度\n')
else:
	print('已配置局部代理 ' + proxy + '，请确保其可用\n')

rewriteable_word('按任意键开始...')
os.system('pause>nul')

try:
	(list_persons,emby) = read_persons(host_url,api_key)
	gfriends_map = get_gfriends_map(repository_url)
	if os.path.exists('未收录的演员清单.txt'): os.remove('未收录的演员清单.txt')
	write_txt("未收录的演员清单.txt",'【未收录的演员清单】\n（!!该清单仅供参考，正规影片演员、非日本女友、导演、编导、作品系列名及一些稀奇古怪的名字均可能出现在该清单中。但这些人员，女友头像仓库不会收录!!）\n\n')
	if os.path.exists('已匹配的演员清单.txt'): os.remove('已匹配的演员清单.txt')
	write_txt("已匹配的演员清单.txt",'【已匹配的演员清单】\n（!!该清单仅记录从女友仓库找到了头像的演员。根据个人配置，可能会下载导入，也可能会跳过!!）\n\n')
	print('>> 初始化...')
	with alive_bar(len(list_persons), theme = 'ascii', enrich_print = False) as bar:
		for dic_each_actor in list_persons:
			actor_name = dic_each_actor['Name']
			actor_id = dic_each_actor['Id']
			bar()
			if dic_each_actor['ImageTags']: 
				num_exist += 1
				if not overwrite:
					write_txt("已匹配的演员清单.txt",'跳过：' + actor_name + '\n')
					num_skip += 1
					continue
			if not os.path.exists(local_path+actor_name+".jpg"):
				pic_link = get_gfriends_link(actor_name)
				if pic_link == None:
					actor_name = re.sub(r'（.*）','',actor_name)
					actor_name = re.sub(r'\(.*\)','',actor_name)
					pic_link = get_gfriends_link(actor_name)
					if pic_link == None:
						write_txt("未收录的演员清单.txt",'未找到：' + actor_name + '\n')
						num_fail += 1
						continue
				write_txt("已匹配的演员清单.txt",'下载：' + actor_name + '\n')
				name_list.append(actor_name)
				link_list.append(pic_link)
				actor_dict[actor_name] = actor_id
	print('√ 初始化完成')
	print('\n>> 下载头像...')
	with alive_bar(len(name_list), theme = 'ascii', enrich_print = False) as bar:
		for link,actor_name in zip(link_list,name_list):
			try:
				download_avatar(link,actor_name)
				if '（' in actor_name:	
					bar(re.sub(r'（.*）','',actor_name))
				else:
					bar(actor_name)
				while True:
					if threading.activeCount() > max_download_connect + 1:
						time.sleep(0.1)
					else:
						break
			except (KeyboardInterrupt):
				sys.exit()
			except:
				with bar.pause():
					if debug: 
						print(format_exc())
					print('× 网络连接异常且重试 ' + str(max_retries) + ' 次失败')
					print('× 请尝试开启全局代理或配置 HTTP 局部代理；若已开启代理，请检查其可用性')
					print('× 按任意键继续运行则跳过下载这些头像：'+ str(actor_name)+'\n')
					os.system('pause>nul')
				continue
	while True:
		if threading.activeCount() > 1:	
			time.sleep(0.1); 
		else: 
			break
	print('√ 下载完成')
	if fixsize != '0':
		print('\n>> 尺寸优化...')
		for folderName, subfolders, filenames in os.walk(download_path):	
			with alive_bar(len(filenames), theme = 'ascii', enrich_print = False) as bar:
				for filename in filenames:
					if '（' in filename:	
						bar(re.sub(r'（.*）','',filename).replace('.jpg',''))
					else:
						bar(filename.replace('.jpg',''))
					if '.jpg' in filename and filename.replace('.jpg','') in name_list:
						pic_path = download_path+filename
						fix_size(fixsize,pic_path)
		for folderName, subfolders, filenames in os.walk(local_path):
			with alive_bar(len(filenames), theme = 'ascii', enrich_print = False) as bar:
				for filename in filenames:
					if '（' in filename:	
						bar(re.sub(r'（.*）','',filename).replace('.jpg',''))
					else:
						bar(filename.replace('.jpg',''))
					if '.jpg' in filename and filename.replace('.jpg','') in name_list:
						pic_path = local_path+filename
						fix_size(fixsize,pic_path)
		print('√ 优化完成')
	print('\n>> 导入头像...')
	for folderName, subfolders, filenames in os.walk(download_path):		
		with alive_bar(len(filenames), theme = 'ascii', enrich_print = False) as bar:
			for filename in filenames:
				if '（' in filename:	
					bar(re.sub(r'（.*）','',filename).replace('.jpg',''))
				else:
					bar(filename.replace('.jpg',''))
				if '.jpg' in filename:
					pic_path = download_path+filename		
					pic = open(pic_path, 'rb')
					b6_pic = b64encode(pic.read())
					pic.close()
					actor_key_name = filename.replace('.jpg','')
					if actor_key_name in name_list:
						if emby:
							url_post_img = host_url + 'emby/Items/' + actor_dict[actor_key_name] + '/Images/Primary?api_key=' + api_key
						else:
							url_post_img = host_url + 'jellyfin/Items/' + actor_dict[actor_key_name] + '/Images/Primary?api_key=' + api_key
						input_avatar(url_post_img,b6_pic)
						while True:
							if threading.activeCount() > max_upload_connect + 1:
								time.sleep(0.1)
							else:
								break				
						num_suc += 1
	for folderName, subfolders, filenames in os.walk(local_path):
		with alive_bar(len(filenames), theme = 'ascii', enrich_print = False) as bar:
			for filename in filenames:	
				if '（' in filename:	
					bar(re.sub(r'（.*）','',filename).replace('.jpg',''))
				else:
					bar(filename.replace('.jpg',''))
				if '.jpg' in filename:
					pic_path = local_path+filename		
					pic = open(pic_path, 'rb')
					b6_pic = b64encode(pic.read())
					pic.close()
					actor_key_name = filename.replace('.jpg','')
					if actor_key_name in name_list:
						if emby:
							url_post_img = host_url + 'emby/Items/' + actor_dict[actor_key_name] + '/Images/Primary?api_key=' + api_key
						else:
							url_post_img = host_url + 'jellyfin/Items/' + actor_dict[actor_key_name] + '/Images/Primary?api_key=' + api_key
						input_avatar(url_post_img,b6_pic)
						while True:
							if threading.activeCount() > max_upload_connect + 1:
								time.sleep(0.1)
							else:
								break
						num_suc += 1
	while True:	
		if threading.activeCount() > 1:	
			time.sleep(0.1); 
		else: 
			break
	print('√ 导入完成')
	print('\nEmby / Jellyfin 拥有演员 ' + str(len(list_persons)) + ' 人，其中 ' + str(num_exist) + ' 人之前已有头像')
	print('本次导入 ' + str(num_suc) + ' 人，还有 ' + str(num_fail) + ' 人没有头像\n')
	if not overwrite: print('!! 未开启覆盖已有头像，所以跳过了一些演员，详见运行日志')
	print('按任意键退出程序...')
	os.system('pause>nul')
except (KeyboardInterrupt, SystemExit):
	print('× 强制停止或已知致命错误！')
	print('按任意键退出程序...')
	os.system('pause>nul')
except:
	if debug: print(format_exc())
	print('× 未知致命错误！')
	print('按任意键退出程序...')
	os.system('pause>nul')
