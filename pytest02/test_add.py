import pytest
#from unit_practice.pytest02 import conftest
def add(a):
    if a%2 ==0:
        print('{}是偶数'.format(a))
        return True
    else:
        print('{}是奇数'.format(a))
        return False
#data  =conftest.data
test1 = [1, 2]
class Test_Add():

    #@pytest.mark.parametrize('a',test1,ids=["0", "1"])
    def test_case(self,data):
        assert add(data) == True

# data = {
#         i=haha
#         from=AUTO,
#         to=AUTO,
#         smartresult=dict,
#         client=fanyideskweb,
#         salt=15590530599175,
#             =15590536631920
#         sign=6f86c6876471aa95ebeba9e4a491eda1,

#         ts=1559053059917,
#         bv=d39271655f6b7da338c7d58f74b0fad8,
#         doctype=json,
#         version=2.1,
#         keyfrom=fanyi.web,
#         action=FY_BY_REALTlME,
# }
import requests
import json
import random

host = "http://httpbin.org/"
endpoint = "headers"
url = "http://httpbin.org/headers"



UseAgent = ['Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36',
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60",
                "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
                "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16"]
header = {
        'User-Agent':random.choices(UseAgent)[0],
'Accept-Encoding': 'sss',
'Connection':"123",
    "yesy1":"bbb"
    }

header1 = {

"test":"aaa"
    }

session = requests.Session()
session.headers.update(header)
h = session.get(url,headers=header1)
print(h.text)
session.headers["yesy1"] = None
h = session.get(url,headers=header1)
print(h.text)
if __name__ == '__main__':
    # pytest.main(['C:/Users/Administrator/PycharmProjects/untitled/unit_practice/pytest02/','-v'])
    # print(html.status_code)
    # print(html.text)
    pass