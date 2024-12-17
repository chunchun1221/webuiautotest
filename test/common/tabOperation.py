"""封装思路为：先找到父元素，然后在找父元素下面的内容，进行点击"""
import os
import re
import time

from selenium.webdriver.common.by import By

from chaper99.test.common.elementExit import ElementExit
from chaper99.until.LoggingConfig import Loging


class TabOperation(object):


    def __init__(self,driver):
        self.driver=driver
        self.logger=Loging().get_log()

    def get_all_tab(self):
        father_css = ".v-list-group.e-list-group.v-list-group--active.v-list-group--no-action.pageMenuItem--text"
        tab_css = ".e-list-title"
        #先判断夫元素是否存在，先找到父级元素，然后在进行找父级元素下面的东西
        father_exit=ElementExit(self.driver).is_exit(father_css)
        tabs_list = []
        if father_exit:
            father_tabs=self.driver.find_elements(By.CSS_SELECTOR,father_css)
            for father_tab in father_tabs:
                tabs=father_tab.find_elements(By.CSS_SELECTOR,tab_css)
                for tab in tabs:
                    tabs_list.append(tab)
            return tabs_list
        else:
            return []

    def switch_tab(self,tab_text):
        tabs=self.get_all_tab()
        for tab in tabs:


            # if tab.text == tab_text:
            #     tab.click()
            #     self.logger.debug(tab.text)
            #     return

            pattern = re.compile(re.escape(tab_text), re.IGNORECASE)

            if pattern.search(tab.text):
                tab.click()
                return
            self.logger.debug(tab.text)
# if __name__=="__main__":
#     from selenium import webdriver
#     from chaper99.until.ReadConfig import ReadConfig
#     def login(username, password):
#         username_box = driver.find_element(By.ID, "input-15")
#         username_box.send_keys(username)
#         time.sleep(1)
#         password_box = driver.find_element(By.ID, "password")
#         password_box.send_keys(password)
#         time.sleep(1)
#         login_bottom = driver.find_element(By.CSS_SELECTOR, ".v-btn__content")
#         login_bottom.click()
#
#     yaml_data = ReadConfig(file_name="base_data.yaml").read_yaml()
#     url = yaml_data["database"]["url"]
#     username = yaml_data["database"]["username"]
#     password = yaml_data["database"]["password"]
#     driver = webdriver.Edge()
#     driver.get(url)
#     driver.implicitly_wait(10)
#     login(username,password)
#     tabs=TabOperation(driver)
#     tabs.switch_tab("update")












