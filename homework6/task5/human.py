#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
@File : human.py
@Time : 2020/04/16 22:38:00
@Author : KingFar 
@Version : 1.0
@Contact : 1136421682@qq.com
@WebSite : https://github.com/KingFarGrace
"""

# here put the import lib


class Human(object):
    """
    类功能概述：人类 类，用于描述一个人类对象
    
    类功能具体描述：完成了人类的初始化/信息描述/攻击/受伤/判断是否死亡等功能
    
    类变量
    --------------------
    私有变量：
    __hp：初始化为100，描述人类的血量
    __attack：初始化为10，描述人类的攻击力
    __alive_flag：初始化为True，描述一个人类的实例是否存活

    公有变量：
    id：表示了一个人类实例的编号，不同实例的编号是彼此不同的
    
    方法及功能概述
    --------------------
    实例方法：
    attack(self, dog_obj)：攻击一个狗的实例
    get_damage(self, enm_dam)：受伤方法
    is_alive(self)：判断人类是否存活
    get_attack(self)：返回人类攻击力数值

    类方法：

    静态方法：   
    
    """
    __hp = 100
    __attack = 10
    __alive_flag = True
    id = 0

    def __init__(self, id):
        self.id = id
    
    # 描述一个人类实例的信息
    def __str__(self):
        return "Human No.{0:<2}---HP:{1:<5}ATK:{2:<5}\n"\
                .format(self.id, self.__hp, self.__attack)

    def attack(self, dog_obj):
        # 调用狗对象的受伤方法
        dog_obj.get_damage(self.__attack)

    def get_damage(self, enm_dam):
        """
        enm_dam：某个狗实例的攻击力数值
        根据  enm_dam  大小扣除生命值
        受到不为  0  的伤害时扣除  2  点攻击力
        攻击力最小只能为  0
        生命值为  0  则修改  __alive_flag  变量
        """
        self.__hp -= enm_dam
        if enm_dam == 0:
            self.__attack -= 0
        else:
            self.__attack -= 2
        if self.__hp == 0:
            self.__alive_flag = False
        if self.__attack < 0:
            self.__attack = 0

    def is_alive(self):
        return self.__alive_flag

    def get_attack(self):
        return self.__attack