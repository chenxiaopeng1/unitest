# -*- coding: UTF-8 -*-
import unittest
from base.http_reqs import *
from data import oprate_excel
from data.get_data import *
from data.comparing_data import *
import json

#Testcase = '/Users/macbookair/Downloads/testcase.xlsx'
#sheetName = 'Testcase'

class RunTest:
    def __init__(self):
        self.Testcase=data_config.get_filepath()
        self.sheetName=data_config.get_sheetName()
        self.fp = OperateExcel(self.Testcase)
        self.data = GetData(self.Testcase, self.sheetName)
        self.reqs = http_reqs().reqs
        # self._type_equality_funcs = {}

    # 程序执行
    def test_run(self):
        res = None
        pass_count=[]
        fail_count=[]
        rows_count = self.data.get_lines(self.sheetName)
        for i in range(1, rows_count):
            if self.data.isrun(i) == False:
                continue
            elif self.data.isrun(i) == True:
                url = self.data.getUrl(i)
                headers = self.data.get_header(i)
                data = self.data.get_data(i)
                method = self.data.get_method(i)
                expect_result = self.data.get_expect_result(i)
                res = self.reqs(method, url, data, headers)
                # print(i,res.text)
                # print(int(expect_result))
                # print (type(res.status_code))
                str_status_code = str(res.status_code)
                result = Comparing_Data().is_match(str_status_code, expect_result)

                if result:
                    self.data.set_result(i, 'Pass')
                    pass_count.append(i)
                else:
                    self.data.set_result(i, res.text)
                    fail_count.append(i)

                try:
                    print(i, res.json())

                except Exception as e:
                    print(e)
                    print('返回结果为', res.text)
                # ecode=json.dumps(res.json())
                # print(type(ecode))
        print('Pass的 case为 ：',len(pass_count),'条，分别为',pass_count)
        print('Fail 的case为 ：',len(fail_count),'条，分别为',fail_count)



if __name__ == '__main__':
    rt = RunTest()
    rt.test_run()

