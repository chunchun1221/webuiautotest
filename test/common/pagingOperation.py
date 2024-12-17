import time

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from chaper99.until.LoggingConfig import Loging



""""这个也是找到那个分页按钮的父项目，然后子在定位到首页，下一页，上一页，输入等等"""
class PagingOperation(object):
    def __init__(self, driver):
        self.driver = driver
        self.logger = Loging().get_log()  # 假设Logging类和get_logger方法已正确定义
        # 分页元素的XPath和CSS选择器
        self.firstpage_element_xpath = '//*[@id="app"]/div/div/main/div/div/div/div[1]/div/div/div[2]/div/div/div/div[2]/div/div[3]/div/div/nav/ul/li[2]/button'
        self.nextpage_element_xpath = '//*[@id="app"]/div/div/main/div/div/div/div[1]/div/div/div[2]/div/div/div/div[2]/div/div[3]/div/div/nav/ul/li[9]/button/i'
        self.prevpage_element_xpath = '<i aria-hidden="true" class="v-icon notranslate mdi mdi-chevron-left theme--light"></i>'  # 注意这个XPath可能不正确，因为它指向的是i标签的属性
        self.inputbottom_element_css = ".v-text-field__slot"  # 修正CSS选择器

        # 在查找分页元素前，先滚动到底部
        self.scroll_data_table_by_steps()

        # try:
        #     # 初始化分页按钮和输入框
        #     self.first_page_button = self.driver.find_element(By.XPATH, self.firstpage_element_xpath)
        #     self.logger.debug(self.first_page_button.text)
        #     self.next_page_button = self.driver.find_element(By.XPATH, self.nextpage_element_xpath)
        #     self.prev_page_button = self.driver.find_element(By.XPATH,
        #                                                      self.prevpage_element_xpath)  # 这里可能需要修正XPath以直接定位按钮
        #     self.page_input_box = self.driver.find_element(By.CSS_SELECTOR, self.inputbottom_element_css)
        # except NoSuchElementException:
        #     self.logger.error("分页元素未找到，请检查页面加载或选择器是否正确。")

    def scroll_data_table_by_steps(self):
        wrapper_element = self.driver.find_element(By.CSS_SELECTOR, ".v-responsive__content")
        SCROLL_PAUSE_TIME = 0.5

        # 获取当前滚动高度
        last_height = self.driver.execute_script("return arguments[0].scrollHeight", wrapper_element)

        while True:
            # 同样地，这里也改为使用driver执行脚本
            self.driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight);", wrapper_element)
            time.sleep(SCROLL_PAUSE_TIME)

            # 更新new_height的获取方式
            new_height = self.driver.execute_script("return arguments[0].scrollHeight", wrapper_element)
            if new_height == last_height:
                break
            last_height = new_height



    # def paging_opertaion(self,text):
    #
    #     self.scroll_data_table_to_bottom()
    #     time.sleep(2)
    #
    #     if text == "首页" or text =="第一页":
    #         return self.first_page_button.click()
    #     elif text== "下一页":
    #         return self.next_page_button.click()
    #     elif text =="上一页":
    #         return self.prev_page_button.click()
    #     elif type(text) == int:
    #         self.page_input_box.click()
    #         self.page_input_box.send_keys(str(text))
    #         self.page_input_box.send_keys(Keys.ENTER)
    #     else:
    #         print("暂时不支持更多操作")




if __name__=="__main__":
    from selenium import webdriver
    from chaper99.until.ReadConfig import ReadConfig
    from chaper99.test.common.multiMenuOperation import MultiMenuOperation
    from chaper99.test.common.tabOperation import TabOperation


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
    driver.maximize_window()
    driver.implicitly_wait(20)
    login(username, password)
    tms=TabOperation(driver)
    app_update=tms.switch_tab("App Update")
    paging=PagingOperation(driver)
    paging.scroll_data_table_by_steps()






