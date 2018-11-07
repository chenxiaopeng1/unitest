# -*- coding: UTF-8 -*-
from mock import mock


def mock_test(mock_method, url, method, request_data, respon_data):
    mock_method=mock.Mock(return_value=respon_data)
    res=mock_method(url,method,request_data,respon_data)
    return res
