#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
@File : task3.py
@Time : 2020/03/29 10:51:32
@Author : KingFar 
@Version : 1.0
@Contact : 1136421682@qq.com
@WebSite : https://github.com/KingFarGrace
"""

# here put the import lib
import hashlib

"""
从键盘输入5个同学的账号和密码,然后将他们的姓名,账号和密码(密码需要加密)保存到一个文件中;
Tom   admin   XXXXX
Jack   root   XXXXX  
"""


if __name__ == '__main__':
        print("请输入5名同学的姓名，账号，密码：")
        with open("homework4\info.txt", "w") as file:
                md5 = hashlib.md5()
                for i in range(5):
                        print("第{}名同学信息：".format(i + 1))
                        name = input("姓名：")
                        uid = input("账号：")
                        psw = input("密码：")
                        md5.update(psw.encode("utf-8"))
                        dig = md5.hexdigest()
                        file.write(name + ' ')
                        file.write(uid + ' ')
                        file.write(dig + '\n')
