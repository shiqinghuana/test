import pytest
import time


data = ['1','2','3','4']
@pytest.fixture(scope='class',params=data)
def haha(request):
    print('开始测试')
    #a = '5'
    a = request.param
    print(a == '1')
    yield a
    print('测试结束')



class Test_Case(object):

   # @pytest.mark.parametrize('haha', data, indirect=True)
    @pytest.mark.skipif(haha =='1',reason='dont test evev 2')
    def test_case(self,haha):

           # print(self.a,)
           # time.sleep(1)
            assert haha =='5','不是5'

   # @pytest.mark.parametrize('haha', data, indirect=True)
   # @pytest.mark.skipif(haha != '2', reason='dont test evev 2')
    def test_case2(self,haha):

            assert haha=='2','不是2'






if __name__ == '__main__':
    pytest.main(['-v','C:/Users/sunni/PycharmProjects/untitled4/package_test/l_pytest/','--junitxml=./reports.xml'])