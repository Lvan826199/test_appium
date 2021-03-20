from appium import webdriver
from appium_xueqiu_testframework.page.base_page import BasePage
from appium_xueqiu_testframework.page.main import Main


class App(BasePage):
    def start(self):
        if self._driver == None:
            print("setup_class")
            caps = {}
            caps["platformName"] = "Android"
            caps["platformVersion"] = "10.0.0"
            caps["deviceName"] = "HA17QKKD"
            caps["udid"] = "HA17QKKD"
            caps["appPackage"] = "com.xueqiu.android"
            caps["appActivity"] = ".view.WelcomeActivityAlias"
            caps["noReset"] = "True"
            caps["skipServerInstallation"] = True
            caps["skipDeviceInitialization"] = True
            # 中文输入
            caps["unicodeKeyboard"] = "True"  # 使用Unicode编码方式发送字符串
            caps["resetKeyBoard"] = "True"  # 隐藏键盘

            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        else:
            #launch_app()是appium提供的方法，可以直接启动你的应用[apppackage的包]
            self._driver.launch_app()
            #上面的launch_app相当于是区执行这个self.driver.start_activity(app_package=,app_activity=)

        self._driver.implicitly_wait(10)
        return self

    def restart(self):
        pass

    def stop(self):
        pass

    def main(self) -> Main:
        return Main(self._driver)