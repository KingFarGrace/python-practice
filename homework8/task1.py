#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
@File : task1.py
@Time : 2020/05/05 19:38:44
@Author : KingFar 
@Version : 1.0
@Contact : 1136421682@qq.com
@WebSite : https://github.com/KingFarGrace
"""

# here put the import lib
import random
import threading

"""
1  有100个同学的分数：数据请用随机函数生成；
     A  利用多线程程序（比如，5个线程，每个线程负责输出20条记录），快速输出这100个同学的信息；
     B 利用线程池来实现
"""


class MyThread(threading.Thread):
     def __init__(self, name, seq):
          threading.Thread.__init__(self)
          self.name = name
          self.seq = seq

     def set_attrs(self, head, end):
          self.head = head
          self.end = end
          
     def run(self):
          print("|-+线程{}开始+-|".format(self.name))
          print_score(self.seq, self.head, self.end)
          print("|-+线程{}结束+-|".format(self.name))


def create_score():
     score_list = [random.randint(1, 100) for i in range(100)]
     return score_list


def print_score(seq, start, end):
     for i in range(end - start):
          print("学生{}成绩：{}"
          .format(start + i + 1, seq[start + i]))


def init_pool(seq):
     td_pool = []
     for i in range(5):
          td_pool.append(MyThread(i + 1, seq))
     return td_pool


if __name__ == '__main__':
     score = create_score()
     # print_score(score, 0, 100)
     pool = init_pool(score)
     for i in range(5):
          t = pool[i]
          t.set_attrs(i * 20, (i + 1) * 20 - 1)
          t.start()