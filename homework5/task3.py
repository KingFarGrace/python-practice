#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
@File : task3.py
@Time : 2020/04/07 17:05:05
@Author : KingFar 
@Version : 1.0
@Contact : 1136421682@qq.com
@WebSite : https://github.com/KingFarGrace
"""

# here put the import lib
import hashlib

"""
编写一个装饰器，为多个函数加上认证的功能（必须输入用户的账号密码，才能调用这个函数）
"""

# 录入权限信息
# print("请输入用户名和密码:")
# uid = input("用户名：")
# psw = input("密码：").encode("utf-8")
# md5 = hashlib.md5()
# md5.update(psw)
# with open(r"homework5\priority.txt", "a") as f:
#     f.write(uid + " ")
#     f.write(md5.hexdigest() + '\n')


def login(func):
    def wrapper(*args, **kwargs):
        with open(r"homework5\priority.txt", "r") as f:
            prior = []
            for line in f:
                line = line.strip("\n")
                info = line.split(" ")
                prior.append(info[0])
                prior.append(info[1])

        print("您正在调用{}函数，请输入账号和密码认证权限:\n".format(func.__name__))
        uid = input("用户名：")
        psw = input("密码：")
        try:
            idx = prior.index(uid)
        except ValueError as ve:
            print("用户名不存在！")
        else:
            md5 = hashlib.md5()
            md5.update(psw.encode("utf-8"))
            if md5.hexdigest() == prior[idx + 1]:
                func(*args, **kwargs)
            else:
                print("密码错误！")
    return wrapper


@login
def do_A():
    print("A is running...")


@login
def do_B():
    print("B is running...")


@login
def do_C():
    print("C is running...")


if __name__ == '__main__':
    do_A()
    do_B()
    do_C()