#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
@File : task2.py
@Time : 2020/05/05 19:39:00
@Author : KingFar 
@Version : 1.0
@Contact : 1136421682@qq.com
@WebSite : https://github.com/KingFarGrace
"""

# here put the import lib
import requests
import threading

"""
2 给定一组数据网址数据，请判断这些网址是否可以访问； 用多线程的方式来实现；
   请查资料，Python的 requests库，如何判断一个网址可以访问；
   数据文件（1000个网址）：url_data.txt
"""

# 没做封装的原因是因为就想练习一下不封装的写法
def is_accepted(url):
   try:        
      r = requests.get(url,timeout=10)
      r.raise_for_status()
      return True
   except:
      return False


def get_url():
   with open(r"homework8\url_data.txt", "r") as f:
      url_list = []
      for line in f:
         line = line.strip('\n')
         url_list.append(line)
   return url_list


def group_check(url_list, start, end):
   for i in range(end - start):
      if is_accepted(url_list[start + i]):
         print("{}访问成功！".format(url_list[i]))
      else:
         print("{}访问失败！".format(url_list[i]))


if __name__ == '__main__':
   MAX_THREAD_NUM = 10
   url = get_url()
   gap = int(len(url) / MAX_THREAD_NUM)
   for i in range(MAX_THREAD_NUM):
      t = threading.Thread(target=group_check,
                           args=(url, i * gap, (i + 1) * gap - 1))
      t.start()
