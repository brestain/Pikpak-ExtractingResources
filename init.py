# -*- coding:utf-8 -*-
import json
import time
import requests
import re
import configparser
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

def getCaptchaToken():
    data = {
        "client_id": "YUMx5nI8ZU8Ap8pm",
        "action": "POST:/v1/auth/signin",
        "device_id": "e3b1860983684cbe8a60af6020b34f7c",
        "captcha_token": "ck0.JpNnj9U9uH69PNdg0mUSztQwEs45xVYxrjyCcLw4_Doi8Z5GBsyEGRKYlr9I3cn7ND_FOzRhnv8X7-M381SNRyWyQozgR7KjYtciM1JLhfUkJSBxOLBH4rFsM8K66pzcAt-mk5evPIdk9KXx1TCNsx-jiXtKhIokizj7q-n9J_9Pjz6rX7xkqc3ZQ1UqMd5rJ2_WfS_hMdxM_FrRHsp4pw88i8gS_r0MkdcyHtWAYjZlrGhkHJ-nCE0pthiwZQiAriYCmn3MBCdAJaoduxImyQ3iFShRJe-7ppNqarVbInIFm2XKtqrCJYG7HvKl0FrLuHTawdwmiNuwhm2ns6sopMpAdFsaUQnBU-Cy6ztyXf4.ClAI-ZeUvo0xEhBZVU14NW5JOFpVOEFwOHBtGgUxLjAuMCIMbXlwaWtwYWsuY29tKiBlM2IxODYwOTgzNjg0Y2JlOGE2MGFmNjAyMGIzNGY3YxKAAbjptjRUPjd9RP3b1N9YqZuQkA00m73vMJy-nzRffsYJk92nA106IYGfM5AzE4cMaOQGquDe-gqtt5BsJptsgWm2B8NpqIsAZ7fFEUue1M2pNQmJcnVfuFsHDT9Ts8_ZRJzjmIFa_wdoJ2w8QMJNvG9rFDHbO46cR2HnTlX_MNa-",
        "meta": {
            "email": username
        }
    }
    url = "https://user.mypikpak.com/v1/shield/captcha/init"
    response = requests.post(url=url, data=json.dumps(data), proxies=proxies)
    # print("getCaptchaToken")
    # print(response.text)
    return response.json()["captcha_token"]
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

def signinAndGetToken(username, password):
    print("开始登录")
    if username != "" and password != "":
        print("获取token...")
        url = "https://user.mypikpak.com/v1/auth/signin"
        data = {
            "username": str(username),
            "password": str(password),
            "client_id": "YUMx5nI8ZU8Ap8pm"
        }
        headers = {
            "Accept-Language": "zh-CN",
            "Content-Type": "application/json",
            "Referer": "https://mypikpak.com/",
            "Sec-Ch-Ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": "\"Windows\"",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
            "X-Captcha-Token": getCaptchaToken(),
            "X-Client-Id": "YUMx5nI8ZU8Ap8pm",
            "X-Client-Version": "1.0.0",
            "X-Device-Id": "e3b1860983684cbe8a60af6020b34f7c",
            "X-Device-Model": "chrome%2F114.0.0.0",
            "X-Device-Name": "PC-Chrome",
            "X-Device-Sign": "wdi10.e3b1860983684cbe8a60af6020b34f7cxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            "X-Net-Work-Type": "NONE",
            "X-Os-Version": "Win32",
            "X-Platform-Version": "1",
            "X-Protocol-Version": "301",
            "X-Provider-Name": "NONE",
            "X-Sdk-Version": "6.0.0-alpha.0"
        }
        response = common.postRequest(url=url, headers=headers, data=json.dumps(data), proxies=proxies)
        # print(response.json())
        config.set('pikpak', 'token', response.json()["access_token"])
        with open('config.ini', 'w') as config_file:
            config.write(config_file)
        print("获取token成功")
    else:
        raise Exception("请在config.ini中输入账号和密码")
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
        "Authorization": "Bearer " + config_dict["token"],
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
    response =common.getRequest(url=urlGetFileList, proxies=proxies, headers=headerForGetFileList, params=params)
    print("获取文件列表成功")
    return (response.json())


def verifyFolderId():
    print("获取文件夹id...")
    path = srcfolder.split("/")
    id=""
    for i in path:
        flag = 0
        response = getFileList(id,"folder")
        # print(response)
        for file in response["files"]:
            if file["name"] == i and file["kind"] == "drive#folder":
                id = file["id"]
                flag = 1
                break
        if flag == 0:
            id = createFolder(i, id)
    config.set('pikpak', 'srcfolderid', id)
    path = targetfolder.split("/")
    id = ""
    for i in path:
        flag = 0
        response = getFileList(id, "folder")
        # print(response)
        for file in response["files"]:
            if file["name"] == i and file["kind"] == "drive#folder":
                id = file["id"]
                flag = 1
                break
        if flag == 0:
            id = createFolder(i, id)
    config.set('pikpak', 'targetfolderid', id)
    with open('config.ini', 'w') as config_file:
        config.write(config_file)
    print("获取文件夹id成功")

signinAndGetToken(username, password)

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
proxies = json.loads(proxies)
headers = json.loads(headers)

verifyFolderId()
input("预处理完毕,按任意键退出")

