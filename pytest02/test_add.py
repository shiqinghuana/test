import pytest

def add(a):
    if a%2 ==0:
        print('{}是偶数'.format(a))
        return True
    else:
        print('{}是奇数'.format(a))
        return False

class Test_Add():
   # @pytest.mark.parametrize('data',indirect=True)
    def test_case(self,data):
        assert add(data) == True



if __name__ == '__main__':
    pytest.main(['C:/Users/sunni/PycharmProjects/untitled4/package_test/pytest02'])