import requests
from jsonpath import jsonpath
class TestDemo:
    def test_get(self):
        r = requests.get('http://httpbin.testing-studio.com/get')
        # print(r.status_code) #200
        # print(r)  #<Response [200]>
        # print(r.text)  #响应文本
        # print(r.json())   #json格式的响应文本
        assert r.status_code == 200


    def test_query(self):
        payload = {
            "level":1,
            "name":"xiaozai"
        }
        r = requests.get('http://httpbin.testing-studio.com/get',params=payload)
        print(r.text)
        assert r.status_code == 200

    def test_post_form(self):
        payload = {
            "level":1,
            "name":"xiaozai"
        }
        r = requests.post('http://httpbin.testing-studio.com/post',data=payload)
        print(r.text)
        assert r.status_code == 200

    def test_headers(self):

        r = requests.get('http://httpbin.testing-studio.com/get',headers = {"Myname":"xiaozainiupi"} )
        print(r.text)
        assert r.status_code == 200
        assert r.json()["headers"]["Myname"] == "xiaozainiupi"

    def test_post_json(self):
        payload = {
            "level": 1,
            "name": "xiaozai"
        }
        r = requests.post('http://httpbin.testing-studio.com/post', json=payload)
        print(r.text)
        assert r.status_code == 200


    def test_xiao_json(self):
        from jsonpath import jsonpath
        r = requests.get('http://home.testing-studio.com/categories.json')
        print(r.text)
        assert r.status_code == 200
        assert r.json()["category_list"]["categories"][0]["name"] == "开源项目"
        assert jsonpath(r.json(),'$..name')[0] == "开源项目"
