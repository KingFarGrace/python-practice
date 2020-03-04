#!/usr/bin/python3
# -*- encoding: utf-8 -*-
'''
@File : class_3_4_demo.py
@Time : 2020/03/04 08:18:59
@Author : KingFar 
@Version : 1.0
@Contact : 1136421682@qq.com
@WebSite : https://github.com/KingFarGrace/learngit.com
'''

# here put the import lib

'''
本次练习内容：
1.将控制台输入的字符串,转换成元组, 并输出显示
2.提示输入需要购买的苹果的重量(斤),然后提示输入每斤的价格,请计算应支付的总价,并打印提示输出
3.将4种格式化输出方式实现的代码分别练习一下; 观察输出结果
4.创建一个10个元素的列表，循环输出全部，循环输出偶数
5.2-10间质数
'''


def practice_1():
    print("now start practice_1\n")
    print("输入一个列表：")
    list1 = input().split(" ")
    tup1 = tuple(list1)
    print(f"转化成元组输出：{tup1}\n")


def practice_2():
    print("now start practice_2\n")
    count = int(input("请输入购买苹果的量："))
    price = int(input("请输入苹果的单价："))
    print(f"总价为:{count * price}\n")


def practice_3():
    print("now start practice_3\n")
    a = 'a'
    b = 'b'
    print("字符串拼接：" + a + " and " + b + '\n')
    print("格式控制符：%s and %s\n" % (a, b))
    print("大括号name：{_a} and {_b}\n".format(_a=a, _b=b))
    print("大括号索引：{0} and {1}\n".format(a, b))


def practice_4():
    print("now start practice_4\n")
    list1 = range(1, 11)
    print("列表为：")
    for i in list1:
        print(i, end=" ")
    print('\n')
    for i in list1:
        if i % 2 == 0:
            print("%d是偶数" % i, end=" ")


def practice_5():
    print("now start practice_5\n")
    for i in range(2, 11):
        flag = 1
        for j in range(2, i):
            if i % j == 0:
                flag = 0
                break
        if flag == 1:
            print("%d是质数" % i)
    else :
        print("没有循环数据")

if __name__ == '__main__':
    # practice_1()
    # print("\n————————————————————————————\n")
    # practice_2()
    # print("\n————————————————————————————\n")
    # practice_3()
    # print("\n————————————————————————————\n")
    practice_4()
    print("\n————————————————————————————\n")
    practice_5()
