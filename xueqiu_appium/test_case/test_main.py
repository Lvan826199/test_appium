import yaml

from xueqiu_appium.page.app import App
import pytest

from xueqiu_appium.test_case.test_base import TestBase


class TestMain(TestBase):
    '''
    yaml：https://www.runoob.com/w3cnote/yaml-intro.html
    '''
    @pytest.mark.parametrize("value1,value2",yaml.safe_load(open("./test_main.yaml")))
    def test_main(self,value1,value2):
        self.app.start().main().goto_search()
        print(value1)
        print(value2)

    def test_windows(self):
        self.app.start().main().go_to_windows()