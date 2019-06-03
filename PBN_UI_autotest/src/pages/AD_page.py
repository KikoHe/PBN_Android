#!/usr/bin/env python
# encoding: utf-8

#coding=utf-8

import time, base64, random,sys
from selenium import webdriver
from appium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from src.common.Base_unit import *
from src.common.gesture_mainpulation import *
from src.pages.Library_page import *
from src.pages.CN_page import *
reload(sys)
sys.setdefaultencoding('utf-8')


def Close_AD(driver):
    '''检查是否有全屏广告'''


    if isExistElementByClass(driver,"android.widget.ImageButton"):

        driver.find_element_by_class_name("android.widget.ImageButton").click()

    else:

        driver.press_keycode(4)

# def Reward_AD_Check(driver):
#     '''检查是否有Reward广告'''
#
#     AD_Check(driver)
#
#     if isExistElementByClass(driver,"android.widget.ImageButton"):
#
#         driver.find_element_by_class_name("android.widget.ImageButton").click()
#
#     else:
#
#         driver.press_keycode(4)


def AD_Check(driver):
    ''''''
    i = 1
    while not isExistElementByClass(driver,"android.webkit.WebView"):
        time.sleep(3)
        i = i + 1
        if i > 15:
            break
            print "AD error"

    if isExistElementByClass(driver,"android.webkit.WebView"):
        print "AD pass"

    driver.implicitly_wait(3)
    Close_AD(driver)


def Banner_AD_Check(driver):
    '''检查是否有BANNER广告'''

    if isExistElementByID(driver,"paint.by.number.pixel.art.coloring.drawing.puzzle:id/btnMoreHint"):

        clickbyid(driver,"paint.by.number.pixel.art.coloring.drawing.puzzle:id/btnMoreHint")

        driver.implicitly_wait(3)

        clickbyid(driver,"paint.by.number.pixel.art.coloring.drawing.puzzle:id/ivBack")


        if isExistElementByID(driver,"bannerContainer") or isExistElementByID(driver,"adBanner") or isExistElementByID("large_bannerContainer"):
            print "Banner AD PASS"
        else:
            print "Banner AD error"

    else:

        if isExistElementByID(driver,"bannerContainer") or isExistElementByID(driver,"adBanner") or isExistElementByID("large_bannerContainer"):
            print "Banner AD PASS"
        else:
            print "Banner AD error"






def Get_New_Banner_AD(driver,i):
    '''进入New分类的素材，重复拉取bannerg广告'''

    while not (isExistElementByID(driver, "bannerContainer") or isExistElementByID(driver,"adBanner") or isExistElementByID(driver,"large_bannerContainer")):

        print "No banner AD"

        driver.close_app()

        time.sleep(3)

        driver.launch_app()

        Allow_box(driver)

        time.sleep(5)

        ele = driver.find_elements_by_xpath(
            "//android.support.v4.view.ViewPager/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.FrameLayout")

        ele[i].click()

        time.sleep(3)

    Banner_AD_Check(driver)


def Get_Animal_Banner_AD(driver,i):
    '''进入Animal分类的素材，重复拉取bannerg广告'''

    while not isExistElementByID(driver, "paint.by.number.pixel.art.coloring.drawing.puzzle:id/bannerContainer"):
        print "No banner AD"

        driver.close_app()

        time.sleep(3)

        driver.launch_app()

        time.sleep(5)

        clickbytext(driver,"//android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.TextView[contains(@text,'Flower')]")
        time.sleep(3)
        clickbytext(driver,"//android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.TextView[contains(@text,'Animal')]")
        time.sleep(3)
        swipe_down(driver)
        time.sleep(3)

        ele = driver.find_elements_by_xpath(
            "//android.support.v4.view.ViewPager/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.FrameLayout")

        ele[i].click()

        time.sleep(i)

    Banner_AD_Check(driver)



def Drawing_Reward_AD(driver,i):
    '''触发Reward 广告'''

    hint_num = driver.find_element_by_id("paint.by.number.pixel.art.coloring.drawing.puzzle:id/tv_num")

    while hint_num.text != "AD":

        if hint_num.text == "0":

            print "Get none Reward AD!"

            driver.close_app()

            time.sleep(3)

            driver.launch_app()

            # clickbyid(driver,"paint.by.number.pixel.art.coloring.drawing.puzzle:id/btnExit")

            driver.implicitly_wait(3)

            # ele[0].click()

            ele = driver.find_elements_by_xpath(
                "//android.support.v4.view.ViewPager/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.FrameLayout")

            driver.implicitly_wait(3)

            ele[i].click()

            driver.implicitly_wait(3)

        else:

            clickbyid(driver,"paint.by.number.pixel.art.coloring.drawing.puzzle:id/tipsView")

            print "hints number" + hint_num.text

            driver.implicitly_wait(3)

    time.sleep(3)

    clickbyid(driver,"paint.by.number.pixel.art.coloring.drawing.puzzle:id/iv_hints")

    driver.implicitly_wait(3)
    if driver.find_element_by_xpath("//android.widget.FrameLayout/android.widget.TextView").text == "Free Hint":
        Free_hint_Check(driver)
    elif driver.find_element_by_xpath("//android.widget.FrameLayout/android.widget.TextView").text == "免费提示":
        Free_hint_CN_Check(driver)

    driver.implicitly_wait(3)

    clickbyid(driver,"paint.by.number.pixel.art.coloring.drawing.puzzle:id/card_btn")

    driver.implicitly_wait(3)

    AD_Check(driver)

    driver.implicitly_wait(3)

    # if  isExistElementByID(driver,"count_down"):
    #     print "Admob Reward video 显示正常"
    #     clickbyid(driver,"close_button_icon")
    #     driver.implicitly_wait(3)
    #     if isExistElementByID(driver,"close_video_button"):
    #         clickbyid(driver,"close_video_button")
    #         time.sleep(3)
    #
    # elif isExistElementByClass(driver,"//android.widget.RelativeLayout/android.widget.VideoView") and isExistElementByClass(driver,"//android.widget.RelativeLayout/android.widget.ProgressBar"):
    #     print "vungle Reward video显示正常"
    #     WebDriverWait(driver,5).until(driver.find_element_by_id(""))
    #     driver.sendKeyEvent(4)
    #     driver.pressKeyCode(4)
    #
    # elif driver.find_element_by_xpath("//android.webkit.WebView"):
    #     print "Reward video显示正常"


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
    except AssertionError,msg:
        print msg
        print "free hint box error"
