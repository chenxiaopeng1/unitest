# -*- coding: UTF-8 -*-
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart     #添加附件用的包

class send_Email():


    def sendEmail(self):
        #port = 25
        content = '本次的测试结果为'
        from_addr = 'cxp-qq@163.com'
        password = 'cxp15999867402'
        smtp_server = 'smtp.163.com'
        to_addrs = 'xp@duoweimmm.com'
        message = MIMEText(content, _subtype='plain', _charset='utf-8')
        message['Subject'] = str(datetime.datetime.now()) + '测试结果为'
        message['From'] = from_addr
        message['To'] = to_addrs

        server = smtplib.SMTP_SSL(smtp_server)
        server.set_debuglevel(1)
        server.login(from_addr, password)
        server.sendmail(from_addr, to_addrs, message.as_string())
        server.quit()
        print(str(datetime.datetime.now())+'测试结果邮件发送成功')


if __name__=='__main__':
    send=send_Email().sendEmail()