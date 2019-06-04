# coding:utf-8
__author__ = 'kiko'
'''
description:邮件发送最新的测试报告
'''
import os,smtplib,os.path,sys
from config import globalparameter as gl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
reload(sys)
sys.setdefaultencoding('utf8')

class send_email:
    # 定义邮件内容
    def email_init(self,report,reportName):
        with open(report,'rb')as f:
            mail_body = f.read()

        # 创建一个带附件的邮件实例
        msg = MIMEMultipart()
        # 以测试报告作为邮件正文
        msg.attach(MIMEText(mail_body,'html','utf-8'))
        report_file = MIMEText(mail_body,'html','utf-8')
        # 定义附件名称（附件的名称可以随便定义，你写的是什么邮件里面显示的就是什么）
        report_file["Content-Disposition"] = 'attachment;filename='+reportName
        msg.attach(report_file) # 添加附件
        msg['Subject'] = 'PBN_Android Auto Test Report : ' + reportName # 邮件标题
        msg['From'] = gl.email_name  #发件人
        msg['To'] = gl.email_To  #收件人列表
        try:
            server = smtplib.SMTP(gl.smtp_sever)
            server.login(gl.email_name,gl.email_password)
            server.sendmail(msg['From'],msg['To'].split(';'),msg.as_string())
            server.quit()
        except smtplib.SMTPException:
            print "send mail fail"
            # self.mylog.error(u'send mail fail  at'+__file__)
        else:
            print "send mail success"

    def sendReport(self):
        # 找到最新的测试报告
        report_list = os.listdir(gl.report_path)
        report_list.sort(key=lambda fn: os.path.getmtime(gl.report_path+fn) if not os.path.isdir(gl.report_path+fn) else 0)
        new_report = os.path.join(gl.report_path,report_list[-1])
        # 发送邮件
        self.email_init(new_report,report_list[-1])






        