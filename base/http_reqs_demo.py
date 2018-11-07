# -*- coding: UTF-8 -*-
from datetime import datetime
import requests
import json
# import urllib.parse
import ssl

now = datetime.now()  # 获取当前datetime
print(now)
dt = datetime(2015, 4, 19, 12, 20)
dt.timestamp()

print(dt)

# ssl._create_default_https_context = ssl._create_unverified_context

#   https://m.jd.com/index/msgCenter.json?randomKey=1534154194307
url = 'https://m.jd.com/index/msgCenter.json'

data = {
    "randomKey": 1534154194307
}


class my_send_reqs(object):
    def __init__(self):
       print("-----init------")

    def send_get(self,url, data=None):
        print(url)
        res = requests.get(url, data)
        return res

    def send_post(self,url, data):
        res = requests.post(url, data)
        return res

    def send_reqs(self,url, method, data=None):
        print(method)
        if method == 'GET':
            res =self.send_get(url, data)
        elif (method == 'POST'):
            res = self.send_post(url, data)
        print(res)
        # self.prn_obj(res)
        return res



if __name__ == '__main__':

    sr = my_send_reqs()
    result = sr.send_reqs(url, 'GET', json.dumps(data))
    print(result.text)
    print(result.status_code)
