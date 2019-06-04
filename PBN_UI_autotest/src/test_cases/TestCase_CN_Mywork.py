# -*- coding:utf-8 -*-

import os,time,unittest
from selenium import webdriver
from src.common.Base_unit import *
from src.pages.Library_page import *
from src.common.before_test import *
from src.pages.Drawing_page import *
from src.pages.Catagory_page import *
from src.pages.AD_page import *
from src.pages.CN_page import *
from src.pages.MyWork_page import *

class PNB_CN_Mywork(unittest.TestCase):
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

        cls.driver.close_app()

    def setUp(self):

        self.driver.launch_app()

        Allow_box(self.driver)
        Install_xiaomi_APK(self.driver)

        print ""
        print "start CN mywork case"

        before_test(self.driver)

        self.driver.implicitly_wait(3)


    def tearDown(self):

        print ""
        print "end CN mywork case"

        self.driver.close_app()

        self.driver.implicitly_wait(3)

    def MyWork_CN_Static_Check(self):
        '''国内包没有账户体系和成就的My work页面'''

        driver = self.driver

        driver.implicitly_wait(3)

        clickbyid(driver,"item_2")

        driver.implicitly_wait(3)

        CheckCNMyworktitle(driver)

        driver.implicitly_wait(3)

        if isExistElementByID(driver,"emptyImg"):

            CheckMywWorkCNNoPic(driver)
        else:
            CheckMyWorkDonePic(driver)

        driver.implicitly_wait(3)



if __name__=='__main__':

    suite = unittest.TestSuite()
    suite.addTest(PNB_CN_Mywork("MyWork_CN_Static_Check"))
    runner = unittest.TextTestRunner()
    runner.run(suite)