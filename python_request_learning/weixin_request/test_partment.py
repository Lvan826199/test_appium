import requests


def test_token():
    corpid = "wwc1d0ddd580034c52"
    corpsecret = "FnPFMpcCM_LYi76qzGQ0FCk11hRqs-NPVyhfU5Mi8Jk"
    r= requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}")
    token = r.json()["access_token"]
    return token

#创建部门
def test_creat():
    token = test_token()
    data = {
   "name": "广州研发中心",
   "parentid": 1
    }
    res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={token}",json=data)
    print(res.text)

def test_update():
    token = test_token()
    data = {
   "id": 2,
   "name": "小仔研究所"
}
    res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={token}", json=data)
    print(res.text)
