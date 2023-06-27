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

def getToken():
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


def getFileList(folderId,kind):
    print("获取文件列表"+folderId+"...")
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
        "X-Captcha-Token": getToken(),
        "X-Device-Id": "69f39ffa2113448bb1e055334cc905b3"
    }
    response = common.getRequest(url=urlGetFileList, proxies=proxies, headers=headerForGetFileList, params=params)
    if  response.json().get("error") and response.json()["error"]=="unauthenticated":
        raise Exception("token已过期,请重新运行init")
    print("获取文件列表成功")
    return (response.json())


def moveFile(id, targetFolderId):
    print("移动文件中...")
    urlMoveFile = "https://api-drive.mypikpak.com/drive/v1/files:batchMove"
    ids=[id]
    to={"parent_id":targetFolderId}
    data = {"ids": ids,
            "to": to
            }
    data = json.dumps(data)
    headersForMoveFile = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN",
        "Authorization": "Bearer " + token,
        "Content-Length": "86",
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
    if id!=targetFolderId:
        responses = common.postRequest(url=urlMoveFile, headers=headersForMoveFile, proxies=proxies, data=data)
    print("移动成功")



def deleteFile(id):
    print("删除文件中...")
    urlDeleteFile = "https://api-drive.mypikpak.com/drive/v1/files:batchTrash"
    ids=[id]
    data = {"ids": ids}
    data = json.dumps(data)
    headersForDeleteFile = {"Accept": "*/*",
                            "Accept-Encoding": "gzip, deflate, br",
                            "Accept-Language": "zh-CN",
                            "Authorization": "Bearer " + token,
                            "Content-Length": "38",
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
                            "X-Device-Id": "69f39ffa2113448bb1e055334cc905b3"}
    responses = common.postRequest(url=urlDeleteFile, headers=headersForDeleteFile, proxies=proxies, data=data)
    print("删除成功")
def operation(root,to):
    response = getFileList(root,"folder")
    for i in response["files"]:
        list = getFileList(i["id"],"folder")
        for file in list["files"]:
            operation(file["id"],to)
        list = getFileList(i["id"], "file")
        for file in list["files"]:
            if int(file["size"])<int(threshold_size):
                # deleteFile(file["id"])
                pass
            else:
                moveFile(file["id"],to)
        deleteFile(i["id"])
    response = getFileList(root, "file")
    for i in response["files"]:
        if int(i["size"]) < int(threshold_size):
            # deleteFile(i["id"])
            pass
        else:
            moveFile(i["id"],to)

if __name__ == '__main__':
    operation(root=srcfolderid,to=targetfolderid)
    # //root是源文件夹id,to是目标文件夹id
end_time = time.time()
total_time = end_time - start_time
print(f"程序执行时间为：{total_time:.5f} 秒")
input("提取资源完毕,按任意键退出")
