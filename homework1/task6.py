#!/usr/bin/python3
# -*- encoding: utf-8 -*-
'''
@File : task6.py
@Time : 2020/03/05 19:48:56
@Author : KingFar 
@Version : 1.0
@Contact : 1136421682@qq.com
@WebSite : https://github.com/KingFarGrace
'''

# here put the import lib

'''
前面2个元素为0，1，输出100以内的斐波那契数列
'''

if __name__ == '__main__':
    fib = [0, 1]
    item = 1                #新添项，初始化为fib[0]+fib[1]
    while item <= 100:
        fib.append(item)
        item += fib[-2]
    print(f"数列为：{fib}")