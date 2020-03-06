#!/usr/bin/python3
# -*- encoding: utf-8 -*-
'''
@File : task10.py
@Time : 2020/03/05 21:30:54
@Author : KingFar 
@Version : 1.0
@Contact : 1136421682@qq.com
@WebSite : https://github.com/KingFarGrace
'''

# here put the import lib

import re

'''
给定一段英文文本，统计每个单词出现的次数；打印输出，按照词频从高到低输出
'''

if __name__ == '__main__':
    text = """I love python, python is the best language all over the world.
    No, I don't agree. I think the best one must be Java.
    Java is complex you know? Whatever I love python.
    And python is turtle-like? Come on.
    """

    #将文本中特殊字符替换为空格,大写替换为小写，再做拆分
    text.lower()
    for ch in '[]\;,./<>?:{}|~!@#$%^&*()_+':
        text = text.replace(ch, " ")
    word_list = text.split()

    word_dict = {}
    for word in word_list:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1

    key_list = []
    value_list = []
    for k, v in word_dict.items():
        key_list.append(k)
        value_list.append(v)
    
    for i in range(len(key_list) - 1):
        for j in range(len(key_list) - i - 1):
            if value_list[j] < value_list[j + 1]:
                value = value_list[j]
                value_list[j] = value_list[j + 1]
                value_list[j + 1] = value
                key = key_list[j]
                key_list[j] = key_list[j + 1]
                key_list[j + 1] = key

    print("单词数从高到低为：\n")
    for i in range(len(key_list)):
        print("{0:15}+————+{1:5d}次".format(key_list[i], value_list[i]))