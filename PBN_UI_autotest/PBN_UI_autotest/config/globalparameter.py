# -*- coding:utf-8 -*-

__author__='kiko'

'''description:配置全局参数'''

import time, os

# 获取项目路径
# project_path = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)[0]), '.'))
project_path = os.path.abspath(os.path.join(os.path.dirname(os.path.split(os.path.realpath(__file__))[0]), '.'))

# 测试用例代码存放路径（用于构建suite,注意该文件夹下的文件都应该以test开头命名）
test_cases_path = project_path + "/src/test_cases/"

# 测试包的存放路径
test_apk = project_path + "/Apk/"

# 测试报告存储路径，并以当前时间作为报告名称前缀
report_path = project_path + "/report/"
report_name = report_path + time.strftime('%Y%m%d%H%S', time.localtime())


# 设置发送测试报告的公共邮箱、用户名和密码
smtp_sever = 'smtp.163.com'  # 邮箱SMTP服务，各大运营商的smtp服务可以在网上找，然后可以在foxmail这些工具中验正
email_name = "atdailyinnovation@163.com"  # 发件人名称
email_password = "ht123456789"  # 发件人登录密码
email_To = 'atdailyinnovation@163.com;hetao@dailyinnovation.biz'  # 收件人
# email_To = 'atdailyinnovation@163.com;junjie@dailyinnovation.biz;hetao@dailyinnovation.biz'  # 收件人
# email_To = 'junjie@dailyinnovation.biz;hetao@dailyinnovation.biz;atdailyinnovation@163.com;liuyingying@dailyinnovation.biz;yudan@dailyinnovation.biz;bob@dailyinnovation.biz;xuyi@dailyinnovation.biz;lingou@dailyinnovation.biz;gaomin@dailyinnovation.biz;xinru@dailyinnovation.biz;chunfei@dailyinnovation.biz;aiping@dailyinnovation.biz;xiayang@dailyinnovation.biz;guomin@dailyinnovation.biz'  # 收件人