#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
@File : task2.py
@Time : 2020/05/06 21:56:05
@Author : KingFar 
@Version : 1.0
@Contact : 1136421682@qq.com
@WebSite : https://github.com/KingFarGrace
"""

# here put the import lib
import socket
from threading import Thread

"""
编写一个UDP的聊天程序，客户端和服务器端能互相聊天应答
"""

def client():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 使用8080端口
    dest_addr = ('192.168.234.1', 8080)
    while(True):
        send_msg = input("请输入要发送的数据:")
        udp_socket.sendto(send_msg.encode('utf-8'), dest_addr)
    udp_socket.close()


def server():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(('192.168.234.1', 8080))
    while(True):
        recv_msg = udp_socket.recvfrom(1024)
        print(">>>客户端{}消息：{}".format(recv_msg[1], recv_msg[0]))
    udp_socket.close()

   
if __name__ == "__main__":   
    t1 = Thread(target=server)
    t1.start()
    client()