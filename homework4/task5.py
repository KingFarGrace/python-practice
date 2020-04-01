#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
@File : task4.py
@Time : 2020/03/29 10:52:04
@Author : KingFar 
@Version : 1.0
@Contact : 1136421682@qq.com
@WebSite : https://github.com/KingFarGrace
"""

# here put the import lib
import shutil

"""
通过Python来模拟实现一个txt文件的拷贝过程;
"""


if __name__ == '__main__':
    # 可以采用shutil模块直接复制
    # shutil.copy("homework4\source.txt", "homework4\copy.txt")
    try:
        source = open(r"homework4\source.txt", "r")
        copy = open(r"homework4\copy.txt", "w")
        for line in source:
            copy.write(line)
    except IOError as ioe:
        print(ioe)
    finally:
        source.close()
        copy.close()
