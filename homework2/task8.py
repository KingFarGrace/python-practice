#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
@File : task8.py
@Time : 2020/03/11 18:51:16
@Author : KingFar 
@Version : 1.0
@Contact : 1136421682@qq.com
@WebSite : https://github.com/KingFarGrace
"""

# here put the import lib


"""
请用Python定义一个函数，给定一个字符串，找出该字符串中出现次数最多的那个字符，并打印出该字符及其出现的次数。
例如，输入 aaaabbc，输出：a:4
"""

def get_frequencest_letter(any_str):
    visited = {}
    for letter in any_str:
        if letter not in visited:
            visited[letter] = any_str.count(letter)
    max = 0
    for k, v in visited.items():
        if max < v:
            max = v
            max_key = k
    print("{}:{}".format(max_key, max))

if __name__ == '__main__':
    get_frequencest_letter(r"jhkjhdasuiy31544151\\[][\//")