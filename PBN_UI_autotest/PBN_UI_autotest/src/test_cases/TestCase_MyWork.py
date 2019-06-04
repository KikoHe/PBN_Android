# -*- coding:utf-8 -*-

import os,time,unittest
from selenium import webdriver
from src.common.Base_unit import *
from src.pages.Library_page import *
from src.pages.Catagory_page import *
from src.pages.MyWork_page import *


class PNB_MyWork(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        desired_caps = {}

        desired_caps['platformName'] = 'Android'  # 设备系统

        desired_caps['platformVersion'] = '8.0.0'  # 设备系统版本

        desired_caps['deviceName'] = '3836414438313098'  # 设备名称

        desired_caps['appPackage'] = 'paint.by.number.pixel.art.coloring.drawing.puzzle'  #需要测试的APP包名

        desired_caps['appActivity'] = 'com.meevii.business.splash.SplashActivity'  #需要测试的APP启动首页名称

        desired_caps['unicodeKeyboard'] = True

        desired_caps['resetKeyboard'] = True    #关闭设备系统键盘

        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):

        self.driver.launch_app()

        Allow_box(self.driver)

        Install_gp_APK(self.driver)

        print ""
        print "start work case"

        before_test(self.driver)

        self.driver.implicitly_wait(5)

    def tearDown(self):

        print "end work case"
        print ""

        self.driver.close_app()

        self.driver.implicitly_wait(5)

    def MyWork_Static_Check(self):
        '''未登录状态下的My work页面及成就页面'''

        driver = self.driver

        driver.implicitly_wait(3)

        clickbyid(driver,"item_3")

        driver.implicitly_wait(3)

        CheckMyWorkNoLoginTitle(driver)

        driver.implicitly_wait(3)

        CheckMywWorkNoPic(driver)

        driver.implicitly_wait(3)

        clickbyid(driver,"btn_badge")

        time.sleep(3)

        ClickHintReward(driver)

        time.sleep(3)

        CheckAchievement(driver)

        driver.implicitly_wait(3)


    def MyWork_Login_Check(self):
        '''登录账户，并检查MY WORK'''

        driver = self.driver

        driver.implicitly_wait(3)

        clickbyid(driver,"item_3")

        driver.implicitly_wait(3)

        clickbyid(driver,"iv_header")

        driver.implicitly_wait(3)

        CheckLoginScreen(driver)

        driver.implicitly_wait(3)

        clickbyid(driver,"cvGoogle")

        driver.implicitly_wait(30)

        if isExistElementByID(driver,"com.google.android.gms:id/account_picker"):

            ele = driver.find_elements_by_id("com.google.android.gms:id/account_display_name")

            name = ele[0].text

            ele[0].click()

            driver.implicitly_wait(30)

            if driver.find_element_by_id("tv_name").text == name:

                print "google account log in success"

                print name

            else:

                print "login fail"
        else:

            if isExistTextInElementByID(driver,"tv_sync_tip","Last sync time: less than 1 day") == True:

                print "login success"

            else:

                print "login fail"

        driver.implicitly_wait(3)

        CheckMyWorkLoginTitle(driver)

        driver.implicitly_wait(3)

        CheckMyWorkDonePic(driver)

        driver.implicitly_wait(3)

        CheckLogout(driver)

if __name__=='__main__':

    suite = unittest.TestSuite()

    suite.addTest(PNB_MyWork("MyWork_Static_Check"))

    # suite.addTest(PNB_MyWork("MyWork_Login_Check"))

    runner = unittest.TextTestRunner()

    runner.run(suite)

