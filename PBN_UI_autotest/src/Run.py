# coding:utf-8
import unittest
import time
import smtplib
import os,sys
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from src.common.HTML_TEST import HTMLTestRunner
from src.test_cases import TestCase_Daily
from src.test_cases import TestCase_Drawing
from src.test_cases import TestCase_Library
from src.test_cases import TestCase_MyWork
from src.test_cases import TestCase_News
reload(sys)
sys.setdefaultencoding('utf8')

# 获取项目路径
project_path = os.path.abspath(os.path.join(os.path.dirname(os.path.split(os.path.realpath(__file__))[0]), '.'))

# 测试用例代码存放路径（用于构建suite,注意该文件夹下的文件都应该以test开头命名）
test_cases_path = project_path + "/src/test_cases"

# 测试报告存储路径，并以当前时间作为报告名称前缀
report_path = project_path + "/report/"
report_name = report_path + time.strftime('%Y%m%d%H%S', time.localtime()) + "report.html"
print report_name

# 发送邮件
def sendmail(sendfile):
    smtpserver = 'smtp.qq.com'
    user = '547151061@qq.com'
    password = 'sgymocifnfqabcfi'  #授权码，不是密码
    sender = '547151061@qq.com'
    # receiver = '731389931@qq.com'
    receiver = '547151061@qq.com'
    subject = 'PBN Android auto test report'

    # f = open(sendfile, 'rb')
    # mailbody = f.read()  # 读取测试报告作为邮件正文
    # f.close()
    with open(sendfile, 'rb')as f:
        mailbody = f.read()

    # 创建一个带附件的邮件实例
    msg = MIMEMultipart()

    # 以测试报告作为邮件正文
    msg.attach(MIMEText(mailbody, 'html', 'utf-8'))
    report_file = MIMEText(mailbody, 'html', 'utf-8')

    # 定义附件名称（附件的名称可以随便定义，你写的是什么邮件里面显示的就是什么）
    report_file["Content-Disposition"] = 'attachment;filename=' + report_name
    msg.attach(report_file)  # 添加附件

    msg["Subject"] = Header(subject, 'utf-8')

    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(user, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print('Email has send out')


# 查找目录下最新生成的测试报告,返回最新报告的详细路径
def find_Report(reportpath):
    lists = os.listdir(reportpath)
    lists.sort(key=lambda fn: os.path.getmtime(reportpath + "/" + fn))
    newfile = os.path.join(reportpath, lists[-1])
    print(newfile)
    return newfile


# 运行case，并生成测试报告
def run_case():
    suite = unittest.TestSuite()
    suite.addTest(TestCase_Library.PNB_Library("Library_static_check"))
    # suite.addTest(TestCase_Library.PNB_Library("Category_check"))
    # suite.addTest(TestCase_Library.PNB_Library("Category_swipe"))

    suite.addTest(TestCase_Daily.PNB_DAILY("Daily_Static_Check"))

    suite.addTest(TestCase_MyWork.PNB_MyWork("MyWork_Static_Check"))
    suite.addTest(TestCase_MyWork.PNB_MyWork("MyWork_Login_Check"))

    suite.addTest(TestCase_News.PNB_News("News_Static_Check"))

    suite.addTest(TestCase_Drawing.PNB_DRAW("Reward_AD"))
    suite.addTest(TestCase_Drawing.PNB_DRAW("Drawwing_Flower"))
    # suite.addTest(TestCase_Drawing.PNB_DRAW("Drawwing_horse"))

    fp = open(report_name, 'wb')
    runner = HTMLTestRunner(
        stream=fp,
        title='Auto test report',
        description='PBN testcase',
    )
    runner.run(suite)
    # 运行case，生成HTML测试报告
    fp.close()


if __name__ == '__main__':
    run_case()
    new_report = find_Report(report_path)
    sendmail(new_report)