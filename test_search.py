#coding=utf-8
import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestWeChat():
    def setup_class(self):
        print("setup_class")
        caps = {}
        caps["platformName"] = "Android"
        caps["platformVersion"]= "10.0.0"
        caps["deviceName"] = "HA17QKKD"
        caps["udid"] = "HA17QKKD"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = "com.tencent.wework.launch.LaunchSplashActivity"
        caps["noReset"] = "True"
        caps["skipServerInstallation"] = True
        caps["skipDeviceInitialization"] = True
        #中文输入
        caps["unicodeKeyboard"] = "True" #使用Unicode编码方式发送字符串
        caps["resetKeyBoard"] = "True" #隐藏键盘

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub",caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()


    def test_addcontact(self):
        print("添加联系人")
        time.sleep(3)
        self.driver.find_element(MobileBy.XPATH,'//*[@text="通讯录"]').click()
        self.driver.find_element(MobileBy.XPATH,'//*[@text="添加成员"]').click()
        self.driver.find_element(MobileBy.XPATH,'//*[@text="手动输入添加"]').click()
        # self.driver.find_element(MobileBy.XPATH,'//*[@text="完整输入"]').click()

        #查找姓名旁边的那个输入框，先找到姓名，然后找到姓名的父节点，再通过父节点找到下边的class子节点的输入框
        name_element = self.driver.find_element(MobileBy.XPATH,'//*[@text="姓名　"]/..//*[@class="android.widget.EditText"]')
        name_element.send_keys("莉莉")
        gender = self.driver.find_element(MobileBy.XPATH,'//*[@text="性别"]/..//*[contains(@class,"TextView") and @text="男"]')
        gender.click()
        self.driver.find_element(MobileBy.XPATH,'//*[@text="女"]').click()
        telephone = self.driver.find_element(MobileBy.XPATH,
                                                '//*[@text="手机　"]/..//*[contains(@class,"EditText")]')
        telephone.send_keys("18812348880")

        #保存
        self.driver.find_element(MobileBy.ID,'com.tencent.wework:id/aj_').click()

        #获取页面信息，获取toast元素
        time.sleep(2)
        print(self.driver.page_source)
        # #添加成功有个添加成功的toast
        # self.driver.find_element(MobileBy.ID,'//*[@text="添加成功"]')

    def testing(self):
        print("the home work pycharm ")







