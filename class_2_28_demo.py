#!/usr/bin/python3
# -*- encoding: utf-8 -*-
'''
@File : class_2_28_demo.py
@Time : 2020/03/03 20:32:35
@Author : KingFar 
@Version : 1.0
@Contact : 1136421682@qq.com
@WebSite : https://github.com/KingFarGrace/learngit.com
'''

# here put the import lib

'''
本次练习内容：
1.定义元组,进行基本的操作(元组的基本运算,元素的输出,内置函数的使用); 定义一个元组,来保存成绩,输出最高分;
2.定义一个字典,存放某个同学的信息(学号,姓名,班级,年龄);   再定义另外一个字典,存放5个同学的学号,姓名信息;
    通过键来访问相应的数据; 或者整体输出
3.字典的元素的增加, 修改,删除;并观察输出
4.定义一个集合类型的变量(用2种方法初始化),然后进行相应的 元素的操作
'''

def practice_1() :
    print("now start practice_1\n")
    tup1 = ('what', 'a', 'nice', 'day')
    tup2 = ('isn\'t', 'it')
    print(f"tup1: {tup1}\n")
    print(f"tup2: {tup2}\n")
    print(f"tup1 + tup2: {tup1 + tup2}\n")
    print(f"tup2 * 2: {tup2 * 2}\n")
    print(f"tup1[1 : 3]: {tup1[1 : 3]}\n")
    print(f"tup2[-2] : {tup2[-2]}\n")

    score = (98, 67, 78, 93, 72, 83, 87, 69, 54, 88)
    print(f"成绩依次为：{score}\n最高分为：{max(score)}\n")

def practice_2() :
    print("now start practice_2\n")
    info = {'id' : '01', 'name' : 'Tom', 'class' : 'A', 'age' : '18'}
    print(f"一个人的信息：{info}\n")
    infos = {'info1' : ['02', 'Alice'], 'info2' : ['03', 'Jack'], 'info3' : ['04', 'John'], 'info4' : ['05', 'Bob']}
    print(f"第一个人的名字: {infos['info1'][1]}\n")
    print(f"第二个人的学号：{infos['info2'][0]}\n")
    print(f"剩下两个人的信息：{infos['info3'] + infos['info4']}\n")

def practice_3() :
    print("now start practice_3\n")
    dict1 = {'1' : 'A'}
    print(f"init dict: {dict1}\n")
    dict1['2'] = 'B'
    print(f"add 2-B to dict1: {dict1}\n")
    dict1['2'] = 'b'
    print(f"change 2-B to 2-b: {dict1}\n")
    del dict1['2']
    print(f"delete key 2: {dict1}\n")

def practice_4() :
    print("now start practice_4\n")
    set1 = {'1', '2', '3'}
    set2 = set('a')
    print(f"set1: {set1}\nset2: {set2}\n")
    set2.add('b')
    print(f"add b to set2: {set2}\n")
    set2.discard('b')
    print(f"delete b from set2: {set2}\n")
    random = set1.pop()
    print(f"delete a random value \'{random}\' from set1: {set1}\n")
    set2.clear()
    print(f"clear set2: {set2}\n")
    set1.clear()
    print(f"clear set1: {set1}\n")

if __name__ == "__main__" :
    practice_1()
    print("\n————————————————————————————\n")
    practice_2()
    print("\n————————————————————————————\n")
    practice_3()
    print("\n————————————————————————————\n")
    practice_4()