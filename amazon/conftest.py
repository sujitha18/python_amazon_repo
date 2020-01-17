import pytest
from selenium import webdriver
from sources.utilities.webdriver_factory import WebDriverFactory
@pytest.yield_fixture()
def setUp():
    print("login the page")
    yield
    print("logout the page")
@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request,browser):
    wdf=WebDriverFactory(browser)
    driver=wdf.getWebDriverInstance()
    if request.cls is not None:
        request.cls.driver=driver
    yield driver
    print("close the Browser")
    driver.quit()
def pytest_addoption(parser):
    parser.addoption("--browser",help="to run on different browser")
@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

