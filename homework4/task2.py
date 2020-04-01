#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
@File : task2.py
@Time : 2020/03/29 10:51:18
@Author : KingFar 
@Version : 1.0
@Contact : 1136421682@qq.com
@WebSite : https://github.com/KingFarGrace
"""

# here put the import lib
from datetime import date
from datetime import datetime
from datetime import timedelta

"""
定义一个函数，判断一个输入的日期，是当年的第几周，周几？  将程序改写一下，能针对我们学校的校历时间进行计算（校历第1周，2月17-2月23；校历第27周，8月17-8月23；）
"""


def get_week(date):
    gap = timedelta(days=47)
    sch_date = date - gap
    date_info = sch_date.isocalendar()
    # print("{}是{}年第{}周的周{}".format(date.date(), 
    #         datetime.strftime(date, "%Y"), 
    #         date_info[1], date_info[2]))
    print("校历第{}周".format(date_info[1]))


if __name__== '__main__':
    date_str = input("请输入年月日，用-分开：")
    real_date = datetime.strptime(date_str, "%Y-%m-%d")
    get_week(real_date)