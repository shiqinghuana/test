import pytest
import time
import conftest


@pytest.fixture(scope='class')
def haha(request):
    print('开始测试')
    #a = '5'
    a = request.param['a']
    yield a
    print('测试结束')



class Test_Case(object):

    #@pytest.mark.parametrize('haha', data, indirect=True)
    def test_case(self,haha):
       # print(self.a,)
        time.sleep(1)
        assert haha =='5','不是5'


    def test_case2(self,haha):
        assert haha=='2','不是2'

    def test_case3(self):
        assert '2' == '1', '不是1'





if __name__ == '__main__':
    pytest.main(['C:/Users/sunni/PycharmProjects/untitled4/package_test/l_pytest/','--junitxml=./reports.xml'])