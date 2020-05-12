#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
@File : task4.py
@Time : 2020/04/15 23:40:22
@Author : KingFar 
@Version : 1.0
@Contact : 1136421682@qq.com
@WebSite : https://github.com/KingFarGrace
"""

# here put the import lib

"""
封装一个学生类，有姓名，有年龄，有性别，有英语成绩，数学成绩，语文成绩，
      封装方法，求单个学生的总分，平均分，以及打印学生的信息。
"""

class Student(object):
    __score = {'语文': 0, '数学': 0, '英语': 0}

    def __init__(self, name, age, sex, score):
        self.__name = name
        self.__age = age
        self.__sex = sex
        idx = 0
        for k in self.__score.keys():
            self.__score[k] = score[idx]
            idx += 1

    def __str__(self):
        return  """
                学生姓名：{0:<10}年龄：{1:<5}性别：{2:<5}
                语文成绩：{3:<5}
                英语成绩：{4:<5}
                数学成绩：{5:<5}
                """\
                .format(self.__name, self.__age, self.__sex, 
                self.__score['语文'], 
                self.__score['数学'], 
                self.__score['英语'])

    def get_sum(self):
        sum = 0
        for v in self.__score.values():
            sum += v
        return sum

    def get_avg(self):
        return self.get_sum() / 3


if __name__ == '__main__':
    stu = Student("Tom", 19, "男", [66, 77, 88])
    print("学生信息为：{}".format(stu))
    print("学生总分为：{}".format(stu.get_sum()))
    print("学生平均分为：{}".format(stu.get_avg()))
