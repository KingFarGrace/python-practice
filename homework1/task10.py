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

def text_spliter(text_part):
    #将文本中特殊字符替换为空格,大写替换为小写，再做拆分
    text_part.lower()
    for ch in r'[]\;,./<>?:{}|~!@#$%^&*()_+':
        text_part = text_part.replace(ch, " ")
    return text.split()


def dict_to_list(any_dict):
    any_list = [(k, v) for k, v in any_dict.items()]
    return any_list


if __name__ == '__main__':
    text = """I love python, python is the best language all over the world.
    No, I don't agree. I think the best one must be Java.
    Java is complex you know? Whatever I love python.
    And python is turtle-like? Come on.
    """

    word_list = text_spliter(text)
    word_dict = {}
    for word in word_list:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    word_list = dict_to_list(word_dict)
    word_list.sort(key=lambda k : k[1], reverse=True)

    print("单词数从高到低为：\n")
    for i in word_list:
        print("{0:15}+————+{1:5d}次".format(i[0], i[1]))