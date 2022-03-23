= 66yun自动签到

== 环境准备

使用selenium+chrome 进行每日签到

[soruce, python]
----
pip install -r requirements.txt

wget -N http://npm.taobao.org/mirrors/chromedriver/对应的版本号/chromedriver_linux64.zip

unzip chromedriver_linux64.zip

chmod +x chromedriver

sudo mv -f chromedriver /usr/local/share/chromedriver

sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver

sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedrive

----


== 使用说明

更改init包下的`UserNameList`和`PassWordList`的内容即可

== 执行命令

[soruce, python]
----
python AutoCheakIn.py
----
