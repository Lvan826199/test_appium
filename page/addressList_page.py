import time

from appium.webdriver.common.mobileby import MobileBy
from page.base_page import BasePage
from page.member_invite_page import MemberInvitePage


class AddressList(BasePage):

    def add_member(self):
        time.sleep(1)
        self.find(MobileBy.XPATH, '//*[@text="添加成员"]').click()
        return MemberInvitePage(self._driver)

    # def get_toast(self):
    #     print(self._driver.page_source)
    #     return self.find(MobileBy.XPATH, '//*[@text="添加成功"]').text
    #     # return "toast"