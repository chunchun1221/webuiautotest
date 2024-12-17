"""封装思路也是，先点击出现下拉菜单，然后通过父类找到每个menus的名字进行点击"""
from selenium.webdriver.common.by import By
from chaper99.test.common.elementExit import ElementExit
from chaper99.until.LoggingConfig import Loging
import time

class MultiMenuOperation(object):
    def __init__(self,driver):
        self.driver=driver
        self.loger=Loging().get_log()

    def open_menus(self):
        """点击打开menus"""
        time.sleep(1)
        menus_bottom_css=".router-name"
        menus_bottom=self.driver.find_element(By.CSS_SELECTOR,menus_bottom_css)
        menus_bottom.click()

    def get_all_menus(self):
        """获取所有可以点击的内容"""

        self.open_menus()
        time.sleep(1)

        parents_css=".v-item-group"
        menus_css=".e-ellipsis-1.right-title"
        parents_exit=ElementExit(self.driver).is_exit(parents_css)
        if parents_exit:
            menus_list=[]
            parents=self.driver.find_elements(By.CSS_SELECTOR,parents_css)
            for parent in parents:
                menus=parent.find_elements(By.CSS_SELECTOR,menus_css)
                menus_list.extend(menus)
            return menus_list
        else:
            return []

    def swit_menus(self,menu_name):

        menus_list=self.get_all_menus()
        for menu in menus_list:
            if menu.text == menu_name:
                menu.click()
                self.loger.debug(menu.text)
                return




if __name__=="__main__":
    from selenium import webdriver
    from chaper99.until.ReadConfig import ReadConfig
    import time
    def login(username, password):
        username_box = driver.find_element(By.ID, "input-15")
        username_box.send_keys(username)
        time.sleep(1)
        password_box = driver.find_element(By.ID, "password")
        password_box.send_keys(password)
        time.sleep(1)
        login_bottom = driver.find_element(By.CSS_SELECTOR, ".v-btn__content")
        login_bottom.click()

    yaml_data = ReadConfig(file_name="base_data.yaml").read_yaml()
    url = yaml_data["database"]["url"]
    username = yaml_data["database"]["username"]
    password = yaml_data["database"]["password"]
    driver = webdriver.Edge()
    driver.get(url)
    driver.implicitly_wait(10)
    driver.maximize_window()
    login(username,password)
    menus=MultiMenuOperation(driver)
    menus.swit_menus(menu_name="CMS")
