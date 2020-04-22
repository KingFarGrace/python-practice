#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
@File : dog.py
@Time : 2020/04/16 22:37:57
@Author : KingFar 
@Version : 1.0
@Contact : 1136421682@qq.com
@WebSite : https://github.com/KingFarGrace
"""

# here put the import lib


class Dog(object):
    """
    类功能概述：狗 类，用于描述一个狗对象
    
    类功能具体描述：完成了狗的初始化/信息描述/攻击/受伤/判断是否死亡等功能
    
    类变量
    --------------------
    私有变量：
    __hp：初始化为100，描述狗的血量
    __attack：初始化为10，描述狗的攻击力
    __alive_flag：初始化为True，描述一个狗的实例是否存活

    公有变量：
    id：表示了一个狗实例的编号，不同实例的编号是彼此不同的
    
    方法及功能概述
    --------------------
    实例方法：
    attack(self, dog_obj)：攻击一个人类的实例
    get_damage(self, enm_dam)：受伤方法
    is_alive(self)：判断狗是否存活
    get_attack(self)：返回狗攻击力数值

    类方法：

    静态方法：   
    
    """
    __hp = 80
    __attack = 15
    __alive_flag = True
    id = 0

    def __init__(self, id):
        self.id = id

    # 描述一个人类实例的信息
    def __str__(self):
        return "Dog No.{0:<2}---HP:{1:<5}ATK:{2:<5}\n"\
                .format(self.id, self.__hp, self.__attack)

    def attack(self, human_obj):
        # 调用人类对象的受伤方法
        human_obj.get_damage(self.__attack)

    def get_damage(self, enm_dam):
        """
        enm_dam：某个人类实例的攻击力数值
        根据  enm_dam  大小扣除生命值
        受到不为  0  的伤害时扣除  3  点攻击力
        攻击力最小只能为  0
        生命值为  0  则修改  __alive_flag  变量
        """
        self.__hp -= enm_dam
        if enm_dam == 0:
            self.__attack -= 0
        else:
            self.__attack -= 3
        if self.__hp == 0:
            self.__alive_flag = False
        if self.__attack < 0:
            self.__attack = 0

    def is_alive(self):
        return self.__alive_flag

    def get_attack(self):
        return self.__attack
