# -*- coding: UTF-8 -*-
import unittest
import json
#from urllib import parse as parse
#import urllib
import requests
from base.http_reqs_demo import my_send_reqs
from mock import mock
from base.mock_test import mock_test
'''
requests.adapters.DEFAULT_RETRIES = 5 # 增加重连次数
s = requests.session()
s.keep_alive = False # 关闭多余连接
'''
url='https://ynuf.aliapp.org/service/um.json'

data='data=ENCODE~~V01~~eyJ4diI6IjMuMy43IiwieHQiOiJGRkZGMDAwMDAwMDAwMTc5NjM0NjoxNTM0MzE2OTYzMjU4OjAuMzAxNzE5Mzg5NjU1ODAxNyIsImV0ZiI6ImIiLCJ4YSI6IkZGRkYwMDAwMDAwMDAxNzk2MzQ2Iiwic2l0ZUlkIjoiIiwidWlkIjoiIiwiZW1sIjoiQUEiLCJldGlkIjoiIiwiZXNpZCI6IiIsInR5cGUiOiJwYyIsIm5jZSI6dHJ1ZSwicGxhdCI6Ik1hY0ludGVsIiwibmFjbiI6Ik1vemlsbGEiLCJuYW4iOiJOZXRzY2FwZSIsIm5sZyI6InpoLUNOIiwic3ciOjQwMCwic2giOjYzNiwic2F3Ijo0MDAsInNhaCI6NjM2LCJic3ciOjEyNTAsImJzaCI6MzEzNiwiZWxvYyI6Imh0dHBzJTNBJTJGJTJGdGcudHVhbmRhaS5jb20lMkZ3ZWIlMkZSZWdpc3RlcjIwMTgwNDE2X2pkJTJGaW5kZXguYXNweCIsImV0eiI6NDgwLCJldHQiOjE1MzQzMTY5NjM1NDgsImVjbiI6IjgzYjA2MmNlNjI3YTAyNTU1NDI1OTljZWY3YjFmYzM5YjcwZDgzMTkiLCJlc3QiOjIsInhzIjoiMDcxMkYzMzI5MEFCOEE2REUyMjY3RDU2MUY2NDA4M0RENTY4REY4OEVDNzVFMjVFMjBCN0I1NDhBNzQ1MDEzQ0M2QUMxQjMyMThBNDM2MUJDRDQzQUQzRTc5NUM5MTRDOUUzRkIyOUIxNjU3MjM4MEE3RUQ2QTc0RkEyNTUzRDgiLCJtcyI6IjExNTMiLCJlcmQiOiJkZWZhdWx0LGM5MDI0NTYwYzZkYWY2MDEwNGMwZDdiNzNjZmY1YWMzY2FjNzg4OTljMzc5NjM5NGZlYmUwNTNlYTAyN2Q3OTMsNTg3N2NjN2Y4NDRmOWE4OTdlY2E5YmI5MGUyYzU5NmRhMzg5ODdhN2QzN2RmZjAyMzFhNWZkZmQxMGFlZDdmOSxkZWZhdWx0LGM5ZGEzYjdlNmNhNDg4ZWNhZDVkYjUwYTQyNWY0M2Q4YWY3ZjIyOWY1ZGRhZDBkZGRlMTVjMDc0OTVmNjE4OTUiLCJjYWNoZWlkIjoiYmYzNzg2M2U2MDc4OTFhMSIsInhoIjoiIiwiaXBzIjoiMTcxLjIyLjAuMjYiLCJlcGwiOjAsImVwIjoiZGEzOWEzZWU1ZTZiNGIwZDMyNTViZmVmOTU2MDE4OTBhZmQ4MDcwOSIsImVwbHMiOiIiLCJlc2wiOmZhbHNlfQ%3D%3Dum.json'

class mytest(unittest.TestCase):

    # 类方法只执行一次
    @classmethod
    def setUpClass(cls):
        print ("init login")

    def setUp(self):
        print("test--setup")
        self.msq=my_send_reqs()

    def tearDown(self):
        print("test--teardown")

    def test_my_send_reqs(self):

        print("这是第一个测试方法")

        '''
        mock_data=mock.Mock(return_value=data)
        print(mock_data)
        self.msq.send_reqs=mock_data
        '''
        res=mock_test(self.msq,url,'GET',data,data)
        #res.mock_data(self.msq,url,'GET',data,data)
        #res=self.msq.send_reqs(url,'GET',data)
        print(res)
        self.assertEqual(res,data)
        #self.assertEqual(res.status_code,200)
        #print(res.text)

    def test_second_method(self):
        print("这是第二个方法")
        print("do something")


if __name__=='__main__':
    print("---88888-----")
    unittest.TextTestRunner().run(my_send_reqs())
    print('main')