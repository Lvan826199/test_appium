import time

from selenium.webdriver.common.by import By

from xueqiu_appium.page.base_page import BasePage

class Main(BasePage):
    def goto_search(self):
        time.sleep(3)
        # self.find(By.ID,'com.xueqiu.android:id/home_search').click()
        self.steps("../page/main.yaml")

    def go_to_windows(self):
        self.find(By.ID, "post_status").click()
        self.find(By.ID,'com.xueqiu.android:id/home_search').click()
