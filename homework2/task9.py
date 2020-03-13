#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
@File : task9.py
@Time : 2020/03/11 18:50:31
@Author : KingFar 
@Version : 1.0
@Contact : 1136421682@qq.com
@WebSite : https://github.com/KingFarGrace
"""

# here put the import lib
import random as rd

"""
定义一个函数，函数接收一个数组，并把数组里面的数据从小到大排序(冒泡排序, 也可以直接使用相关的函数)
"""

def bubble_sort(num_arr):
    bound = len(num_arr)
    for i in range(bound) :
        for j in range(bound - i - 1) :
            if num_arr[j] > num_arr[j + 1] :
                # t = num_arr[j]
                # num_arr[j] = num_arr[j + 1]
                # num_arr[j + 1] = t
                num_arr[j], num_arr[j + 1] =\
                num_arr[j + 1], num_arr[j]
                
    return num_arr


if __name__ == '__main__':
    nums = []
    for i in range(10):
        nums.append(rd.randint(1, 100))
    print("排序前的数组为：{}".format(nums))
    nums = bubble_sort(nums)
    print("排序后的数组为：{}".format(nums))