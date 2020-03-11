#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
@File : task1.py
@Time : 2020/03/11 16:49:13
@Author : KingFar 
@Version : 1.0
@Contact : 1136421682@qq.com
@WebSite : https://github.com/KingFarGrace
"""

# here put the import lib

"""
写函数，判断用户传入的对象（字符串、列表、元组）长度,并返回给调用者。
"""

def length(seq):
    count = 0
    for i in seq:
        count += 1
    return count


if __name__ == '__main__':
    str1 = "ABCDEF"
    list1 = ['A', 'B', 'C', 'D', 'E', 'F']
    tup1 = ('A', 'B', 'C', 'D', 'E', 'F')
    print("str1的长度是：{}\nlist1的长度是：{}\ntup1的长度是：{}\n"
                .format(length(str1), length(list1), length(tup1)))