#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding=utf-8
__author__='kiko'

'''description:测试前准备'''

import time, base64, unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from src.common.Base_unit import *
from src.common.gesture_mainpulation import *

def before_test(driver):

    Debug_Set_GroupID(driver, 1)

    Close_Newwork_Error(driver)

    closewelcomeview(driver)

    closedrawview(driver)



def closewelcomeview(driver):
    '''关闭启动时的免责声明页面'''

    if isExistElementByID(driver,"paint.by.number.pixel.art.coloring.drawing.puzzle:id/cv_accept") == True:

        checkwelcomeview(driver)

        driver.implicitly_wait(2)

        clickbyid(driver,"paint.by.number.pixel.art.coloring.drawing.puzzle:id/cv_accept")

        driver.implicitly_wait(2)

        print "Skip Privacy Policy and Terms View"



def checkwelcomeview(driver):
    '''检查免责声明页面'''

    try:
        assert (isExistElementByID(driver,"paint.by.number.pixel.art.coloring.drawing.puzzle:id/action_bar_root") == True)
        assert (isExistElementByID(driver,"android:id/content") == True)

        assert (isExistElementByID(driver,"paint.by.number.pixel.art.coloring.drawing.puzzle:id/cv_accept") == True)
        # assert (isExistElementByClass(driver,"//android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ImageView") == True)


        assert (isExistTextInElementsByxpath(driver, "//android.widget.ScrollView/android.widget.LinearLayout/android.widget.TextView",0,"Please accept our Privacy Policy and Terms of Use to proceed.") == True)
        assert (isExistTextInElementsByxpath(driver, "//android.widget.ScrollView/android.widget.LinearLayout/android.widget.TextView",1,"Note that using the app you grant us the right to process your personal data as described in Privacy Policy including providing them to our partners to show interest-based ad. By accepting you are confirming that you are over the age of ten.") == True)
        assert (isExistTextInElementsByxpath(driver, "//android.widget.ScrollView/android.widget.LinearLayout/android.widget.TextView",2,"You can opt-out of interest-based ad as described in Privacy Policy.") == True)
        assert (isExistTextInElementsByxpath(driver, "//android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.TextView",0,"Accept") == True)

    except AssertionError,msg:

        print msg
        print "Privacy Policy and Terms View Error"



def closedrawview(driver):
    '''关闭新手引导'''

    if isExistElementByID(driver, "paint.by.number.pixel.art.coloring.drawing.puzzle:id/fillColorImageView"):

        driver.find_element_by_id("paint.by.number.pixel.art.coloring.drawing.puzzle:id/btnExit").click()

        driver.implicitly_wait(2)

        print "Close Coloring View"