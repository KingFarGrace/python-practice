#!/usr/bin/python3
# -*- encoding: utf-8 -*-
'''
@File : task8.py
@Time : 2020/03/05 20:20:41
@Author : KingFar 
@Version : 1.0
@Contact : 1136421682@qq.com
@WebSite : https://github.com/KingFarGrace
'''

# here put the import lib

'''
设计一个数据结构，用来存放10个员工的信息并初始化，每个员工信息包括：工号，姓名，工龄，工资；  
将这10个员工，按照工资从高到低打印输出
'''


if __name__ == '__main__':
    info = [{'id' : '01', 'name' : 'A', 'age' : '3', 'salery' : 1200},
            {'id' : '02', 'name' : 'B', 'age' : '2', 'salery' : 1000},
            {'id' : '03', 'name' : 'C', 'age' : '6', 'salery' : 2400},
            {'id' : '04', 'name' : 'D', 'age' : '4', 'salery' : 1500},
            {'id' : '05', 'name' : 'E', 'age' : '9', 'salery' : 3000},
            {'id' : '06', 'name' : 'F', 'age' : '14', 'salery' : 6000},
            {'id' : '07', 'name' : 'G', 'age' : '6', 'salery' : 2500},
            {'id' : '08', 'name' : 'H', 'age' : '1', 'salery' : 800},
            {'id' : '09', 'name' : 'I', 'age' : '10', 'salery' : 5000},
            {'id' : '10', 'name' : 'J', 'age' : '12', 'salery' : 5500}]

    #以工资作为排序依据进行降序排序
    info.sort(key = lambda k : k['salery'], reverse = True)
    for i in range(len(info)):
        print("工资排行第{}的员工信息--工号：{}--姓名：{}--工龄：{}--工资：{}\n"
                .format(i + 1, info[i]['id'], info[i]['name'], 
                info[i]['age'], info[i]['salery']))
