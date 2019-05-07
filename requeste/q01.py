import requests
import pytest
from time import sleep
import xlrd
import sys


#pytestmark = pytest.mark.skipif(True,reason="all tests still WIP")
pexpect = pytest.importorskip("time")
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

#@pytest.fixture(scope='class')
@pytest.fixture(scope='function',params=excel())
def post(request):
    data = request.param

    base_url = 'http://v.juhe.cn/toutiao/index'
    rsp = requests.post(url=base_url, data=data)

    yield str(rsp.status_code)
    #print(rsp.status_code)



'''
def lala(request):
    #print('开始')
    f = open('01.txt','a')
    f.write('kaishi\n')
    yield request.param
    f.write('jiesu\n')
    f.close()
   # print('结束')
'''
data = [{'type':'top','key':'8dfc0c61b8a940f90e74e41dbaa9097d'},
        ]
class Test_Case01():
    #@pytest.mark.parametrize('post',data,indirect=True)
    def test_case(self,post):
        assert post == '200', '反问失败'

   # @pytest.mark.skipif(True, reason='skip')
    def test_case1(self,post):

        assert post == '201', '反问失败'

    def test_case2(self, post):
        assert post == '202', '反问失败'


if __name__ == '__main__':
    pytest.main(['C:/Users/Administrator/PycharmProjects/untitled/unit_practice/requeste/q01.py','-v'])
