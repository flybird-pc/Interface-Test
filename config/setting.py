#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:Yafei.ding
# @Time:2020/10/14 17:18

import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

# 配置文件
TEST_CONFIG =  os.path.join(BASE_DIR,"database","config.ini")

# 测试用例模板文件
# SOURCE_FILE = os.path.join(BASE_DIR,"database","InterFaceAPITestCase.xlsx")
SOURCE_FILE = os.path.join(BASE_DIR,"database","AI_InterFaceAPITestCase.xlsx")

# excel测试用例结果文件
# TARGET_FILE = os.path.join(BASE_DIR,"report","excelReport","InterFaceAPITestCase.xlsx")
TARGET_FILE = os.path.join(BASE_DIR,"report","excelReport","AI_InterFaceAPITestCase_result.xlsx")

# 测试用例报告
TEST_REPORT = os.path.join(BASE_DIR,"report")

# 测试用例程序文件
TEST_CASE = os.path.join(BASE_DIR,"testcase")

