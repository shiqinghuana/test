import pytest
import time
@pytest.fixture(scope='class')
def haha():
    print('开始测试')
    a = '5'
    yield a
    print('测试结束')



class Test_Case(object):

    def test_case(self,haha):
       # print(self.a,)
        time.sleep(1)
        assert haha =='4','不是5'

    def test_case2(self,haha):
        assert haha =='2','不是2'

    def test_case3(self):
        assert '2' == '1', '不是1'




if __name__ == '__main__':
    pytest.main(['C:/Users/Administrator/PycharmProjects/untitled/unit_practice','--html=./report.html','--self-contained-html'])