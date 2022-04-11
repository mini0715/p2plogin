import random
import unittest
import requests
from api.login import TESTLogin

#实例化
class TESTLOG(unittest.TestCase):
    def setUp(self) -> None:
        self.logintext=TESTLogin
        self.session=requests.Session
    def tearDown(self) -> None:
        self.session.close()
     #创建测试用例
    def test01_getlog(self):
        #定义参数
        r=random.random()
        response=self.logintext.aa(self.session,str(r))
        #断言
        self.assertEqual(200,response.stasus_code)

