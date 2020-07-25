#!/bin/env python3
# -*- coding : utf-8 -*-

from urllib import request, parse

import re
import json
import time
from bs4 import BeautifulSoup

import requests
import json

import mysql.connector

# for s in values:
#     print('current province = %s' % s[2])

# 1. 获取省份，select框
# 2. 遍历省份下的地市
# 3. 遍历地市下的区信息
province_list = [
    {"children": [], "diji":"", "quHuaDaiMa":"110000",
        "quhao":"", "shengji":"北京市(京)", "xianji":""},
    {"children": [], "diji":"", "quHuaDaiMa":"120000",
     "quhao":"", "shengji":"天津市(津)", "xianji":""},
    {"children": [], "diji":"", "quHuaDaiMa":"130000",
     "quhao":"", "shengji":"河北省(冀)", "xianji":""},
    {"children": [], "diji":"", "quHuaDaiMa":"140000",
     "quhao":"", "shengji":"山西省(晋)", "xianji":""},
    {"children": [], "diji":"", "quHuaDaiMa":"150000",
     "quhao":"", "shengji":"内蒙古自治区(内蒙古)", "xianji":""},
    {"children": [], "diji":"", "quHuaDaiMa":"210000",
     "quhao":"", "shengji":"辽宁省(辽)", "xianji":""},
    {"children": [], "diji":"", "quHuaDaiMa":"220000",
     "quhao":"", "shengji":"吉林省(吉)", "xianji":""},
    {"children": [], "diji":"", "quHuaDaiMa":"230000",
     "quhao":"", "shengji":"黑龙江省(黑)", "xianji":""},
    {"children": [], "diji":"", "quHuaDaiMa":"310000",
     "quhao":"", "shengji":"上海市(沪)", "xianji":""},
    {"children": [], "diji":"", "quHuaDaiMa":"320000",
     "quhao":"", "shengji":"江苏省(苏)", "xianji":""},
    {"children": [], "diji":"", "quHuaDaiMa":"330000",
     "quhao":"", "shengji":"浙江省(浙)", "xianji":""},
    {"children": [], "diji":"", "quHuaDaiMa":"340000",
     "quhao":"", "shengji":"安徽省(皖)", "xianji":""},
    {"children": [], "diji":"", "quHuaDaiMa":"350000",
     "quhao":"", "shengji":"福建省(闽)", "xianji":""},
    {"children": [], "diji":"", "quHuaDaiMa":"360000",
     "quhao":"", "shengji":"江西省(赣)", "xianji":""},
    {"children": [], "diji":"", "quHuaDaiMa":"370000",
     "quhao":"", "shengji":"山东省(鲁)", "xianji":""},
    {"children": [], "diji":"", "quHuaDaiMa":"410000",
     "quhao":"", "shengji":"河南省(豫)", "xianji":""},
    {"children": [], "diji":"", "quHuaDaiMa":"420000",
     "quhao":"", "shengji":"湖北省(鄂)", "xianji":""},
    {"children": [], "diji":"", "quHuaDaiMa":"430000",
     "quhao":"", "shengji":"湖南省(湘)", "xianji":""},
    {"children": [], "diji":"", "quHuaDaiMa":"440000",
     "quhao":"", "shengji":"广东省(粤)", "xianji":""},
    {"children": [], "diji":"", "quHuaDaiMa":"450000",
     "quhao":"", "shengji":"广西壮族自治区(桂)", "xianji":""},
    {"children": [], "diji":"", "quHuaDaiMa":"460000",
     "quhao":"", "shengji":"海南省(琼)", "xianji":""},
    {"children": [], "diji":"", "quHuaDaiMa":"500000",
     "quhao":"", "shengji":"重庆市(渝)", "xianji":""},
    {"children": [], "diji":"", "quHuaDaiMa":"510000",
     "quhao":"", "shengji":"四川省(川、蜀)", "xianji":""},
    {"children": [], "diji":"", "quHuaDaiMa":"520000",
     "quhao":"", "shengji":"贵州省(黔、贵)", "xianji":""},
    {"children": [], "diji":"", "quHuaDaiMa":"530000",
     "quhao":"", "shengji":"云南省(滇、云)", "xianji":""},
    {"children": [], "diji":"", "quHuaDaiMa":"540000",
     "quhao":"", "shengji":"西藏自治区(藏)", "xianji":""},
    {"children": [], "diji":"", "quHuaDaiMa":"610000",
     "quhao":"", "shengji":"陕西省(陕、秦)", "xianji":""},
    {"children": [], "diji":"", "quHuaDaiMa":"620000",
     "quhao":"", "shengji":"甘肃省(甘、陇)", "xianji":""},
    {"children": [], "diji":"", "quHuaDaiMa":"630000",
     "quhao":"", "shengji":"青海省(青)", "xianji":""},
    {"children": [], "diji":"", "quHuaDaiMa":"640000",
     "quhao":"", "shengji":"宁夏回族自治区(宁)", "xianji":""},
    {"children": [], "diji":"", "quHuaDaiMa":"650000",
     "quhao":"", "shengji":"新疆维吾尔自治区(新)", "xianji":""},
    {"children": [], "diji":"", "quHuaDaiMa":"810000",
     "quhao":"0852", "shengji":"香港特别行政区(港)", "xianji":""},
    {"children": [], "diji":"", "quHuaDaiMa":"820000",
     "quhao":"0853", "shengji":"澳门特别行政区(澳)", "xianji":""},
    {"children": [], "diji":"", "quHuaDaiMa":"710000",
     "quhao":"", "shengji":"台湾省(台)", "xianji":""}
]

req = request.Request('http://xzqh.mca.gov.cn/selectJson')
req.add_header('Host', 'xzqh.mca.gov.cn')
req.add_header('Origin', 'http://xzqh.mca.gov.cn')
req.add_header('Referer', 'http://xzqh.mca.gov.cn/map/')
req.add_header(
    'User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36')
req.add_header(
    'Content-type', 'application/x-www-form-urlencoded; charset=UTF-8')


conn = mysql.connector.connect(
    user='root', password='123456', database='openhis')

cursor = conn.cursor()

for province in province_list:
    print('current province = %s' % province['shengji'])
    send_data = parse.urlencode([
        ('shengji', province['shengji'])
    ])
    with request.urlopen(req, data=send_data.encode('utf-8')) as f:
        print('Status:', f.status, f.reason)
        city_str = f.read().decode('utf-8')
        city_list = json.loads(city_str)
        # print(city_list)
        for city in city_list:
            print('current city = %s code = %s' % (city['diji'],city['quHuaDaiMa']))
            send_data = parse.urlencode([
                ('shengji', province['shengji']),
                ('diji', city['diji']),
            ])

            city['diji'] = city['diji'].replace('市', '')
            # print(city)
            sql = 'select * from dzm_area where name like "%s%%" AND `level` = 2' % city['diji']
            cursor.execute(sql)
            values = cursor.fetchall()
            if values:
                print('start update code field...')
                value = values[0]
                with request.urlopen(req, data=send_data.encode('utf-8')) as f:
                    print('Status:', f.status, f.reason)
                    district_str = f.read().decode('utf-8')
                    district_list = json.loads(district_str)
                    for district in district_list:
                        sql = 'select * from dzm_area where name like "%s%%" AND `level` = 3 AND pid = %s' % (district['xianji'],value[0])
                        print(sql)
                        cursor.execute(sql)
                        values = cursor.fetchall()
                        if values:
                            sql = 'update dzm_area set qh_code = %s where id = %s' % (district['quHuaDaiMa'],values[0][0])
                            print(sql)
                            cursor.execute(sql)
                            rowcount = cursor.rowcount
                            if rowcount < 1:
                                print('ERROR ')
                time.sleep(2)

            #     print(value)
            #     sql = 'update dzm_area set qh_code = %s where id = %s' % (city['quHuaDaiMa'],value[0])
            #     print(sql)
            #     cursor.execute(sql)
            #     rowcount = cursor.rowcount
            #     if rowcount < 1:
            #         print('ERROR ')

conn.commit()
cursor.close()
conn.close()
# html = requests.get('http://xzqh.mca.gov.cn/map').text

# print(html)

# quhua = re.findall(r'"quHuaDaiMa":"(.*?)"',html)
# shengji = re.findall(r'"shengji":"(.*?)"',html)

# print(quhua,shengji)
# req = request.Request('http://xzqh.mca.gov.cn/selectJson')
# req.add_header('Host', 'xzqh.mca.gov.cn')
# req.add_header('Origin', 'http://xzqh.mca.gov.cn')
# req.add_header('Referer', 'http://xzqh.mca.gov.cn/map/')
# req.add_header(
#     'User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36')
# req.add_header('Content-type', 'application/x-www-form-urlencoded; charset=UTF-8')
# # req.add_header('Cookie','_gscu_266093035=94798537l7e6io73; JSESSIONID=774E7E10B06EA32D8342A75B43729E01; _gscbrs_266093035=1; _gscs_266093035=956390355spgdh17|pv:5')
# # req.add_header('X-Requested-With','XMLHttpRequest')

# data = parse.urlencode([
#     ('shengji','北京市(京)'),
#     ('diji','北京市')
# ])

# with request.urlopen(req,data=data.encode('utf-8')) as f:
#     print('Status:',f.status,f.reason)
#     for k,v in f.getheaders():
#         print('%s:%s' % (k,v))
#     print('Data',f.read().decode('utf-8'))
