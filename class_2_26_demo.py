#!/usr/bin/python3
# -*- encoding: utf-8 -*-
'''
@File : class_2_26_demo.py
@Time : 2020/03/03 19:42:08
@Author : KingFar 
@Version : 1.0
@Contact : 1136421682@qq.com
@WebSite : https://github.com/KingFarGrace/learngit.com
'''

# here put the import lib

'''
本次练习内容：
1.自定义不同字符串，练习输出和换行
2.练习: 定义一个字符串,分别进行查找某个字符串是否包含在这个字符串里面; 进行某个字符串的替换; 打印字符串的长度;
3.用列表定义10个同学的成绩,输出最高分,最低分,总分和平均值
'''

def practice_1() :
    print("now start practice_1\n")
    str1 = 'this is str1 defined by \'\t\''
    str2 = "this is str2 defined by \"\t\""
    para1 = '''
    this is para1
    defined by \'\'\'\t\'\'\'
    '''
    print("普通方法打印str1：%s\n" % str1)
    print(f"f_string打印str2：{str2}\n")
    print("普通方法打印para1：%s\n" % para1)

def practice_2() :
    print("now start practice_2\n")
    str1 = 'this is an example'
    print(f"str1：{str1}，字符串长度为：%d\n" % len(str1))
    flag1 = str1.find('example')
    flag2 = str1.find('instance')
    print("字符串中是否含有example？\t", flag_to_bool(flag1), '\n')
    print("字符串中是否含有instance？\t", flag_to_bool(flag2), '\n')
    print("将example替换为instance：")
    str1 = str1.replace('example', 'instance', 1)
    print(f"替换后的str1：{str1}，字符串长度为：%d\n" % len(str1))

def flag_to_bool(flag) :
    if(flag >= 0) :
        return "Yes"
    else :
        return "No"

def practice_3() :
    print("now start prctice_3\n")
    score = [98, 67, 78, 93, 72, 83, 87, 69, 54, 88]
    print(f"{len(score)}名同学的成绩依次为：{score}\n")
    print(f"最高分为：{max(score)}\n")
    print(f"最低分为：{min(score)}\n")
    print(f"总分为：{sum(score)}\n")
    print(f"平均分为：{sum(score) / len(score)}\n")

if __name__ == "__main__" :
    practice_1()
    print("\n————————————————————————————\n")
    practice_2()
    print("\n————————————————————————————\n")
    practice_3()