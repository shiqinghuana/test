import unittest


'''

unittest 框架实例
'''


class tui(unittest.TestCase):

    def setUp(self):
        print('开始测试')

        self.number = 10
        self.number = int(self.number)

    def test_case1(self):
        self.assertEqual(self.number, 10, msg='you input is not 10')

    def test_case2(self):
        self.assertEqual(self.number, 5, msg='you input is not 5')

    def test_case3(self):
        self.assertEqual(self.number, 2, msg='you input is not 2')

    def tearDown(self):
        print('测试结束')

