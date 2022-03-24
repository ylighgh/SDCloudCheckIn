UserNameList = [
    '邮箱@qq.com1',
    '邮箱@qq.com2'
]
PassWordList = [
    '密码1',
    '密码2'
]

MsgList = [
    '签到成功',
    '网址变更，更换网址'
]

# 发送多种类型的邮件
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def mailto(i):
    msg_from = '邮箱@qq.com'  # 发送方邮箱
    passwd = '邮箱授权码'  # 就是上面的授权码

    to = ['邮箱@qq.com']  # 接受方邮箱

    # 设置邮件内容
    # MIMEMultipart类可以放任何内容
    msg = MIMEMultipart()
    conntent = MsgList[i]
    # 把内容加进去
    msg.attach(MIMEText(conntent, 'plain', 'utf-8'))

    # 设置邮件主题
    msg['Subject'] = "签到"

    # 发送方信息
    msg['From'] = msg_from

    # 开始发送

    # 通过SSL方式发送，服务器地址和端口
    s = smtplib.SMTP_SSL("smtp.qq.com", 465)
    # 登录邮箱
    s.login(msg_from, passwd)
    # 开始发送
    s.sendmail(msg_from, to, msg.as_string())
    # print("邮件发送成功")
