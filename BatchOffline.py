# -*- coding:utf-8 -*-
import json
import time
import requests
import traceback
import configparser
import re
import common
# 读取配置文件
config = configparser.ConfigParser()
config.read('config.ini', encoding="utf-8")

# 将配置文件中的键值对保存到一个字典对象中
config_dict = {}
for section in config.sections():
    for option in config.options(section):
        value = config.get(section, option)
        config_dict[option] = value

# 将字典中的键值对转换为程序中的同名变量
for key in config_dict:
    globals()[key] = config_dict[key]

start_time = time.time()

proxies = json.loads(proxies)
headers = json.loads(headers)

# 在这里编写你的程序



def extract_magnet_links(text):
    magnet_pattern = r"magnet:\?xt=urn:[^\s]+"
    magnet_links = re.findall(magnet_pattern, text)
    return magnet_links


def extract_ed2k_links(text):
    ed2k_pattern = r"ed2k://\|file\|[^|]+\|[^|]+\|[^|]+\|/"
    ed2k_links = re.findall(ed2k_pattern, text)
    return ed2k_links



def getToken():
    # print("init")
    urlInit = "https://user.mypikpak.com/v1/shield/captcha/init"
    headerForInit = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,ja-JP;q=0.8,ja;q=0.7",
        "Content-Length": "955",
        "Content-Type": "application/json",
        "Origin": "https://mypikpak.com",
        "Referer": "https://mypikpak.com/",
        "Sec-Ch-Ua": "\"Google Chrome\";v=\"113\", \"Chromium\";v=\"113\", \"Not-A.Brand\";v=\"24\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
        "X-Client-Id": "YUMx5nI8ZU8Ap8pm",
        "X-Client-Version": "1.0.0",
        "X-Device-Id": "69f39ffa2113448bb1e055334cc905b3",
        "X-Device-Model": "chrome%2F113.0.0.0",
        "X-Device-Name": "PC-Chrome",
        "X-Device-Sign": "wdi10.69f39ffa2113448bb1e055334cc905b3xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "X-Net-Work-Type": "NONE",
        "X-Os-Version": "Win32",
        "X-Platform-Version": "1",
        "X-Protocol-Version": "301",
        "X-Provider-Name": "NONE",
        "X-Sdk-Version": "6.0.0-alpha.0"
    }
    dataForInit = {"client_id": "YUMx5nI8ZU8Ap8pm", "action": "POST:/drive/v1/files",
                   "device_id": "69f39ffa2113448bb1e055334cc905b3",
                   "captcha_token": "ck0.a9ARS0QjMAo9vqGP6gDxiMyr60KcfRuMT_XQzaRWprxt6qdfyAprWuHrXw2X4lIlah9QawcWJ1BMbmD2pXho1M-V2qMXe9RgSvQq4zK9yiJFW_hMfQxyOuwuoJbnWN5FY0wB7Quan7fAEqGO1XGJXdKmrkU9Aj32sw51ih0Kmqo1GnUHKtAXrlIUOtQXlH_QF0_uBIMAMniAm6leWX59agXYH3Y7bfY5r6sD7FDWpWyJ_9_N8HCgX2u082yfPeEGRX8zuqH55nTX_cDLH_lnF9YV3LO-3l3iZPILi4_Dblgt8CG_Jy9YlPW7vOpvTgWxIgWH0vRYOzEd6xfSa4_pUqW0Vj17iVyQa1RZlGeUO3U.ClAI_bb2iYgxEhBZVU14NW5JOFpVOEFwOHBtGgUxLjAuMCIMbXlwaWtwYWsuY29tKiA2OWYzOWZmYTIxMTM0NDhiYjFlMDU1MzM0Y2M5MDViMxKAAWlm5buMRn1NnpGKA_NTHI6S6YNU8l_T1qjHl31XDm7kHLkqu_Q5n2vYRX2PSjT7TRrj_Sq8ug11rOQlhBSVxFg3ti3gLqME7pZn1DlNrk_bu60z1pLIMLMulhIux4rROQaAQvp4a_vGq4DHkGwliXZBBT9F6tkiSPeIOUtfCdOR",
                   "meta": {"captcha_sign": "1.d4066053ce2fc514884baafc2bae500e", "client_version": "1.0.0",
                            "package_name": "mypikpak.com", "user_id": "ZFXTk9GE0B_C_0FY",
                            "timestamp": "1685691905935"}}
    dataForInit = json.dumps(dataForInit)
    response = common.postRequest(url=urlInit, proxies=proxies, headers=headerForInit, data=dataForInit)
    token = response.json()["captcha_token"]
    return token


def createFolder(name, fatherId):
    print("创建文件夹...")
    url = "https://pikpak.kinh.cc/CreateFolder.php"
    data = {
        "AccessToken": token,
        "Name": name,
        "ID": fatherId
    }
    operatHeader = {
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN",
        "Authorization": "Bearer " + token,
        "Content-Type": "application/json",
        "Origin": "https://mypikpak.com",
        "Referer": "https://mypikpak.com/",
        "Sec-Ch-Ua": "\"Google Chrome\";v=\"113\", \"Chromium\";v=\"113\", \"Not-A.Brand\";v=\"24\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
        "X-Captcha-Token": getToken(),
        "X-Device-Id": "69f39ffa2113448bb1e055334cc905b3"
    }
    responses = common.postRequest(url=url, data=json.dumps(data), headers=operatHeader, proxies=proxies)
    responses = responses.json()
    print(responses)
    print("文件夹" + name + "创建中....")
    time.sleep(4)
    print("文件夹" + name + "创建完毕")
    return responses["ID"]
def getFileList(folderId,kind):
    print("获取文件列表...")
    urlGetFileList = "https://api-drive.mypikpak.com/drive/v1/files"
    params = {
        "thumbnail_size": "SIZE_MEDIUM",
        "limit": "200",
        "parent_id": f"{folderId}",
        "with_audit": "true",
        "order": "MODIFY_TIME_DESC",
        "filters": """{"kind":{"eq":"drive#folder"},"trashed":{"eq":false},"phase":{"eq":"PHASE_TYPE_COMPLETE"}}"""
    }
    if "folder" in kind:
        params["filters"]= """{"kind":{"eq":"drive#folder"},"trashed":{"eq":false},"phase":{"eq":"PHASE_TYPE_COMPLETE"}}"""
    elif "file" in kind:
        params["filters"]="""{"kind":{"eq":"drive#file"},"trashed":{"eq":false},"phase":{"eq":"PHASE_TYPE_COMPLETE"}}"""
    headerForGetFileList = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN",
        "Authorization": "Bearer " + token,
        "Content-Type": "application/json",
        "Origin": "https://mypikpak.com",
        "Referer": "https://mypikpak.com/",
        "Sec-Ch-Ua": "\"Google Chrome\";v=\"113\", \"Chromium\";v=\"113\", \"Not-A.Brand\";v=\"24\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
        "X-Captcha-Token":getToken(),
        "X-Device-Id": "69f39ffa2113448bb1e055334cc905b3"
    }
    # print(headerForGetFileList["Authorization"])
    response = common.getRequest(url=urlGetFileList, proxies=proxies, headers=headerForGetFileList, params=params)
    if  response.json().get("error") and response.json()["error"]=="unauthenticated":
        raise Exception("token已过期,请重新运行init")
    print("获取文件列表成功")
    return (response.json())



def uploadAMagnet(magnet):
    print("正在离线"+magnet+"...")
    url = "https://api-drive.mypikpak.com/drive/v1/files"
    operatHeader = {
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN",
        "Authorization": "Bearer " + token,
        "Content-Type": "application/json",
        "Origin": "https://mypikpak.com",
        "Referer": "https://mypikpak.com/",
        "Sec-Ch-Ua": "\"Google Chrome\";v=\"113\", \"Chromium\";v=\"113\", \"Not-A.Brand\";v=\"24\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
        "X-Captcha-Token": getToken(),
        "X-Device-Id": "69f39ffa2113448bb1e055334cc905b3"
    }
    # 根据源文件夹和目标文件夹获取文件夹id
    data = {
        "kind": "drive#file",
        "parent_id": srcfolderid,
        "upload_type": "UPLOAD_TYPE_URL",
        "url": {
            "url": f"{magnet}"
        },
        "params": {
            "with_thumbnail": "true",
            "from": "manual"
        }
    }
    response = common.postRequest(url=url, proxies=proxies, headers=operatHeader, data=json.dumps(data))
    # print(response.json())
    print(response.json()["task"]["name"] + "上传成功")


def uploadFromTxt(filename):
    print("开始")
    with open(filename, 'r', encoding="utf-8") as file:
        file_content = file.read()
    # 提取磁力链接和 ed2k 链接
    magnet_links = extract_magnet_links(file_content)
    ed2k_links = extract_ed2k_links(file_content)
    # 对每个链接执行上传操作
    for magnet_link in magnet_links:
        uploadAMagnet(magnet_link)
    for ed2k_link in ed2k_links:
        uploadAMagnet(ed2k_link)
    input("批量离线资源完毕,按任意键退出")





uploadFromTxt(offlinefilename)






end_time = time.time()
total_time = end_time - start_time
print(f"程序执行时间为：{total_time:.5f} 秒")
