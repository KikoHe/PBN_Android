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


def Check_CN_Lib_Banner(driver):

    try:
        assert  (isExistElementByID(driver,"paint.by.number.pixel.art.coloring.drawing.puzzle:id/bannerViewPager")==True),"bannerViewPager error"
        assert  (isExistElementByID(driver,"paint.by.number.pixel.art.coloring.drawing.puzzle:id/root")==True),"root error"
        assert  (isExistElementByID(driver, "paint.by.number.pixel.art.coloring.drawing.puzzle:id/container_cv") ==True),"container_cv error"
        assert  (isExistElementByID(driver, "paint.by.number.pixel.art.coloring.drawing.puzzle:id/circleIndicator") ==True),"circleIndicator error"
        assert  (isExistTextInElementByID(driver, "paint.by.number.pixel.art.coloring.drawing.puzzle:id/view_text", "每日礼物") ==True),"每日礼物 error"
        assert  (isExistTextInElementByID(driver, "paint.by.number.pixel.art.coloring.drawing.puzzle:id/view_sub_text", "现在开启礼物！") ==True),"现在开启礼物！ error"
    except AssertionError,msg:
        print msg
        print "daily banner error"
    else:
        print "daily banner pass"

def checkcncategorytab(driver):
    '''检查第一页分类标题是否正常'''

    try:
        assert (isExistTextInElementByxpath(driver,"//android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.TextView[contains(@text,'推荐')]") == True)
        assert (isExistTextInElementByxpath(driver,"//android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.TextView[contains(@text,'人物')]") == True)
        assert (isExistTextInElementByxpath(driver,"//android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.TextView[contains(@text,'萌宠')]") == True)
        assert (isExistTextInElementByxpath(driver,"//android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.TextView[contains(@text,'卡通')]") == True)
        assert (isExistTextInElementByxpath(driver,"//android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.TextView[contains(@text,'人气')]") == True)
    except AssertionError,msg:
        print msg
        print "First five category error"
    else:
        print "First five category pass"

def checkcntab(driver):
    '''tab'''
    try:
        assert  (isExistElementByID(driver, "paint.by.number.pixel.art.coloring.drawing.puzzle:id/tabLayout") ==True)
        assert  (isExistElementByID(driver, "paint.by.number.pixel.art.coloring.drawing.puzzle:id/bottom_content") ==True)
        assert  (isExistElementByID(driver, "paint.by.number.pixel.art.coloring.drawing.puzzle:id/item_0") ==True)
        assert  (isExistElementByID(driver, "paint.by.number.pixel.art.coloring.drawing.puzzle:id/item_1") ==True)
        assert  (isExistElementByID(driver, "paint.by.number.pixel.art.coloring.drawing.puzzle:id/item_2") ==True)
        assert  (isExistElementByID(driver, "paint.by.number.pixel.art.coloring.drawing.puzzle:id/image_checked_bg") ==True)
        assert  (isExistElementByID(driver, "paint.by.number.pixel.art.coloring.drawing.puzzle:id/view_bg") ==True)
        assert  (isExistElementsByID(driver, "paint.by.number.pixel.art.coloring.drawing.puzzle:id/real_icon") ==True)
        assert  (isExistTextInElementsByid(driver, "paint.by.number.pixel.art.coloring.drawing.puzzle:id/tv_title",0,"图库")==True)
        assert  (isExistTextInElementsByid(driver, "paint.by.number.pixel.art.coloring.drawing.puzzle:id/tv_title",1,"每日更新")==True)
        assert  (isExistTextInElementsByid(driver, "paint.by.number.pixel.art.coloring.drawing.puzzle:id/tv_title",2,"我的作品")==True)
    except AssertionError,msg:
        print msg
        print "tab display error"
    else:
        print "tab display pass"

def CheckCNMyworktitle(driver):


    try:
        assert (isExistElementByID(driver, "titleContainer") == True), "titleContainer error"
        assert (isExistElementByID(driver, "tv_title") == True), "app_bar error"
        assert (isExistTextInElementByID(driver, "tv_title",
                                          "我的作品") == True)
        assert (isExistElementByID(driver, "view_setting") == True), "view_setting error"

    except AssertionError, msg:
        print msg
        print "MyWork title log out display error"

    else:
        print "MyWork title log out display pass"

def CheckMywWorkCNNoPic(driver):

    try:
        assert (isExistElementByID(driver,"emptyImg") == True),"emptyImg error"
        assert (isExistElementByID(driver,"emptyText") == True),"emptyText error"
        assert (isExistTextInElementByID(driver, "emptyText",
                                          "你还没有涂色作品，快去绘制你的艺术品吧！") == True)

    except AssertionError,msg:
        print msg
        print "My work without pic display error"
    print "My work without pic display pass"


def Free_hint_CN_Check(driver):
    '''free hint 弹窗检查'''
    try:
        assert (isExistElementByID(driver,"paint.by.number.pixel.art.coloring.drawing.puzzle:id/cv_root") == True)
        assert (isExistTextInElementByxpath(driver,"//android.widget.FrameLayout/android.widget.TextView[contains(@text,'免费提示')]") == True)
        assert (isExistElementByID(driver,"paint.by.number.pixel.art.coloring.drawing.puzzle:id/iv_close") == True)
        assert (isExistTextInElementByxpath(driver,
                                            "//android.widget.FrameLayout/android.widget.TextView[contains(@text,'观看视频以获取提示？')]") == True)
        assert (isExistTextInElementByxpath(driver,
                                            "//android.widget.FrameLayout/android.widget.ImageView") == True)
        assert (isExistElementByID(driver,"paint.by.number.pixel.art.coloring.drawing.puzzle:id/card_btn") == True)
        assert (isExistTextInElementByxpath(driver,
                                            "//android.widget.FrameLayout/android.widget.TextView[contains(@text,'观看')]") == True)
    except AssertionError,msg:
        print msg
        print "free hint box error"
