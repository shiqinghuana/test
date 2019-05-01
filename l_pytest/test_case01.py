import pytest



class Test_Case(object):
    @pytest.fixture(scope='class')
    def setup(self):
        print('开始测试!!!!!')
    def a(self):
        self.a = '5'
        return self.a
    def test_case1(self):
        print(self.a,)
        assert self.a() =='5','不是5'

    def test_case2(self):
        assert self.a() =='2','不是2'

    def test_case3(self):
        assert self.a() == '1', '不是1'

    @pytest.fixture()
    def tear_down(self):
        print('结束测试!!!!')



if __name__ == '__main__':
    p =Test_Case()
    print(p.a()=='5')
    pytest.main()