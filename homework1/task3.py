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
    same = set()
    for i in list1:
        #开始寻找list1与list2的相同元素
        for j in list2:
            if i == j:
                #若找到相同元素，加入相同元素集合
                same.add(i)
    if len(same) > 0:
        print(f"相同元素为：{same}\n")
    else:
        print("没有相同元素！")