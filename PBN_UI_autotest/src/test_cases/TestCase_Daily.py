# -*- coding:utf-8 -*-

import os,time,unittest
from selenium import webdriver
from src.common.Base_unit import *
from src.pages.Library_page import *
from src.pages.Drawing_page import *
from src.pages.Catagory_page import *
from src.pages.AD_page import *

class PNB_DAILY(unittest.TestCase):
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
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver.launch_app()
        before_test(self.driver)
        self.driver.implicitly_wait(3)
        Install_gp_APK(self.driver)
        print ("start Daily case")
        self.driver.implicitly_wait(3)

    def tearDown(self):
        self.driver.close_app()
        self.driver.implicitly_wait(3)
        print ("end daily case")

    def Daily_Static_Check(self):
        '''daily页礼包及素材列表检查（仅b方案）'''
        driver = self.driver
        driver.implicitly_wait(3)
        clickbyid(driver,"item_1")
        driver.implicitly_wait(3)
        if isExistElementByID(driver,"hand_decree"):
            try:
                assert (isExistElementByID(driver,"paint.by.number.pixel.art.coloring.drawing.puzzle:id/ivGiftLarge") == True),"gift error"
                assert (isExistElementByID(driver,"paint.by.number.pixel.art.coloring.drawing.puzzle:id/ivImageBk") == True),"ivImageBk error"
                assert (isExistElementByID(driver,"paint.by.number.pixel.art.coloring.drawing.puzzle:id/ivImage") == True),"ivImage error"
                assert (isExistElementByID(driver,"paint.by.number.pixel.art.coloring.drawing.puzzle:id/hand_decree") == True),"hand_decree error"
                assert (isExistElementByID(driver,"paint.by.number.pixel.art.coloring.drawing.puzzle:id/ivRipple") == True),"ivRipple error"
            except AssertionError as msg:
                print (msg)
                print ("Daily without open gift display error")
            print ("Daily without open gift display pass")
            driver.implicitly_wait(3)
            clickbyid(driver,"ivGiftLarge")
            driver.implicitly_wait(3)
            try:
                assert (isExistElementByID(driver,"recyclerView") == True),"gift error"
                assert (isExistElementsByID(driver,"ivImage") == True),"ivImage error"
                assert (isExistElementByID(driver,"start_btn") == True),"start_btn error"

                assert (isExistElementByID(driver,"timeTipsInfo") == True),"timeTipsInfo error"
                assert (isExistTextInElementByID(driver,"tvTips","Tomorrow Free Daily Pic") == True),"Tomorrow Free Daily Pic error"
                assert (isExistElementByID(driver,"tvTime") == True),"tvTime error"
            except AssertionError as msg:
                print (msg)
                print ("daily already open gift error")
            else:
                print ("daily already open gift pass")
        driver.implicitly_wait(3)
        try:
            assert (isExistElementsByID(driver, "textView") == True), "month error"
            i = 0
            while i < 10:
                assert (isExistElementsByID(driver, "cardView") == True), "cardView error"
                assert (isExistElementByID(driver, "ivImage") == True), "ivImage error"

                assert (isExistElementsByID(driver, "tvNumber") == True), "tvNumber error"
                swipe_down(driver)
                driver.implicitly_wait(3)
                i = i + 1
        except AssertionError as msg:
            print (msg)
            print ("daily pic list error")
        else:
            print ("daily pic list pass")

if __name__=='__main__':
    suite = unittest.TestSuite()
    suite.addTest(PNB_DAILY("Daily_Static_Check"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
