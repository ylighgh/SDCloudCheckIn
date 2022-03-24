import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from init import *

# 配置
# 创建chrome参数对象
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
# options.add_argument('window-size=1600x900')  # 指定浏览器分辨率
options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
# options.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
options.add_argument('--headless')  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
driver = webdriver.Chrome(options=options)
url = 'https://66yun104.xyz/auth/login'


try:
    driver.get(url)
except BaseException:
    mailto(1)
    exit()
else:
    def login_out():
        driver.delete_all_cookies()
        driver.get(url)


    for i in range(len(UserNameList)):
        username = UserNameList[i]
        password = PassWordList[i]

        # 获取用户名 密码 登陆按钮 签到按钮 组件
        element_username = driver.find_element(By.XPATH, '//*[@id="email"]')
        element_password = driver.find_element(By.XPATH, '//*[@id="passwd"]')
        element_sign_in = driver.find_element(By.XPATH, '//*[@id="login"]')

        # 键入用户名和密码
        element_username.send_keys(username)
        element_password.send_keys(password)

        # 点击登陆
        element_sign_in.click()
        time.sleep(5)

        # 点击签到
        try:
            element_sign = driver.find_element(By.XPATH, '//*[@id="checkin"]')
            element_sign.click()
        except BaseException:
            # print("%s今日已签到" % username)
            login_out()
        else:
            element_sign.click()
            login_out()

# 关闭浏览器
time.sleep(5)
mailto(0)
driver.close()
