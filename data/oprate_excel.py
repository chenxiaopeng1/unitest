#coding:utf-8
import xlwt,xlrd
from data import data_config
from xlutils.copy import copy
import logging

class OperateExcel(object):

    #初始化读取数据
    def __init__(self,filepath):
        self.filepath=data_config.get_filepath()
        self.sheetName=data_config.get_sheetName()
        self.data=xlrd.open_workbook(filepath)

    #获取excel的所有表 名称
    def get_sheetsNames(self):
        sheetsNames=self.data.sheet_names()
        return sheetsNames

    #获取同一行多个单元格的数据,sheetsName 为某一个子表格的名字，sheet_id 为格子的坐标，如[3,2]
    def get_rowsValues(self,sheetsName,row,col):
        rowsValues=self.data.sheet_by_name(sheetsName).row_values(row,col)
        return  rowsValues


    #获取行数
    def get_lines(self,sheetName=None):
        lines= self.data.sheet_by_name(sheetName).nrows
        return lines

    #获取列数
    def get_clos(self,sheetName=None):
        return  self.data.sheet_by_name(sheetName).ncols

    #获取某一个格子的数据
    def get_cell_Data(self,sheetName,row,col):
        tables=self.data.sheet_by_name(sheetName)
        cellValues=tables.cell_value(row,col)
        return cellValues

    #写入单元格内容
    def set_velue(self,row,col,value):
        '''写入excel数据'''
        try:
            logging.info('Writing sheet_value...')
            read_data=xlrd.open_workbook(self.filepath) #formatting_info=True
            write_data=copy(read_data)
            sheet_value=write_data.get_sheet(self.sheetName)
            sheet_value.write(row,col,value)
            write_data.save(self.filepath)
        except Exception as e:
            logging.error('Write sheet_value Fail...')
            #logging(e)


    #根据caseID找到相关的行号index ,行号=index+1
    def find_rows_by_ID(self,caseID):
        cols_data=self.data.sheet_by_name(data_config.get_sheetName()).col_values(data_config.get_id())
        rowNum=cols_data.index(caseID)
        #print('rowNum=',rowNum)
        return rowNum



    #根据行号获取整行的内容
    def getRowVelue_by_rowNum(self,row):
        table=self.data
        row_Data=table.sheet_by_name(data_config.get_sheetName()).row_values(row)
        print(row_Data)
        return row_Data

    #根据caseID 查找到对应的内容
    def getvelue_by_caseID(self,caseID):
        row=self.find_rows_by_ID(caseID)
        row_data=self.getRowVelue_by_rowNum(row)
        print(row_data)
        return row_data

    #获取整列的内容
    def get_col_data(self,col_id=None):
        if col_id !=None:
            col_values=self.data.sheet_by_name(data_config.get_sheetName()).col_values(col_id)
        else:
            col_values=self.data.sheet_by_name(data_config.get_sheetName()).col_values(0)
        return col_values



if __name__=='__main__':
    op=OperateExcel(data_config.get_filepath())
    print(type(op.get_lines(data_config.get_sheetName())))
    op.getRowVelue_by_rowNum(3)
    op.find_rows_by_ID('用例1')
    #print(op.get_cell_Data(data_config.get_sheetName(),3,8))