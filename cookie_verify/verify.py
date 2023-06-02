
"""打开另一个页面需要先获取登录状态时的信息"""
import json
import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://121.199.63.211:8088/bugfree/Login.php')
driver.delete_all_cookies()
print(driver.get_cookies())
with open('cookie/c.json', 'r') as f:
    new_cookie = json.loads(f.read())
    for c in new_cookie:
        driver.add_cookie(c)
    print(driver.get_cookies())
driver.get('http://121.199.63.211:8088/bugfree/EditMyInfo.php')
driver.refresh()


time.sleep(3)
driver.quit()
# import requests
#
# s = requests.Session()
# print(s.cookies)
# c = requests.cookies.RequestsCookieJar()
# c.set("BFUserName","houliu")
# c.set('BFUserPWD',"houliu")
# c.set("PHPSESSID","faff2dfdb40c24cb86b9d0da260e271e")
# c.set("BFRememberStatus","1")
# s.cookies.update(c)
#
# print(s.cookies)
# b = {"xajax":'xCheckUserLogin',
#      "xajaxr":"1676273297427",
#      "xajaxargs[]":"<xjxquery><q>TestUserName=houliu&TestUserPWD=houliu&Language=ZH_CN_UTF-8&HttpRefer=</q></xjxquery>"}
#
#
#
# res = s.post(url='http://121.199.63.211:8088/bugfree/Login.php',data=b)
# print(s.cookies)
