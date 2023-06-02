"""allure生成测试报告的动态方式"""
import allure


# 描述信息
def allure_description(description):
    allure.dynamic.description(description)
