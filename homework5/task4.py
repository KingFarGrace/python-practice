#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
@File : task4.py
@Time : 2020/04/07 17:05:18
@Author : KingFar 
@Version : 1.0
@Contact : 1136421682@qq.com
@WebSite : https://github.com/KingFarGrace
"""

# here put the import lib

"""
编写装饰器来实现，对目标函数进行装饰，分3种情况：目标函数无参数无返回值，目标函数有参数，目标函数有返回值；
     三个目标函数分别为：
     A 打印输出20000之内的素数；
     B 计算整数2-10000之间的素数的个数；
     C 计算整数2-M之间的素数的个数；
"""

def type_check(state):
     def decorator(func):
          def wrapper(*args, **kwargs):
               print("{}(){}".format(func.__name__, state))
               return func(*args, **kwargs)
          return wrapper
     return decorator


def isprime(x):
     if x <= 1:
          return False
     if x == 2:
          return True
     flag = True
     for j in range(2, x):
          if x % j == 0:
               flag = False
               break
     return flag


@type_check("无参数和返回值")
def print_prime():
     count = 0
     for i in range(20000):
          if isprime(i):
               print(i, end=" ")
               count += 1
               if count % 10 == 0:
                    print('\n')
     print('\n')


@type_check("有返回值")
def count_prime_2_10000():
     count = 0
     for i in range(10001):
          if isprime(i):
               count += 1
     return count


@type_check("有参数")
def count_prime_2_m(m):
     count = 0
     for i in range(m + 1):
          if isprime(i):
               count += 1
     return count


if __name__ == '__main__':
     print_prime()
     print("2-10000中有{}个质数\n".format(count_prime_2_10000()))
     bound = int(input("请输入m的值："))
     print("2-{}中有{}个质数\n".format(bound, count_prime_2_m(bound)))