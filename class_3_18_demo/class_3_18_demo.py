#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
@File : class_3_18_demo.py
@Time : 2020/03/18 08:57:09
@Author : KingFar 
@Version : 1.0
@Contact : 1136421682@qq.com
@WebSite : https://github.com/KingFarGrace
"""

# here put the import lib
import os
import pickle

"""
1.在window平台下练习os.path 相关方法的使用
2.打印class_3_18_demo_f1.txt中的内容
3.分别在指定位置打开文件进行写入操作
4.给定一个字典,保存了5个同学的学号,姓名,年龄;使用pickle模块将数据对象保存到文件中去
5.读取文件里面的内容(包含中文), 进行打印输出显示;
         注意:  请设置文件的不同编码格式进行观察;  另外,文件内容中包含中文字符
"""

def show_some_file_op():
    print(os.path.basename('/root/class_3_18_demo.py'))         # 返回文件名
    print(os.path.dirname('/root/class_3_18_demo.py'))          # 返回目录路径
    print(os.path.split('/root/class_3_18_demo.py'))            # 分割文件名与路径
    print(os.path.join('root', 'test', 'class_3_18_demo.py'))   # 将目录和文件名合成一个路径


def print_file1():
    with open("class_3_18_demo_f1.txt", "r", encoding='utf-8') as file1:
        for line in file1:
            print(line)


def open_some_file():
    f1 = open("class_3_18_demo_f1.txt", "r", encoding='utf-8')
    print(f1.readlines())
    f2 = open(r"homework2\task_list.txt", "r", encoding='utf-8')
    print(f2.readlines())
    # f3 = open(r"..\somefile\aa.txt", "r", encoding='utf-8')


def test_pickle():
    dict1 = {   'info1': [1, 88, 18],
                'info2': [2, 78, 18],
                'info3': [3, 85, 19],
                'info4': [4, 79, 18],
                'info5': [5, 66, 19]}

    with open("class_3_18_demo_f2.txt", "wb") as file:
        pickle.dump(dict1, file)
        
    with open("class_3_18_demo_f2.txt", "rb") as file:
        file_data = pickle.load(file)
        print(file_data)


# 读不进来
# def show_ch_in_file():
#     with open("class_3_18_demo_f3.txt", "r") as file:
#         print(file.readline(), encoding="utf-8")
#         print(file.readline(), encoding="gbk2000")


if __name__ == '__main__':
    show_some_file_op()
    print("\n——————————————————————————————\n")
    print_file1()
    print("\n——————————————————————————————\n")
    open_some_file()
    print("\n——————————————————————————————\n")
    test_pickle()
    print("\n——————————————————————————————\n")
    # show_ch_in_file()