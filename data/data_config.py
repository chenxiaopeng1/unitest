# -*- coding: UTF-8 -*-

class global_var():
    # case_id
    id = 0
    url = 1
    isrun = 2
    method = 3
    header = 4
    case_depend = 5
    data_depend = 6
    keyValue_depend = 7
    data = 8
    result = 9
    expect = 10
    iscorrect = 11

def get_filepath():
    filepath='E:\\APItest\\unitest\\excel\\testcase.xlsx'
    return filepath

def get_sheetName():
    sheetName='Testcase'
    return sheetName


def get_id():
    return global_var.id


def get_url():
    return global_var.url


def get_isrun():
    return global_var.isrun


def get_method():
    return global_var.method


def get_header():
    return global_var.header


def get_case_depend():
    return global_var.case_depend


def get_data_depend():
    return global_var.data_depend


def get_keyValue_depend():
    return global_var.keyValue_depend


def get_data():
    return global_var.data


def get_result():
    return global_var.result


def get_expect():
    return global_var.expect


def get_iscorrect():
    return global_var.iscorrect
