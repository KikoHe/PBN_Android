# -*- coding:utf-8 -*-

import os, time, unittest

from selenium import webdriver
from appium import webdriver
from src.common.Base_unit import *
from src.pages.Library_page import *
from src.pages.Catagory_page import *
from src.common.gesture_mainpulation import *
# from src.common.before_APPtest import *
from selenium.webdriver.support import expected_conditions as EC

desired_caps = {}
desired_caps['platformName'] = 'Android'  # 设备系统
desired_caps['platformVersion'] = '8.0.0'  # 设备系统版本
desired_caps['deviceName'] = '3836414438313098'  # 设备名称
desired_caps['appPackage'] = 'paint.by.number.pixel.art.coloring.drawing.puzzle'
desired_caps['appActivity'] = 'com.meevii.business.splash.SplashActivity'
desired_caps['noReset'] = True  #重置应用，清楚数据
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

time.sleep(5)

while True:
    ele_ivflag = driver.find_elements_by_id("ivFlag")
    if int(ele_ivflag[0].size['width']) == 117:
        print("Not sort test..")
    elif int(ele_ivflag[0].size['width']) == 177:
        print("Sort test..")
    elif int(ele_ivflag[0].size['width']) == 90:
        print("test..")
    relaunch(driver)



# def test(driver,latter):
#     ele = poco("Canvas").offspring("Bottom").offspring(latter).offspring("Letter")
#     return ele
#
#
# lb_a = test(driver,"LetterBlock_A")
# lb_b = test(driver,"LetterBlock_b")
