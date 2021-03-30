import requests


def test_demo():
    #根据企业微信官方文档书写
    # https://open.work.weixin.qq.com/api/doc/90000/90135/91039
    corpid = "wwc1d0ddd580034c52"
    corpsecret = "FnPFMpcCM_LYi76qzGQ0FCk11hRqs-NPVyhfU5Mi8Jk"
    r= requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}")
    # print(r.text)
    print(r.json()["access_token"])