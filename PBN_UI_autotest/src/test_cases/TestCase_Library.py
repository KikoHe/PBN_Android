# -*- coding:utf-8 -*-

import os,time,unittest
from selenium import webdriver
from src.common.Base_unit import *
from src.pages.Library_page import *
from src.common.before_test import *
from src.pages.Catagory_page import *


class PNB_Library(unittest.TestCase):
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
        print "start library case"

        before_test(self.driver)

        self.driver.implicitly_wait(5)

    def tearDown(self):

        print "end library case"
        print ""
        self.driver.close_app()

        self.driver.implicitly_wait(5)


    def Library_static_check(self):
        '''检查library页：banner、分类标题、素材列表、页面底部tab'''

        driver = self.driver

        checkbanner(driver)

        checkcategorytab(driver)

        checklibrarylist(driver)

        checktab(driver)

        driver.implicitly_wait(5)

    def Category_check(self):
        '''点击素材分类tab，检查分类页素材'''
        driver = self.driver

        clickbytext(driver,
                    "//android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.TextView[contains(@text,'Bonus')]")

        checkBonus(driver)

        checkclickcategory(driver)

    def Category_swipe(self):
        '''左右滑动分类，检查分类页素材'''
        driver = self.driver

        checkswiperightcategorylist(driver)

        driver.implicitly_wait(3)

        checkswipeleftcategorylist(driver)


if __name__=='__main__':
    suite = unittest.TestSuite()
    suite.addTest(PNB_Library("Library_static_check"))
    # suite.addTest(PNB_Library("Category_check"))
    # suite.addTest(PNB_Library("Category_swipe"))
    runner = unittest.TextTestRunner()
    runner.run(suite)

