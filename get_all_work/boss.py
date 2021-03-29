import time

from selenium import  webdriver

class TestTesterHome(object):
    def setup(self):
        self.driver = webdriver.Firefox()
        #也可以指定的目录下放exe
        #self.driver = webdriver.Firefox(executable_path=r"写入你exe的地址")
        self.driver.implicitly_wait(10)
        query = '测试工程师'
        self.driver.get(f"https://www.zhipin.com/job_detail/?query={query}&city=101020100&industry=&position=")

    def test_mtsc2019(self):
        list = []
        for i in range(4):
            i=i+1
            #document.documentElement.scrollTop = 3000
            # 点击完之后想要滑动到屏幕的最底端，然后点击下一页
            self.driver.execute_script("document.documentElement.scrollTop = 4000")
            time.sleep(5)
            self.driver.find_element_by_link_text(f'{i}').click()
        # text = self.driver.find_element_by_xpath('//*[@id="main"]/div/div[3]')
        # print(text.text)