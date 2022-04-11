import app
#封装定义类
class TESTLogin():
    #初始化
    def __init__(self):
        self.aa_url=app.BASE_URL+ "/common/public/verifycode1/"

    #封装调用的方法
    def aa(self, session,r):
        url = self.aa_url + r
        response=session.get(url)
        return response