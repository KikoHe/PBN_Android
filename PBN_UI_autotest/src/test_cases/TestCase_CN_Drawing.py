# -*- coding:utf-8 -*-

import os,time,unittest
from selenium import webdriver
from src.common.Base_unit import *
from src.pages.Library_page import *
from src.pages.Drawing_page import *
from src.pages.Catagory_page import *
from src.pages.AD_page import *
from src.pages.CN_page import *
from src.test_cases.TestCase_Drawing import *

class PNB_CN_DRAW(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'  # 设备系统
        desired_caps['platformVersion'] = '8.0.0'  # 设备系统版本
        desired_caps['deviceName'] = '3836414438313098'  # 设备名称
        desired_caps['appPackage'] = 'paint.by.number.pixel.art.coloring.drawing.puzzle'
        desired_caps['appActivity'] = 'com.meevii.business.splash.SplashActivity'
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        desired_caps['noReset'] = True
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close_app()

    def setUp(self):
        self.driver.launch_app()
        before_test(self.driver)
        Install_xiaomi_APK(self.driver)
        print ("start CN Drawwing case")
        self.driver.implicitly_wait(3)

    def tearDown(self):
        print ("end CN Drawwing case")
        self.driver.close_app()
        self.driver.implicitly_wait(3)

    def Reward_CN_AD(self):
        '''打开素材分类new的第4张素材，检查reward广告显示是否正常'''
        driver = self.driver
        wait_list_pic(driver,3)
        driver.implicitly_wait(5)
        click_list_pic_number(driver,3)
        driver.implicitly_wait(5)
        Drawing_Reward_AD(driver,3)

    def Drawing_CN_Flower(self):
        '''打开花朵素材，检查banner广告、插屏广告、着色完成页'''
        driver = self.driver
        wait_list_pic(driver,3)
        driver.implicitly_wait(10)
        click_list_pic_number(driver,0)
        driver.implicitly_wait(5)
        if isExistElementByClass(driver, "android.webkit.WebView"):
            print("pop up inter AD")
            driver.implicitly_wait(5)
            Close_AD(driver)
            driver.implicitly_wait(5)
        Get_New_Banner_AD(driver,0)
        Drawing_UI_check(driver)
        Drawing_pic_flower(driver)
        driver.implicitly_wait(5)
        if isExistElementByID(driver, "tvContinue"):
            clickbyid(driver, "tvContinue")
        else:
            driver.press_keycode(4)
        driver.implicitly_wait(5)
        Close_Write_Review(driver)
        driver.implicitly_wait(5)
        Close_Achievement(driver)

    def Drawing_CN_horse(self):
        '''打开小马素材，检查banner广告、插屏广告、着色完成页'''
        driver = self.driver
        wait_list_pic(driver,3)
        click_list_pic_number(driver,2)
        driver.implicitly_wait(3)
        if isExistElementByClass(driver, "android.webkit.WebView"):
            print("pop up inter AD")
            driver.implicitly_wait(5)
            Close_AD(driver)
            driver.implicitly_wait(5)
        Get_New_Banner_AD(driver, 2)
        driver.implicitly_wait(3)
        Drawing_pic_horse(driver)
        driver.implicitly_wait(3)
        if isExistElementByID(driver, "tvContinue"):
            clickbyid(driver, "tvContinue")
        else:
            driver.press_keycode(4)
        driver.implicitly_wait(3)
        AD_Check(driver)
        Close_AD(driver)
        driver.implicitly_wait(3)
        Close_Write_Review(driver)
        Close_Achievement(driver)

if __name__=='__main__':
    suite = unittest.TestSuite()
    # suite.addTest(PNB_CN_DRAW("Reward_CN_AD"))
    suite.addTest(PNB_CN_DRAW("Drawing_CN_Flower"))
    suite.addTest(PNB_CN_DRAW("Drawing_CN_horse"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
