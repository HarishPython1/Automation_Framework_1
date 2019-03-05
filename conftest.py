import pytest
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                help="Type in Your Browser Name e.g chrome, Firefox")
@pytest.fixture(scope='class')
def test_setup(request):
    from selenium import webdriver
    browser = request.config.getoption("--browser")
    if browser=='chrome':
        driver=webdriver.Chrome()
    elif browser=='ff':
        driver=webdriver.Firefox()
    driver.get("http://localhost:8080/login?from=%2F")
    driver.maximize_window()
    driver.implicitly_wait(30)
    request.cls.driver = driver
    yield
    driver.quit()