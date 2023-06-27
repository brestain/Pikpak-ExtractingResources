# -*- coding:utf-8 -*-
import _thread
import datetime
import json
import time
import requests
import random
from collections import deque
import portalocker
import pymysql
import datetime
import re
import math
import traceback
import threading
import queue
import configparser
from concurrent.futures import ThreadPoolExecutor
import commen
from commen import logger, exceptionHandler, getResponse, postForResponse
import configparser
import biliFunctions

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
headers = json.loads(headerwithnocookie)
from loguru import logger

# logger.add("test.log", rotation="1 week", retention="7 days", compression="zip")
logger.add("test.log")

# 在这里编写你的程序

import requests

# 读取target.txt文件内容
with open("target.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

results = []

# 遍历每行内容
for line in lines:
    content = line.strip()  # 去除行尾的换行符和空格
    # 发送GET请求
    url = f"https://api.jucili.com/api.php?s=btfuk&q={content}&p=1"
    response = requests.get(url,proxies=proxies)
    print(response.text)
    try:
        response=response.json()
        # 提取结果
        if response and "data" in response and response["data"]:
            result = response["data"][0]
        else:
            result = "空"
    except:
        result="空"
    results.append(f"{content}:{result}")
# 写入output.txt文件
with open("output.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(results))




end_time = time.time()
total_time = end_time - start_time
print(f"程序执行时间为：{total_time:.5f} 秒")
