#coding:utf-8

from HTMLTestRunner_PY3 import HTMLTestRunner_PY3 as HTMLTestRunner
import unittest
from base.http_reqs import *
from data.comparing_data import *
from ddt import ddt



class ReportRunner(unittest.TestCase):
    def __init__(self):
        pass
    def setUp(self):
        self.Testcase=data_config.get_filepath()
        self.sheetName=data_config.get_sheetName()
        self.fp = OperateExcel(self.Testcase)
        self.data = GetData(self.Testcase, self.sheetName)
        self.reqs = http_reqs().reqs
        rows_count = self.data.get_lines(self.sheetName)

        self.setTestSuit()
        pass

    def tearDown(self):
        pass

    def makeCase(self,row):
        '''
        把一行的数据拼接成一条用例,参数为行号
        :return:
        '''
        url = self.data.getUrl(row)
        headers = self.data.get_header(row)
        data = self.data.get_data(row)
        method = self.data.get_method(row)
        expect_result = self.data.get_expect_result(row)
        res = self.reqs(method, url, data, headers)
        return res
        #str_status_code = str(res.status_code)
        #result = Comparing_Data().is_match(str_status_code, expect_result)

    def setTestSuit(self):
        '''
        把excel的用例添加到testSuit
        :return:  testSuit
        '''
        testsuite = unittest.TestSuite()

        for row in range(1,self.rows_count):
            if self.data.isrun(row) == False:
                continue
            elif self.data.isrun(row) == True:

                testcase=[].append()

    @ddt
    def testRunner(self):
        pass




if __name__=="__main__":
    print(">>>>>>>>>>>"*8)
    report_title = 'test用例执行报告'
    desc = '用于展示修改样式后的HTMLTestRunner'
    report_file = 'e:\\test.html'

    testsuite = unittest.TestSuite()
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestTest))
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(ExampleCase1))
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(ExampleCase2))
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(ExampleCase3))

    with open(report_file, 'wb') as report:
        runner = HTMLTestRunner(stream=report, title=report_title, description=desc)
        runner.run(testsuite)