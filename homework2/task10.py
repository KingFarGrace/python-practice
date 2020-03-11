#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
@File : task10.py
@Time : 2020/03/11 20:22:45
@Author : KingFar 
@Version : 1.0
@Contact : 1136421682@qq.com
@WebSite : https://github.com/KingFarGrace
"""

# here put the import lib


"""
编写一个函数cacluate, 可以实现2个数的运算(加,减 乘,除)
"""

def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        print("非法运算符！")
        return None


if __name__ == '__main__':
    a = int(input("第一个数："))
    op = input("运算符符（仅限四则运算）：")
    b = int(input("第二个数："))
    print("运算结果为：{}".format(calculate(a, b, op)))