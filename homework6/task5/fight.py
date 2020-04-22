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
    """
    类功能概述：封装了开始一场战斗所必要的功能
    
    类功能具体描述：实现了战斗的开始/胜负条件判断/战场信息更新描述等功能
    
    类变量
    --------------------
    私有变量：
    __dog_num：当前战场上存活的狗的数量，初始化为  3
    __human_num：当前战场上存活的人类的数量， 初始化为  2
    __dog_list：狗对象列表
    __human_list：人对象列表
    __key：决定人狗攻击次序，小于  500  为狗队先攻击，
            随机在  1-1000  之间取值，初始化为  0

    公有变量：
    
    方法及功能概述
    --------------------
    实例方法：
    show_battle_info(self)：输出当前战场信息
    start(self)：开始一场战斗，满足胜负条件时自动结束
    __dog_round(self)：开始狗队的行动轮次
    __human_round(self)：开始人队的行动轮次
    __is_dog_exhausted(self)：判断狗队是否已经无战斗能力（攻击力都为0）
    __is_human_exhausted(self)：判断人队是否已经无战斗能力（攻击力都为0）

    类方法：

    静态方法：   
    
    """

    __dog_num= 3
    __human_num = 2
    __dog_list = []
    __human_list = []
    __key = 0
    
    def __init__(self):
        # 初始化  3  条狗和  2  个人，随机生成一个判断轮次优先的  key
        for idx in range(self.__dog_num):
            self.__dog_list.append(Dog(idx + 1))
        for idx in range(self.__human_num):
            self.__human_list.append(Human(idx + 1))
        self.__key = random.randint(1, 1001)
        
    def show_battle_info(self):
        print("当前战场信息")
        print("+------------------------------+")
        print("狗队：\n")
        for idx in range(self.__dog_num):
            print(self.__dog_list[idx])
        print("人队：\n")
        for idx in range(self.__human_num):
            print(self.__human_list[idx])

    def start(self):
        """
        划分攻击先后次序后，进入循环战斗直到满足胜负条件
        胜负条件：
        1. 先死光的队伍输
        2. 攻击力全部为零的队伍自动判负
        3. 先攻击的队伍先判断胜负

        每一个战斗轮次顺序：
        -> 输出战场信息
        -> 先攻击的队伍开始战斗轮次
        -> 判断一次胜负条件
        -> 后攻击的队伍开始战斗轮次
        -> 判断一次胜负条件
        因为判断了两次，所以不会出现平局
        """
        if self.__key <= 500:
            while True:
                self.show_battle_info()
                dog_rem = self.__dog_round()
                if self.__human_num == 0 or self.__is_human_exhausted():
                    print("狗队胜利！")
                    break
                human_rem = self.__human_round()
                if self.__dog_num == 0 or self.__is_dog_exhausted():
                    print("人队胜利！")
                    break
        else:
            while True:
                self.show_battle_info()               
                human_rem = self.__human_round()
                if self.__dog_num == 0 or self.__is_dog_exhausted():
                    print("人队胜利！")
                    break
                dog_rem = self.__dog_round()
                if self.__human_num == 0 or self.__is_human_exhausted():
                    print("狗队胜利！")
                    break

    
    def __dog_round(self):
        # 用户选择一名攻击者
        print("请狗队选择进攻队员：")
        dog_id = int(input("请输入编号："))
        # 系统随机选择一名攻击对象
        human_idx = random.randint(0, self.__human_num - 1)
        human_obj = self.__human_list[human_idx]
        self.__dog_list[dog_id - 1].attack(human_obj)
        # 输出攻击信息
        print("\n狗队{}号--攻击-->人队{}号\n".format(dog_id, human_obj.id + 1))
        # 判断被攻击者是否存活，死亡则离场（从列表中删除）
        if not human_obj.is_alive():
            print("人队{}号退场".format(human_obj.id))
            del human_obj
            # 更新存活者数量
            self.__human_num -= 1

    def __human_round(self):
        # 结构同  __dog_round(self)
        print("请人队选择进攻队员：")
        human_id = int(input("请输入编号："))
        dog_idx = random.randint(0, self.__dog_num - 1)
        dog_obj = self.__dog_list[dog_idx]
        self.__human_list[human_id - 1].attack(dog_obj)
        print("\n人队{}号--攻击-->狗队{}号\n".format(human_id, dog_obj.id + 1))
        if not dog_obj.is_alive():
            print("狗队{}号退场".format(dog_obj.id))
            del dog_obj
            self.__dog_num -= 1

    def __is_dog_exhausted(self):
        # 如果有攻击力不为零的狗存在，则返回False，反之返回True
        for idx in range(self.__dog_num):
            if self.__dog_list[idx].get_attack() != 0:
                return False
        return True    

    def __is_human_exhausted(self):
        # 如果有攻击力不为零的人存在，则返回False，反之返回True
        for idx in range(self.__human_num):
            if self.__human_list[idx].get_attack() != 0:
                return False
        return True                


if __name__ == '__main__':
    fight = Fight()
    fight.start()