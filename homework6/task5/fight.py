#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
@File : fight.py
@Time : 2020/04/16 22:37:52
@Author : KingFar 
@Version : 1.0
@Contact : 1136421682@qq.com
@WebSite : https://github.com/KingFarGrace
"""

# here put the import lib
from dog import Dog
from human import Human
import random

"""
请写一个小游戏，人狗大站;  规则:
    1 2个角色，人和狗，游戏开始后，生成2个人，3条狗，人狗互相交替对战(注意,人只能打狗,  狗也只会咬人); 
        人的打击力为10;  初始化血为100;    狗的攻击力为 15; 初始化血为80;
    2 人被狗咬了会掉血，狗被人打了也掉血，狗和人的攻击力，具备的功能都不一样。血为0的话,表示死亡,退出游戏;
        人和狗的攻击力,都会因为被咬, 或者被打而降低(人被咬一次,打击力降低2;  狗被打一次,攻击力降低3);
    3 对战规则: 
        A  随机决定,谁先开始攻击; 
        B  一方攻击完毕后, 另外一方再开始攻击;  攻击的目标是随机的(比如, 人要打狗了, 随机找一条血不为0的狗攻击);
        C  每次攻击, 双方只能安排一个人,或者一条狗进行攻击;
提示：注意组织代码的方式；狗类用一个单独的py文件； 人用一个单独的py文件； 
在写一个fight模块（也用类来组织；在这个模块中，导入人和狗模块中编写好的方法）
"""


class Fight(object):
    __DOG_NUM = 3
    __HUMAN_NUM = 2
    __dog_list = []
    __human_list = []
    # 决定人狗攻击次序，小于500为狗队先攻击，随机取值为1-1000
    __key = 0
    
    def __init__(self):
        for idx in range(self.__DOG_NUM):
            self.__dog_list.append(Dog(idx + 1))
        for idx in range(self.__HUMAN_NUM):
            self.__human_list.append(Human(idx + 1))
        self.__key = random.randint(1, 1001)
        
    def show_battle_info(self):
        print("当前战场信息")
        print("+------------------------------+")
        print("狗队：\n")
        for idx in range(self.__DOG_NUM):
            print(self.__dog_list[idx])
        print("人队：\n")
        for idx in range(self.__HUMAN_NUM):
            print(self.__human_list[idx])

    def start(self):
        if self.__key <= 500:
            while True:
                self.show_battle_info()
                dog_rem = self.__dog_round()
                if self.__HUMAN_NUM == 0:
                    print("狗队胜利！")
                    break
                human_rem = self.__human_round()
                if self.__DOG_NUM == 0:
                    print("人队胜利！")
                    break
        else:
            while True:
                self.show_battle_info()               
                human_rem = self.__human_round()
                if self.__DOG_NUM == 0:
                    print("人队胜利！")
                    break
                dog_rem = self.__dog_round()
                if self.__HUMAN_NUM == 0:
                    print("狗队胜利！")
                    break

    
    def __dog_round(self):
        print("请狗队选择进攻队员：")
        dog_id = int(input("请输入编号："))
        human_idx = random.randint(0, self.__HUMAN_NUM - 1)
        human_obj = self.__human_list[human_idx]
        self.__dog_list[dog_id - 1].attack(human_obj)
        print("\n狗队{}号--攻击-->人队{}号\n".format(dog_id, human_obj.id + 1))
        if not human_obj.is_alive():
            print("人队{}号退场".format(human_obj.id))
            del human_obj
            self.__HUMAN_NUM -= 1

    def __human_round(self):
        print("请人队选择进攻队员：")
        human_id = int(input("请输入编号："))
        dog_idx = random.randint(0, self.__DOG_NUM - 1)
        dog_obj = self.__dog_list[dog_idx]
        self.__human_list[human_id - 1].attack(dog_obj)
        print("\n人队{}号--攻击-->狗队{}号\n".format(human_id, dog_obj.id + 1))
        if not dog_obj.is_alive():
            print("狗队{}号退场".format(dog_obj.id))
            del dog_obj
            self.__DOG_NUM -= 1


if __name__ == '__main__':
    fight = Fight()
    fight.start()