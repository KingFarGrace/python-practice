#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
@File : task2.py
@Time : 2020/03/11 17:01:58
@Author : KingFar 
@Version : 1.0
@Contact : 1136421682@qq.com
@WebSite : https://github.com/KingFarGrace
"""

# here put the import lib

"""
编写一个函数,接收n个数字，求这些参数数字的和
"""

def get_sum(*kwarg):
    sum = 0
    for i in kwarg:
        sum += i
    return sum


if __name__ == '__main__':
    print("2, 3, 4, 5的和为：{}".format(get_sum(2, 3, 4, 5)))
    print("1, 8, 9, 10, 6的和为：{}".format(get_sum(1, 8, 9, 10, 6)))