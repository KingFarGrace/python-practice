#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
@File : task4.py
@Time : 2020/03/29 10:49:09
@Author : KingFar 
@Version : 1.0
@Contact : 1136421682@qq.com
@WebSite : https://github.com/KingFarGrace
"""

# here put the import lib
import os

"""
在当前目录新建目录img, 里面包含10个文件, 10个文件名各不相同(X4G5.png)
将当前img目录所有以.png结尾的后缀名改为.jpg.
"""


if __name__ == '__main__':
    path = r"homework3\img"
    try:
        for root, dirs, files in os.walk(path):
            for file_name in files:
                old_name = path + "\\" + file_name
                new_name = path + "\\" + file_name.split(".")[0] + ".jpg"
                os.rename(old_name, new_name)
    except OSError as ose:
        print(ose)