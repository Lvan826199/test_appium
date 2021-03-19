import time

from selenium.webdriver.common.by import By

from xueqiu_appium.page.base_page import BasePage

class Main(BasePage):
    def goto_search(self):
        time.sleep(5)
        self.find(By.ID,'com.xueqiu.android:id/home_search').click()