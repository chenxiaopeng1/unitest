# -*- coding: UTF-8 -*-
from data import data_config
from data.get_data import *
from data.oprate_excel import *
class Comparing_Data:

    '''

    def get_result(self):
        pass

    def get_expect(self,row):
        filepath=data_config.get_filepath()
        sheetName=data_config.get_sheetName()
        print(filepath,sheetName)
        expect=GetData(filepath,sheetName).get_expect_result(row)
        return expect
    '''


    def is_match(self, result, expect):
        if expect == result:
            print('测试通过')
            return True
        else:
            print('测试失败')
            return False



if __name__=='__main__':

    print('哇咔咔')
#cd=comparing_data().get_expect(1)