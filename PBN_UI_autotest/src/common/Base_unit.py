#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding=utf-8
__author__='kiko'

'''description:UI公共类'''

import time, base64, unittest,os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from config import globalparameter as gl
from src.common.gesture_mainpulation import *

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
    try:
        driver.find_element_by_id(ele_id).text == word
        return True
    except:
        return False

def isExistTextInElementsByxpath(driver, ele_xpath,number,word):
    '''Usage: 通过xpath判断该元素组文案是否预期'''
    try:
        driver.find_elements_by_xpath(ele_xpath)[number].text == word
        return True
    except:
        return False


def isExistTextInElementByxpath(driver, ele_xpath):
    '''Usage: 通过xpath判断该元素文案是否预期'''
    try:
        driver.find_element_by_xpath(ele_xpath)
        return True
    except:
        return False

def isExistTextwordInElementByxpath(driver, ele_xpath,word):
    '''Usage: 通过xpath判断该元素文案是否预期'''
    try:
        driver.find_element_by_xpath(ele_xpath).text == word
        return True
    except:
        return False

def isExistTextInElementsByid(driver, ele_id,number,word):
    '''Usage: 通过id判断该元素组文案是否预期'''
    try:
        driver.find_elements_by_id(ele_id)[number].text == word
        return True
    except:
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
    try:
        element.location['x'] < ele_layout.location['x'] + ele_layout.size['width'] \
            and element.location['y'] < ele_layout.location['y'] + ele_layout.size['height']
        return True
    except:
        return False

def get_eles_attribute(driver,ele_xpath,number,attribute):
    ele = driver.find_elements_by_xpath(ele_xpath)[number].get_attribute(attribute)
    return ele

def get_ele_attribute(driver,ele_xpath,attribute):
    ele = driver.find_element_by_xpath(ele_xpath).get_attribute(attribute)
    return ele

def DebugApp_Set_GroupID(driver,id):
    '''测试包设置group id'''
    if isExistElementByClass(driver,"android.widget.EditText"):
        print ("Test APP")
        driver.find_element_by_class_name("android.widget.EditText").clear()
        driver.implicitly_wait(3)
        driver.find_element_by_class_name("android.widget.EditText").send_keys(id)
        driver.implicitly_wait(3)
        driver.find_element_by_class_name("android.widget.Button").click()
        driver.implicitly_wait(3)
    else:
        print ("Online APP")

def Install_xiaomi_APK(driver):
    '''安装国内小米包'''
    while isExistElementByID(driver,"item_3"):
        driver.remove_app("paint.by.number.pixel.art.coloring.drawing.puzzle")
        driver.implicitly_wait(3)
        driver.install_app(get_other_app())
        print ("install : " + get_other_app())
        driver.launch_app()
        before_test(driver)
        driver.implicitly_wait(3)
    print ("this is CN Apk")

def Install_gp_APK(driver):
    '''安装google play 包'''
    while not isExistElementByID(driver,"item_3"):
        driver.remove_app("paint.by.number.pixel.art.coloring.drawing.puzzle")
        driver.install_app(get_gp_app())
        print ("install : " + get_gp_app())
        driver.launch_app()
        driver.implicitly_wait(3)
        before_test(driver)
    print ("this is gp Apk")

def Allow_box(driver):
    '''allow 授权弹框'''
    while isExistElementByID(driver,"com.android.packageinstaller:id/permission_allow_button"):
        driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
        driver.implicitly_wait(3)

def Close_Newwork_Error(driver):
    '''启动app时，网络错误时重试'''
    while isExistElementByID(driver,"cv_try_again"):
        driver.find_element_by_id("cv_try_again").click()
        driver.implicitly_wait(3)
        print("close launch network box...")

def before_test(driver):
    ''''启动前准备'''
    Allow_box(driver)
    DebugApp_Set_GroupID(driver, 1)
    Close_Newwork_Error(driver)
    closewelcomeview(driver)
    closedrawview(driver)
    close_box(driver)
    while test_imagetestcase(driver) == 2:
        relaunch(driver)
        if test_imagetestcase(driver) == 1:
            break

def relaunch(driver):
    '''
    重启
    :param driver:
    :return:
    '''
    driver.close_app()
    driver.implicitly_wait(3)
    driver.launch_app()
    before_test(driver)

def test_imagetestcase(driver):
    '''通过第一个素材的标签判断素材方案'''
    wait_until_id(driver,"ivFlag",5)
    try:
        assert (isExistElementsByID(driver,"ivFlag") == True)
    except AssertionError:
        print("no ivFlag...")
        driver.get_screenshot_as_file("/Users/apple/Desktop/pbn_autotest_android_pyton3/screenshot/error4.png")
    else:
        ele_ivflag = driver.find_elements_by_id("ivFlag")
        if ele_ivflag:
            if int(ele_ivflag[0].size['width']) == 117:
                print("Not sort test..")
                return 1
            elif int(ele_ivflag[0].size['width']) == 177:
                print("Sort test..")
                return 2
            elif int(ele_ivflag[0].size['width']) == 90:
                print("test..")
        else:
            print("list is empty...")

def close_box(driver):
    '''
    关闭赠送会员弹框
    :param driver:
    :return:
    '''
    if isExistElementByID(driver,'paint.by.number.pixel.art.coloring.drawing.puzzle:id/iv_close'):
        clickbyid(driver,'paint.by.number.pixel.art.coloring.drawing.puzzle:id/iv_close')

def closewelcomeview(driver):
    '''关闭启动时的免责声明页面'''
    while isExistElementByID(driver,"paint.by.number.pixel.art.coloring.drawing.puzzle:id/cv_accept") == True:
        checkwelcomeview(driver)
        driver.implicitly_wait(2)
        clickbyid(driver,"paint.by.number.pixel.art.coloring.drawing.puzzle:id/cv_accept")
        driver.implicitly_wait(2)
        print ("Skip Privacy Policy and Terms View")

def closedrawview(driver):
    '''关闭新手引导'''
    while isExistElementByID(driver, "paint.by.number.pixel.art.coloring.drawing.puzzle:id/fillColorImageView"):
        driver.find_element_by_id("paint.by.number.pixel.art.coloring.drawing.puzzle:id/btnExit").click()
        driver.implicitly_wait(2)
        print ("Close Coloring View...")

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
    except AssertionError as msg:
        print (msg)
        print ("Privacy Policy and Terms View Error")

def wait_until_id(driver,id,i):
    '''等待ID元素'''
    n = 0
    while not isExistElementByID(driver, id):
        driver.implicitly_wait(3)
        n = n + 1
        if n > i:
            break
            print ("not display id:  " + id)

def wait_list_pic(driver,i):
    m = 0
    while not isExistElementByID(driver, "recyclerView"):
        driver.implicitly_wait(3)
        m = m + 1
        if m > i:
            break
            print("enter library error")

def get_gp_app():
    '''获取gp apk'''
    for dir,redir,files in os.walk(gl.test_apk):
        i = 1
        while i < len(files):
            if len(files[i]) <= 23 :
                l = []
                l.append(files[i])
            i = i + 1
    print(l)
    return (gl.test_apk + l[-1])

def get_other_app():
    '''获取0ther apk'''
    for dir,redir,files in os.walk(gl.test_apk):
        i = 1
        while i < len(files):
            if len(files[i]) > 23 :
                l_cn = []
                l_cn.append(files[i])
            i = i + 1
    print(l_cn)
    return gl.test_apk + l_cn[-1]
