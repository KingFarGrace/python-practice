#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
@File : task2.py
@Time : 2020/03/29 10:47:52
@Author : KingFar 
@Version : 1.0
@Contact : 1136421682@qq.com
@WebSite : https://github.com/KingFarGrace
"""

# here put the import lib

"""
写一个程序，从input.txt中读取之前输入的数据，存入列表中，再加上行号打印显示；格式如下
#第一行： xxxx
#第二行： xxxx
"""


if __name__ == '__main__':
    str_list = []
    try:
        file = open("homework3/input.txt", "r", newline="\n")
        i = 1
        for line in file:
            line = line.strip('\n')
            str_list.append(line)
            print("第{}行：{}".format(i, line))
            i += 1
        # print(str_list)
    except IOError as ioe:
        print(ioe)
    finally:
        file.close()