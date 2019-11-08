# -*- coding: UTF-8 -*-
import requests,json

def reqs(method,url,data=None,headers=None):

        if type(data)==str:
            data=json.loads(data)

        if method=='post':
            res=requests.post(url,data=data,headers=headers,verify=False)
        elif method=='get':
            res=requests.get(url,data,headers=headers)
        return res


if __name__=="__main__":
    method="get"
    url="https://apiv2.pinduoduo.com/api/gindex/subject/limited/goods"
    data='''{"subject_id":"5571","page":"1","size":"3"}'''
    headers='''{"content-type": "application/x-www-form-urlencoded",
             "Origin":"https://m.pinduoduo.com",
             "Referer":"https://m.pinduoduo.com/home/",
             "Sec-Fetch-Mode": "cors",
             "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}'''

    res=reqs(method,url,json.loads(data),json.loads(headers))
    print(res.text)


