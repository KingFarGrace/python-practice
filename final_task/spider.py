# !/usr/bin/python3
# -*- encoding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import dbutil.database as db


def get_info(head, end):
    header = {'User-Agent':
             'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
             AppleWebKit/537.36 (KHTML, like Gecko) \
             Chrome/81.0.4044.122 Safari/537.36'}
    url = "https://search.51job.com/list/000000,000000,0000,00,9,99,\
            Python%2B%25E5%25BC%2580%25E5%258F%2591,2,{}.html?lang=c&\
                postchannel=0000&workyear=99&cotype=99&degreefrom=99&\
                    jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="
   
    for idx in range(head, end):       
        try:
            model = db.Model()
            page_url = url.format(idx)
            page = requests.get(page_url, headers=header, timeout=10)
            page.raise_for_status()
            soup = BeautifulSoup(page.content, 'lxml')
            # 爬取搜索结果集
            res_list = soup.find('div', id="resultList")
            infos = res_list.find_all('div', class_='el')
            # 第0项是网页表头
            del infos[0]    
            for item in infos:
                # 将信息提出装入数据库
                cmp_name = item.find('span', attrs={'class': 't2'}).string
                loc = item.find('span', attrs={'class': 't3'}).string
                wage = item.find('span', attrs={'class': 't4'}).string
                model.set_info(cmp_name, loc, wage)
        except Exception as e:
            print(e)
        finally:           
            model.close_link()
