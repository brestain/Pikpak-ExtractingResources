 # -*- coding:utf-8 -*-
import json
import time
import requests


def getRequest(url,params,headers,proxies):
    while True:
        try:
            response = requests.get(url=url, timeout=20,params=params,headers=headers,proxies=proxies)  # 设置超时时间为20秒
            response.raise_for_status()  # 检查请求是否成功（状态码为200）
            return response  # 如果成功收到响应，直接返回响应对象
        except (requests.RequestException, TimeoutError):
            print("请求超时，可能是触发风控，重新发送请求...")

def postRequest(url,data,headers,proxies):
    while True:
        try:
            response = requests.post(url=url, timeout=20,data=data,headers=headers,proxies=proxies)  # 设置超时时间为20秒
            response.raise_for_status()  # 检查请求是否成功（状态码为200）
            return response  # 如果成功收到响应，直接返回响应对象
        except (requests.RequestException, TimeoutError):
            print("请求超时，可能是触发风控，重新发送请求...")
