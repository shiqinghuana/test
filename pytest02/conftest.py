import pytest

test1 = [1, 2, 3, 4, 5, 6, 7, 8]


@pytest.fixture(scope='class', params=test1)
def data(request):
    print('开始测试')
    yield request.param
    print('结束测试')
