#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding=utf-8
__author__='kiko'

'''description:手势操作'''

import time, base64, unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

def swipe_left(driver):
    '''左滑'''
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    driver.swipe(x*9/10,y/2,x/10,y/2)

def swipe_right(driver):
    '''右滑'''
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    driver.swipe(x/4,y/4,x*3/4,y/4)

def swipe_down(driver):
    '''下滑'''
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    driver.swipe(x/2,y*3/4,x/2,y/4)

def swipe_up(driver):
    '''上滑'''
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    driver.swipe(x/2,y/4,x/2,y*3/4)

def my_swipe(driver, offset_x, offset_y, delay):
    """
    offset_x:左右滑动的距离
    offset_y:上下滑动的距离
    delay:滑动时间，毫秒
    """
    driver.swipe(driver.get_window_size()['width'] / 2 + offset_x,
                 driver.get_window_size()['height'] / 2 + offset_y,
                 driver.get_window_size()['width'] / 2 - offset_x,
                 driver.get_window_size()['height'] / 2 - offset_y,
                 delay)

def clickbyid(driver, ele_id):
    """
    :param driver:
    :param ele_id:id元素
    :return:
    """
    driver.find_element_by_id(ele_id).click()

def clickbytext(driver,ele_xpath):
    driver.find_element_by_xpath(ele_xpath).click()