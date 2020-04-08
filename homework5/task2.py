#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
@File : task2.py
@Time : 2020/04/07 17:04:35
@Author : KingFar 
@Version : 1.0
@Contact : 1136421682@qq.com
@WebSite : https://github.com/KingFarGrace
"""

# here put the import lib
from datetime import datetime
import functools

"""
编写一个装饰器，能记录其他函数调用的日志，将日志写入到文件中；
"""


def log(logf):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            rec = "call {}() at {}\n".format(func.__name__, datetime.now())
            print(rec)
            logf.write(rec)
        return wrapper
    return decorator

# 追加操作句柄
file = open(r"homework5\task2_log.txt", "a")

@log(file)
def do_A():
    print("A is running...")


@log(file)
def do_B():
    print("B is running...")


@log(file)
def do_C():
    print("C is running...")


if __name__ == '__main__':
    do_A()
    do_B()
    do_C()
