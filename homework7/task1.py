#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
@File : task1.py
@Time : 2020/04/22 21:31:15
@Author : KingFar 
@Version : 1.0
@Contact : 1136421682@qq.com
@WebSite : https://github.com/KingFarGrace
"""

# here put the import lib
import re

"""
给定一个文件 webspiderUrl.txt，请用正则表达式，逐行匹配提取其中的URL链接信息，并保存到另外一个文件中；
提示，文件有1000行，注意控制每次读取的行数
"""

if __name__ == '__main__':
    # 因为文件中只有网址是http://开头的格式，因此后续只需要匹配可能出现的字符即可
    rule = re.compile(r"http://[a-zA-Z0-9\.\-\_]{0,25}")
    with open(r"homework7\webspiderUrl.txt", "r", encoding="utf-8") as rf:
        with open(r"homework7\url.txt", "w") as wf:
            for line in rf:
                all_match = rule.findall(line)
                for rec in all_match:
                    wf.write(rec)
                    wf.write('\n')
    print("All done.")