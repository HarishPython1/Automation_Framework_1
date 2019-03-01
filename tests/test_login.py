from selenium import webdriver
import pytest
from pages.loginpage import LoginPage

class TestLogin:
    @pytest.fixture(scope='class')
    def test_setup(self):
        global driver
        driver=webdriver.Chrome()
        driver.get("http://localhost:8080/login?from=%2F")
        driver.maximize_window()
        driver.implicitly_wait(30)
        yield
        driver.quit()

    def test_login(self,test_setup):
        lp=LoginPage()
        lp.enter_un()
        lp.enter_pwd()
        lp.click_on_login_btn()

        # driver.find_element_by_name("j_username").send_keys("admin")
        # driver.find_element_by_name("j_password").send_keys("manager")
        # driver.find_element_by_name("Submit").click()
    def test_logout(self,test_setup):
        driver.find_element_by_xpath("//*[text()='log out']").click()


# test_launch_url()
# test_login()
# test_logout()
