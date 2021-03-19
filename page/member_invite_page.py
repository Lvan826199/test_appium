from appium.webdriver.common.mobileby import MobileBy

from page.base_page import BasePage


class MemberInvitePage(BasePage):


    def addmember_by_manul(self):
        from page.conntat_add import ContactAddPage
        self._driver.find_element(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
        return ContactAddPage(self._driver)

    def get_toast(self):
        print(self._driver.page_source)
        return self.find(MobileBy.XPATH, '//*[@text="添加成功"]').text
        # return "toast"
