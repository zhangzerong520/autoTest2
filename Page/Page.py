from Page.login import Login_Page


class Page_Obj:
    def __init__(self, driver):
        self.driver = driver

    def Login_Page(self):
        return Login_Page(self.driver)

