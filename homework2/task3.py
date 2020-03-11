#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
@File : task3.py
@Time : 2020/03/11 17:12:02
@Author : KingFar 
@Version : 1.0
@Contact : 1136421682@qq.com
@WebSite : https://github.com/KingFarGrace
"""

# here put the import lib
import random as rd

"""
编写一个函数, 传入一个数字列表, 输出列表中的奇数;
   数字列表请用随机数函数生成;
"""

def find_odds(num_list):
    print("数组中奇数为：")
    for num in num_list:
        if num % 2 != 0:
            print(num, end="  ")


if __name__ == '__main__':
    nums = []
    for i in range(10):
        nums.append(rd.randint(1, 1000))
    print("生成的数组为：{}".format(nums))
    find_odds(nums)