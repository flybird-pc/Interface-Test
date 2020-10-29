#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:Yafei.ding
# @Time:2020/10/16 15:53

import unittest
import requests
#禁用安全请求警告
import urllib3
urllib3.disable_warnings()
import warnings
warnings.simplefilter("ignore",ResourceWarning)

class City_Requests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def city_requests(self):
        par = {
            'Cookie': 'UToken=defaultadmin@TGT-684-9SjwMNd7-tk5iyafXrhYbMtYH7VoZFP43-5W41fkm0W-kl9qUIY8zrpVm7mD5kdtoaAcas-server-76989d47c8-vglk7',
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"
        }
        url_dict = {
                    "城市总览-濮阳概况": "10104003,10104005,10104007,10101009,10101010,10102008,10102013,10102010,10102009",
                    "城市总览-人口分布": "10102001&startTime=1514736000&endTime=1601349303",
                    "城市总览-产业经济": "10101003,10101011,10101012,10101013",
                    "城市总览-社会民生": "10102010,10102009&startTime=1262275200&endTime=1602311792",
                    "城市总览-生态环境": "90504001,90504002,90504003,90504004,90504005,90504006,90504007",
                    "城市总览-城市交通": "10104043,10104044&startTime=1262275200&endTime=1602311792",
                    "城市总览-不动产受理件数统计": "10104047&startTime=1570700472&endTime=1602322872",
                    "城市总览-濮阳市疫情实时数据": "90601007,90601008,90601012,90601011",
                    "城市总览-扶贫成效": "10503001,10503002,10501001",
                    "城市总览-数据采集情况统计": "110100001,110100002,110100003",
                    "城市总览-电力扶贫": "90702001,90702002,90701007",
                    "城市总览-社会信用": "100601001,100601002,100601003,100601004",
                    "数据晾晒-数据采集情况统计": "110100001,110100002,110100003",
                    "数据晾晒-数据目录趋势图": "110100008&startTime=1577808000&endTime=1602728957",
                    "数据晾晒-部门数据目录top10": "110100006,110100007",
                    "数据晾晒-数据集开放类型统计": "110200012",
                    "数据晾晒-数据目录分布统计": "110200004,110200008",
                    "数据晾晒-数据使用统计": "110300001,110300013",
                    "数据晾晒-数据访问历史": "110300014,110300015",
                    "数据晾晒-数据下载部门排名": "110300008",
                    "数据晾晒-数据下载行业占比": "110300016",
                    "数据晾晒-数据目录访问情况": "110300011,110300012",
                    "数据晾晒-数据使用占比": "110300017,110300018",
                    "辅助决策-企业总览趋势图": "100200001,100200002",
                    "辅助决策-常住人口": "10102007,10102012&endTime=1602747029&startTime=1287387029",
                    "辅助决策-总人口构成": "100100004,100100009,100100012",
                    "辅助决策-企业类型占比": "100601001,100601002,100601003,100601004",
                    "辅助决策-失信人员画像": "100300003,100300005",
                    "辅助决策-扶贫人口画像": "10502004,10502002,10502001",
                    "辅助决策-光伏电站分布": "90701003",
                    "辅助决策-贫困原因分布": "10501002",
                    "辅助决策-电力扶贫户数": "90702003",
                    "辅助决策-扶贫措施": "10503003",
                    "辅助决策-历年收益金发放情况": "90703001&endTime=1602754101&startTime=1287394101",
                    }

        # 获取接口返回数据
        req_list = []
        for key in url_dict:
            https_path = url_dict[key]
            try:
                url_https = 'https://data.puyangxian.gov.cn:39090/ioc/card/index/data?indicatorIds='
                r = requests.get(url = url_https + https_path,headers=headers, data=par, verify=False)
                result = r.json()
                list1 = result['data']
                if key == '城市总览-城市交通':
                    for i in range(0, len(list1)):
                        par_value = list1[i]['data'][8]['value']
                        req_list.append(par_value)
                        # print(key, req_list)
                else:
                    for i in range(0,len(list1)):
                        list2 = list1[i]['data']
                        for j in range(0,len(list2)):
                            par_value = list2[j]['value']
                            req_list.append(par_value)
                            # print(key,req_list)
            except:
                print(key,"request is failed")
        print(req_list)
        return req_list

if __name__ == '__main__':
    a = City_Requests()
    a.city_requests()
