#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
@File : task8.py
@Time : 2020/03/29 10:54:20
@Author : KingFar 
@Version : 1.0
@Contact : 1136421682@qq.com
@WebSite : https://github.com/KingFarGrace
"""

# here put the import lib
import random

"""
京东二面笔试题
1） 生成一个大文件ip.txt,要求1200行，每行随机为172.25.254.0---172.25.254.254段的ip;
2） 读取ip.txt文件统计这个文件中ip出现频率排前10的ip
"""


def create_ip():
    with open("homework4\ip.txt", "w") as f:
        for i in range(1200):
            rand_ip = "172.25.254." + str(random.randint(0, 255))
            f.write(rand_ip + '\n')


def count_ip():
    ip_dict = {}
    with open("homework4\ip.txt", "r") as f:
        for line in f:
            line = line.strip('\n')
            ip_reg = line.split(".")[3]
            if ip_reg not in ip_dict:
                ip_dict[ip_reg] = 1
            else:
                ip_dict[ip_reg] += 1
    return ip_dict


def dict_to_list(any_dict):
    any_list = [(k, v) for k, v in any_dict.items()]
    return any_list


if __name__ == '__main__':
    # create_ip()
    ip_list = dict_to_list(count_ip())
    ip_list.sort(key=lambda k : k[1], reverse=True)
    ip_list = ip_list[0: 11]
    print("出现频率前十的ip地址从高到低为：")
    for rec in ip_list:
        print("172.25.254.{}".format(rec[0]))
