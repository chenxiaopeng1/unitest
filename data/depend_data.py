# -*- coding: UTF-8 -*-
from data.get_data import *
from data.oprate_excel import *
from base.http_reqs import *
from jsonpath_rw import jsonpath,parse
import json
import time
import datetime

class RunCase:
    def __init__(self):
        self.filepath = data_config.get_filepath()
        self.sheetName = data_config.get_sheetName()
        self.fp = OperateExcel(self.filepath)
        self.data = GetData(self.filepath, self.sheetName)
        #self.http_reqs = http_reqs

    #运行当前的case ，如果有依赖，先运行依赖用例，然后在依赖用例中拿到相关的字段值
    def run_case(self, i):
        try:
            url = self.data.getUrl(i)
            headers = json.loads(self.data.get_header(i))
            data = json.loads(self.data.get_data(i))
            method = self.data.get_method(i)
            #expect_result = self.data.get_expect_result(i)
            depend_key=self.data.get_depend_key(i)

            if depend_key:
                #关联不为空，先拿到关联用例的结果
                depend_data=self.run_depend_case(i)
                data[depend_key]=depend_data

            res = reqs(method, url, data, headers)
            return res
        except IndexError as e:
            print(e)


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

    #根据caseID 运行对应的case，返回关联字段的值
    def run_case_by_caseID(self,caseID):
        #self.fp.getvelue_by_caseID(caseID)
        depend_row = self.fp.find_rows_by_ID(caseID)
        respon_Data = self.run_case(depend_row)
        return respon_Data

    #运行关联用例获取 关联data ，并回写到Excel中
    def run_depend_case(self,row,index=0):
        depend_key=self.data.get_depend_key(row)

        if depend_key==None or depend_key=="":
            return
        else:
            depend_case=self.data.get_depend_case(row) #读取当前行上记录的关联用例,拿到caseID
            depend_row=self.fp.find_rows_by_ID(depend_case) #根据当前行上关联用例的用例名 ，拿到对应的关联行号
            respon_Data=self.run_case(depend_row).json()   #运行关联用例
            #从返回的结果中，找到关联的关键字，返回关联字段的值
            col=data_config.get_data_depend()

            json_exe=parse(depend_key)
            key_set = json_exe.find(respon_Data)
            key_value=[math.value for math in key_set][index]
            self.fp.set_velue(row,col,key_value)
            #print('depend-case-result :',depend_key,key_value)
            return key_value
    '''
    #把关联到key的值加入到 row 中到用例的请求data，拼接后，再请求
    def runcase(self,row):
        depend_Data=self.run_depend_case(row)
        pass
    '''
    def getDependData(self,row):
        #根据行号运行对应的case后 ，根据key ，返回对应的值 ，要处理对应的值不存在的异常
        pass


if __name__ == '__main__':
    #print(time.strftime("%Y-%m-%d %H:%M:%S %f", time.localtime()))
    print(datetime.datetime.now().strftime('%H:%M:%S.%f'))
    dd = RunCase()
    dd.run_case(3)
    #print(time.strftime("%Y-%m-%d %H:%M:%S &f", time.localtime()))
    print(datetime.datetime.now().strftime('%H:%M:%S.%f'))
