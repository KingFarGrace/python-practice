#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
@File : class_4_1_demo.py
@Time : 2020/04/01 08:39:31
@Author : KingFar 
@Version : 1.0
@Contact : 1136421682@qq.com
@WebSite : https://github.com/KingFarGrace
"""

# here put the import lib

"""
1.定义一个高阶函数, 实现加,减,乘,除计算器功能；
"""


def add(a, b):
    return a + b


def minus(a, b):
    return a - b


def muiti(a, b):
    return a * b


def div(a, b):
    return a / b


def calculator(a, b, f):
    return f(a, b)


if __name__ == '__main__':
    x = int(input("请输入x的值："))
    y = int(input("请输入y的值："))
    print("x+y={}\nx-y={}\nx*y={}\nx/y={}\n"
            .format(calculator(x, y, add), calculator(x, y, minus),
            calculator(x, y, muiti), calculator(x, y, div)))