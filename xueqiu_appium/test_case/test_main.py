import yaml

from xueqiu_appium.page.app import App
import pytest

class TestMain():
    '''
    yaml：https://www.runoob.com/w3cnote/yaml-intro.html
    '''
    @pytest.mark.parametrize("value1,value2",yaml.safe_load(open("./test_main.yaml")))
    def test_main(self,value1,value2):
        app =App()
        app.start().main().goto_search()
        print(value1)
        print(value2)

    def test_windows(self):
        app=App()
        app.start().main().go_to_windows()