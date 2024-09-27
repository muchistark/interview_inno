from selenium.webdriver.common.by import By


class Scrapper:
    def __init__(self, driver):
        self.driver = driver

    def load(self, url):
        self.driver.get(url)

    def findone(self, selector):
        try:
            ele = self.driver.find_element(By.XPATH, selector)
        except Exception:
            ele = None
        return ele

    def findall(self, selector):
        try:
            ele = self.driver.find_elements(By.XPATH, selector)
        except Exception:
            ele = None
        return ele

    def find(self, ele, selector):
        try:
            ele = ele.find_element(By.XPATH, selector)
        except Exception:
            ele = None
        return ele

    def get_current_url(self):
        return self.driver.current_url
