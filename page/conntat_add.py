from appium.webdriver.common.mobileby import MobileBy
from page.base_page import BasePage

class ContactAddPage(BasePage):

    def input_name(self):
        name_element = self.find(MobileBy.XPATH,
                                                '//*[@text="姓名　"]/..//*[@class="android.widget.EditText"]')
        name_element.send_keys("麦乐")
        return self

    def set_gender(self):
        gender = self.find(MobileBy.XPATH,
                                          '//*[@text="性别"]/..//*[contains(@class,"TextView") and @text="男"]')
        gender.click()
        self.find(MobileBy.XPATH, '//*[@text="女"]').click()
        return self

    def input_phonenum(self):
        telephone = self.find(MobileBy.XPATH,
                                             '//*[@text="手机　"]/..//*[contains(@class,"EditText")]')
        telephone.send_keys("18812348580")
        return self

    def click_save(self):
        #页面互相调用使用局部导入
        from page.member_invite_page import MemberInvitePage
        self.find(MobileBy.ID, 'com.tencent.wework:id/aj_').click()

        return MemberInvitePage(self._driver)