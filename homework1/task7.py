#!/usr/bin/python3
# -*- encoding: utf-8 -*-
'''
@File : task7.py
@Time : 2020/03/05 20:02:30
@Author : KingFar 
@Version : 1.0
@Contact : 1136421682@qq.com
@WebSite : https://github.com/KingFarGrace
'''

# here put the import lib

'''
打印输出9*9乘法表，按照下面的格式
1*1=1
1*2=2   2*2=4
...
1*9=9   2*9=18  ... 9*9=81
'''

if __name__ == '__main__':
    for i in range(1, 10):
        for j in range(1, i + 1):
            item = "{1}*{0}={2}".format(i, j, i * j)
            print("{0:10}".format(item), end = ' ')
        print('\n')