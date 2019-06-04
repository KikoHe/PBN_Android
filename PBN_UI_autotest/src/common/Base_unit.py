#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding=utf-8
__author__='kiko'

'''description:UI公共类'''

import time, base64, unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from config import globalparameter
from src.common.before_test import *

def isExistElementByID(driver, ele_id):
    """
    :Usage: 使用id判断元素是否存在
    :param driver: Page Object
    :param ele_id: 元素的id属性
    :return: boolean value,若存在则为true，否则为false
    """
    try:
        driver.find_element_by_id(ele_id)
        return True
    except:
        return False


def isExistElementsByID(driver, eles_id):
    '''Usage: 使用id判断元素组是否存在'''
    try:
        driver.find_elements_by_id(eles_id)
        return True
    except:
        return False


def isExistfloatInElementByID(driver, ele_id):
    '''Usage: 通过ID判断该元素存不存在数字'''
    try:
        float(driver.find_element_by_id(ele_id).text)
        return True
    except:
        return False


def isExistfloatInElementsByID(driver, ele_id, id):
    '''Usage: 通过ID判断某元素组中某一个元素存不存在数字'''
    try:
        float(driver.find_elements_by_id(ele_id)[id].text)
        return True
    except:
        return False


def isExistTextInElementByID(driver, ele_id, word):
    '''Usage: 通过ID判断该元素文案是否预期'''
    if  driver.find_element_by_id(ele_id).text == word:
        return True
    else:
        return False

def isExistTextInElementsByxpath(driver, ele_xpath,number,word):
    '''Usage: 通过xpath判断该元素组文案是否预期'''
    if  driver.find_elements_by_xpath(ele_xpath)[number].text == word:
        return True
    else:
        return False


def isExistInElementByxpath(driver, ele_xpath):
    '''Usage: 通过xpath判断该元素文案是否预期'''
    if  driver.find_element_by_xpath(ele_xpath):
        return True
    else:
        return False

def isExistTextInElementByxpath(driver, ele_xpath,word):
    '''Usage: 通过xpath判断该元素文案是否预期'''
    if  driver.find_element_by_xpath(ele_xpath).text == word:
        return True
    else:
        return False

def isExistTextInElementsByid(driver, ele_id,number,word):
    '''Usage: 通过id判断该元素组文案是否预期'''
    if  driver.find_elements_by_id(ele_id)[number].text == word:
        return True
    else:
        return False



def isExistElementByClass(driver, ele_class):
    '''Usage: 通过class判断元素存不存在'''
    try:
        driver.find_element_by_class_name(ele_class)
        return True
    except:
        return False


def isExistElementsByClass(driver, eles_class, i):
    '''Usage: 通过class判断元素组存不存在'''
    try:
        driver.find_elements_by_class_name(eles_class)[i]
        return True
    except:
        return False


def is_element_exist(ele_layout, element):
    """
    :Usage: 将页面上的局部样式（LinerLayout或者RelativeLayout）看作一个object对象，判断目标元素是否
            在布局样式内
    :param ele_layout: object of LinerLayout or RelativeLayout
    :param element:  所检索的目标WebElement
    :return: boolean value, True means that webElement in side，False means outside
    """
    if element.location['x'] < ele_layout.location['x'] + ele_layout.size['width'] \
            and element.location['y'] < ele_layout.location['y'] + ele_layout.size['height']:
        return True
    else:
        return False


def get_eles_attribute(driver,ele_xpath,number,attribute):
    ele = driver.find_elements_by_xpath(ele_xpath)[number].get_attribute(attribute)
    return ele

def get_ele_attribute(driver,ele_xpath,attribute):
    ele = driver.find_element_by_xpath(ele_xpath).get_attribute(attribute)
    return ele


def Debug_Set_GroupID(driver,id):
    '''测试包设置group id'''
    if isExistElementByClass(driver,"android.widget.EditText"):
        print "Test APP"
        driver.find_element_by_class_name("android.widget.EditText").clear()
        driver.implicitly_wait(3)
        driver.find_element_by_class_name("android.widget.EditText").send_keys(id)
        driver.implicitly_wait(3)
        driver.find_element_by_class_name("android.widget.Button").click()
        driver.implicitly_wait(3)
    else:
        print "Online APP"


def Install_xiaomi_APK(driver):
    '''安装国内小米包'''

    while isExistElementByID(driver,"item_3"):
        driver.remove_app("paint.by.number.pixel.art.coloring.drawing.puzzle")
        driver.install_app(r'/Users/apple/Desktop/PBN_UI_autotest/Apk/pbn-v1.15.2-r448-xiaomi.apk')
        driver.launch_app()
        Allow_box(driver)
        driver.implicitly_wait(3)
    print "this is CN Apk"


def Install_gp_APK(driver):
    '''安装google play 包'''

    while not isExistElementByID(driver,"item_3"):
        driver.remove_app("paint.by.number.pixel.art.coloring.drawing.puzzle")
        driver.install_app(r'/Users/apple/Desktop/PBN_UI_autotest/Apk/pbn-v1.16.3-r480-gp.apk')
        driver.launch_app()
        driver.implicitly_wait(3)
        Allow_box(driver)
    print "this is gp Apk"

def Allow_box(driver):
    '''allow 授权弹框'''

    while isExistElementByID(driver,"com.android.packageinstaller:id/permission_allow_button"):
        driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
        driver.implicitly_wait(3)


def Close_Newwork_Error(driver):
    '''启动app时，网络错误时重试'''
    while isExistElementByID(driver,"cv_try_again"):
        driver.find_element_by_id("cv_try_again").click()