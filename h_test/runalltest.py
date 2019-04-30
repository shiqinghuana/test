import unittest
import HTMLTestRun



if __name__ == '__main__':

    discover =unittest.defaultTestLoader.discover('./','test_*.py')
    print(discover)
    with open('./report/resurt.html','wb') as  f:

        runner = HTMLTestRun.HTMLTestRunner(stream=f,
                                            title='my test',
                                            verbosity= 2,
                                            description=' resourt')
        runner.run(discover)