#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:Yafei.ding
# @Time:2020/10/16 16:43

import pymysql

class City_Sql:
    def city_sql(self):
        dict1 = {
                "2019年总面积": "select total_area from main_indicators_of_cities where statistics_year = '2019'",
                "耕地面积": "select cultivated_land_area from main_indicators_of_cities where statistics_year = '2019'",
                "同比耕地面积": "select growth_rate_of_cultivated_land_area from main_indicators_of_cities where statistics_year = '2019'",
                "粮食总产量": "select grain_yield from main_indicators_of_cities where statistics_year = '2019'",
                "同比粮食总产量": "select grain_yield_growth from main_indicators_of_cities where statistics_year = '2019'",
                "总人口": "select total_population from main_indicators_of_cities where statistics_year = '2019'",
                "同比总人口": "select total_population_growth from main_indicators_of_cities where statistics_year = '2019'",
                "人均可支配收入": "select per_capita_income from main_indicators_of_cities where statistics_year = '2019'",
                "同比人均收入": "select per_capita_income_growth from main_indicators_of_cities where statistics_year = '2019'",
                "第一人口数": "select resident_population from statistical_table_of_township_main_information WHERE statistics_year = 2018 order by resident_population desc limit 0,1",
                "第二人口数": "select resident_population from statistical_table_of_township_main_information WHERE statistics_year = 2018 order by resident_population desc limit 1,1",
                "第三人口数": "select resident_population from statistical_table_of_township_main_information WHERE statistics_year = 2018 order by resident_population desc limit 2,1",
                "第四人口数": "select resident_population from statistical_table_of_township_main_information WHERE statistics_year = 2018 order by resident_population desc limit 3,1",
                "第五人口数": "select resident_population from statistical_table_of_township_main_information WHERE statistics_year = 2018 order by resident_population desc limit 4,1",
                "生产总值": "select gross_production from main_indicators_of_cities where statistics_year = '2019'",
                "第一产业": "select primary_industry from main_indicators_of_cities where statistics_year = '2019'",
                "第二产业": "select secondary_industry from main_indicators_of_cities where statistics_year = '2019'",
                "第三产业": "select tertiary_industry from main_indicators_of_cities where statistics_year = '2019'",
                "2010人均可支配收入": "select per_capita_income from main_indicators_of_cities where statistics_year = '2010'",
                "2011人均可支配收入": "select per_capita_income from main_indicators_of_cities where statistics_year = '2011'",
                "2012人均可支配收入": "select per_capita_income from main_indicators_of_cities where statistics_year = '2012'",
                "2013人均可支配收入": "select per_capita_income from main_indicators_of_cities where statistics_year = '2013'",
                "2014人均可支配收入": "select per_capita_income from main_indicators_of_cities where statistics_year = '2014'",
                "2015人均可支配收入": "select per_capita_income from main_indicators_of_cities where statistics_year = '2015'",
                "2016人均可支配收入": "select per_capita_income from main_indicators_of_cities where statistics_year = '2016'",
                "2017人均可支配收入": "select per_capita_income from main_indicators_of_cities where statistics_year = '2017'",
                "2018人均可支配收入": "select per_capita_income from main_indicators_of_cities where statistics_year = '2018'",
                "2019人均可支配收入": "select per_capita_income from main_indicators_of_cities where statistics_year = '2019'",
                "PM2.5": "SELECT pm25 FROM air_quality_info WHERE county_name = '濮阳县胡状镇' order by statistics_time desc limit 1,1",
                "SO2": "SELECT so2 FROM air_quality_info WHERE county_name = '濮阳县胡状镇' order by statistics_time desc limit 1,1",
                "PM10": "SELECT pm10 FROM air_quality_info WHERE county_name = '濮阳县胡状镇' order by statistics_time desc limit 1,1",
                "CO": "SELECT co FROM air_quality_info WHERE county_name = '濮阳县胡状镇' order by statistics_time desc limit 1,1",
                "NO2": "SELECT no2 FROM air_quality_info WHERE county_name = '濮阳县胡状镇' order by statistics_time desc limit 1,1",
                "O3": "SELECT o3 FROM air_quality_info WHERE county_name = '濮阳县胡状镇' order by statistics_time desc limit 1,1",
                "AQI": "SELECT aqi FROM air_quality_info WHERE county_name = '濮阳县胡状镇' order by statistics_time desc limit 1,1",
                "年度公交客运总量": "select passenger_num  from  bus_info where statistics_year = 2018",
                "公共车辆总数": "select bus_num from  bus_info where statistics_year = 2018",
                "累计确诊": "select py_cumulative_diagnosis from epidemic_statistics where DATE_FORMAT(now(), '%Y%m%d') = statistics_time",
                "现有确诊": "select py_current_diagnosis from epidemic_statistics where DATE_FORMAT(now(), '%Y%m%d') = statistics_time",
                "治愈人数": "select py_cumulative_cure from epidemic_statistics where DATE_FORMAT(now(), '%Y%m%d') = statistics_time",
                "死亡人数": "select py_cumulative_death from epidemic_statistics where DATE_FORMAT(now(), '%Y%m%d') = statistics_time",
                "贫困人口脱贫比率": "SELECT (count(*) - sum(if(poverty_alleviation_signs IN ('未脱贫', '返贫'), 1, 0))) /count(*) percent FROM poor_info",
                "贫困人口帮扶占比": "SELECT sum(if( helper is not null && helper != ''  ,1,0)) / count(1) percent FROM poor_info",
                "贫困人口总数": "select cast(sum(family_count) AS SIGNED ) AS family_count FROM poor_info where poverty_alleviation_signs  in ('未脱贫','返贫')",
                "部门": "SELECT COUNT(*) count FROM dept_info",
                "数据目录总量": "SELECT count(catalog_name) r_count FROM catalog_info WHERE date_format(now(), '%Y-%m')",
                "数据项总量": "SELECT COUNT(*) num FROM table_property_info",
                "红名单": "select count(enterprise_name) as count from  enterprise_rating WHERE credit_rank = '红榜' and year(effect_time) = year(now())",
                "黑名单": "select count(enterprise_name) as count from  enterprise_rating WHERE credit_rank = '黑榜' and year(effect_time) = year(now())",
                "失信企业": "select count(enterprise_name) as count from  enterprise_rating WHERE credit_rank = '失信' and year(effect_time) = year(now())",
                "其他": "select count(enterprise_name) as count from  enterprise_rating WHERE credit_rank = '其他' and year(effect_time) = year(now())",

            }
        # 打开数据库连接
        conn = pymysql.connect(host='10.20.23.6', port=3306, user='root', passwd='Lcmysql!23', db='index_theme')
        # 使用cursor()方法创建一个游标对象
        cursor = conn.cursor()

        sql_list = []
        for key in dict1:
            sql = dict1[key]
            try:
                cursor.execute(sql)
                sql_result = cursor.fetchall()
                sq = sql_result[0][0]
                sql_list.append(sq)

            except:
                print('Uable to fetch data!')
        print(sql_list)
        return sql_list