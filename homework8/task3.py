#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
@File : task3.py
@Time : 2020/05/05 19:39:36
@Author : KingFar 
@Version : 1.0
@Contact : 1136421682@qq.com
@WebSite : https://github.com/KingFarGrace
"""

# here put the import lib
import time
from multiprocessing import Process
from multiprocessing import Pool

"""
3  多进程练习：
计算1～100000之间所有素数的个数， 要求如下:
- 编写函数判断一个数字是否为素数，然后统计素数的个数；
-对比1: 对比使用多进程和不使用多进程两种方法的统计速度。
-对比2：对比开启4个多进程和开启10个多进程两种方法的速度。
"""


def is_prime(x):
    for i in range(2, x):
        if x % i == 0 and x != 2:
            return False
    return True


def count_prime(head, end):
    s = time.time()
    count = 0
    for i in range(end - head):
        if is_prime(i + head):
            count += 1
    e = time.time()
    return count, e - s


def group_count_prime(p_num):
    count = 0
    gap = int(100000 / p_num)
    result = []
    pool = Pool(p_num)
    for i in range(p_num):
        result.append(pool.apply_async(count_prime,
                    args=(i * gap, (i + 1) * gap)))
    pool.close()
    for rec in result:
        count += rec.get()[0]
        t = rec.get()[1]
    print("{}进程运行时间为：{}s，共{}个质数"
            .format(p_num, t, count - 2))    # 去掉0和1


if __name__ == '__main__':
    # 单进程运行时间为：27s
    group_count_prime(1)
    # 4进程运行时间为：11s
    group_count_prime(4)
    # 10进程运行时间为：6s
    group_count_prime(10)
