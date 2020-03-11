#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
@File : task6.py
@Time : 2020/03/11 17:39:04
@Author : KingFar 
@Version : 1.0
@Contact : 1136421682@qq.com
@WebSite : https://github.com/KingFarGrace
"""

# here put the import lib


"""
定义一个函数, 打印输出n以内的斐波那契数列
"""

def fib(n):
    fib_1 = 1
    fib_2 = 1
    print("{}, {}".format(fib_1, fib_2), end=", ")
    if n >= 2:
        fib_n = fib_1 + fib_2
        while fib_n <= n:
            print("{}".format(fib_n), end = ", ")
            fib_1 = fib_2
            fib_2 = fib_n
            fib_n = fib_1 + fib_2
    

if __name__ == '__main__':
    bound = int(input("请输入最大值："))
    print("{}以内的斐波那契数列如下：\n".format(bound))
    fib(bound)