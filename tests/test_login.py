import pytest
from pages.loginpage import LoginPage

@pytest.mark.usefixtures("test_setup")
class TestLogin:
    def test_login(self):
        driver = self.driver
        lp=LoginPage(driver)
        lp.enter_un()
        lp.enter_pwd()
        lp.click_on_login_btn()
        # driver.find_element_by_name("j_username").send_keys("admin")
        # driver.find_element_by_name("j_password").send_keys("manager")
        # driver.find_element_by_name("Submit").click()
    def test_logout(self):
        driver = self.driver
        driver.find_element_by_xpath("//*[text()='log out']").click()


# test_launch_url()
# test_login()
# test_logout()
