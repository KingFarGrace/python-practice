#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
@File : task4.py
@Time : 2020/03/11 17:20:57
@Author : KingFar 
@Version : 1.0
@Contact : 1136421682@qq.com
@WebSite : https://github.com/KingFarGrace
"""

# here put the import lib

"""
写函数，统计字符串中有几个字母，几个数字，几个空格，几个其他字符，并返回结果
"""

def str_counter(any_str):
    letter_count = 0
    num_count = 0
    space_count = 0
    other_count = 0

    for i in any_str:
        if i.isalpha():
            letter_count += 1
        elif i.isdigit():
            num_count += 1
        elif i.isspace():
            space_count += 1
        else:
            other_count += 1

    return {'字母数': letter_count, '数字数': num_count, 
            '空格数': space_count, '其它字符数': other_count}


if __name__ == '__main__':
    str1 = r"as\d\\hjgfj 12 345\dsa35"
    count_dict = str_counter(str1)
    print("str1中的各种字符数如下：\n")
    for k, v in count_dict.items():
        print("{}: {}".format(k, v))
    