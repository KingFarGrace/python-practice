#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
@File : class_4_8_demo.py
@Time : 2020/04/08 10:28:10
@Author : KingFar 
@Version : 1.0
@Contact : 1136421682@qq.com
@WebSite : https://github.com/KingFarGrace
"""

# here put the import lib

"""
定义一个dog类(颜色, 名称), 里面有一个狗叫的方法; 不同的狗叫声可能不一样;  然后实例化几条狗, 然后统计实例化狗的数量
"""


class Dog(object):
    obj_count = 0

    def __init__(self, color, name):
        # super().__init__()
        self.__color = color
        self.__name = name
        Dog.obj_count += 1

    def bark(self):
        print("{}的{}叫了".format(self.__color, self.__name))


if __name__ == '__main__':
    akita = Dog("黄色", "秋田犬")
    akita.bark()
    husky = Dog("灰色", "哈士奇")
    husky.bark()
    gold = Dog("金色", "金毛犬")
    gold.bark()
    print("现在有{}只狗".format(Dog.obj_count))
