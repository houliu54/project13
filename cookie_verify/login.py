"""利用携带cookie跳过验证码"""
import json
import time

import timer
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://121.199.63.211:8088/bugfree/Login.php')
# 第一次的登录，获取它的cookie信息，保存到文件
# time.sleep(3)
# driver.find_element(By.ID,'TestUserName').send_keys('houliu')
# driver.find_element(By.ID,'TestUserPWD').send_keys('houliu')
# driver.find_element(By.ID,'RememberLoginStatus').click()
#
# driver.find_element(By.ID,'SubmitLoginBTN').click()
# with open('./cookie/c.txt','w+') as f:
#     f.write(json.dumps(driver.get_cookies()))
# print(driver.get_cookies())
#
# time.sleep(3)
# driver.quit()

# 如果后续页面如果还要在登录后的情况下才能打开或者获取信息，可以携带cookie信息，打开指定页面
driver.delete_all_cookies()   #  打开首页后，先清除一下页面缓存的cookies
with open('cookie/c.json', 'r') as f:
    cc = json.loads(f.read())
    for c in cc:
        if 'expiry' in c:
            del c['expiry']
        driver.add_cookie(c)
    print(driver.get_cookies())
    driver.get('http://121.199.63.211:8088/bugfree/EditMyInfo.php')
# driver.refresh() ## 再次刷新本url页面
time.sleep(4)
driver.quit()
