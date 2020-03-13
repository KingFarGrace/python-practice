#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
@File : task5.py
@Time : 2020/03/11 17:33:59
@Author : KingFar 
@Version : 1.0
@Contact : 1136421682@qq.com
@WebSite : https://github.com/KingFarGrace
"""

# here put the import lib

"""
写函数，检查传入字典的每一个value长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者
"""

def check_input(any_dict, **kwarg):
    for k, v in kwarg.items():
        if len(str(v)) > 2:
            v = v[0: 2]
        any_dict[k] = v
    return any_dict


if __name__ == '__main__':
    dict1 = {}
    dict1 = check_input(dict1, a="12", b="345", c="6", d = "789")
    print("经过检查输入后的dict1：{}".format(dict1))