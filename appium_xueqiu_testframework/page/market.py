from selenium.webdriver.common.by import By

from appium_xueqiu_testframework.page.base_page import BasePage
from appium_xueqiu_testframework.page.search import Search


class Market(BasePage):
    def goto_search(self):
        #click
        self.find(By.XPATH,"//*[@resource-id='com.xueqiu.android:id/action_search']").click()
        return Search(self._driver)