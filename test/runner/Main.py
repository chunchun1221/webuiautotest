"""定义获取所有测试用例的方法：get_all_case,测试报告的输出：set_report,和执行用例输出测测试的方法，run_case"""
import datetime
import os
import time
import unittest
from HTMLTestRunner import HTMLTestRunner

from chaper99.until.LoggingConfig import Loging


CURRENT_PATH=os.path.abspath(os.path.dirname(__file__))
print(CURRENT_PATH)
class Main(object):

    def __init__(self):
        self.loger=Loging().get_log()

    def get_all_case(self):
        """导入所有测试用例"""
        case_path = os.path.join(CURRENT_PATH, "../case/")
        try:
            discover=unittest.defaultTestLoader.discover(case_path,pattern="test*.py")
            self.loger.info(f"case的路径为:{case_path},discover为：{discover}")
            return discover
        except Exception as e:
            self.loger.error(f"有点问题，检查下。case的路径为:{case_path}")


    def set_report(self,all_case,report_path=None):
        if report_path is None:
            report_path=os.path.join(CURRENT_PATH,"../../report/")
        else:
            report_path=report_path

        #获取当前时间
        now=datetime.datetime.now().strftime("%Y_%m_%d_%H_%M")
        title=u"skyway后台管理系统"
        #设置存放路径
        report_abspath=os.path.join(report_path,title+now+".html")
        self.loger.debug(report_abspath)
        try:
            #测试报告的写入
            with open(report_abspath,"wb") as f:
                runner=HTMLTestRunner(stream=f,title=title)
                if all_case:
                    runner.run(all_case)
            return
        except Exception as e:
            self.loger.error(e)

    def run_case(self, report_path=None):
        all_case=self.get_all_case()
        self.set_report(all_case,report_path)

# if __name__=="__main__":
#     Main().run_case()



