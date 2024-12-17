from time import sleep

from chaper99.test.pages.basePage import BasePage
from chaper99.until.ReadConfig import ReadConfig

class LoginPage(BasePage):
    # def __init__(self):
    #     super().__init__()
    USERNAME_BOX_SELECTOR = ("id", "input-15")
    PASSWORD_BOX_SELECTOR = ("id", "password")
    LOGIN_BUTTON_SELECTOR = ("css_selector", ".v-btn__content")
    USERNAME_ERROR_SELECTOR = ("css_selector", ".v-messages__message")
    PASSWORD_ERROR_SELECTOR = ("css_selector", ".v-messages__message.message-transition-enter-to")

    def username_box_element(self):
       return self.find_element(*self.USERNAME_BOX_SELECTOR)

    def password_box_element(self):
        return self.find_element(*self.PASSWORD_BOX_SELECTOR)

    def login_bottom(self):
        return self.find_element(*self.LOGIN_BUTTON_SELECTOR)

    def username_error_element(self):
        try:
            return  self.find_element(*self.USERNAME_ERROR_SELECTOR)

        except Exception as e:
            self.loger.error(e)

    def password_error_element(self):
        return  self.find_element(*self.PASSWORD_ERROR_SELECTOR)

    # def login_fail_element(self):
    def login_assert(self,assert_type,assert_message):
        sleep(1)
        if assert_type == "username error":
            username_massage=self.username_error_element()
            assert username_massage.text==assert_message
        elif assert_type =="password error":
            password_massage=self.password_error_element()
            assert password_massage.text ==assert_message
        elif assert_type in ["login sucess","login fail"]:
            login_message = self.driver.switch_to.alert.text
            assert login_message.text == assert_message
        else:
            self.loger.error("断言有问题")



    def login(self,username=None,password=None):
        account_username,account_password=self.get_account()
        if username is None:
            username=account_username
        else:
            username=username
        self.loger.debug(username)

        if password is None:
            password=account_password
        else:
            password=password
        self.loger.debug(password)
        try:
            self.username_box_element().send_keys(username)
            self.password_box_element().send_keys(password)
            sleep(1)
            self.login_bottom().click()
            sleep(10)
        except AttributeError as A:
            self.loger.error(A)
    @staticmethod
    #静态方法装饰器，使用装饰器定义方法，python解释器会认为该方法为静态方法。静态方法通常用于工具函数或者那些不依赖于对象状态的操作。
    def get_account():
        data=ReadConfig(file_name="base_data.yaml").read_yaml()
        return data["database"]["username"],data["database"]["password"]



if __name__=="__main__":
    a=LoginPage()
    a.login(username="")
    uer_massage=a.username_error_element()
    print(uer_massage.text)



