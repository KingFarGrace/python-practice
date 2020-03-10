#!/usr/bin/python3
# -*- encoding: utf-8 -*-
'''
@File : task1.py
@Time : 2020/03/04 23:46:55
@Author : KingFar 
@Version : 1.0
@Contact : 1136421682@qq.com
@WebSite : https://github.com/KingFarGrace
'''

# here put the import lib
import matplotlib

'''
元素输出和查找：  请输出0-50之间的奇数，偶数，质数；能同时被2和3整除的数
'''

if __name__ == '__main__':
    even_nums = []
    odd_nums = []
    prime_nums = []
    div_2_3_nums = []
    
    for x in range(51):
        # 先判断质数
        flag = 1
        for i in range(2, x):
            if x % i == 0:
                flag = 0
                break
        if flag == 1 and x >= 2:
            prime_nums.append(x)
            
        #判断奇偶数的同时可以判断是否被2和3同时整除
        if x % 2 == 0:
            even_nums.append(x)
            if x % 3 == 0:
                div_2_3_nums.append(x)
        else:
            odd_nums.append(x)
        
    print(f"0-50之间的奇数有：{odd_nums}")
    print(f"0-50之间的偶数有：{even_nums}")
    print(f"0-50之间的质数有：{prime_nums}")
    print(f"0-50之间能同时被2和3整除的数有：{div_2_3_nums}")