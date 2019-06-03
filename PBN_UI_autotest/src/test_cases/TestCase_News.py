# -*- coding:utf-8 -*-

import os,time,unittest
from selenium import webdriver
from src.common.Base_unit import *
from src.pages.Library_page import *
from src.common.before_test import *
from src.pages.Catagory_page import *
from src.pages.News_page import *


class PNB_News(unittest.TestCase):
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

        Allow_box(self.driver)

        Install_gp_APK(self.driver)

        print ""
        print "start news case"

        Debug_Set_GroupID(self.driver,1)

        self.driver.implicitly_wait(3)

        before_test(self.driver)

        self.driver.implicitly_wait(5)


    def tearDown(self):

        print "end news case"
        print ""
        self.driver.close_app()

        self.driver.implicitly_wait(5)

    def News_Static_Check(self):
        '''News活动页面检查'''

        driver = self.driver

        clickbyid(driver,"paint.by.number.pixel.art.coloring.drawing.puzzle:id/item_2")

        checknewsstaticUI(driver)



if __name__=='__main__':
    suite = unittest.TestSuite()
    suite.addTest(PNB_News("News_Static_Check"))
    runner = unittest.TextTestRunner()
    runner.run(suite)

