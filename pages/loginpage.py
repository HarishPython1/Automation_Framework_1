class LoginPage:
    def __init__(self,driver):
        self.driver=driver
        self.un_txt_bx_name='j_username'
        self.pwd_txt_bx_name='j_password'
        self.login_btn_name='Submit'

    def enter_un(self):
        self.driver.find_element_by_name(self.un_txt_bx_name).send_keys("admin")

    def enter_pwd(self):
        self.driver.find_element_by_name(self.pwd_txt_bx_name).send_keys("manager")

    def click_on_login_btn(self):
        self.driver.find_element_by_name(self.login_btn_name).click()