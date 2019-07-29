# coding:utf-8
__author__ = 'kiko'
'''
description:执行测试
'''
import os,sys,unittest,time
from src.common.HTML_TEST import *
from config.globalparameter import test_cases_path,report_name
from src.common import send_mail
from src.test_cases import TestCase_Daily
from src.test_cases import TestCase_Drawing
from src.test_cases import TestCase_Library
from src.test_cases import TestCase_MyWork
from src.test_cases import TestCase_News
from src.test_cases import TestCase_CN_Daily
from src.test_cases import TestCase_CN_Drawing
from src.test_cases import TestCase_CN_Library
from src.test_cases import TestCase_CN_Mywork

# 构建测试集,包含src/test_cases目录下的所有以test开头的.py文件
# suite = unittest.defaultTestLoader.discover(test_cases_path,pattern='test*.py',top_level_dir=None)

#手动添加测试集
suite = unittest.TestSuite()
suite.addTest(TestCase_Library.PNB_Library("Library_static_check"))
suite.addTest(TestCase_Library.PNB_Library("Category_check"))
suite.addTest(TestCase_Daily.PNB_DAILY("Daily_Static_Check"))
suite.addTest(TestCase_MyWork.PNB_MyWork("MyWork_Static_Check"))
suite.addTest(TestCase_MyWork.PNB_MyWork("MyWork_Login_Check"))
suite.addTest(TestCase_News.PNB_News("News_Static_Check"))
suite.addTest(TestCase_Drawing.PNB_DRAW("Reward_AD"))
suite.addTest(TestCase_Drawing.PNB_DRAW("Drawing_Flower"))
suite.addTest(TestCase_Drawing.PNB_DRAW("Drawing_horse"))

suite.addTest(TestCase_CN_Library.PNB_CN_LIB("Check_CN_Library"))
suite.addTest(TestCase_CN_Library.PNB_CN_LIB("Category_CN_check"))
suite.addTest(TestCase_CN_Daily.PNB_CN_Daily("Daily_CN_Static_Check"))
suite.addTest(TestCase_CN_Mywork.PNB_CN_Mywork("MyWork_CN_Static_Check"))
suite.addTest(TestCase_CN_Drawing.PNB_CN_DRAW("Reward_CN_AD"))
suite.addTest(TestCase_CN_Drawing.PNB_CN_DRAW("Drawing_CN_Flower"))
suite.addTest(TestCase_CN_Drawing.PNB_CN_DRAW("Drawing_CN_horse"))



if __name__=="__main__":
    report = report_name+"Report.html"
    fb = open(report,'wb')
    runner = HTMLTestRunner(
        stream=fb,
        title=u'PBN_Android Auto Test Report',
        description=u'Online App',
        verbosity = 2  ###在控制台打印执行log
    )
    runner.run(suite)
    fb.close()
    # 发送邮件
    time.sleep(10)  # 设置睡眠时间，等待测试报告生成完毕
    email = send_mail.send_email()
    email.sendReport()


