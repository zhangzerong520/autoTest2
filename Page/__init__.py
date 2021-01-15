from selenium.webdriver.common.by import By

'''
   登录页面
'''
# 用户框
user_id = (By.ID, 'inputAccount')
# 密码框
passwd_id = (By.ID, 'inputPassword')
# 勾选框
remember_id = (By.ID, 'remember')
# 登录按钮
login_button = (By.XPATH, '/html/body/div/form/button')

'''
   邮件页面
'''