from selenium import webdriver
import pytest
from data.test_data import TestData


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(TestData.CHROME_PATH)
    elif browser_name == "firefox":
        driver = webdriver.Firefox(TestData.FIREFOX_PATH)
    request.cls.driver = driver
    driver.get(TestData.BASE_URL)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield
    driver.close()
