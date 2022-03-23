import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from init import UserNameList, PassWordList



def login_out():
    driver.delete_all_cookies()
    driver.get(url)


driver = webdriver.Chrome()


url = 'https://66yun104.xyz/auth/login'
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
        print("%s今日已签到" % username)
        login_out()
    else:
        element_sign.click()
        print("签到成功")

# 关闭浏览器
time.sleep(5)
driver.close()
