import requests

class Work():
    def boss(self):
        query = '测试工程师'
        r = requests.get(f"https://www.zhipin.com/job_detail/?query={query}&city=101020100&industry=&position=")
        print(r.text)
        # print(r.json())

    def lagou(self):
        query = '测试工程师'

        url = f"https://www.lagou.com/jobs/list_{query}?labelWords=&fromSearch=true&suginput="
        r = requests.get(url)
        print(r.text)

if __name__ == '__main__':
    r = Work()
    r.boss()