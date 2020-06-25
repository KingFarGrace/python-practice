# !/usr/bin/python3
# -*- encoding: utf-8 -*-

import dbutil.database as db
import re


if __name__ == '__main__':
    model = db.Model()
    results = model.find_bj_info()
    sum_wage = 0
    for res in results:
        if res.wage == None:
            continue
        wage_list = re.findall(r"\d+\.?\d*", res.wage)
        wage = 0
        if len(wage_list) == 2:
            wage = (float(wage_list[0])+float(wage_list[1])) / 2
        else:
            wage = float(wage_list[0])
        if re.search("元", res.wage):
            wage /= 10000
        if re.search("千", res.wage):
            wage /= 10
        if re.search("日", res.wage):
            wage *= 30
        if re.search("年", res.wage):
            wage /= 12
        sum_wage += wage
    avg = sum_wage / len(results)
    print("北京地区python开发者平均收入约为：{:.2f} 万/月".format(avg))
    model.close_link()