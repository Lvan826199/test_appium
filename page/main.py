import time

from appium.webdriver.common.mobileby import MobileBy
from page.base_page import BasePage
from page.addressList_page import AddressList

class Main(BasePage):


    def goto_message(self):
        pass

    def goto_addresslist(self):
        time.sleep(3)
        self.find(MobileBy.XPATH, '//*[@text="通讯录"]').click()

        return AddressList(self._driver)

    def goto_workbench(self):
        pass

    def goto_profile(self):
        pass
