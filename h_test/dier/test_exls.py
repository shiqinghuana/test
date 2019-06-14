import pytest
import xlwt, xlrd
from xlutils.copy import copy
import unittest

xs1 = r'C:\Users\Administrator\Documents\Tencent Files\2244939288\FileRecv\MobileFile\交易所库存表(20190610) - 副本.xls'
x1 = xlrd.open_workbook(xs1, formatting_info=True)

xs2 = r'C:\Users\Administrator\Documents\Tencent Files\2244939288\FileRecv\MobileFile\交易所库存表(20190610).xls'
x2 = xlrd.open_workbook(xs2, formatting_info=True)

# 获取样本文件第一张表
sheet1 = x1.sheet_by_index(0)
all_low1 = sheet1.nrows  # 有效行
all_col1 = sheet1.ncols  # 有效列
# 获取对比文件第一张表
sheet2 = x2.sheet_by_index(0)
wb = copy(x2)


# all_low2 = sheet1.nrows
# all_col2 = sheet1.ncols
@pytest.fixture(scope='function', params=[i for i in range(0, all_low1)])
def lows(request):
    a = request.param
    yield a


@pytest.fixture(scope='function', params=[i for i in range(0, all_col1)])
def colls(request):
    b = request.param
    yield b

def a_cell(low, coll):
    c1 = sheet1.cell(low, coll).value
    c2 = sheet2.cell(low, coll).value
    if c1 == c2:
        return True
    else:
        return low, coll

class A_x(unittest.TestCase):
    def test_case(lows, colls):
        if a_cell(lows, colls) == True:
            assert 1 == 1
        else:
            ws = wb.get_sheet(0)
            c1 = sheet1.cell(lows, colls).value
            c2 = sheet2.cell(lows, colls).value
            ws.write(lows, colls, c2 + "|" + c1)
            wb.save(xs2)
            assert 3 == 1


if __name__ == '__main__':
    pytest.main(['-v', 'C:/Users/Administrator/PycharmProjects/untitled/unit_practice/1exls.py'])
