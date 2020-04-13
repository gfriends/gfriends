# -*- coding:utf-8 -*-
# By xinxin8816, Many thanks for junerain123, ddd354, moyy996.
#new add by xp2020rlby 
#新增本地文件导入，不用连接git（快）
#代码部分增加如下：
#1. 新增一个fix_size_l函数用于本地图片的裁剪和存放，图片存放在Handled文件夹内
#2. 在打开对应头像部分和寻找json文件部分都增加了本地文件夹导入的功能，本地和仓库导入两者用if else分隔，简单修改了一些变量以便两个功能可以在一个函数内执行
#3.新增读入config文件的本地头像包目录部分
import requests, os, json, ssl, urllib.request
from configparser import RawConfigParser
from base64 import b64encode
from traceback import format_exc
from json import loads
from PIL import Image


def fix_size(name):
    f_pic = Image.open("Downloads/" + name + ".jpg")
    (x, y) = f_pic.size
    if not 2 / 3 - 0.1 <= x / y <= 2 / 3 + 0.1:  # 仅处理会过度拉伸的图片
        cropped = f_pic.crop((0, 0, x, 3 / 2 * x))
        new_f_pic = Image.new("RGB", (int(x), int(3 / 2 * x)), (0, 0, 0))
        new_f_pic.paste(cropped, (0, int((3 / 2 * x - y) / 2)))
        new_f_pic.save("Downloads/" + name + ".jpg")
def fix_size_l(name,path):
    f_pic = Image.open(path)
    (x, y) = f_pic.size
    if not 2 / 3 - 0.1 <= x / y <= 2 / 3 + 0.1:  # 仅处理会过度拉伸的图片
        cropped = f_pic.crop((0, 0, x, 3 / 2 * x))
        new_f_pic = Image.new("RGB", (int(x), int(3 / 2 * x)), (0, 0, 0))
        new_f_pic.paste(cropped, (0, int((3 / 2 * x - y) / 2)))
        new_f_pic.save("Handled/" + name + ".jpg")
        return True
    else:
        return  False

def get_gfriends_map(switch):
    if switch==False:
        print('下载头像仓库文件树...')
        if repository_url == '默认/':
            github_template = 'https://raw.githubusercontent.com/xinxin8816/gfriends/master/{}/{}/{}'
            request_url = 'https://raw.githubusercontent.com/xinxin8816/gfriends/master/Filetree.json'
        else:
            github_template = repository_url + '{}/{}/{}'
            request_url = repository_url + 'Filetree.json'
        context = getattr(ssl, '_create_unverified_context')()
        response = urllib.request.urlopen(request_url, context=context)
        if response.code != 200:
            print('无法连接头像仓库，请检查配置和网络 {}'.format(response.code))
            return {}
        PATH_Template=github_template
    else:#新增本地json文件读取
        print('从{}读取本地文件树...'.format(LocalDirPath))
        Local_template = LocalDirPath + '\{}\{}\{}'
        try:
            response = open(LocalDirPath + '\Filetree.json', 'r', encoding='utf-8')
        except:
            print("无法打开Filetree.json！")
            os.system('pause')
        print("成功打开Filetree.json！")
        PATH_Template=Local_template
    map_json = json.load(response)
    output = {}
    first_lvls = map_json.keys()
    for first in first_lvls:
        second_lvls = map_json[first].keys()
        for second in second_lvls:
            for k, v in map_json[first][second].items():
                output[k[:-4]] = PATH_Template.format(first, second, v)#将两种地址合并为一个变量PATH_Template

    print('读取头像仓库文件树完成\n')
    return output


def get_gfriends_link(name):
    if name in gfriends_map:
        output = gfriends_map[name]
        return output
    else:
        return None


os.system('title Gfriends 一键导入工具')
print('Gfriends 一键导入工具本地增强版')
print('https://github.com/xinxin8816/gfriends')
print('如果从git导入推荐开启全局代理以加快下载速度，或者提前下载好头像集合包使用本地导入\n')
os.system('pause')
config_settings = RawConfigParser()
try:
    config_settings.read('config.ini', encoding='UTF-8')
    repository_url = config_settings.get("gfriends", "repository url")
    host_url = config_settings.get("gfriends", "host url")
    api_key = config_settings.get("gfriends", "api id")
    overwrite = True if config_settings.get("gfriends", "是否覆盖以前上传的头像？") == '是' else False
    fixsize = True if config_settings.get("gfriends", "是否处理下载的头像？") == '是' else False
    #新增两个变量读取
    LocalImport = True if config_settings.get("gfriends", "是否在本地导入？") == '是' else False
    LocalDirPath = config_settings.get("gfriends", "本地文件夹根目录地址") if LocalImport==True else None
except:
    print(format_exc())
    print('无法读取 config.ini')
    os.system('pause')
# 修正用户的URL
if not host_url.endswith('/'):
    host_url += '/'
if not repository_url.endswith('/'):
    repository_url += '/'
num_suc = 0
num_fail = 0
num_exist = 0
try:
    print('读取 Emby / Jellyfin 演员...')
    host_url_persons = host_url + 'emby/Persons?api_key=' + api_key  # &PersonTypes=Actor
    try:
        rqs_emby = requests.get(url=host_url_persons)
    except requests.exceptions.ConnectionError:
        print('连接 Emby / Jellyfin 服务器失败，请检查：', host_url, '\n')
    except:
        print(format_exc())
        print('连接 Emby / Jellyfin 服务器未知错误', host_url, '\n')
    if rqs_emby.status_code == 401:
        print('无权访问 Emby / Jellyfin 服务器，请检查 Api id\n')
    list_persons = loads(rqs_emby.text)['Items']
    num_persons = len(list_persons)
    print('读取 Emby / Jellyfin 演员完成\n')
    gfriends_map = get_gfriends_map(LocalImport)#导入文件树，可选从本地或者git
    f_txt = open("已匹配的演员清单.txt", 'w', encoding="utf-8")
    f_txt.close()
    f_txt = open("未收录的演员清单.txt", 'w', encoding="utf-8")
    f_txt.close()
    folder_path = './Downloads/'
    #处理过的图片路径
    handle_path='./Handled/'

    if os.path.exists(folder_path) == False:
        os.makedirs(folder_path)
    if os.path.exists(handle_path) == False:
        os.makedirs(handle_path)

    for dic_each_actor in list_persons:
        actor_name = dic_each_actor['Name']
        path = get_gfriends_link(actor_name)
        if path == None:
            print('>>仓库未收录：', actor_name)
            f_txt = open("未收录的演员清单.txt", 'a', encoding="utf-8")
            f_txt.write(actor_name + '\n')
            f_txt.close()
            num_fail += 1
        else:
            f_txt = open("已匹配的演员清单.txt", 'a', encoding="utf-8")
            f_txt.write(actor_name + '\n')
            f_txt.close()
            if dic_each_actor['ImageTags']:
                num_exist += 1
                if not overwrite:
                    continue
            if LocalImport==False:
                print('>>从仓库下载：', path)
                f_pic = requests.get(get_gfriends_link(actor_name))
                with open("Downloads/" + actor_name + ".jpg", "wb") as code:
                    code.write(f_pic.content)
                if fixsize:
                    fix_size(actor_name)
                f_pic = open("Downloads/" + actor_name + ".jpg", 'rb')
            else:
                print('>>：从本地文件中寻找', path)
                if fixsize:
                    deal=fix_size_l(actor_name, path)
                    if deal:
                        f_pic = open("Handled/" + actor_name + ".jpg", 'rb')
                    else:
                        f_pic = open(path, 'rb')
                else:
                    f_pic = open(path, 'rb')
            b6_pic = b64encode(f_pic.read())
            f_pic.close()
            url_post_img = host_url + 'emby/Items/' + dic_each_actor['Id'] + '/Images/Primary?api_key=' + api_key
            requests.post(url=url_post_img, data=b6_pic, headers={"Content-Type": 'image/jpeg', })
            print('>>设置成功：', actor_name)
            num_suc += 1
    print('\nEmby / Jellyfin 拥有演员', num_persons, '人，其中已有头像', num_exist, '人')
    print('本次成功导入', num_suc, '人')
    print('仓库未收录', num_fail, '人')
    print('已保存至“未收录的演员清单.txt”\n')
    os.system('pause')
except:
    print(format_exc())
    print('强制停止或致命错误退出')
    os.system('pause')
