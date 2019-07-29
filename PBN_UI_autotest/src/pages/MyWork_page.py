#!/usr/bin/env python
# encoding: utf-8

#coding=utf-8

import time, base64, random
from selenium import webdriver
from appium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from src.common.Base_unit import *
from src.common.gesture_mainpulation import *
from src.pages.Library_page import *

def CheckMywWorkNoPic(driver):
    '''
    mywork页没有图片
    :param driver:
    :return:
    '''
    try:
        assert (isExistElementByID(driver,"rv_mywork") == True),"rv_mywork error"
        assert (isExistElementByID(driver,"l_empty") == True),"l_empty error"
        # assert (isExistElementByClass(driver,"//android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView",
        #                               "You have no works yet,go to color your paintings !") == True)
    except AssertionError as msg:
        print (msg)
        print ("My work without pic display error")
    print ("My work without pic display pass")

def CheckMyWorkNoLoginTitle(driver):
    '''
    CheckMyWorkNoLoginTitle
    :param driver:
    :return:
    '''
    try:
        assert (isExistElementByID(driver,"coord_layout") == True),"coord_layout error"
        assert (isExistElementByID(driver,"iv_header_bg") == True),"iv_header_bg error"
        assert (isExistElementByID(driver,"iv_header") == True),"iv_header error"
        assert (isExistTextInElementByID(driver,"login_hint","Log in to sync data") == True),"Log in error"
        assert (isExistTextInElementByID(driver,"tv_sync_tip","Sync your data on any device.") == True),"Sync your data on any device. error"

        assert (isExistElementByID(driver,"btn_badge") == True),"btn_badge error"

        assert (isExistElementByID(driver,"iv_bg_title") == True),"iv_bg_title error"
        assert (isExistElementByID(driver,"iv_setting") == True),"iv_setting error"
    except AssertionError as msg:
        print (msg)
        print ("MyWork title log out display error")
    else:
        print ("MyWork title log out display pass")

def CheckMyWorkLoginTitle(driver):
    try:
        assert (isExistElementByID(driver,"coord_layout") == True),"coord_layout error"
        assert (isExistElementByID(driver,"iv_header_bg") == True),"iv_header_bg error"
        assert (isExistElementByID(driver,"iv_header") == True),"iv_header error"
        assert (isExistElementByID(driver,"tv_name") == True),"tv_name error"
        assert (isExistElementByID(driver,"tv_sync_tip") == True),"tv_sync_tip error"

        assert (isExistElementByID(driver,"btn_badge") == True),"btn_badge error"

        assert (isExistElementByID(driver,"iv_bg_title") == True),"iv_bg_title error"
        assert (isExistElementByID(driver,"iv_setting") == True),"iv_setting error"
    except AssertionError as msg:
        print (msg)
        print ("MyWork title login display error")
    else:
        print ("MyWork title login display pass")

def CheckMyWorkDonePic(driver):
    try:
        assert (isExistElementsByID(driver,"cardView")),"cardView error"
        assert (isExistElementsByID(driver,"img_frame")),"img_frame error"
        assert (isExistElementsByID(driver,"ivImage")),"ivImage error"
    except AssertionError as msg:
        print (msg)
        print ("Done pic in mywork display error")
    else:
        print ("Done pic in mywork display pass")

def CheckLoginScreen(driver):
    try:
        assert (isExistElementByID(driver,"action_bar_root") == True),"action_bar_root error"
        assert (isExistElementByID(driver,"fClose") == True),"fClose error"
        assert (isExistElementByID(driver,"cvFb") == True),"cvFb error"
        assert (isExistElementByID(driver,"cvGoogle") == True),"cvGoogle error"
    except AssertionError as msg:
        print (msg)
        print ("Log in view error")
    else:
        print ("Log in view pass")

def CheckLogout(driver):
    clickbyid(driver,"iv_setting")
    driver.implicitly_wait(3)
    CheckSettingscreen(driver)
    driver.implicitly_wait(3)
    clickbyid(driver,"tvLogout")
    driver.implicitly_wait(3)
    clickbyid(driver,"android:id/button1")
    if not isExistElementByID(driver,"tvLogout"):
        print ("Log out success!")
    else:
        print ("Log out fail!")

def CheckSettingscreen(driver):
    try:
        assert (isExistElementByID(driver,"btnBack") == True)
        assert (isExistElementByID(driver,"itemHidden") == True)
        assert (isExistElementByID(driver,"itemVibrate") == True)
        assert (isExistElementByID(driver,"itemSounds") == True)
        assert (isExistElementByID(driver,"itemRateUs") == True)
        assert (isExistElementByID(driver,"itemFeedBack") == True)
        assert (isExistElementByID(driver,"itemPolicy") == True)
        assert (isExistElementByID(driver,"itemTermsOfUse") == True)
    except AssertionError as msg:
        print (msg)
        print ("Settings view error")
    else:
        print ("settings view pass")

def CheckAchievement(driver):
    try:
        assert (isExistElementByID(driver,"action_bar_root") == True),"action_bar_root error"
        assert (isExistElementByID(driver,"ivBack") == True),"ivBack error"
        assert (isExistTextInElementByID(driver,"title","Hall Of Badges") == True),"Hall Of Badges error"
        assert (isExistTextInElementByID(driver,"des","Complete missions to earn your badges & bonus hints!") == True),"Complete missions to earn your badges & bonus hints! error"

        assert (isExistElementByID(driver,"recycle") == True),"recycle error"
        assert (isExistElementsByID(driver,"rootLayout") == True),"rootLayout error"
        assert (isExistElementsByID(driver,"imageView") == True),"imageView error"
        assert (isExistElementsByID(driver,"tv_level") == True),"tv_level error"
        assert (isExistElementsByID(driver,"des") == True),"des error"
        assert (isExistElementsByID(driver,"process") == True),"process error"
        assert (isExistElementsByID(driver,"progressBar") == True),"progressBar error"
        assert (isExistElementsByID(driver,"tipsViewContain") == True),"tipsViewContain error"
        assert (isExistElementsByID(driver,"tipsView") == True),"tipsView error"
        assert (isExistElementsByID(driver,"hintContain") == True),"hintContain error"
        assert (isExistElementsByID(driver,"hint") == True),"hint error"
        assert (isExistElementsByID(driver,"periods") == True),"periods error"
    except AssertionError as msg:
        print (msg)
        print ("Achievement view error")
    else:
        print ("Achievement view pass")

def ClickHintReward(driver):
    ele = driver.find_elements_by_id("tipsViewContain")
    number = len(ele)
    while number >= 0:
        driver.find_elements_by_id("tipsViewContain")[number-1].click()
        time.sleep(3)
        number = number - 1
