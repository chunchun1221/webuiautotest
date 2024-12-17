import unittest

from ddt import ddt, data, unpack

from chaper99.test.pages.loginPage import LoginPage
from chaper99.until.ExcelUntil import ExcelUtil


def get_test_cases():
    sheet = "Login"
    excel_data = ExcelUtil(sheet_name=sheet).get_all_data()
    user_index = excel_data[0].index("账号名")
    password_index = excel_data[0].index("密码")
    expect_element_index = excel_data[0].index("预期结果定位")
    expect_index = excel_data[0].index("预期结果")

    cases = [
        (row[user_index], row[password_index], row[expect_element_index], row[expect_index])
        for row in excel_data[1:]
    ]
    return cases

@ddt
class TestLogin(unittest.TestCase):
    # @classmethod
    def setUp(self):
        self.login=LoginPage()
    # @classmethod
    def tearDown(self):
        self.login.quit_driver()

    case=get_test_cases()
    @data(*case)
    @unpack
    def test_Login01(self,username,password,assert_type,assert_message):
        """需要测试的步骤"""
        self.login.login(username,password)
        self.login.login_assert(assert_type,assert_message)


if __name__=="__main__":
    unittest.main()

