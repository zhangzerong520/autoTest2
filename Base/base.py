from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, timeout=10, poll=0.5):
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*locator))

    def click_element(self, locator):
        self.find_element(locator).click()

    def input_element(self, locator, text):
        ele = self.find_element(locator)
        ele.clear()
        ele.send_keys(text)

    def close_browser(self):
        self.driver.close()

    def open_browser(self, url):
        self.driver.get(url)
        self.driver.maximize_window()