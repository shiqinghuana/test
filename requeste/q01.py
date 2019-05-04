import requests
import json
import pytest
from time import sleep
import xlrd
import sys
from functools import wraps

def excel(xlsname='./02.xls',
          index=0):
    # xlsname = request.param
    print('xlsname', xlsname)
    try:
        table = xlrd.open_workbook(xlsname)
        sheet = table.sheet_by_index(index)
    except FileNotFoundError:
        print('There is no {} file currently. Exit after 3 seconds'.format(xlsname))
        sleep(0.1)
        sys.exit()
    lows = sheet.nrows
    cols = sheet.ncols
    # print(lows,cols)
    global data
    data = {}
    list = []
    for low in range(1, lows):
        for col in range(0, cols):
            key = sheet.cell(0, col).value
            value = sheet.cell(low, col).value
            data[key] = value
        list.append(data)
    return list

@pytest.fixture(params=excel('./02.xls',0))
def post(request):
    data = request.param
    base_url = 'http://v.juhe.cn/toutiao/index'
    rsp = requests.post(url=base_url, data=data)
    yield str(rsp.status_code)


def test_case(post):
    assert post == '200', '反问失败'


if __name__ == '__main__':
    pytest.main(['C:/Users/Administrator/PycharmProjects/untitled/123test/q01.py', '-v'])
