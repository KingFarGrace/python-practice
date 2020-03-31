#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
@File : task1.py
@Time : 2020/03/29 09:38:45
@Author : KingFar 
@Version : 1.0
@Contact : 1136421682@qq.com
@WebSite : https://github.com/KingFarGrace
"""

# here put the import lib

"""
写一个程序，读取键盘输入的任意行文字信息，当输入空行时结束输入，将读入的字符串存于列表;然后将列表里面的内容写入到文件input.txt中
"""


if __name__ == '__main__':
    str_list = []
    str_in = input("请输入任意行信息：\n")
    while str_in != "" :
        str_list.append(str_in)
        str_in = input()
    try:
        file = open("homework3/input.txt", "w")
        for str_in in str_list:
            file.write("{}\n".format(str_in))
        file.flush()
        file.close()
    except IOError as ioe:
        print(ioe)
    finally:
        file.close()