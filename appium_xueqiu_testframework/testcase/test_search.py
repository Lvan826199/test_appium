from appium_xueqiu_testframework.page.app import App

class TestSearch():
    def test_search(self):
        App().start().main().goto_market().goto_search().search()