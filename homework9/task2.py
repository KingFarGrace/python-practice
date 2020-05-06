#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
@File : tak1-2.py
@Time : 2020/05/06 21:48:56
@Author : KingFar 
@Version : 1.0
@Contact : 1136421682@qq.com
@WebSite : https://github.com/KingFarGrace
"""

# here put the import lib
import socket

"""
编写一个接收数据的网络程序，由“网络调试工具”发送数据，你的程序接收数据并打印输出
"""


def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    
    udp_socket.bind(('192.168.234.1', 54804))
    # 接收数据
    recv_msg = udp_socket.recvfrom(1024)  # 1024表示本次接收的最大字节数
    # 打印显示接收到的数据
    print(recv_msg)
    #print(recv_msg[0].decode('gbk'))
    #print(recv_msg[1])
    # 关闭套接字
    udp_socket.close()

if __name__ == "__main__":
    main()