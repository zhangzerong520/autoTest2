from selenium.webdriver.common.by import By

import Page
from Base.base import Base


class Login_Page(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    # 输入用户名
    def input_user(self, input_text):
        self.input_element(Page.user_id, input_text)

    # 输入密码
    def input_passwd(self, input_text):
        self.input_element(Page.passwd_id, input_text)

    # 记住密码
    def remember_passwd(self):
        self.click_element(Page.remember_id)

    # 登录按钮
    def login(self):
        self.click_element(Page.login_button)

    # 登录流程
    def test_login(self, user, passwd):
        self.input_user(user)
        self.input_passwd(passwd)
        self.remember_passwd()
        self.login()
