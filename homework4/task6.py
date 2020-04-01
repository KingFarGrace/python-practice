#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
@File : task6.py
@Time : 2020/03/29 10:53:43
@Author : KingFar 
@Version : 1.0
@Contact : 1136421682@qq.com
@WebSite : https://github.com/KingFarGrace
"""

# here put the import lib
import os
from datetime import datetime

"""
通过Python来实现显示给定文件夹下的所有文件和文件夹,以及时间，如果是文件，显示大小; 输出格式效果如下:
    名称         日期                   类型（文件夹或者 文件）       大小
"""


if __name__ == '__main__':
    dir_name = "homework4\\"
    print("{0:-^30}{1:-^30}{2:-^20}{3:-^20}"
            .format("名称", "日期", "类型", "大小"))
    for root, dirs, files in os.walk(dir_name):
        for name in files:
            file_name = os.path.join(root, name)
            print("{0:^30}{1:^30}{2:^20}{3:^20}"
                    .format(os.path.basename(file_name), 
                    str(datetime.fromtimestamp(os.path.getctime(file_name))),
                    str(os.path.splitext(file_name)[1] + "文件"), 
                    str(os.path.getsize(file_name))) + "byte")
        for name in dirs:
            sub_dir_name = os.path.join(root, name)
            print("{0:^30}{1:^30}{2:^20}{3:^20}"
                    .format(os.path.basename(file_name), 
                    str(datetime.fromtimestamp(os.path.getctime(file_name))),
                    "文件夹",
                    str(os.path.getsize(file_name))) + "byte")