#!/usr/bin/python3
# -*- encoding: utf-8 -*-
'''
@File : task4.py
@Time : 2020/03/05 00:56:48
@Author : KingFar 
@Version : 1.0
@Contact : 1136421682@qq.com
@WebSite : https://github.com/KingFarGrace
'''

# here put the import lib
'''
判断用户输入的年份是否为闰年
'''

if __name__ == '__main__':
    year = int(input("请输入年份："))
    if year % 400 == 0:
        print("%d是世纪闰年\n" % year)
    elif year % 4 == 0 and year % 100 != 0:
        print("%d是闰年\n" % year)
    else:
        print("%d不是闰年\n" % year)