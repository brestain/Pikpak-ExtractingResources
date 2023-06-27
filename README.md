# pikpak-
python实现, 提供exe文件. 批量离线磁力链接, 自动提取离线后文件夹中的视频资源, 删除广告文件. 

想把资源往pikpak上传一份备份, 就写了一些脚本, 包括批量通过资源名获取磁力链接, 批量离线磁力链接, 自动提取离线后文件夹的资源, 删除广告文件. 但是之前搜索磁力链接的api好像收费了, 项目里的getMagnet暂时没法用喽,后续有空可能会写用爬虫的.

## 使用方法
### 写配置
在config.ini中写入相应的配置,包括用户名,密码,源文件夹路径,目标文件夹路径等,具体写法在config.ini中的注释里有写
### 预处理
运行init.exe或init.python  
以此获取token和文件夹id等,获取到的信息会自动填入config.ini中.
![Snipaste_2023-06-27_21-59-18.jpg](..%2FSnipaste_2023-06-27_21-59-18.jpg)
### 获取磁力链接
由于之前用的api失效,此项暂不可用  
可以把自己找的磁力链接扔到toOffline.txt中  
toOffline.txt示例:
![Snipaste_2023-06-27_22-00-51.jpg](..%2FSnipaste_2023-06-27_22-00-51.jpg)
magnet链接和ed2k链接都可以
### 批量离线
运行BatchOffline.exe或BatchOffline.py.  
等待程序结束.  
![Snipaste_2023-06-27_22-05-32.jpg](..%2FSnipaste_2023-06-27_22-05-32.jpg)
### 提取视频资源
运行ExtractingResources.exe或ExtractingResources.py.  
等待程序结束
![Snipaste_2023-06-27_22-18-34.jpg](..%2FSnipaste_2023-06-27_22-18-34.jpg)
会把配置文件中srcfolder路径下在大小范围区间内的文件提取出来,放到targetfolder文件夹下,其余文件删除.