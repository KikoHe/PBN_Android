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


def checknewsstaticUI(driver):
    try:
        assert (isExistElementByID(driver,"paint.by.number.pixel.art.coloring.drawing.puzzle:id/titleContainer") == True)
        assert (isExistElementsByID(driver,"paint.by.number.pixel.art.coloring.drawing.puzzle:id/tv_title") == True)

        assert (isExistElementByID(driver,"paint.by.number.pixel.art.coloring.drawing.puzzle:id/recyclerView") == True)
        assert (isExistElementsByID(driver,"paint.by.number.pixel.art.coloring.drawing.puzzle:id/cardView") == True)
        assert (isExistElementsByID(driver,"paint.by.number.pixel.art.coloring.drawing.puzzle:id/ivImage") == True)
        assert (isExistElementsByID(driver,"paint.by.number.pixel.art.coloring.drawing.puzzle:id/tv_title") == True)
        assert (isExistElementsByID(driver,"paint.by.number.pixel.art.coloring.drawing.puzzle:id/tv_des") == True)
        assert (isExistElementsByID(driver,"paint.by.number.pixel.art.coloring.drawing.puzzle:id/tv_get_now") == True)
    except AssertionError,msg:
        print msg
        print "news view error"
    else:
        print "news view pass"