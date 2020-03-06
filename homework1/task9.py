#!/usr/bin/python3
# -*- encoding: utf-8 -*-
'''
@File : task9.py
@Time : 2020/03/05 20:55:36
@Author : KingFar 
@Version : 1.0
@Contact : 1136421682@qq.com
@WebSite : https://github.com/KingFarGrace
'''

# here put the import lib
import random

"""
功能概述：猜数字游戏

功能具体描述：最多只能猜测N次，在N次之内猜不出，就退出程序，提示猜测失败

参数
--------------------
N：记录最多猜测次数的常量，初始化为10
start：单次猜测的最小值，初始化为1
end：单次猜测的（最大值 + 1），初始化为1000
num：随机产生的整型值
flag：是否猜中的标记，猜中为1，否则为0，初始化为0

返回值
--------------------

参看
--------------------

示例
--------------------

"""

if __name__ == '__main__':
    N = 10
    start = 1
    end = 1000
    num = random.randint(start, end)
    flag = 0
    for i in range(N):
        user_num = int(input("请猜一个{}到{}之间的数：".format(start, end)))
        if user_num < num:
            start = user_num
            print("你猜的数字小了！还剩{}次机会。".format(N - i - 1))
        elif user_num > num:
            end = user_num
            print("你猜的数字大了！还剩{}次机会。".format(N - i - 1))
        else:
            flag = 1
            print("猜对了！答案是{}！一共猜了{}次！".format(num, i + 1))
            break

    if flag == 0:
        print("很遗憾你没有猜对，答案是{}。".format(num))