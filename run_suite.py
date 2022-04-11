import time
import unittest

import app
from script.test_login import TESTLOG
from tools.HTMLTestRunner import HTMLTestRunner
#封装测试套件

suite=unittest.TestSuite()
suite=unittest.makeSuite(TESTLOG)
#指定报告路径
file=app.BASE_URL+"/report/report-{}.html".format(time.strftime("%Y%m%d-%H%M%S"))
#打开文件流
with open(file,"wb")as f:
    #创建HTMLTestRunner运行器
    runner=HTMLTestRunner(f,title="p2p的自动化测试报告")
    # 执行测试套件
    runner.run(suite)