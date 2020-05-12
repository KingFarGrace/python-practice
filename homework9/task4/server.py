#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
@File : server.py
@Time : 2020/05/07 21:51:23
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
服务器端
"""


class Server(object):

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.addr = (get.get_ip(), 8080)
        self.users = {}
        self.flag = False

    def __str__(self):
        return """
        服务器ip：{}
        服务器端口号：{}
        服务器状态：{}
        服务器当前连接用户：\n{}
        """.format(self.addr[0], self.addr[1], 
                    self.get_status(), self.get_users())

    def get_status(self):
        if self.flag == True:
            return "服务器已开启"
        else:
            return "服务器已关闭"

    def get_users(self):
        ustr = ""
        for a, s in self.users.items():
            ustr += "用户地址：{}\n".format(a)
            ustr += "用户套接字：{}\n".format(s)
        return ustr

    def start_server(self):
        try:
            self.sock.bind(self.addr)
            self.sock.listen(5)
            self.flag = True
            print("服务器启动成功！等待用户连接...")
            print("输入quit关闭服务器\info查看服务器信息")
        except Exception as e:
            print("服务器启动失败！\n错误报告：{}".format(e))
        self.get_conn()

    def get_conn(self):
        while True:
            s, a = self.sock.accept()
            self.users[a] = s
            print("用户ip：{}连接至服务器\n当前服务器内人数：{}"
                                    .format(a, len(self.users)))
            t = threading.Thread(target=self.recv_msg, args=(s, a))
            t.start()
    
    def recv_msg(self, s, a):
        while True:
            try:
                resp = s.recv(1024).decode("utf-8")
                print("{}\n用户 {}：{}".format(get.get_time(), a, resp))
                for user in self.users.values():
                    user.send(resp.encode("utf-8"))
            except ConnectionResetError:
                print("用户{}断开连接".format(a))
                self.users.pop(a)
                break
            except TypeError:
                print("接收信息失败！")

    def quit_server(self):
        for user in self.users.values():
            user.close()
        self.sock.close()
        self.flag = False
        os._exit(0)


if __name__ == '__main__':
    server = Server()
    print(server)
    server.start_server()
    while True:
        cmd = input()
        if cmd == "quit":
            server.quit_server()
        if cmd == "info":
            print(server)
        