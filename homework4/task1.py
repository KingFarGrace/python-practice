#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
@File : task1.py
@Time : 2020/03/29 10:50:55
@Author : KingFar 
@Version : 1.0
@Contact : 1136421682@qq.com
@WebSite : https://github.com/KingFarGrace
"""

# here put the import lib'
from datetime import datetime
from collections import deque

"""
定义一个10个元素的列表，通过列表自带的函数，实现元素在尾部插入和头部插入并记录程序运行的时间；用deque来实现，同样记录程序所耗费的时间；输出这2个时间的差值；
    提示：列表原生的函数实现头部插入数据：list.insert(0, v)；list.append（2）)
"""


if __name__ == '__main__':
    start_t = datetime.now()
    seq = deque([1, 2, 3, 4, 5])
    seq.appendleft(0)
    seq.append(6)
    # print(seq)
    end_t = datetime.now()
    gap = (end_t - start_t).microseconds
    if gap == 0:
        print("程序运行<1ms")
    else:
        print("程序运行消耗{}ms".format(gap))