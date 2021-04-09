import requests
import base64
import json

# def test_encode():
#     url = "http://127.0.0.1:9999/demo1.txt"
#     r = requests.get(url=url)
#     #解密接口返回的内容
#     res = json.loads(base64.b64decode(r.content))
#     print(res)

class ApiRequests():

    def __init__(self):
        pass

    req_data = {
        "method": "get",
        "url": "http://127.0.0.1:9999/demo1.txt",
        "headers": None,
        "encoding": "base64"
    }

    def send(self,data:dict):
        res = requests.request(data["method"],data["url"],headers = data["headers"])
        if data["encoding"] == "base64":
            return  json.loads(base64.b64decode(res.content))
        #把加密过后的响应值发给第三方服务.让第三方去做解密然后返回
        elif data["encoding"] == "private":
            return requests.post("url",data = res.content)

