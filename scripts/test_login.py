import sys, os

sys.path.append(os.getcwd())

import pytest
import allure
import pymysql as pymysql
from selenium import webdriver
from Page.Page import Page_Obj
from time import sleep


def read_database():
    db = pymysql.connect(host='localhost', user='root', password='123456', database='user', port=3306,
                         charset='utf8')
    sql = 'select username, password from user'
    cursor = db.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    db.close()
    cursor.close()
    return results


@allure.feature("测试登录模块")
class Test_login:

    @allure.step("初始化对象，打开浏览器")
    def setup(self):
        self.driver = webdriver.Chrome()
        self.lp = Page_Obj(self.driver).Login_Page()
        self.lp.open_browser('http://119.29.235.245:9003/index.php/user/login')

    @allure.step("关闭浏览器")
    def teardown(self):
        self.lp.close_browser()

    # @pytest.mark.parametrize("user,passwd", [('zerong.zhang', 'RK0A9ICT'), ('zzzzrr', '123456')])
    # def test_login(self, user, passwd):
    #     self.lp.test_login(user, passwd)
    #     expect_url = 'http://119.29.235.245:9003/index.php/home/welcome'
    #     current_url = self.driver.current_url
    #     assert expect_url == current_url

    @pytest.mark.parametrize("user,passwd", read_database())
    @allure.story("用户登录验证")
    def test_login(self, user, passwd):
        with allure.step("输入用户名，密码"):
            self.lp.test_login(user, passwd)
            allure.attach(self.driver.get_screenshot_as_png(), "登录截图",
                          allure.attachment_type.PNG)
        expect_url = 'http://119.29.235.245:9003/index.php/home/welcome'
        current_url = self.driver.current_url
        assert expect_url == current_url
