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

        Allow_box(self.driver)

        Install_xiaomi_APK(self.driver)

        print ""
        print "start CN Library case"

        Debug_Set_GroupID(self.driver,1)

        self.driver.implicitly_wait(3)

        before_test(self.driver)

        self.driver.implicitly_wait(3)


    def tearDown(self):

        print ""
        print "end CN Library case"

        self.driver.close_app()

        self.driver.implicitly_wait(3)

    def Check_CN_Library(self):
        '''检查library页：banner、分类标题、素材列表、页面底部tab'''

        driver = self.driver

        Check_CN_Lib_Banner(driver)

        checkcncategorytab(driver)

        checklibrarylist(driver)

        checkcntab(driver)

    def Category_CN_check(self):
        '''点击素材分类tab，检查分类页素材'''

        driver = self.driver

        category = ["推荐", "人物", "萌宠", "卡通", "人气", "曼陀罗", "美食", "鲜花", "节日", "插画"]

        i = 0

        while i <= 9:
            clickbytext(driver,
                        "//android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.TextView[contains(@text,'{label}')]".format(label=category[i]))

            driver.implicitly_wait(3)

            checklibrarylist(driver)

            assert (get_ele_attribute(driver,
                                      "//android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.TextView[contains(@text,'{label}')]".format(label=category[i]), "selected") == "true")

            print category[i] + 'display normal'

            i = i + 1

    def Category_CN_swipe(self):
        '''左右滑动分类，检查分类页素材'''
        driver = self.driver

        category = ["推荐", "人物", "萌宠", "卡通", "人气", "曼陀罗", "美食", "鲜花", "节日", "插画"]

        i = 0

        while i <= 9:

            driver.implicitly_wait(3)

            while not (isExistElementsByID(driver, "rootLayout") and isExistElementsByID(driver, "imageView")):
                time.sleep(3)
            m = 0
            while (get_ele_attribute(driver,
                                     "//android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.TextView[contains(@text,'{label}')]".format(label=category[i]), "selected")) != "true":
                driver.implicitly_wait(3)
                driver.find_element_by_xpath(
                    "//android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.TextView[contains(@text,'{label}')]".format(label=category[i])).click()
                m = m + 1
                if m > 3:
                    break
                    print "swipe category error"

            driver.implicitly_wait(3)

            print "swipe to" + category[i]

            driver.swipe(1020, 1300, 60, 1300, 2000)

            i = i + 1

        category1 = ["插画","节日","鲜花","美食","曼陀罗","人气","卡通","萌宠","人物","推荐"]

        n = 0

        while n <= 9:

            driver.implicitly_wait(5)

            while not (isExistElementsByID(driver,"rootLayout") and isExistElementsByID(driver,"imageView")):
                time.sleep(3)

            p = 0
            while (get_ele_attribute(driver,"//android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.TextView[contains(@text,'{label}')]".format(label=category1[n]),"selected")) != "true":
                driver.implicitly_wait(3)
                driver.find_element_by_xpath("//android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.TextView[contains(@text,'{label}')]".format(label=category1[n])).click()
                p = p + 1
                if p > 3:
                    break
                    print "swipe category error"

            driver.implicitly_wait(3)

            print "swipe to " + category1[n]

            driver.swipe(60,1300,1020,1300,3000)

            n = n + 1



if __name__=='__main__':

    suite = unittest.TestSuite()
    # suite.addTest(PNB_News("Drawing_static_check"))
    # suite.addTest(PNB_DRAW("Reward_AD"))
    # suite.addTest(PNB_CN_LIB("Category_CN_check"))
    suite.addTest(PNB_CN_LIB("Category_CN_swipe"))
    # suite.addTest(PNB_DRAW("Drawwing_tiger"))
    runner = unittest.TextTestRunner()
    runner.run(suite)