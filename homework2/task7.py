#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
@File : task7.py
@Time : 2020/03/11 17:54:50
@Author : KingFar 
@Version : 1.0
@Contact : 1136421682@qq.com
@WebSite : https://github.com/KingFarGrace
"""

# here put the import lib
import random as rd


"""
随机生成20个学生的成绩; 判断这20个学生成绩的等级; 用函数来实现;  
    A---成绩>=90;  
    B-->成绩在 [80,90)
    C-->成绩在 [70,80)
    D-->成绩<70
"""

def score_classify(score_dict):
    rank_dict = {}
    for k, v in score_dict.items():
        if v <= 100 and v >= 90:
            rank_dict[k] = 'A'
        elif v < 90 and v >= 80:
            rank_dict[k] = 'B'
        elif v < 80 and v >= 70:
            rank_dict[k] = 'C'
        else:
            rank_dict[k] = 'D'
    return rank_dict


if __name__ == '__main__':
    score = {}
    for i in range(20):
        score['学生%d' % (i + 1)] = rd.randint(40, 100)
    print("学生成绩单为：\n{}".format(score))
    rank = score_classify(score)
    print("\n学生评级为：\n{}".format(rank))