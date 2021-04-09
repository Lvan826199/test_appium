import requests
import yaml

'''
在请求之前，对请求的url进行替换
1。需要二次封装requests，对请求进行定制化。
2。将请求的结构体的url从一个写死的ip地址改为一个(任意的)域名。
3。使用一个env配置文件，存放各个环境的配置信息。
4。然后将请求结构体中的url替换为`env`配置文件中个人选择的url。
5。将env配置文件使用yaml进行管理。
'''

class Api:

    data = {
        "method": "get",
        "url": "http://127.0.0.1:9999/demo1.txt",
        "headers": None,
    }

    # env = {
    #     "default":"dev",
    #     "testing":
    #     {
    #     "dev" : "127.0.0.1",
    #     "test" : "127.0.0.2"
    #      }
    # }
    env = yaml.safe_load(open("env.yaml"))

    def send(self,data:dict):
        data['url'] = str(data['url']).replace("127.0.0.1",self.env["testing"][self.env["default"]])
        requests.request(method=data['method'],url=data["url"],headers=data["headers"])

