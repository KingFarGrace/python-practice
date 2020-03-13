#!/usr/bin/python3
# -*- encoding: utf-8 -*-
'''
@File : task5.py
@Time : 2020/03/05 01:07:06
@Author : KingFar 
@Version : 1.0
@Contact : 1136421682@qq.com
@WebSite : https://github.com/KingFarGrace
'''

# here put the import lib
import random

'''
使用random模块，生成随机数，来初始化一个列表，元组；
'''

if __name__ == '__main__':
    rand_list = [random.randint(1, 100) for i in range(10)]
    rand_tup = tuple([random.randint(1, 100) for i in range(10)])
    print(f"随机列表为：{rand_list}\n随机元组为：{rand_tup}\n")