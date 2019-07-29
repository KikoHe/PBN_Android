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

def checkbanner(driver):
    '''检查Library页的banner'''

    if isExistTextInElementByID(driver, "paint.by.number.pixel.art.coloring.drawing.puzzle:id/view_text",
                                "Daily Update") == True:
        checkdailybanner(driver)
        driver.swipe(1000, 300, 100, 300, 3000)
        checkfbbanner(driver)
    else:
        checkfbbanner(driver)
        driver.swipe(1000, 300, 100, 300, 3000)
        checkdailybanner(driver)

def checkfbbanner(driver):
    '''FB banner'''
    try:
        assert  (isExistElementByID(driver,"paint.by.number.pixel.art.coloring.drawing.puzzle:id/bannerViewPager")==True),"bannerViewPager error"
        assert  (isExistElementByID(driver,"paint.by.number.pixel.art.coloring.drawing.puzzle:id/root")==True),"root error"
        assert  (isExistElementByID(driver, "paint.by.number.pixel.art.coloring.drawing.puzzle:id/container_cv") ==True),"container_cv error"
        assert  (isExistElementByID(driver, "paint.by.number.pixel.art.coloring.drawing.puzzle:id/circleIndicator") ==True),"circleIndicator error"
        assert  (isExistTextInElementByID(driver, "paint.by.number.pixel.art.coloring.drawing.puzzle:id/view_text", "Exclusive images") ==True),"Exclusive images error"
        assert  (isExistTextInElementByID(driver, "paint.by.number.pixel.art.coloring.drawing.puzzle:id/view_sub_text", "Only on our Facebook page") ==True),"Only on our Facebook page error"
        assert  (isExistTextInElementByID(driver, "paint.by.number.pixel.art.coloring.drawing.puzzle:id/view_btn", "Open") ==True),"Open error"
    except AssertionError as msg:
        print (msg)
        print ("fb banner error")
    else:
        print ("fb banner pass")

def checkdailybanner(driver):
    '''daily banner'''
    try:
        assert  (isExistElementByID(driver,"paint.by.number.pixel.art.coloring.drawing.puzzle:id/bannerViewPager")==True),"bannerViewPager error"
        assert  (isExistElementByID(driver,"paint.by.number.pixel.art.coloring.drawing.puzzle:id/root")==True),"root error"

        assert  (isExistTextInElementByID(driver, "paint.by.number.pixel.art.coloring.drawing.puzzle:id/view_text", "Daily Gift") ==True),"Daily Gift error"
        assert  (isExistTextInElementByID(driver, "paint.by.number.pixel.art.coloring.drawing.puzzle:id/view_sub_text", "Open your DAILY GIFT picture now!") ==True),"Open your DAILY GIFT picture now! error"
        assert  (isExistElementByID(driver, "paint.by.number.pixel.art.coloring.drawing.puzzle:id/container_cv") ==True),"container_cv error"
        assert  (isExistElementByID(driver, "paint.by.number.pixel.art.coloring.drawing.puzzle:id/view_image") ==True),"view_image error"

        assert  (isExistElementByID(driver, "paint.by.number.pixel.art.coloring.drawing.puzzle:id/circleIndicator") ==True),"circleIndicator error"
    except AssertionError as msg:
        print (msg)
        print ("daily banner error")
    else:
        print ("daily banner pass")

def checkcategoryselected(driver):
    ''''category选中状态'''
    try:
        assert (get_ele_attribute(driver,"//android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.TextView[contains(@text,'New')]","selected") == "true"),"new 分类选中异常"
        assert (get_ele_attribute(driver,"//android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.TextView[contains(@text,'Bonus')]","selected") == "false"),"Bonus 分类未选中异常"
        clickbytext(driver,"//android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.TextView[contains(@text,'Bonus')]")
        driver.implicitly_wait(2)
        assert (get_ele_attribute(driver,"//android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.TextView[contains(@text,'New')]","selected") == "false"),"new 分类未选中异常"
        assert (get_ele_attribute(driver,"//android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.TextView[contains(@text,'Bonus')]","selected") == "true"), "Bonus 分类选中异常"
    except AssertionError as msg:
        print (msg)
        print ("category selected error")
    else:
        print ("category selected ok")

def checklibrarylist(driver,m):
    '''列表图片'''
    try:
        i = 0
        while i<m:
            assert  (isExistElementByID(driver, "paint.by.number.pixel.art.coloring.drawing.puzzle:id/recyclerView") ==True),"1"
            assert  (isExistElementsByID(driver, "paint.by.number.pixel.art.coloring.drawing.puzzle:id/rootLayout") ==True),"2"
            swipe_down(driver)
            driver.implicitly_wait(2)
            i = i+1
    except AssertionError as msg:
        print (msg)
    else:
        print ("library list pass")

def checktab(driver):
    '''tab'''
    try:
        assert  (isExistElementByID(driver, "paint.by.number.pixel.art.coloring.drawing.puzzle:id/tabLayout") ==True)
        assert  (isExistElementByID(driver, "paint.by.number.pixel.art.coloring.drawing.puzzle:id/bottom_content") ==True)
        assert  (isExistElementByID(driver, "paint.by.number.pixel.art.coloring.drawing.puzzle:id/item_0") ==True)
        assert  (isExistElementByID(driver, "paint.by.number.pixel.art.coloring.drawing.puzzle:id/item_1") ==True)
        assert  (isExistElementByID(driver, "paint.by.number.pixel.art.coloring.drawing.puzzle:id/item_2") ==True)
        assert  (isExistElementByID(driver, "paint.by.number.pixel.art.coloring.drawing.puzzle:id/item_3") ==True)
        assert  (isExistElementByID(driver, "paint.by.number.pixel.art.coloring.drawing.puzzle:id/image_checked_bg") ==True)
        assert  (isExistElementByID(driver, "paint.by.number.pixel.art.coloring.drawing.puzzle:id/view_bg") ==True)
        assert  (isExistElementsByID(driver, "paint.by.number.pixel.art.coloring.drawing.puzzle:id/real_icon") ==True)
        assert  (isExistTextInElementsByid(driver, "paint.by.number.pixel.art.coloring.drawing.puzzle:id/tv_title",0,"Library")==True)
        assert  (isExistTextInElementsByid(driver, "paint.by.number.pixel.art.coloring.drawing.puzzle:id/tv_title",1,"Daily")==True)
        assert  (isExistTextInElementsByid(driver, "paint.by.number.pixel.art.coloring.drawing.puzzle:id/tv_title",2,"News")==True)
        assert  (isExistTextInElementsByid(driver, "paint.by.number.pixel.art.coloring.drawing.puzzle:id/tv_title",3,"My Works")==True)
    except AssertionError as msg:
        print (msg)
        print ("tab display error")
    else:
        print ("tab display pass")

