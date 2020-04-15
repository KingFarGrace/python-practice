#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
@File : class_4_15_demo.py
@Time : 2020/04/15 09:08:54
@Author : KingFar 
@Version : 1.0
@Contact : 1136421682@qq.com
@WebSite : https://github.com/KingFarGrace
"""

# here put the import lib
import re

"""
匹配出163的邮箱地址，且@符号之前有4到20位英文或者数字字符，例如hello@163.com
"""


if __name__ == '__main__':
    text = input("请输入邮箱地址：\n")  
    if re.match(r'[0-9a-zA-Z_]{0,19}@163.com$',text):  
        print("邮箱地址正确！")  
    else:  
        print('邮箱地址错误！')  