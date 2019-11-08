# -*- coding: UTF-8 -*-
import unittest
from data.comparing_data import *
from data.depend_data import *
import HTMLTestRunner_PY3


#Testcase = '/Users/macbookair/Downloads/testcase.xlsx'
#sheetName = 'Testcase'

class RunTest:
    def __init__(self):
        self.Testcase=data_config.get_filepath()
        self.sheetName=data_config.get_sheetName()
        #self.fp = OperateExcel(self.Testcase)
        self.data = GetData(self.Testcase, self.sheetName)


    def run_TestCase(self):
        pass_count=[]
        fail_count=[]
        rows_count = self.data.get_lines(self.sheetName)
        rc=RunCase()
        for i in range(1, rows_count):
            if self.data.isrun(i):
                res=rc.run_case(i)
                expect_result = self.data.get_expect_result(i)
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

        print('Pass的 case为 ：',len(pass_count),'条，分别为',pass_count)
        print('Fail 的case为 ：',len(fail_count),'条，分别为',fail_count)

if __name__ == '__main__':
    rt = RunTest()
    rt.run_TestCase()

