#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
@File : task4.py
@Time : 2020/04/02 00:38:03
@Author : KingFar 
@Version : 1.0
@Contact : 1136421682@qq.com
@WebSite : https://github.com/KingFarGrace
"""

# here put the import lib
import hashlib

"""
模拟用户登录:
     5个同学的姓名,账号和密码(加密后的),保存在一个文件上;   
     系统提示,请输入登录同学姓名, 正确后,请输入账号, 正确后,提示请输入密码（输入明文）;  如果都正确,打印提示, 您登录成功(失败);
"""


if __name__ == '__main__':
     with open("homework4\info.txt", "r") as file:
          infos = []
          for line in file:
               line = line.strip('\n')
               infos.append(line.split(" "))
     # print(infos)
     name = input("请输入用户名：")
     flag = False
     for info in infos:
          if info[0] == name:
               flag = True
               uid = input("请输入账号：")
               if info[1] == uid:
                    psw = input("请输入密码：")
                    md5 = hashlib.md5()
                    md5.update(psw.encode("utf-8"))
                    if md5.hexdigest() == info[2]:
                         print("登录成功！")
                         break
                    else:
                         print("密码错误！登录失败！")
                         break
               else:
                    print("账户错误！登录失败！")
                    break
     if flag == False:
          print("未找到用户名！")