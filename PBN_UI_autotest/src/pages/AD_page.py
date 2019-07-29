#!/usr/bin/env python
# encoding: utf-8

#coding=utf-8

import time, base64, random, sys
from selenium import webdriver
from appium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from src.common.Base_unit import *
from src.common.gesture_mainpulation import *
from src.pages.Library_page import *
from src.pages.CN_page import *
from src.pages.Drawing_page import *


def Close_AD(driver):
    '''关闭全屏广告'''
    if isExistElementByClass(driver,"android.widget.ImageButton"):
        driver.find_element_by_class_name("android.widget.ImageButton").click()
    else:
        driver.press_keycode(4)

def AD_Check(driver):
    '''
    检查并关闭差评广告
    :param driver:
    :return:
    '''
    i = 1
    while not isExistElementByClass(driver,"android.webkit.WebView"):
        time.sleep(3)
        i = i + 1
        if i > 15:
            break
            print ("AD error")
    if isExistElementByClass(driver,"android.webkit.WebView"):
        print ("AD pass")
    driver.implicitly_wait(3)
    Close_AD(driver)

def Banner_AD_Check(driver):
    '''检查是否有BANNER广告'''
    if isExistElementByID(driver,"btnMoreHint"):
        clickbyid(driver,"btnMoreHint")
        driver.implicitly_wait(3)
        clickbyid(driver,"ivBack")
        if isExistElementByID(driver,"bannerContainer") or isExistElementByID(driver,"adBanner") or isExistElementByID(driver,"large_bannerContainer"):
            print ("Banner AD PASS")
        else:
            print ("Banner AD error")
    else:
        if isExistElementByID(driver,"bannerContainer") or isExistElementByID(driver,"adBanner") or isExistElementByID(driver,"large_bannerContainer"):
            print ("Banner AD PASS")
        else:
            print ("Banner AD error")

def Get_New_Banner_AD(driver,i):
    '''进入New分类的素材，重复拉取bannerg广告'''
    while not (isExistElementByID(driver, "bannerContainer") or isExistElementByID(driver,"adBanner") or isExistElementByID(driver,"large_bannerContainer")):
        print ("No banner AD")
        relaunch(driver)
        driver.implicitly_wait(3)
        click_list_pic_number(driver,i)
        driver.implicitly_wait(3)
    Banner_AD_Check(driver)

def Drawing_Reward_AD(driver,i):
    '''触发Reward 广告'''
    try:
        assert (isExistElementByID(driver,"tv_num") == True)
    except AssertionError:
        driver.get_screenshot_as_file("/Users/apple/Desktop/pbn_autotest_android_pyton3/screenshot/tv_num.png")
    else:
        hint_num = driver.find_element_by_id("tv_num")
        while hint_num.text != "AD":
            driver.implicitly_wait(3)
            if hint_num.text == "0":
                print ("None Reward AD!")
                relaunch(driver)
                driver.implicitly_wait(3)
                click_list_pic_number(driver,i)
                driver.implicitly_wait(3)
            else:
                clickbyid(driver,"tipsView")
                driver.implicitly_wait(3)
        time.sleep(3)
        driver.find_element_by_id("tipsView").click()
        driver.implicitly_wait(3)
        if isExistElementByID(driver,"tv_btn"):
            clickbyid(driver,"tv_btn")
        driver.implicitly_wait(3)
        AD_Check(driver)
        Close_AD(driver)
        driver.implicitly_wait(3)

def Free_hint_Check(driver):
    '''free hint 弹窗检查'''
    try:
        assert (isExistElementByID(driver,"paint.by.number.pixel.art.coloring.drawing.puzzle:id/cv_root") == True)
        assert (isExistTextInElementByxpath(driver,"//android.widget.FrameLayout/android.widget.TextView[contains(@text,'Free Hint')]") == True)
        assert (isExistElementByID(driver,"paint.by.number.pixel.art.coloring.drawing.puzzle:id/iv_close") == True)
        assert (isExistTextInElementByxpath(driver,
                                            "//android.widget.FrameLayout/android.widget.TextView[contains(@text,'Watch a video to get hint?')]") == True)
        assert (isExistTextInElementByxpath(driver,
                                            "//android.widget.FrameLayout/android.widget.ImageView") == True)
        assert (isExistElementByID(driver,"paint.by.number.pixel.art.coloring.drawing.puzzle:id/card_btn") == True)
        assert (isExistTextInElementByxpath(driver,
                                            "//android.widget.FrameLayout/android.widget.TextView[contains(@text,'Watch')]") == True)
    except AssertionError as msg:
        print (msg)
        print ("free hint box error")
