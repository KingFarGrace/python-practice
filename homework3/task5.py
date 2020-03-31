#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
@File : task5.py
@Time : 2020/03/29 10:49:43
@Author : KingFar 
@Version : 1.0
@Contact : 1136421682@qq.com
@WebSite : https://github.com/KingFarGrace
"""

# here put the import lib
import pickle

"""
在2个文件中存放了英文计算机技术文章(可以选择2篇关于Python技术文件操作处理技巧的2篇英文技术文章), 请读取文章内容,进行词频的统计;并分别输出统计结果到另外的文件存放;
比较这2篇文章的相似度(如果词频最高的前10个词,重复了5个,相似度就是50%;重复了6个,相似度就是60% ,......)
"""

def text_spliter(text_path):
    #将文本中特殊字符替换为空格,大写替换为小写，再做拆分
    try:
        txt = open(text_path, "r", encoding="utf-8")
        text_part = ""
        for line in txt:
            line = line.strip('\n')
            text_part += line
        text_part.lower()
        for ch in r'[]\;,./<>?:{}|~!@#$%^&*()_+1234567890':
            text_part = text_part.replace(ch, " ")
    except IOError as ioe:
        print(ioe)
    finally:
        txt.close()
        return text_part.split()


def count_word(word_list):
    word_dict = {}
    for word in word_list:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    return word_dict


def dict_to_list(any_dict):
    any_list = [(k, v) for k, v in any_dict.items()]
    return any_list


def save_result(url, result):
    try:
        result_file = open(url, "wb")
        pickle.dump(result, result_file)
    except IOError as ioe:
        print(ioe)
    finally:
        result_file.close()


def rep_rate(r1, r2):
    word_list1 = [record[0] for record in r1]
    word_list2 = [record[0] for record in r2]
    rep_count = 0
    for word in word_list1:
        for idx in word_list2:
            if word == idx:
                rep_count += 1
                del idx
                break
    return rep_count / 10


if __name__ == '__main__':
    art1_path = r"homework3\art1.txt"
    art2_path = r"homework3\art2.txt"
    text1 = dict_to_list(count_word(text_spliter(art1_path)))
    text1.sort(key=lambda k : k[1], reverse=True)
    text2 = dict_to_list(count_word(text_spliter(art2_path)))
    text2.sort(key=lambda k : k[1], reverse=True)
    # print(text1)
    # print(text2)
    result_path = r"homework3\word_count.pkl"
    save_result(result_path, text1)
    save_result(result_path, text2)
    text1 = text1[0: 11]
    text2 = text2[0: 11]
    print("两篇文章重复率为：{}%".format(rep_rate(text1, text2) * 100))
