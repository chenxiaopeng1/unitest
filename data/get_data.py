# -*- coding: UTF-8 -*-
from data import data_config
from data.oprate_excel import OperateExcel
import logging
import urllib.parse

class GetData:

    def __init__(self,filepath,sheetName):
        self.oprateExcel=OperateExcel(filepath)
        self.sheetName=sheetName

    def get_lines(self,sheetName):
        lines= self.oprateExcel.get_lines(sheetName)
        return lines

    def isrun(self,row):
        col=data_config.get_isrun()
        isrun=self.oprateExcel.get_cell_Data(self.sheetName,row,col)
        if isrun=='no':
            return False
        else:
            return True

    def getUrl(self,row):
        col=data_config.get_url()
        url=self.oprateExcel.get_cell_Data(self.sheetName,row,col)
        return url

    def get_method(self,row):
        col=data_config.get_method()
        method=self.oprateExcel.get_cell_Data(self.sheetName,row,col)
        return method

    def get_header(self,row):
        col=data_config.get_header()
        headers=self.oprateExcel.get_cell_Data(self.sheetName,row,col)
        return headers

    def get_data(self,row):
        col=data_config.get_data()
        data=self.oprateExcel.get_cell_Data(self.sheetName,row,col).strip()
        return data

    def get_expect_result(self,row):
        col=data_config.get_expect()
        expect_result=self.oprateExcel.get_cell_Data(self.sheetName,row,col)
        return expect_result

    def set_result(self,row,value):
        '''写入 result 数据'''
        col=data_config.get_result()
        result=self.oprateExcel.set_velue(row,col,value)
        print("写入数据成功，位置为",row,col)

    #获取 dependent key 关联字段
    def get_depend_key(self,row):
        col=data_config.get_keyValue_depend()
        depend_key=self.oprateExcel.get_cell_Data(self.sheetName,row,col)
        if depend_key=='' or depend_key==None:
            return
        else:
            return depend_key

    #返回关联数据
    def get_depend_data(self,row):
        col=data_config.get_data_depend()
        depend_data=self.oprateExcel.get_cell_Data(self.sheetName,row,col)
        return depend_data

    def get_depend_case(self,row):
        col=data_config.get_case_depend()
        caseID=self.oprateExcel.get_cell_Data(self.sheetName,row,col)
        #depend_case=self.oprateExcel.getvelue_by_caseID(caseID)
        #return depend_case
        return caseID

    def getRowData(self,row):
        row_data=self.oprateExcel.getRowVelue_by_rowNum(row)
        return row_data
    '''
    #返回关联字段
    def get_depend_field(self,row):
        col=data_config.get_field_depend()
        depend_field=self.oprateExcel.get_cell_Data(self.sheetName,row,col)
        return depend_field
        '''






'''
if __name__=='__main__':
    oe=OperateExcel('/Users/macbookair/Downloads/testcase.xlsx')
    gd=GetData(filepath)
    print('dg初始化后')

    gd.isrun(1)

    print(gd.isrun(1))
'''