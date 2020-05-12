#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
@File : client.py
@Time : 2020/05/07 21:52:02
@Author : KingFar 
@Version : 1.0
@Contact : 1136421682@qq.com
@WebSite : https://github.com/KingFarGrace
"""

# here put the import lib
import socket
import threading
import os
import get

"""
客户端
"""

def recv_msg(s):
    print("消息接收：已开启")
    while True:
        try:
            resp = s.recv(1024)
            print(resp.decode("utf-8"))
        except ConnectionResetError:
            print("服务器已关闭，您已被强制断开连接。")
            s.close()
            break
    os._exit(0)


def send_msg(s):
    print("消息发送：已开启")
    print("输入消息，按回车发送")
    print("输入exit离开聊天室")
    while True:
        msg = input()
        if msg == "exit":
            print("已退出聊天室")
            print("与服务器的连接已断开")
            s.close()
            break
        s.send(msg.encode("utf-8"))
    os._exit(0)


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = input("请输入服务器地址：")
    server_port = int(input("请输入服务器端口号："))
    addr = (server_ip, server_port)
    sock.connect(addr)
    recv_t = threading.Thread(target=recv_msg, args=(sock, ))
    send_t = threading.Thread(target=send_msg, args=(sock, ))
    recv_t.start()
    send_t.start()