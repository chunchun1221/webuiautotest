from time import sleep

from chaper99.test.pages.loginPage import LoginPage

class ManagementPage(LoginPage):
    ADD_GROUP_BOTTOM_CSS=("css_selector","#app > div.v-application--wrap > div > main > div > div > div > div > div > div > div:nth-child(2) > div > div.fill-height.v-card.v-card--flat.v-sheet.theme--light.transparent > header > div > button:nth-child(3)")
    GROUP_NAME_BOX_ID=("xpath","//div[@class='v-text-field__slot']/input[1]")
    GROUP_DER_BOX_ID = ("xpath","//div[@class='v-text-field__slot']/input[2]")
    GROUP_info_save_bottom_css=("css_selector",".v-btn.v-btn--is-elevated.v-btn--has-bg.theme--light.v-size--default.primary")
    GROUP_info_cancel_bottom_css = ("css_selector", ".v-btn.v-btn--is-elevated.v-btn--has-bg.theme--light.v-size--default")


    def switch_devices(self):
        sleep(10)
        return  self.switch_menus("devices")

    def switch_groups(self):
        sleep(10)
        return  self.switch_menus("group")

    #按钮
    def add_group_bottom(self):
        """添加组的按钮"""
        return self.find_element(*self.ADD_GROUP_BOTTOM_CSS)

    def group_name_box(self):
        """新增组名的输入框"""
        return self.find_element(*self.GROUP_NAME_BOX_ID)

    def group_der_box(self):
        """组的描述输入框"""
        return  self.find_element(*self.GROUP_DER_BOX_ID)

    def group_info_save_bottom(self):
        """保存按钮"""
        return  self.find_element(*self.group_info_save_bottom())

    def group_info_cancel_bottom(self):
        """取消按钮"""
        return self.find_element(*self.GROUP_info_cancel_bottom_css)


    def add_group(self,group_name,group_der):
        try:
            self.add_group_bottom().click()
            self.group_name_box().send_keys(group_name)
            self.group_der_box().send_keys(group_der)
            self.group_info_save_bottom()
        except Exception as e:
            self.loger.debug(e)


if __name__=="__main__":
    groups_page=ManagementPage()
    groups_page.login()
    groups_page.switch_groups()
    groups_page.add_group("test","test")



