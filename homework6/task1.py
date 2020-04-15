#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
@File : task1.py
@Time : 2020/04/15 20:59:15
@Author : KingFar 
@Version : 1.0
@Contact : 1136421682@qq.com
@WebSite : https://github.com/KingFarGrace
"""

# here put the import lib

"""
定义一个狗类,里面有一个 列表成员变量(列表的元素是字典), 分别记录了 3种颜色的狗的颜色, 数量,和价格;
       实现狗的买卖交易方法;  打印输出经过2-3次买卖方法后,剩下的各类狗的数量;
"""

class Dog(object):
    dog_list = [{'name': 'akita', 'color': 'yellow', 'count': 10, 'price': 1000},
                {'name': 'husky', 'color': 'gray', 'count': 20, 'price': 2000},
                {'name': 'goldhair', 'color': 'gold', 'count': 5, 'price': 4000}]

    def __str__(self):
        info = "当前剩余：\n"
        for rec in Dog.dog_list:
            info += "品种：{0:^10}颜色：{1:^10}数量：{2:^10}价格：{3:^10}\n"\
                .format(rec['name'], rec['color'], rec['count'], rec['price'])
        return info
    
    def sell(self, name):
        for rec in self.dog_list:
            if rec['name'] == name:
                rec['count'] -= 1
                return "售出颜色为{}的{}一只，花费{}元"\
                        .format(rec['color'], name, rec['price'])
                
        return "没有名为{}的狗！".format(name)


if __name__ == '__main__':
    dog = Dog()
    print(dog)
    print(dog.sell("akita"))
    print(dog.sell("husky"))
    print(dog.sell("goldhair"))
    print(dog)
