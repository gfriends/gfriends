# -*- coding:utf-8 -*-
# Gfriends Inputer / 女友头像仓库导入工具
# Licensed under the MIT license.
# Designed by xinxin8816, many thanks for junerain123, ddd354, moyy996.
version = 'v2.5'

import requests, os, sys
from configparser import RawConfigParser
from base64 import b64encode
from traceback import format_exc
from json import loads
from PIL import Image,ImageFilter
from alive_progress import alive_bar

def fix_size(type,path):
	pic = Image.open(path)
	(x,y) = pic.size
	if not 2/3-0.05 <= x/y <= 2/3+0.05: #仅处理会过度拉伸的图片
		if type == '1':
			fixed_pic = pic.resize((int(x),int(3/2*x))) #拉伸图片
			fixed_pic = fixed_pic.filter(ImageFilter.GaussianBlur(radius=50)) #高斯模糊
			fixed_pic.paste(pic,(0,int((3/2*x-y)/2))) #粘贴原图
			fixed_pic.save(path)
		elif type == '2':
			fixed_pic = pic.crop((int(x/2-1/3*y),0,int(x/2+1/3*y),int(y)))
			fixed_pic.save(path)
		else:
			print('头像处理配置错误，没有此选项：' + str(type))
			sys.exit()

def get_gfriends_map(repository_url):
	print('下载头像仓库文件树...')
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
		print('网络连接异常且重试 ' + str(max_retries) + ' 次失败')
		print('请尝试开启全局代理或配置 HTTP 局部代理；若已开启代理，请检查其可用性')
		sys.exit()
	if response.status_code != 200:
		print('女友仓库返回了一个错误： {}'.format(response.status_code))
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
	print('读取头像仓库文件树完成')
	print('当前仓库头像数量：' + str(response.text.count('\n')) + '枚\n')
	return output

def get_gfriends_link(name):
	if name in gfriends_map:
		output = gfriends_map[name]
		return output
	else:
		return None

def read_config():
	if os.path.exists('config.ini'):
		config_settings = RawConfigParser()
		try:
			config_settings.read('config.ini', encoding='UTF-8-SIG') # UTF-8-SIG 适配 Windows 记事本
			repository_url = config_settings.get("下载设置", "repository url")
			host_url = config_settings.get("媒体服务器", "host url")
			api_key = config_settings.get("媒体服务器", "api id")
			max_retries = config_settings.get("下载设置", "max retry")
			proxy = config_settings.get("下载设置", "proxy")
			download_path = config_settings.get("下载设置", "download_path")
			local_path = config_settings.get("导入设置", "local_path")
			aifix = True if config_settings.get("下载设置", "AI fix") == '是' else False
			overwrite = True if config_settings.get("导入设置", "覆盖以前上传的头像") == '是' else False
			debug = True if config_settings.get("调试功能", "更详尽的错误输出") == '是' else False
			deleteall = True if config_settings.get("调试功能", "删除服务器中所有头像") == '是' else False
			fixsize = config_settings.get("导入设置", "处理下载的头像")
			# 修正用户的URL
			if not host_url.endswith('/'): host_url += '/'
			if not repository_url.endswith('/'): repository_url += '/'
			# 创建文件夹
			if not os.path.exists(download_path):
				os.makedirs(download_path)
				write_txt(download_path+"/README.txt",'本目录自动生成，用于存放从仓库下载和处理过的头像。')
			if not os.path.exists(local_path):
				os.makedirs(local_path)
				write_txt(local_path+"/README.txt",'本目录自动生成，您可以存放自己收集的头像，这些头像将被优先导入服务器。\n\n仅支持JPG格式，且请勿再创建子目录。\n\n如果您收集的头像位于子目录，可通过 Move To Here.bat（Only for Windows） 工具将其全部提取到根目录。')
				write_txt(local_path+"/Move To Here.bat",'@echo off\necho This tool will help you move all files which in the subdirectory to this root directory\npause\nfor /f "delims=" %%a in ("dir /a-d /b /s ") do (\nmove "%%~a" ./ 2>nul\n)\n')
			return (repository_url,host_url,api_key,overwrite,fixsize,int(max_retries),proxy,aifix,debug,deleteall,download_path,local_path)
		except:
			print(format_exc())
			print('无法读取 config.ini')
			os.system('pause')
	else:
		content='''[媒体服务器]
# Emby / Jellyfin 服务器地址
host url = http://localhost:8096/
	
# Emby / Jellyfin API 密匙
api id = 

[下载设置]
# 下载文件夹
download_path = ./Downloads/

# 女友头像仓库地址，"默认"使用主分支：https://raw.githubusercontent.com/xinxin8816/gfriends/master/，备用镜像：https://gfriends.imfast.io/
repository url = 默认

# 在不可避免下载低质量头像时，自动挑选经AI算法放大优化的副本，质量更高但更占空间
AI fix = 是

# HTTP代理地址，格式为"IP:端口"，推荐开启全局代理而不是使用此处
proxy = 不使用

# 最大重试次数，若网络不稳定、丢包率或延迟较高，可适当增加重试次数
max retry = 3

[导入设置]
# 本地头像文件夹，将第三方头像包或自己收集的头像移动至该目录，可优先于仓库导入服务器。仅支持非子目录下的 jpg 格式。
local_path = ./Avatar/

# Emby / Jellyfin 会拉伸比例不符合 2:3 的头像，通过处理功能来避免拉伸
# 0 - 不处理直接导入
# 1 - 图片放大并模糊
# 2 - 图片放大并裁剪
处理下载的头像 = 2

覆盖以前上传的头像 = 是

[调试功能]
# 谨慎操作！
删除服务器中所有头像 = 否

# 这有助于出现BUG时快速定位问题
更详尽的错误输出 = 否'''
		write_txt("config.ini",content)
		print('没有找到配置文件 config.ini，已为阁下生成，请修改配置后重新运行程序\n')
		os.system('pause')
		sys.exit()

def read_persons(host_url,api_key):
	print('读取 Emby / Jellyfin 演员...')
	emby = True
	host_url_persons = host_url + 'emby/Persons?api_key=' + api_key	 # &PersonTypes=Actor
	try:
		rqs_emby = session.get(url=host_url_persons)
	except session.exceptions.ConnectionError:
		print('连接 Emby / Jellyfin 服务器失败，请检查：', host_url, '\n')
		sys.exit()
	except:
		if debug: print(format_exc())
		print('连接 Emby / Jellyfin 服务器未知错误：', host_url, '\n')
		sys.exit()
	if rqs_emby.status_code == 401:
		print('无权访问 Emby / Jellyfin 服务器，请检查 API 密匙\n')
		sys.exit()
	if rqs_emby.status_code == 404:
		try:
			print('可能是新版 Jellyfin，尝试重新读取...')
			emby = False
			host_url_persons = host_url + 'jellyfin/Persons?api_key=' + api_key	 # &PersonTypes=Actor
			rqs_emby = session.get(url=host_url_persons)
		except:
			if debug: print(format_exc())
			print('读取 Emby / Jellyfin 演员列表返回 404，可能是未适配的版本：', host_url, '\n')
			sys.exit()
	output = loads(rqs_emby.text)['Items']
	print('读取 Emby / Jellyfin 演员完成\n')
	return (output,emby)

def write_txt(filename,content):
	txt = open(filename, 'a', encoding="utf-8")
	txt.write(content)
	txt.close()

def del_all():
	print('【调试模式】删除所有头像\n')
	(list_persons,emby) = read_persons(host_url,api_key)
	os.system('pause')
	for dic_each_actor in list_persons:
		if dic_each_actor['ImageTags']:
			actor_name = dic_each_actor['Name']
			print('>> 删除：', actor_name)
			if emby:
				url_post_img = host_url + 'emby/Items/' + dic_each_actor['Id'] + '/Images/Primary?api_key=' + api_key
			else:
				url_post_img = host_url + 'jellyfin/Items/' + dic_each_actor['Id'] + '/Images/Primary?api_key=' + api_key
			session.delete(url=url_post_img)
	print('删除完成')
	os.system('pause')	
	sys.exit()

os.system('title Gfriends 一键导入工具 '+version)
print('尝试读取配置文件...')
(repository_url,host_url,api_key,overwrite,fixsize,max_retries,proxy,aifix,debug,deleteall,download_path,local_path) = read_config()
os.system('cls')

#持久会话
session = requests.Session()
session.mount('http://', requests.adapters.HTTPAdapter(max_retries=max_retries))
session.mount('https://', requests.adapters.HTTPAdapter(max_retries=max_retries))

if deleteall: del_all()

num_suc = 0
num_fail = 0
num_exist = 0
try:
	print('Gfriends 一键导入工具 '+version)
	print('https://github.com/xinxin8816/gfriends')
	#局部代理
	if proxy == '不使用':
		print('推荐开启全局代理以加快下载速度\n')
	else:
		print('已配置 HTTP 局部代理：' + proxy + '，请确保其可用\n')
		proxies={'http':'http://' + proxy,'https':'https://' + proxy}
	os.system('pause')
	(list_persons,emby) = read_persons(host_url,api_key)
	gfriends_map = get_gfriends_map(repository_url)
	if os.path.exists('未收录的演员清单.txt'):
		os.remove('未收录的演员清单.txt')
		write_txt("未收录的演员清单.txt",'【未收录的演员清单】\n（!!该清单仅供参考，正规影片演员、非日本女友、导演、编导、作品系列名及一些稀奇古怪的名字均可能出现在该清单中。但这些人员，女友头像仓库不会收录!!）\n\n')
	if os.path.exists('已匹配的演员清单.txt'):
		os.remove('已匹配的演员清单.txt')
		write_txt("已匹配的演员清单.txt",'【已匹配的演员清单】\n（!!该清单仅记录从女友仓库下载并导入头像的演员!!）\n\n')
	with alive_bar(len(list_persons), theme = 'ascii', enrich_print = False) as bar:
		for dic_each_actor in list_persons:
			bar()
			actor_name = dic_each_actor['Name']
			if dic_each_actor['ImageTags']: num_exist += 1
			if not overwrite:
				print('>> 跳过：', actor_name)
				continue
			if not os.path.exists(local_path+actor_name+".jpg"):
				pic_link = get_gfriends_link(actor_name)
				if pic_link == None:
					print('>> 未收录：', actor_name)
					write_txt("未收录的演员清单.txt",actor_name + '\n')
					num_fail += 1
					continue
				else:
					write_txt("已匹配的演员清单.txt",actor_name + '\n')
					print('>> 下载并导入：', actor_name)
					try:
						if proxy == '不使用':
							pic = session.get(pic_link)
						else:
							pic = session.get(pic_link, proxies = proxies)
					except (KeyboardInterrupt):
						sys.exit()
					except:
						with bar.pause():
							if debug: print(format_exc())
							print('网络连接异常且重试 ' + str(max_retries) + ' 次失败')
							print('请尝试开启全局代理或配置 HTTP 局部代理；若已开启代理，请检查其可用性')
							print('继续运行则跳过下载此头像：'+ pic_link)
							os.system('pause')
						continue
					pic_path = download_path+actor_name+".jpg"
					with open(pic_path,"wb") as code:
						code.write(pic.content)
			else:
				pic_path = local_path+actor_name+".jpg"
				print('>> 本地导入：', actor_name)
			if fixsize != '0': fix_size(fixsize,pic_path)
			pic = open(pic_path, 'rb')
			b6_pic = b64encode(pic.read())
			pic.close()
			if emby:
				url_post_img = host_url + 'emby/Items/' + dic_each_actor['Id'] + '/Images/Primary?api_key=' + api_key
			else:
				url_post_img = host_url + 'jellyfin/Items/' + dic_each_actor['Id'] + '/Images/Primary?api_key=' + api_key
			session.post(url=url_post_img, data=b6_pic, headers={"Content-Type": 'image/jpeg', })
			num_suc += 1
	print('\nEmby / Jellyfin 拥有演员', len(list_persons), '人，当前已有头像', num_exist, '人')
	print('本次成功导入', num_suc, '人')
	print('仓库未收录', num_fail, '人\n')
	os.system('pause')
except (KeyboardInterrupt, SystemExit):
	print('强制停止或已知致命错误！')
	os.system('pause')
except:
	if debug: print(format_exc())
	print('未知致命错误！')
	os.system('pause')
