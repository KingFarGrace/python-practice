#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
@File : task1.py
@Time : 2020/04/07 17:04:04
@Author : KingFar 
@Version : 1.0
@Contact : 1136421682@qq.com
@WebSite : https://github.com/KingFarGrace
"""

# here put the import lib
from datetime import datetime
import time

"""
编写一个装饰器，能计算其他函数的运行时间
"""


def timer(func):
    def wrapper(*args, **kwargs):
        start_t = datetime.now()
        func(*args, **kwargs)
        end_t = datetime.now()
        print("{}运行时间为：{}s".format(func.__name__, (end_t - start_t).seconds))
    return wrapper


@timer
def do_something():
    time.sleep(3)
    print("运行完成！")


if __name__ == '__main__':
    do_something()