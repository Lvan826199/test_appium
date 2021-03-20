from appium import webdriver
from appium.webdriver import webelement
from appium.webdriver.common.mobileby import By
import logging

class BasePage():
    #弹框名单处理列表
    logging.basicConfig(level=logging.INFO)
    _black_list = [
        (By.XPATH,"//*[@text='确认']"),
        (By.XPATH,"//*[@text='下次再说']"),
        (By.XPATH,"//*[@text='确定']")
    ]

    _max_num = 3
    _error_num = 0


    def __init__(self,driver:webdriver=None):
        self._driver = driver


    def find(self,locator,value:str=None):
        #运行的时候就会打印日志
        logging.info(locator)
        logging.info(value)
        element:webelement
        try:

            element = self._driver.find_element(*locator) if isinstance(locator,tuple) else self._driver.find_element(locator, value)

            #判断locator是否是元组类型
            # if isinstance(locator, tuple):
            #     element = self._driver.find_element(*locator)
            # else:
            #     element = self._driver.find_element(locator,value)

            #如果元素被找到了就归零
            self._error_num = 0
            self._driver.implicitly_wait(10)

            return element

        except Exception as  e:
            #出现异常，将隐式等待设置小一点，快速的处理弹
            self._driver.implicitly_wait(1)
            #判断异常处理次数
            if self._error_num > self._error_num:
                raise e
            self._error_num += 1
            #处理弹框
            for ele in self._black_list:
                elelist = self._driver.find_elements(*ele)
                if len(elelist) >0:
                    elelist[0].click()
                    #弹框处理完成继续查找原本元素
                    return self.find(locator,value)
            raise e



