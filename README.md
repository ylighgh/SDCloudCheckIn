# 66yun自动签到

## 环境准备

使用python+selenium模拟登陆进行每日签到获取流量(版本python3.8)

---

pip install -r requirements.txt

wget -N http://npm.taobao.org/mirrors/chromedriver/`yours_chrome_version`/chromedriver_linux64.zip

unzip chromedriver_linux64.zip

chmod +x chromedriver

sudo mv chromedriver /usr/bin/chromedriver

---


## 使用说明

更改init包下的`UserNameList`和`PassWordList`的内容

以及邮箱的部分信息（收发件人 邮箱授权码）

## 执行命令

---

python AutoCheakIn.py

---


## 其他

使用`Linux Crontab`进行任务自动化