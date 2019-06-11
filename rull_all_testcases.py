import unittest
import time
from request_w import HTMLTestReport
import os
from request_w import test_exls



if __name__ == '__main__':
    current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))  # 生成报告的时间
    # case_path = os.getcwd()    # 用例路径    os.getcwd()代表返回当前工作目录
    case_path = "./"  # 设置指定路径
    report_path = os.path.join(case_path, 'report_' + current_time + ".html")  # 报告存放路径
    fp = open(report_path, "wb")
    # 构建测试套件
    testunit = unittest.TestSuite()
    testunit.addTest(test_exls.A_x("test_case"))

    # 用网页的形式显示测试报告
    runner = HTMLTestReport.HTMLTestRunner(stream=fp, title="自动化测试报告", description='关于H6项目接口测试报告', tester='韩宝俊')
    runner.run(testunit)
    fp.close()
