# -*- coding: UTF-8 -*-
from data.get_data import *
from data.oprate_excel import *
from base.http_reqs import *
from jsonpath_rw import jsonpath,parse

class DependData:
    def __init__(self):
        self.Testcase = data_config.get_filepath()
        self.sheetName = data_config.get_sheetName()
        self.fp = OperateExcel(self.Testcase)
        self.data = GetData(self.Testcase, self.sheetName)
        self.reqs = http_reqs().reqs

    def RowData(self,i):
        row_data=self.fp.getRowVelue_by_rowNum(i)
        return row_data


    def run_case(self, i):
        if i in range(self.fp.get_lines(self.sheetName)):
            # print(self.fp.get_lines(self.sheetName))
            url = self.data.getUrl(i)
            headers = self.data.get_header(i)
            data = self.data.get_data(i)
            method = self.data.get_method(i)
            expect_result = self.data.get_expect_result(i)

            #先转化为json，拼接后，再返回整个请求值（未写）
            #print(url.unquote(data))
            print(type(data))
            req_data=data+str(self.run_depend_case(i))


            res = self.reqs(method, url, req_data, headers)
            print('i= ',i)
            print('result ==', res.json())
            return res.json()
        else:
            print('输入的行数大于Excel 中的行数，请检查后再试')

    '''
    #根据key，从依赖case的运行结果中获取对应数据
    def get_data_for_key(self,row):
        depend_key=self.data.get_depend_key(row)
        if depend_key==None:
            print('depend_key=',depend_key)
            return None
        else:

            respon_Data=self.run_case(row)
            json_exe=parse(depend_key)
            key_set=json_exe.find(respon_Data)
            [math.value for math in key_set][0]
            print([math.value for math in key_set][0])
            '''

    #根据caseID 运行对应的case
    def run_case_by_caseID(self,caseID):
        #self.fp.getvelue_by_caseID(caseID)
        depend_row = self.fp.find_rows_by_ID(caseID)
        respon_Data = self.run_case(depend_row)
        return respon_Data

    #运行关联用例获取 关联data ，并回写到Excel中
    def run_depend_case(self,row):
        depend_key=self.data.get_depend_key(row)
        if depend_key==None:
            print('key=None')
            return None
        else:
            depend_case=self.data.get_depend_case(row)
            depend_row=self.fp.find_rows_by_ID(depend_case)
            respon_Data=self.run_case(depend_row)
            col=data_config.get_data_depend()
            print('col=',col)
            json_exe=parse(depend_key)
            key_set = json_exe.find(respon_Data)
            key_value=[math.value for math in key_set][0]
            self.fp.set_velue(row,col,key_value)
            print('depend-case-result == ',key_value)
            return key_value

    #把关联到key到值加入到 row 中到用例的请求data，拼接后，再请求
    def runcase(self,row):
        depend_Data=self.run_depend_case(row)


        pass



if __name__ == '__main__':
    dd = DependData()
    #dd.run_case_by_caseID()
    dd.run_depend_case(5)



