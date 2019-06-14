import pytest
import xlwt, xlrd
from xlutils.copy import copy
import allure

# xs1 =r'C:\Users\sunni\Documents\Tencent Files\2244939288\FileRecv\MobileFile\交易所库存表(20190610) - 副本.xls'
# x1 = xlrd.open_workbook(xs1,formatting_info=True)
#
# xs2 = r'C:\Users\sunni\Documents\Tencent Files\2244939288\FileRecv\MobileFile\交易所库存表(20190610).xls'
# x2 = xlrd.open_workbook(xs2,formatting_info=True)
f = [
    [r'C:\Users\Administrator\Desktop\ceshi1.xls',
r'C:\Users\Administrator\Desktop\ceshi1 - 副本.xls']
]

@pytest.fixture(scope="function",params=f)
def get_excl(request):
    exl = request.param
    x1  = xlrd.open_workbook(exl[0])
    x2 = xlrd.open_workbook(exl[1])
    return (x1,x2)

@pytest.fixture()
def get_sheet(get_excl):
    sheet1 = get_excl[0].sheet_by_index(0)
    sheet2 = get_excl[1].sheet_by_index(0)
    return (sheet1,sheet2)
@pytest.fixture()
def get_low_coll(get_sheet):
    all_low1 = get_sheet[0].nrows  # 有效行
    all_col1 = get_sheet[0].ncols  # 有效列
    return (all_low1,all_col1)


liss=[]
def rs_low_col(get_low_coll):
    lis = []
    for i in range(get_low_coll[0]):
        for b in range(get_low_coll[1]):
            lis.append((i,b))
    liss.append( lis)

@pytest.fixture(scope="function",params=liss)
def low_col(request):
    return request.param

def a_cell(get_sheet,low_col):

        c1 = get_sheet[0].cell(low_col[0], low_col[1]).value
        c2 = get_sheet[1].cell(low_col[0], low_col[1]).value
        if c1 == c2:
            yield True
        else:
            yield low_col

def test_case(get_sheet,low_col,get_low_coll):
    """
    注释：对比两个execl
    """
    rs_low_col(get_low_coll)
    if a_cell(get_sheet,low_col) == True:
        assert 1==1
    else:
        assert 3==1,"正确：{}".format(a_cell(get_sheet,low_col))

if __name__ == '__main__':
    pytest.main(['-v','-q','./ceshifiles.py'])
