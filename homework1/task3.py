#!/usr/bin/python3
# -*- encoding: utf-8 -*-
'''
@File : task3.py
@Time : 2020/03/05 00:33:14
@Author : KingFar 
@Version : 1.0
@Contact : 1136421682@qq.com
@WebSite : https://github.com/KingFarGrace
'''

# here put the import lib

'''
定义2个列表，并初始化；  找出这2个列表中，相同的元素并输出
'''

if __name__ == '__main__':
    list1 = [1, 4, 6, 8, 9, 10]
    list2 = [2, 3, 4, 6, 7, 9]
    #列表生成式，永远滴神！！！！！
    list_same = [i for i in set(list1) for j in set(list2) if i == j]
    if len(list_same) > 0:
        print(f"相同元素为：{list_same}\n")
    else:
        print("没有相同元素！")