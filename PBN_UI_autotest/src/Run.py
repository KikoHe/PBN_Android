#! /usr/bin/env python
#coding=utf-8
__author__ = 'kiko'
'''
description:循环执行测试脚本
'''

import time,os
import config.globalparameter as gl

def recycle_excute(cmd,inc):
    while True:
       os.system(cmd)
       time.sleep(inc)

recycle_excute("/usr/local/bin/python3.7 /Users/apple/Desktop/pbn_autotest_android_pyton3/src/runtest.py", 1800)
