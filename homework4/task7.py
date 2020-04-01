#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
@File : task7.py
@Time : 2020/03/29 10:54:07
@Author : KingFar 
@Version : 1.0
@Contact : 1136421682@qq.com
@WebSite : https://github.com/KingFarGrace
"""

# here put the import lib
import os

"""
使用python代码统计一个文件夹中所有文件的总大小
"""


def file_size_sum(dir):
    sum = 0
    for root, dirs, files in os.walk(dir):
        for name in files:
            file_name = os.path.join(root, name)
            sum += os.path.getsize(file_name)
        for name in dirs:
            sub_dir_name = os.path.join(root, name)
            sum += file_size_sum(sub_dir_name)
    return sum        


if __name__ == '__main__':
    dir_name = "homework4\\"
    print("文件大小总和为：{}byte".format(file_size_sum(dir_name)))