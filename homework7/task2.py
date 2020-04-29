#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
@File : task2.py
@Time : 2020/04/22 21:32:36
@Author : KingFar 
@Version : 1.0
@Contact : 1136421682@qq.com
@WebSite : https://github.com/KingFarGrace
"""

# here put the import lib
import requests
from bs4 import BeautifulSoup
import re

"""
给定100个企业网站首页链接地址（用1中给出的URL地址）；请爬取每个页面上，企业介绍的链接地址；
    说明，满足企业介绍网址的条件是， 标题包含：企业介绍，关于我们，企业发展，发展历史，企业概况等关键字的URL地址；
    提示：要用到requests库，BeautifulSoup库
"""


def get_profiles():
    # Google Chrome 请求头，然而依旧大部分被拒绝访问
    head = {'User-Agent':
             'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
             AppleWebKit/537.36 (KHTML, like Gecko) \
             Chrome/81.0.4044.122 Safari/537.36'}
    # url_f：源链接文件
    # pro_f：简介链接文件
    with open(r"homework7\url.txt", "r") as url_f:
        with open(r"homework7\profile.txt", "a") as pro_f:
            count = 0
            for line in url_f:
                url = line.strip('\n')
                try:
                    html = requests.get(url, headers=head, timeout=30)
                    html.raise_for_status()
                    # 构建BS对象，以lxml方式解析
                    soup = BeautifulSoup(html.content, "lxml")
                    # 在文档树中查找文字部分疑似公司简介的a标签
                    label = soup.findAll("a", 
                                        text=re.compile
                                        (r"企业[介绍,简介,信息,发展,概况]|关于[我们,企业,..]"), 
                                        limit=1)
                    # 写入文件
                    if len(label) != 0:
                        pro_f.write("url:{}--profile link--".format(url))
                        for rec in label:
                            pro_f.write(rec["href"])
                        pro_f.write('\n')
                        pro_f.flush()                    
                        count += 1
                    # 扒够100个简介链接为止
                    if count == 100:
                        break
                except:
                    print("抓取网址为{}的页面失败！".format(url))
   

if __name__ == '__main__':
    get_profiles()