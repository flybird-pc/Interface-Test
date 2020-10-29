#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:Yafei.ding
# @Time:2020/10/16 16:50

from mysql_requests_data_assert.requests_data_all import City_Requests
from mysql_requests_data_assert.mysql_data_all import City_Sql

class Assert_equ(City_Sql,City_Requests):
    def assert_mysql_request(self):
        A = City_Sql()
        B = City_Requests()
        list_mysql = A.city_sql()
        list_requests = B.city_requests()
        print(" 数据库中数据：",list_mysql,'\n',"接口返回数据：",list_requests)
        if list_mysql == list_requests:
            print("测试通过，数据准确",'\n')
        else:
            print("测试失败，数据错误!!!数据错误!!!数据错误!!!",'\n')

if __name__ == '__main__':
    a = Assert_equ()
    a.assert_mysql_request()
