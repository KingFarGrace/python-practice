#!/usr/bin/python3
# -*- encoding: utf-8 -*-
'''
@File : class_3_6_demo.py
@Time : 2020/03/06 08:16:07
@Author : KingFar 
@Version : 1.0
@Contact : 1136421682@qq.com
@WebSite : https://github.com/KingFarGrace
'''

# here put the import lib

'''
1.定义一个函数,来计算苹果的价格(重量*价格); 通过键盘输入重量和价格,然后调用函数来计算
2.定义一个函数,  打印输出列表里面的元素;  然后增加列表中的元素, 然后再输出新的列表;  主程序中,打印这个列表的地址(传参之前,传参之后)
3.初始化一个列表(1-20之间的整数) ; 然后 使用匿名函数,列表解析式, 来打印输出一个列表中的奇数
4.使用不定长参数定义一个函数;实现对输入数据的封装(封装成一个元组和字典),然后打印输出
'''

def sum_price(weight, price):
    return weight * price

def print_list(l):
    for i in range(len(l)):
        print(l[i], end = " ")
    print("列表的地址为：{}".format(id(l)))

def lambda_test():
    list1 = [x for x in range(1, 21)]
    odd_nums = filter(lambda x : x % 2 != 0, list1)
    print(list(odd_nums))

def parameter_test(para1, *para2, **para3):
    print("para1：{}".format(para1))
    print("para2：{}".format(para2))
    print("para3：{}".format(para3))

if __name__ == '__main__':
    # weight = int(input("请输入重量："))
    # price = int(input("请输入单价："))
    # print("总价为：{}".format(sum_price(weight, price)))

    list1 = [1, 2, 3]
    print_list(list1)
    list1.append(4)
    print_list(list1)

    lambda_test()

    parameter_test(1, 2, 3, b=4, c=5)