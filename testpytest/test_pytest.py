import allure


# allure.dynamic.feature('登录模块')
# allure.dynamic.story('登录成功')
from testpytest import dynamic


@allure.feature('登录模块')
class Test(object):
    @allure.story('登录成功场景')
    @allure.title('输入正确的用户名和密码能登录成功')
    @allure.description('xxxxxxxxxxxxx')
    def test_01(self):
        with allure.step('输入用户名'):
            print('....package1')
        with allure.step('输入密码'):
            print('....password')

    @allure.story('登录失败场景')
    @allure.title('用户名错误')
    def test_02(self):
        dynamic.allure_description('dynamic动态')
        print('....package2')

    @allure.story('登录失败场景')
    @allure.title('密码错误')
    def test_03(self):
        print('....package3')

    @allure.story('登录失败场景')
    @allure.title('用户名或密码为空')
    def test_04(self):
        print('....package4')






