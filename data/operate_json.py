# -*- coding: UTF-8 -*-
import urllib.parse
import json
import requests
'''
dict1='data={"platform":1,"uid":"UWSKQH75eB4nrGdxDv31cMyCn4wM3kS3","lang":1,"traceId":"15024","productId":1000006617}'
str1='data: {%22platform%22:1,%22uid%22:%22UWSKQH75eB4nrGdxDv31cMyCn4wM3kS3%22,%22lang%22:1,%22traceId%22:%2215024%22,%22productId%22:1000006617}'
#str2='data: {"platform":1,"uid":"UWSKQH75eB4nrGdxDv31cMyCn4wM3kS3","lang":1,"traceId":"32172","sid":"e9671595-098c-49d8-993d-d5981ff57c79","entityIds":[1000006617],"type":1}'
str2='data= {"platform":1,"uid":"UWSKQH75eB4nrGdxDv31cMyCn4wM3kS3","lang":1,"traceId":"32172","entityIds":[1000006617],"type":1}'
host='http://apim.modernavenue.com/ma/api/306/1'

key='sid'
value='e9671595-098c-49d8-993d-d5981ff57c79'


if __name__=='__main__':
    str3=str2[5:]
    str3=json.loads(str3)
    #str2=json.dumps(str2)
    #print(urllib.parse.urlencode(str2))
    str3[key]=value

    str3=str(str3)
    #str2={'platform': 1, 'uid': 'UWSKQH75eB4nrGdxDv31cMyCn4wM3kS3', 'lang': 1, 'traceId': '32172', 'entityIds': [1000006617], 'type': 1}
    print(type(str3))
    str3='data='+str3
    #str3=str2[:5]+str3
    print(str3)


    res=requests.get(host,dict1)
    print(res.text)
'''

class opernationJson():
    def __init__(self):
        self.url='''http://apim.modernavenue.com'''
        self.data='''data={}'''

    #json转字符串,添加数据，组成新的字符串为请求数据
    def reqs_data(self,req_json):
        #req_json
        pass
