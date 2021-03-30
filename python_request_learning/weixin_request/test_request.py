import requests


def test_get_token():
    #根据企业微信官方文档书写
    # https://open.work.weixin.qq.com/api/doc/90000/90135/91039
    corpid = "wwc1d0ddd580034c52"
    corpsecret = "FnPFMpcCM_LYi76qzGQ0FCk11hRqs-NPVyhfU5Mi8Jk"
    r= requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}")
    # 获取token值
    token = r.json()["access_token"]
    return token

#获取通讯录成员
def test_get():
    token = test_get_token()
    res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid=YuYu")
    print(res.text)

#创建成员
def test_creat():
    token = test_get_token()
    data = {
    "userid": "zhangsan",
    "name": "张三",
    "mobile": "13800000000",
    "department": [1],
    "position": "产品经理",
    }
    res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}",json=data)
    print(res.text)
