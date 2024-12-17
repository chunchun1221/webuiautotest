import os
from time import sleep

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from chaper99.until.LoggingConfig import Loging

from selenium  import webdriver
from selenium.webdriver.edge.service import Service

from chaper99.until.ReadConfig import ReadConfig
from chaper99.test.common.tabOperation import TabOperation


class BasePage(object):
    """基础页面"""
    def __init__(self, base_url=None, driver=None):
        """基础的东西，例如这个项目的url，等等"""
        self.loger=Loging().get_log()
        if driver is None:
            try:
                current_path = os.path.abspath(os.path.dirname(__file__))
                driver_path = os.path.join(current_path, "..", "..", "drivers", "msedgedriver.exe")
                service = Service(executable_path=driver_path)
                self.driver=webdriver.Edge(service=service)
            except Exception as e:
                self.loger.debug(e)
        else:
            self.driver=driver

        if base_url is None:
            try:
                yaml_data=ReadConfig(file_name="base_data.yaml").read_yaml()
                self.base_url=yaml_data["database"]["url"]
                self.loger.info(self.base_url)
            except:
                self.loger.debug("url信息有问题")

        else:
            self.base_url=base_url
        self.open_page()

    def open_page(self):

        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(self.base_url)
        sleep(10)

    def close_page(self):
        return self.driver.close()

    def quit_driver(self):
        return self.driver.quit()

    def find_element(self,by,element):
        sleep(1)
        try:
            return self.driver.find_element(getattr(By,by.upper()),element)
        except NoSuchElementException:
            self.loger.debug(f"没有这样的元素存在{element}")
        except Exception as e:
            self.loger.debug(e)


    def finds_element(self,by,element):
        sleep(1)
        try:
            return self.driver.finds_element(getattr(By,by.upper()),element)
        except NoSuchElementException:
            self.loger.debug(f"没有这样的元素存在{element}")
        except Exception as e:
            self.loger.debug(e)

    def switch_alert(self):
        sleep(1)
        return self.driver.switch_to.alert

    def switch_menus(self,menu_text):
        sleep(1)
        menus=TabOperation(self.driver)
        return  menus.switch_tab(menu_text)








    


# if __name__=="__main__":
#      # test=BasePage()
#     # password_element=test.find_element(by="id",element="password")
#     # password_element.send_keys("test")
#     # print(password_element)

