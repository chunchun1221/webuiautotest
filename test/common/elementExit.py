#先定位在判断吧
from pywinauto.backend import element_class
from selenium.webdriver.common.by import By


class ElementExit(object):
    def __init__(self,driver):
        self.driver=driver

    def is_exit(self,element):
        flag=True
        try:
            self.driver.find_element(By.CSS_SELECTOR,element)
            return flag
        except:
            flag=False
            return flag


if __name__=="__main__":
    from selenium import webdriver
    from chaper99.until.ReadConfig import ReadConfig
    json_data=ReadConfig().read_json()
    url=json_data["url"]
    driver=webdriver.Edge()
    driver.get(url)
    driver.implicitly_wait(10)
    element=".v-icon"
    e=ElementExit(driver).is_exit(element=element)
    print(e)

