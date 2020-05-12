#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
@File : get.py
@Time : 2020/05/07 21:43:12
@Author : KingFar 
@Version : 1.0
@Contact : 1136421682@qq.com
@WebSite : https://github.com/KingFarGrace
"""

# here put the import lib
from datetime import datetime
import socket

"""
存放基本方法的模块
"""


def get_ip():
    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    return ip


def get_time():
    now = datetime.now()
    fnow = now.strftime("%Y-%m-%d %H:%M:%S")
    return fnow