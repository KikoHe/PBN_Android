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


def Drawing_UI_check(driver):
    try:
        assert (isExistElementByID(driver,"paint.by.number.pixel.art.coloring.drawing.puzzle:id/containerImage") == True),"a"
        assert (isExistElementByID(driver,"paint.by.number.pixel.art.coloring.drawing.puzzle:id/fillColorImageView") == True),"b"

        assert (isExistElementByID(driver,"paint.by.number.pixel.art.coloring.drawing.puzzle:id/btnExit") == True),"c"

        assert (isExistElementByID(driver,"paint.by.number.pixel.art.coloring.drawing.puzzle:id/tipsView") == True),"c1"
        assert (isExistElementByID(driver,"paint.by.number.pixel.art.coloring.drawing.puzzle:id/iv_hints") == True),"c2"
        assert (isExistElementByID(driver,"paint.by.number.pixel.art.coloring.drawing.puzzle:id/card_num") == True),"c3"
        assert (isExistElementByID(driver,"paint.by.number.pixel.art.coloring.drawing.puzzle:id/tv_num") == True),"c4"

        assert (isExistElementByID(driver,"paint.by.number.pixel.art.coloring.drawing.puzzle:id/colorPanel") == True),"c5"
        assert (isExistElementByID(driver,"paint.by.number.pixel.art.coloring.drawing.puzzle:id/colorSelectionView") == True),"c6"
        assert ((isExistElementByID(driver,"bannerContainer") or isExistElementByID(driver,"adBanner") or (isExistElementByID(driver,"large_bannerContainer"))) == True),"banner 广告异常"

    except AssertionError,msg:
        print msg
        print "Drawwing view error"

    else:
        print "Drawwing view pass"

def Drawing_hint_check(driver):
    '''点击hint，检查hint数'''


    while isExistElementByID(driver,"paint.by.number.pixel.art.coloring.drawing.puzzle:id/btnExit"):

        hint_num = driver.find_element_by_id("paint.by.number.pixel.art.coloring.drawing.puzzle:id/tv_num")

        print  "hints number:" + hint_num.text

        if hint_num.text == "AD":

            break
            print hint_num.text

        else:

            clickbyid(driver, "paint.by.number.pixel.art.coloring.drawing.puzzle:id/tipsView")

            time.sleep(2)

    try:

        assert (isExistElementByID(driver, "paint.by.number.pixel.art.coloring.drawing.puzzle:id/btnMoreHint"))

    except AssertionError, msg:

        print msg
        print "hint used error"
    else:
        print "hint used normal"

def Back_default_pic(driver):
    '''点击放大方案：还原素材初始大小、位置'''

    driver.tap([(540, 956)], 1000)

    time.sleep(3)

    if isExistElementByID(driver, "paint.by.number.pixel.art.coloring.drawing.puzzle:id/ivZoomBack"):

        driver.find_element_by_id("paint.by.number.pixel.art.coloring.drawing.puzzle:id/ivZoomBack").click()

        time.sleep(3)

def Drawing_Done_UI_Check(driver):
    '''着色完成页UI检查'''

    try:
        assert (isExistElementByID(driver,"paint.by.number.pixel.art.coloring.drawing.puzzle:id/flParticle") == True),"All screen error"
        assert (isExistElementByID(driver,"paint.by.number.pixel.art.coloring.drawing.puzzle:id/shimmer_view_container") == True),"title bannerer error"
        assert (isExistElementByID(driver,"paint.by.number.pixel.art.coloring.drawing.puzzle:id/ivTitle") == True),"title bannerer error"
        assert (isExistElementByID(driver,"paint.by.number.pixel.art.coloring.drawing.puzzle:id/containerFIV") == True),"containerFIV error"
        assert (isExistElementByID(driver,"paint.by.number.pixel.art.coloring.drawing.puzzle:id/fillColorImageView") == True),"fillColorImageView error"
        assert (isExistElementByID(driver,"paint.by.number.pixel.art.coloring.drawing.puzzle:id/ivRainbow") == True),"ivRainbow error"
        assert (isExistElementByID(driver,"paint.by.number.pixel.art.coloring.drawing.puzzle:id/bottomView") == True),"bottomView error"
        assert (isExistElementByID(driver,"paint.by.number.pixel.art.coloring.drawing.puzzle:id/lTop") == True),"lTop wrror"
        assert (isExistElementByID(driver,"paint.by.number.pixel.art.coloring.drawing.puzzle:id/fDownload") == True),"fDownload error"
        assert (isExistElementByID(driver,"paint.by.number.pixel.art.coloring.drawing.puzzle:id/ivDownload") == True),"ivDownload error"
        assert (isExistElementByID(driver,"paint.by.number.pixel.art.coloring.drawing.puzzle:id/fShare") == True),"fShare error"
        assert (isExistElementByID(driver,"paint.by.number.pixel.art.coloring.drawing.puzzle:id/ivShare") == True),"ivShare error"
        assert (isExistElementByID(driver,"paint.by.number.pixel.art.coloring.drawing.puzzle:id/tvContinue") == True),"tvContinue error"

    except AssertionError,msg:
        print msg
        print "Drawwing Done View error"

    else:
        print "Drawwing Done View pass"

def Write_Review_UI(driver):
    '''评论弹窗'''
    try:
        assert (isExistElementByID(driver, "paint.by.number.pixel.art.coloring.drawing.puzzle:id/cv_root") == True)

        assert (isExistElementByID(driver, "paint.by.number.pixel.art.coloring.drawing.puzzle:id/iv_close") == True)

        assert (isExistElementByID(driver, "paint.by.number.pixel.art.coloring.drawing.puzzle:id/iv_logo") == True)
        assert (isExistElementByID(driver, "paint.by.number.pixel.art.coloring.drawing.puzzle:id/cv_rateus") == True)
        assert (isExistElementByID(driver, "paint.by.number.pixel.art.coloring.drawing.puzzle:id/tv_not_now") == True)

    except AssertionError, msg:
        print msg
        print "Review box error"

    else:
        print "Review box pass"

def Close_Write_Review(driver):
    '''关闭评论弹窗'''

    if isExistElementByID(driver, "paint.by.number.pixel.art.coloring.drawing.puzzle:id/cv_rateus"):

        Write_Review_UI(driver)

        driver.implicitly_wait(5)

        clickbyid(driver, "paint.by.number.pixel.art.coloring.drawing.puzzle:id/tv_not_now")

def Close_Achievement(driver):
    '''关闭弹框'''

    if isExistElementByID(driver, "paint.by.number.pixel.art.coloring.drawing.puzzle:id/card_btn"):

        clickbyid(driver, "paint.by.number.pixel.art.coloring.drawing.puzzle:id/card_btn")

        print "Close box"


def Drawing_pic_flower(driver):
    '''新手引导图flower着色方案'''

    Back_default_pic(driver)

    driver.tap([(140, 656)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(994, 784)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(516, 1365)], 1000)
    print "1"

    time.sleep(2)
    driver.tap([(210, 1080)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(678, 1258)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(837, 1061)], 1000)
    print "2"

    time.sleep(2)
    driver.tap([(257, 805)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(774, 700)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(654, 1073)], 1000)
    print "3"

    time.sleep(2)
    driver.tap([(404, 884)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(436, 985)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(756, 798)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(791, 868)], 1000)
    print "4"

    time.sleep(2)
    driver.tap([(672, 887)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(716, 756)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(664, 714)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(468, 640)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(414, 835)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(371, 685)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(395, 671)], 1000)
    print "5"

    time.sleep(2)
    driver.tap([(559, 838)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(498, 680)], 1000)
    print "6"

    time.sleep(2)
    driver.tap([(596, 749)], 1000)
    print "7"

    time.sleep(2)
    driver.tap([(498, 752)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(562, 755)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(526, 736)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(519, 689)], 1000)
    print "8"

    time.sleep(2)
    driver.tap([(551, 717)], 1000)
    driver.implicitly_wait(3)
    print "9"

    time.sleep(3)

    Drawing_Done_UI_Check(driver)


def Drawing_pic_horse(driver):
    '''新手引导图horse着色方案'''

    Back_default_pic(driver)

    driver.tap([(950, 1265)], 1000)
    print "1"

    driver.implicitly_wait(3)
    driver.tap([(535, 1051)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(371, 1264)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(615, 1204)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(683, 1138)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(168, 807)], 1000)
    print "2"

    time.sleep(2)
    driver.tap([(205, 811)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(374, 766)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(353, 850)], 1000)
    print "3"

    time.sleep(2)
    driver.tap([(281, 681)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(774, 771)], 1000)
    print "4"
    time.sleep(2)
    driver.tap([(490, 497)], 1000)
    driver.implicitly_wait(3)
    print "5"
    time.sleep(2)
    driver.tap([(410, 674)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(355, 781)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(792, 796)], 1000)
    print "6"
    driver.implicitly_wait(3)
    driver.tap([(525, 707)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(813, 846)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(725, 880)], 1000)
    print "7"
    time.sleep(2)
    driver.tap([(545, 747)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(756, 615)], 1000)
    driver.implicitly_wait(3)
    print "8"
    driver.tap([(515, 810)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(596, 710)], 1000)
    driver.implicitly_wait(3)
    print "9"
    driver.tap([(508, 842)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(524, 853)], 1000)
    driver.implicitly_wait(3)
    print "10"
    driver.tap([(574, 853)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(736, 579)], 1000)
    driver.implicitly_wait(3)
    print "10"
    driver.tap([(498, 680)], 1000)
    driver.implicitly_wait(3)
    print "11"
    driver.tap([(696, 543)], 1000)
    driver.implicitly_wait(3)
    print "12"
    driver.tap([(265, 850)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(254, 834)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(240, 815)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(225, 785)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(214, 772)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(197, 756)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(194, 737)], 1000)
    print "13"
    driver.tap([(320, 1397)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(576, 1236)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(674, 1265)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(699, 1180)], 1000)
    driver.implicitly_wait(3)
    print "14"

    time.sleep(3)

    Drawing_Done_UI_Check(driver)


def Drawing_pic_tiger(driver):
    '''tiger着色方案'''

    Back_default_pic(driver)

    driver.tap([(435, 1065)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(655, 1066)], 1000)
    driver.implicitly_wait(3)
    print "1"
    driver.tap([(508, 529)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(574, 539)], 1000)
    driver.implicitly_wait(3)
    print "2"
    driver.tap([(395, 1014)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(670, 1007)], 1000)
    driver.implicitly_wait(3)
    print "3"
    driver.tap([(203, 508)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(430, 600)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(641, 627)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(873, 582)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(273, 1152)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(814, 1161)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(440, 1185)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(641, 1179)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(488, 1215)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(590, 1218)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(535, 1392)], 1000)
    driver.implicitly_wait(3)
    print "4"
    driver.tap([(180, 690)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(900, 692)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(360, 820)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(730, 820)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(218, 1025)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(880, 1025)], 1000)
    driver.implicitly_wait(3)
    print "5"
    driver.tap([(324, 635)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(764, 650)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(476, 778)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(618, 783)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(420, 1265)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(666, 1279)], 1000)
    driver.implicitly_wait(3)
    print "6"
    driver.implicitly_wait(3)
    driver.tap([(396, 887)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(678, 888)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(476, 778)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(520, 1233)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(567, 1234)], 1000)
    driver.implicitly_wait(3)
    print "7"
    driver.implicitly_wait(3)
    driver.tap([(268, 794)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(848, 794)], 1000)
    driver.implicitly_wait(3)
    print "8"
    driver.tap([(935, 1297)], 1000)
    driver.implicitly_wait(3)
    print "9"
    driver.tap([(534, 1077)], 1000)
    driver.implicitly_wait(3)
    print "10"
    driver.tap([(369, 925)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(698, 934)], 1000)
    driver.implicitly_wait(3)
    print "11"
    driver.tap([(268, 916)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(814, 934)], 1000)
    driver.implicitly_wait(3)
    print "12"
    driver.tap([(306, 1031)], 1000)
    driver.implicitly_wait(3)
    driver.tap([(791, 1027)], 1000)
    driver.implicitly_wait(3)
    print "13"

    time.sleep(3)
    Drawing_Done_UI_Check(driver)
