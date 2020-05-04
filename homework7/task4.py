#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
@File : task4.py
@Time : 2020/04/22 21:34:00
@Author : KingFar 
@Version : 1.0
@Contact : 1136421682@qq.com
@WebSite : https://github.com/KingFarGrace
"""

# here put the import lib
import requests
from bs4 import BeautifulSoup

"""
爬取这个网址上https://www.programcreek.com/python/，搜索request的范例代码；保存到txt文件中（只保留文字）；
    文本文件类似（注意是类似的效果，不是说一定要做的一模一样）的效果如下：

  参考文档：https://blog.csdn.net/weixin_43687366/article/details/88877996
   大家看完这篇文档后，再开始动手做这道题；
"""


def _get_link():
    # 从https://www.programcreek.com/python/爬取所有代码范例的链接
    try:
        url = "https://www.programcreek.com/python/index/221/requests"
        head = {'user-agent':
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                  AppleWebKit/537.36 (KHTML, like Gecko) \
                  Chrome/81.0.4044.129 Safari/537.36'}
        html = requests.get(url, headers=head)
        html.raise_for_status()
        html.encoding = html.apparent_encoding
        soup = BeautifulSoup(html.content, "lxml")
        url_list = []
        content = soup.find("div", id="content").ul.find_all("li")
        for rec in content:
            url_list.append(rec.find("div").a.attrs['href'])
    except Exception as e:
        print("获取页面信息失败！")
        print(e)
    finally:
        return url_list


def get_source():
    # 范例链接列表
    url_list = _get_link()
    head = {'user-agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/81.0.4044.129 Safari/537.36'}
    # 遍历访问每个链接
    for rec in url_list:
        try:
            html = requests.get(rec, headers = head)
            html.raise_for_status()
            html.encoding = html.apparent_encoding
            soup = BeautifulSoup(html.content, "lxml")
            # 获取页面main标签（包含范例的所有内容）
            main = soup.find("div", id="content").find("div", id="main")
            # 向文件中写入第一个requests方法的范例总标题
            file = open("homework7\python_exm.txt", "a")
            file.write('\n')
            file.write("+------------------------------------------+")
            file.write("Python " + main.h1.span.string + " Example")
            file.write("+------------------------------------------+")
            file.write('\n\n')
            # 找到所有范例框对应标签，存入列表并遍历
            examples = soup.find_all("div", attrs={'class': 'examplebox'})
            count = 0
            for exm in examples:
                count += 1
                # 提取范例项目标题
                exm_head = exm.find("div", attrs={'class': 'exampleboxheader'})
                file.write("example{}-Project:{}"
                .format(count, exm_head.table.tbody.tr.td.span.string))
                file.write('\n')
                # 提取范例代码内容
                exm_body = exm.find("div", attrs={'class': 'exampleboxbody'})
                pre = exm_body.pre
                for child in pre.children:
                    file.write(child.string)
                    file.write('\n\n')
                # 刷新缓存区
                file.flush()
        except Exception as e:
            print("爬取网页失败！")
            print(e)
        finally:
            file.close()


if __name__ == '__main__':
    get_source()