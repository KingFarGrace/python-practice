#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
@File : task3.py
@Time : 2020/04/22 21:33:23
@Author : KingFar 
@Version : 1.0
@Contact : 1136421682@qq.com
@WebSite : https://github.com/KingFarGrace
"""

# here put the import lib
import requests
import subprocess
from urllib.parse import quote
import re

"""
给定一个网址（包含了优质的英语学习音频文件），http://www.listeningexpress.com/studioclassroom/ad/；  
请大家写一个爬虫，将里面的英语节目MP3，都下载下来；
这些音频文件 在网页的html文件内容都是以mp3结尾的，如下图所示：

要求大家使用Requests库获取这个网页html文本内容，并且使用正则表达式获取里面所有的mp3文件的网址；并进行下载；
Windows上的wget可以点击 https://eternallybored.org/misc/wget/ 下载。 这个程序不用安装，直接在命令行里使用即可；
注意：
获取的音频网址前面需要加上 前缀 http://www.listeningexpress.com/studioclassroom/ad/ 才是完整的下载地址
MP3文件中有空格字符，组成下载网址时，需要进行url编码，否则空格会被当成命令行分隔符。参考代码如下所示
>>> from urllib.parse import quote
>>> quote('2019-04-13 NEWSworthy Clips.mp3')
'2019-04-13%20NEWSworthy%20Clips.mp3'

请求头：Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36
"""


def get_source():
     head = {'User-Agent':
             'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
             AppleWebKit/537.36 (KHTML, like Gecko) \
             Chrome/81.0.4044.122 Safari/537.36'}
     try:
          url = "http://www.listeningexpress.com/studioclassroom/ad/"
          html = requests.get(url, headers=head, timeout=30)
          html.raise_for_status()
          html.encoding = html.apparent_encoding
          text = html.text
          rec = re.compile(r"sc-ad\s\d{4}-\d{2}-\d{2}\s.*?\.mp3")
          mp3_link = rec.findall(text)
          for mp3 in mp3_link:
               mp3 = mp3.replace('\\', '')
               com = "Wget -P D:\\doc\\python-practice\\homework7\\mp3 " + url + quote(mp3)
               subprocess.Popen(com, cwd="D:\\doc\\", shell=True)
     except Exception as e:
          print(e)


if __name__ == '__main__':
     get_source()