#!/usr/bin/python3
# -*- encoding: utf-8 -*-
'''
@File : task10.py
@Time : 2020/03/05 21:30:54
@Author : KingFar 
@Version : 1.0
@Contact : 1136421682@qq.com
@WebSite : https://github.com/KingFarGrace
'''

# here put the import lib

"""
功能概述：给定一段英文文本，统计每个单词出现的次数；打印输出，按照词频从高到低输出

功能具体描述：

参数
--------------------

返回值
--------------------

参看
--------------------

示例
--------------------

"""

if __name__ == '__main__':
    file = open("D:\\doc\\python-practice\\homework1\\task_10_text.txt", mode = 'r', encoding = 'utf-8')
    text = file.readlines()
    print(text)