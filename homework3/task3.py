#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
@File : task3.py
@Time : 2020/03/29 10:48:47
@Author : KingFar 
@Version : 1.0
@Contact : 1136421682@qq.com
@WebSite : https://github.com/KingFarGrace
"""

# here put the import lib

"""
编写一个程序，读取文件中保存的10个学生成绩名单信息(学号,姓名, Python课程分数); 然后按照分数从高到低进行排序输出
"""


if __name__ == '__main__':
    try:
        file = open(r"homework3\score.txt", "r")
        score_list = []
        for line in file:
            line = line.strip('\n')
            info = line.split(" ")
            score_list.append(info)        
        score_list.sort(key=lambda k: int(k[2]), reverse=True)
        # print(score_list)
        print("按成绩从高到低排序：\n学号\t姓名\t成绩")
        for info in score_list:
            print("{}\t{}\t{}".format(info[0], info[1], info[2]))
    except IOError as ioe:
        print(ioe)
    finally:
        file.close()