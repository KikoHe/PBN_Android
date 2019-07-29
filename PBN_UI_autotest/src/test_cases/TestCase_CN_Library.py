# -*- coding:utf-8 -*-

import os,time,unittest
from selenium import webdriver
from src.common.Base_unit import *
from src.pages.Library_page import *
from src.pages.Drawing_page import *
from src.pages.Catagory_page import *
from src.pages.AD_page import *
from src.pages.CN_page import *

class PNB_CN_LIB(unittest.TestCase):
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
        before_test(self.driver)
        Install_xiaomi_APK(self.driver)
        print ("start CN Library case")
        self.driver.implicitly_wait(3)

    def tearDown(self):
        self.driver.close_app()
        self.driver.implicitly_wait(3)
        print("end CN Library case")

    def Check_CN_Library(self):
        '''检查library页：banner、分类标题、素材列表、页面底部tab'''
        driver = self.driver
        # Check_CN_Lib_Banner(driver)
        driver.implicitly_wait(3)
        checkcncategorytab(driver)
        driver.implicitly_wait(3)
        checklibrarylist(driver,3)
        driver.implicitly_wait(3)
        checkcntab(driver)

    def Category_CN_check(self):
        '''点击素材分类tab，检查分类页素材'''
        driver = self.driver
        time.sleep(5)
        checkclickcategory_new(driver, "cn")

    def Category_CN_swipe(self):
        '''左右滑动分类，检查分类页素材'''
        driver = self.driver
        category = ["推荐", "精品", "古风", "人物", "萌宠", "恋爱", "鲜花", "文艺", "卡通", "人气", "曼陀罗", "美食", "美景", "节日", "其他"]
        i = 0
        while i <= len(category) - 1:
            driver.implicitly_wait(3)
            while not (isExistElementsByID(driver, "rootLayout") and isExistElementsByID(driver, "imageView")):
                time.sleep(3)
            m = 0
            while (get_ele_attribute(driver,
                                     "//android.widget.HorizontalScrollView/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView[contains(@text,'{label}')]".format(label=category[i]), "selected")) != "true":
                driver.implicitly_wait(3)
                driver.find_element_by_xpath(
                    "//android.widget.HorizontalScrollView/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView[contains(@text,'{label}')]".format(label=category[i])).click()
                m = m + 1
                if m > 3:
                    break
                    print ("swipe category error")
            driver.implicitly_wait(3)
            print ("swipe to category： " + category[i])
            driver.swipe(1020, 1300, 60, 1300, 2000)
            i = i + 1
        i = i - 2
        while i >= 0:
            driver.implicitly_wait(5)
            while not (isExistElementsByID(driver,"rootLayout") and isExistElementsByID(driver,"imageView")):
                time.sleep(3)
            p = 0
            while (get_ele_attribute(driver,"//android.widget.HorizontalScrollView/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView[contains(@text,'{label}')]".format(label=category[i]),"selected")) != "true":
                driver.implicitly_wait(3)
                driver.find_element_by_xpath("//android.widget.HorizontalScrollView/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView[contains(@text,'{label}')]".format(label=category[i])).click()
                p = p + 1
                if p > 3:
                    break
                    print ("swipe category error")
            driver.implicitly_wait(3)
            print ("swipe back to category:  " + category[i])
            driver.swipe(60,1300,1020,1300,3000)
            i = i - 1

if __name__=='__main__':
    suite = unittest.TestSuite()
    # suite.addTest(PNB_CN_LIB("Check_CN_Library"))
    suite.addTest(PNB_CN_LIB("Category_CN_check"))
    # suite.addTest(PNB_CN_LIB("Category_CN_swipe"))
    runner = unittest.TextTestRunner()
    runner.run(suite)