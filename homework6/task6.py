#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
@File : task6.py
@Time : 2020/04/16 22:39:06
@Author : KingFar 
@Version : 1.0
@Contact : 1136421682@qq.com
@WebSite : https://github.com/KingFarGrace
"""

# here put the import lib
import csv
import pandas as pd

"""
用面向对象,实现一个学生Python成绩管理系统;
学生的信息存储在文件中;学生信息的字段有(班级,学号,姓名, Python成绩)
实现对学生信息及成绩的增,删,改,查方法;
"""

class Student(object):

    def __init__(self, class_id, stu_id, name, score):
        self.__class_id = class_id
        self.__stu_id = stu_id
        self.__name = name
        self.__score = score

    @staticmethod
    def add_record(stu_obj):
        # 写入一条学生信息记录
        with open(r"homework6\info.txt", "a") as f:
            f.write("{} {} {} {}"
                    .format(stu_obj.__class_id, stu_obj.__stu_id,
                             stu_obj.__name, stu_obj.__score))
            f.write('\n')

    @staticmethod
    def find_record():
        # 找到一条学生信息记录
        print("请输入需要查找的学生信息：")
        class_id = input("班级为：")
        stu_id = input("学号为：")
        name = input("姓名为：")
        with open(r"homework6\info.txt", "r") as f:
            for line in f:
                line = line.strip('\n')
                record = line.split(' ')
                if  record[0] == class_id and\
                    record[1] == stu_id and\
                    record[2] == name:

                    return "查找成功！\n班级：{0:<10}学号：{1:<10}\
                            姓名：{2:<10}python成绩：{3:<10}"\
                            .format(record[0], record[1], 
                                    record[2], record[3])
            return "没有找到该学生！"

    @staticmethod
    def del_record():
        # 删除一条学生信息记录
        print("请输入需要删除的学生学号：")
        stu_id = input("学号为：")
        with open(r"homework6\info.txt", "r") as f:
            lines = f.readlines()
        with open(r"homework6\info.txt", "w") as f:
            for line in lines:
                if stu_id not in line:
                    f.write(line)

    @staticmethod
    def update_record():
        # 修改一条学生信息记录
        print("请输入需要修改的学生信息（按学号索引，不存在则新建一条记录）：")
        class_id = input("班级为：")
        stu_id = input("学号为：")
        name = input("姓名为：")
        score = input("python成绩为：")
        with open(r"homework6\info.txt", "r") as f:
            lines = f.readlines()
        upd_rec = "{} {} {} {}\n"\
                    .format(class_id, stu_id,name, score)
        with open(r"homework6\info.txt", "w") as f:
            for line in lines:
                if stu_id in line:
                    line = upd_rec
                f.write(line)


if __name__ == '__main__':
    print("+------学生信息管理系统------+")
    while True:
        print("""
        录入一条记录 -> 1
        查找一条记录 -> 2
        删除一条记录 -> 3
        更改一条记录 -> 4
        退出 -> 0""")
        choice = input("请输入操作对应的数字：")
        if choice == '1':
            print("请输入学生信息：")
            class_id = input("班级为：")
            stu_id = input("学号为：")
            name = input("姓名为：")
            score = input("python成绩为：")
            stu = Student(class_id, stu_id, name, score)
            Student.add_record(stu)
        elif choice == '2':
            print(Student.find_record())
        elif choice == '3':
            Student.del_record()
        elif choice == '4':
            Student.update_record()
        else:
            break
