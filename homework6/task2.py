#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
@File : tsak2.py
@Time : 2020/04/15 22:14:42
@Author : KingFar 
@Version : 1.0
@Contact : 1136421682@qq.com
@WebSite : https://github.com/KingFarGrace
"""

# here put the import lib

"""
定义一个学生Student类。有下面的类属性：
1 姓名 name
2 年龄 age
3 成绩 score（语文，数学，英语) [每课成绩的类型为整数]
类方法：
1 获取学生的姓名：get_name() 返回类型:str
2 获取学生的年龄：get_age() 返回类型:int
3 返回3门科目中最高的分数。get_course() 返回类型:int
写好类以后，可以定义2个同学测试下:
"""

class Student(object):
    __score = {'语文': 0, '数学': 0, '英语': 0}

    def __init__(self, name, age, score):
        self.__name = name
        self.__age = age
        idx = 0
        for k in self.__score.keys():
            self.__score[k] = score[idx]
            idx += 1


    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_course(self):
        max = 0
        for k, v in self.__score.items():
            if max < v:
                key = k
                max = v
        return key, max


if __name__ == '__main__':
    stu_A = Student("Tom", 18, [88, 77 ,99])
    course_A, score_A = stu_A.get_course()
    stu_B = Student("Jack", 19, [66, 77, 55])
    course_B, score_B = stu_B.get_course()
    print("学生A的姓名：{0:<10}年龄:{1:<5}最高分科目：{2:<5}分数：{3:<5}"
            .format(stu_A.get_name(), stu_A.get_age(), course_A, score_A))
    print("学生B的姓名：{0:<10}年龄:{1:<5}最高分科目：{2:<5}分数：{3:<5}"
            .format(stu_B.get_name(), stu_B.get_age(), course_B, score_B))
