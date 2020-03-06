#!/usr/bin/python3
# -*- encoding: utf-8 -*-
'''
@File : task2.py
@Time : 2020/03/05 00:23:44
@Author : KingFar 
@Version : 1.0
@Contact : 1136421682@qq.com
@WebSite : https://github.com/KingFarGrace
'''

# here put the import lib

'''
一个字典中，存放了10个学生的学号（key）和分数（value）；请筛选输出，大于80分的同学（按照格式：学号：分数）
'''

if __name__ == '__main__':
    score = {'1' : ['01', 81], '2' : ['02', 65], '3' : ['03', 78], '4' : ['04', 89],
                '5' : ['05', 71], '6' : ['06', 86], '7' : ['07', 91], '8' : ['08', 68], 
                    '9' : ['09', 54], '10' : ['10', 82]}
    for k, v in score.items():
        if v[1] >= 80:
            print(f"学号：{v[0]}，分数：{v[1]}")