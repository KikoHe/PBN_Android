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

international_category = ["New", "Bonus", "Special", "Character", "Flower", "Animal", "Mandala", "Cartoon", "Food", "Popular",
                          "Festival",
                          "Love",
                          "Nature", "Art", "Places", "Quotes", "Fashion", "Others"]

cn_category = ["推荐","精品","古风","人物","萌宠","恋爱","鲜花","文艺","卡通","人气","曼陀罗","美食","美景","节日","其他"]

def checkcategorytab(driver):
    '''检查第一页分类标题是否正常'''
    try:
        assert (isExistTextInElementByxpath(driver,"//android.widget.HorizontalScrollView/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView[contains(@text,'New')]") == True)
        assert (isExistTextInElementByxpath(driver,"//android.widget.HorizontalScrollView/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView[contains(@text,'Bonus')]") == True)
        assert (isExistTextInElementByxpath(driver,"//android.widget.HorizontalScrollView/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView[contains(@text,'Character')]") == True)
        assert (isExistTextInElementByxpath(driver,"//android.widget.HorizontalScrollView/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView[contains(@text,'Special')]") == True)
    except AssertionError as msg:
        print (msg)
        print ("First five category error")
    else:
        print ("First five category pass")

def checkswipecategorytitle(driver):
    '''滑动分类标题'''
    category = ["New","Bonus","Special","Character","Flower","Animal","Mandala","Cartoon","Food","Popular","Festvial","Love","Nature","Art","Places","Quotes","Fashion","Others"]
    label = driver.find_elements_by_xpath(
        "//android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.TextView")
    i = 0
    while True:
        if i < 5 :
            if label[i].text in category:
                print (label[i].text)
                i = i + 1
        elif label[4].text != "Others":
            driver.swipe(950, 700, 54, 700, 1000)
            driver.implicitly_wait(3)
            i = 0
        else:
            break

def checkclickcategory_new(driver,country):
    swipetimes = 1
    if country != "cn":
        for i in international_category:
            clickbytext(driver,
                        "//android.widget.HorizontalScrollView/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView[contains(@text,'{label}')]".format(
                            label=i))
            driver.implicitly_wait(3)
            wait_until_id(driver, "recyclerView", 3)
            if i == "Bonus":
                checkBonus(driver)
            else:
                checklibrarylist(driver,swipetimes)
            print('click to category:  ' + i)
    else:
        for i in cn_category:
            clickbytext(driver,
                        "//android.widget.HorizontalScrollView/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView[contains(@text,'{label}')]".format(
                            label=i))
            driver.implicitly_wait(3)
            wait_until_id(driver, "recyclerView", 3)
            checklibrarylist(driver,swipetimes)
            print('click to category:  ' + i)

def checkclickcategory(driver):
    '''从左到右点击分类标题'''

    category = ["New", "Special","Character", "Flower", "Animal", "Mandala", "Cartoon", "Food", "Popular", "Festival", "Love",
                "Nature", "Art", "Places", "Quotes", "Fashion", "Others"]
    i = 0
    while i <= len(category) - 1:
        clickbytext(driver,
                    "//android.widget.HorizontalScrollView/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView[contains(@text,'{label}')]".format(
                        label=category[i]))
        driver.implicitly_wait(3)
        wait_until_id(driver,"recyclerView",3)
        checklibrarylist(driver,3)
        driver.implicitly_wait(3)
        m = 0
        while (get_ele_attribute(driver,"//android.widget.HorizontalScrollView/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView[contains(@text,'{label}')]".format(label=category[i]),"selected") != "true"):
            driver.implicitly_wait(3)
            clickbytext(driver,"//android.widget.HorizontalScrollView/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView[contains(@text,'{label}')]".format(label=category[i]))
            m = m + 1
            if m > 3:
                break
                print ("click" + category[i] + "fail")
        print ('click to category:  ' + category[i])
        i = i + 1

def go_to_category(driver,categoryname):
    '''
    进入对应的分类
    :param driver:
    :param categoryname:
    :return:
    '''
    category = ["New","Bonus", "Special","Character", "Flower", "Animal", "Mandala", "Cartoon", "Food", "Popular", "Festival", "Love",
                "Nature", "Art", "Places", "Quotes", "Fashion", "Others"]
    i = 0
    while (get_ele_attribute(driver,
                             "//android.widget.HorizontalScrollView/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView[contains(@text,'{label}')]".format(
                                     label=category[i]), "selected") == "true"):
        driver.implicitly_wait(3)
        i = i+1
        clickbytext(driver,
                    "//android.widget.HorizontalScrollView/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView[contains(@text,'{label}')]".format(
                        label=category[i]))
        if category[i] == categoryname:
            break
    print('click to category:  ' + categoryname)

def checkswipeleftcategorylist(driver):
    '''从右到左滑动分类页面'''
    category = ["Others","Fashion","Quotes","Places","Art","Nature","Love","Festival","Popular","Food","Cartoon","Mandala","Animal","Flower","Character","Bonus","New"]
    i = 0
    while i <= len(category) - 1:

        driver.implicitly_wait(5)

        while not (isExistElementsByID(driver,"rootLayout") and isExistElementsByID(driver,"imageView")):
            time.sleep(3)

        m = 0
        while (get_ele_attribute(driver,"//android.widget.HorizontalScrollView/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView[contains(@text,'{label}')]".format(
                        label=category[i]),"selected")) != "true":
            driver.implicitly_wait(3)
            driver.find_element_by_xpath("//android.widget.HorizontalScrollView/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView[contains(@text,'{label}')]".format(
                        label=category[i])).click()
            m = m + 1
            if m > 3:
                break
                print ("swipe" + category[i] + "fail")

        driver.implicitly_wait(3)

        print ("swipe back to category:  " + category[i])

        driver.swipe(60,1300,1020,1300,3000)

        i = i + 1

def checkswiperightcategorylist(driver):
    '''从左到右滑动分类页面'''

    category = ["New", "Bonus", "Special","Character", "Flower", "Animal", "Mandala", "Cartoon", "Food", "Popular", "Festival", "Love",
                "Nature", "Art", "Places", "Quotes", "Fashion", "Others"]
    i = 0
    while i <= len(category) - 1:
        driver.implicitly_wait(3)
        while not (isExistElementsByID(driver,"rootLayout") and isExistElementsByID(driver,"imageView")):
            time.sleep(3)
        m = 0
        while (get_ele_attribute(driver,"//android.widget.HorizontalScrollView/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView[contains(@text,'{label}')]".format(
                        label=category[i]),"selected")) != "true":
            driver.implicitly_wait(3)
            driver.find_element_by_xpath("//android.widget.HorizontalScrollView/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView[contains(@text,'{label}')]".format(
                        label=category[i])).click()
            m = m + 1
            if m > 3:
                break
                print ("swipe category error")
        driver.implicitly_wait(3)
        print ("swipe to category:  "  + category[i])
        driver.swipe(1020,1300,60,1300,2000)
        i = i + 1

def checkBonus(driver):
    '''检查bonus页面为空'''
    try:
        assert  (isExistElementByID(driver, "paint.by.number.pixel.art.coloring.drawing.puzzle:id/emptyFrame") ==True),"1"
        assert (isExistTextInElementByxpath(driver,"//android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView[contains(@text, 'Join our Facebook community for exclusive images!')]") == True),"3"
        assert  (isExistElementByID(driver, "paint.by.number.pixel.art.coloring.drawing.puzzle:id/tv_get_now") ==True),"4"
        assert  (isExistTextInElementByID(driver, "paint.by.number.pixel.art.coloring.drawing.puzzle:id/tv_get_now","Join us") ==True),"5"
    except AssertionError as msg:
        print (msg)
        print ("bonus view error")
        driver.get_screenshot_as_file("/Users/apple/Desktop/pbn_autotest_android_pyton3/screenshot/bonus.png")
    else:
        print ("bonus view pass")

def checkcategorylist(driver):
    '''？'''
    clickbytext(driver,"//android.widget.HorizontalScrollView/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView[contains(@text.Bonus)]")


def check_pic_testcase(driver):
    '''判断当前素材方案中第1个素材是否是彩绘素材，如果是，重启应用拉取方案'''

    ele_ivFlag = driver.find_elements_by_id("paint.by.number.pixel.art.coloring.drawing.puzzle:id/ivFlag")

    # print ele_ivFlag[0].location['x']

    while ele_ivFlag[0].location['x']  != 399.0:

        print ("First is Colored PIC")

        driver.quit()

        before_test(driver)

        driver.implicitly_wait(3)

        driver.launch_app()

    print ("First is normal PIC")

