# -*- coding:utf-8 -*-
# Gfriends Inputer / 女友头像仓库导入工具
# By xinxin8816, Many thanks for junerain123, ddd354, moyy996.

import requests, os
from configparser import RawConfigParser
from base64 import b64encode
from traceback import format_exc
from json import loads
from PIL import Image,ImageFilter

def fix_size(path):
	pic = Image.open(path)
	(x,y) = pic.size
	if not 2/3-0.05 <= x/y <= 2/3+0.05: #仅处理会过度拉伸的图片
		fixed_pic = pic.resize((int(x), int(3/2*x))) #拉伸图片
		fixed_pic = fixed_pic.filter(ImageFilter.GaussianBlur(radius=50)) #高斯模糊
		fixed_pic.paste(pic,(0,int((3/2*x-y)/2))) #粘贴原图
		fixed_pic.save(path)

def get_gfriends_map(repository_url):
	print('下载头像仓库文件树...')
	if repository_url == '默认/':
		repository_url = 'https://raw.githubusercontent.com/xinxin8816/gfriends/master/'
	github_template = repository_url+'{}/{}/{}'
	request_url = repository_url+'Filetree.json'
	response = requests.get(request_url)
	if response.status_code != 200:
		print('无法连接头像仓库，请检查配置和网络 {}'.format(response.status_code))
		os.system('pause')
		exit()
	
	map_json = loads(response.content)
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
		print('推荐开启全局代理以加快下载速度\n')
		os.system('pause')
		config_settings = RawConfigParser()
		try:
			config_settings.read('config.ini', encoding='UTF-8')
			repository_url = config_settings.get("gfriends", "repository url")
			host_url = config_settings.get("gfriends", "host url")
			api_key = config_settings.get("gfriends", "api id")
			overwrite = True if config_settings.get("gfriends", "是否覆盖以前上传的头像？") == '是' else False
			fixsize = True if config_settings.get("gfriends", "是否处理下载的头像？") == '是' else False
			# 修正用户的URL
			if not host_url.endswith('/'):
				host_url += '/'
			if not repository_url.endswith('/'):
				repository_url += '/'
			return (repository_url,host_url,api_key,overwrite,fixsize)
		except:
			print(format_exc())
			print('无法读取 config.ini')
			os.system('pause')
	else:
		content='''[gfriends]
# 女友头像仓库地址，"默认"使用主分支：https://raw.githubusercontent.com/xinxin8816/gfriends/master/
repository url = 默认
	
# Emby/Jellyfin 服务器地址
host url = http://localhost:8096/
	
# Emby/Jellyfin API 密匙
api id = 

# 处理以满足尺寸需求，能避免部分头像被拉伸但会牺牲一定质量
是否处理下载的头像？ = 是

是否覆盖以前上传的头像？ = 是'''
		write_txt("config.ini",content)
		print('没有找到配置文件 config.ini，已为阁下生成，请修改配置后重新运行程序\n')
		os.system('pause')
		exit()

def read_persons(host_url,api_key):
	print('读取 Emby / Jellyfin 演员...')
	host_url_persons = host_url + 'emby/Persons?api_key=' + api_key	 # &PersonTypes=Actor
	try:
		rqs_emby = requests.get(url=host_url_persons)
	except requests.exceptions.ConnectionError:
		print('连接 Emby / Jellyfin 服务器失败，请检查：', host_url, '\n')
	except:
		print(format_exc())
		print('连接 Emby / Jellyfin 服务器未知错误', host_url, '\n')
	if rqs_emby.status_code == 401:
		print('无权访问 Emby / Jellyfin 服务器，请检查 Api id\n')
	output = loads(rqs_emby.text)['Items']
	print('读取 Emby / Jellyfin 演员完成\n')
	return output

def write_txt(filename,content):
	txt = open(filename, 'a', encoding="utf-8")
	txt.write(content)
	txt.close()

os.system('title Gfriends 一键导入工具')
print('Gfriends 一键导入工具')
print('https://github.com/xinxin8816/gfriends')
(repository_url,host_url,api_key,overwrite,fixsize) = read_config()

num_suc = 0
num_fail = 0
num_exist = 0
index = 1
try:
	session = requests.Session()
	session.mount('http://', requests.adapters.HTTPAdapter(max_retries=4))
	session.mount('https://', requests.adapters.HTTPAdapter(max_retries=4))
	list_persons = read_persons(host_url,api_key)
	gfriends_map = get_gfriends_map(repository_url)
	folder_path = './Downloads/'
	if os.path.exists(folder_path) == False:
		os.makedirs(folder_path)
	for dic_each_actor in list_persons:
		actor_name = dic_each_actor['Name']
		progress_rate = format(index/len(list_persons)*100,'.1f')
		if get_gfriends_link(actor_name) == None:
			print('(', progress_rate, '%) >>未收录：', actor_name)
			write_txt("未收录的演员清单.txt",actor_name + '\n')
			num_fail += 1
		else:
			write_txt("已匹配的演员清单.txt",actor_name + '\n')
			if dic_each_actor['ImageTags']:
				num_exist += 1
				if not overwrite:
					print('(', progress_rate, '%) >>跳过：', actor_name)
					index += 1
					continue
			print('(', progress_rate, '%) >>下载并导入：',get_gfriends_link(actor_name))
			pic = session.get(get_gfriends_link(actor_name))
			with open("Downloads/"+actor_name+".jpg","wb") as code:
				code.write(pic.content)
			if fixsize:
				fix_size("Downloads/"+actor_name+".jpg")
			pic = open("Downloads/"+actor_name+".jpg", 'rb')
			b6_pic = b64encode(pic.read())
			pic.close()
			url_post_img = host_url + 'emby/Items/' + dic_each_actor['Id'] + '/Images/Primary?api_key=' + api_key
			session.post(url=url_post_img, data=b6_pic, headers={"Content-Type": 'image/jpeg', })
			num_suc += 1
		index += 1
	print('\nEmby / Jellyfin 拥有演员', len(list_persons), '人，当前已有头像', num_exist, '人')
	print('本次成功导入', num_suc, '人')
	print('仓库未收录', num_fail, '人\n')
	os.system('pause')
except:
	print(format_exc())
	print('强制停止或致命错误退出')
	os.system('pause')
