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
    __hp = 80
    __attack = 15
    __alive_flag = True
    id = 0

    def __init__(self, id):
        self.id = id

    def __str__(self):
        return "Dog No.{0:<2}---HP:{1:<5}ATK:{2:<5}\n"\
                .format(self.id, self.__hp, self.__attack)

    def attack(self, human_obj):
        human_obj.get_damage(self.__attack)

    def get_damage(self, enm_dam):
        self.__hp -= enm_dam
        self.__attack -= 3
        if self.__hp == 0:
            self.__alive_flag = False
        if self.__attack < 0:
            self.__attack = 0

    def is_alive(self):
        return self.__alive_flag
