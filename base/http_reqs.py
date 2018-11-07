# -*- coding: UTF-8 -*-
import requests

class http_reqs():
    def http_post(self,url,data,headers=None):
        res=None
        if headers!=None:
            res=requests.post(url,data,headers)
        else:
            res=requests.post(url,data)
        return res


    def http_get(self,url,data=None,headers=None):

        res=None
        if headers==None or headers=='':
            res=requests.get(url,data)
        else:
            res=requests.get(url,data,headers)
        return res

    def reqs(self,method,url,data=None,headers=None):
        res=None
        if method=='post':
            res=self.http_post(url,data,headers)
        elif method=='get':
            res=self.http_get(url,data,headers)
        return res