# -*- coding:utf-8 -*-

import os, time, unittest

from selenium import webdriver
from appium import webdriver
from src.common.Base_unit import *
from src.pages.Library_page import *
from src.pages.Catagory_page import *
from src.common.gesture_mainpulation import *
from src.common.before_test import *
from selenium.webdriver.support import expected_conditions as EC

desired_caps = {}

desired_caps['platformName'] = 'Android'  # 设备系统

desired_caps['platformVersion'] = '8.0.0'  # 设备系统版本

desired_caps['deviceName'] = '3836414438313098'  # 设备名称

desired_caps['appPackage'] = 'paint.by.number.pixel.art.coloring.drawing.puzzle'

desired_caps['appActivity'] = 'com.meevii.business.splash.SplashActivity'

desired_caps['noReset'] = True  #重置应用，清楚数据

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

driver.find_element_by_id("item_3")
driver.implicitly_wait(3)

assert (isExistElementByID(driver,"iv_header") == True)

driver.find_element_by_id("iv_header")
driver.implicitly_wait(3)

driver.find_element_by_id("cvGoogle")
driver.implicitly_wait(3)



if isExistElementByID(driver, "com.google.android.gms:id/account_picker"):
    ele = driver.find_elements_by_id("com.google.android.gms:id/account_display_name")
    name = ele[0].text
    ele[0].click()
    driver.implicitly_wait(30)
    if driver.find_element_by_id("tv_name").text == name:
        print "google account log in success"
        print name
    else:
        print "login fail"
else:
    if isExistTextInElementByID(driver, "tv_sync_tip", "Last sync time: less than 1 day") == True:
        print "login success"
    else:
        print "login fail"





