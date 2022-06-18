import pytest
import os
import platform
from selenium import webdriver
from . import config


def pytest_addoption(parser):
    parser.addoption("--baseurl",
                     action="store",
                     default="https://www.demoblaze.com",
                     help="base URL for the application under test")
    parser.addoption("--browser",
                     action="store",
                     default="chrome",
                     help="the name of the browser you want to test with")


@pytest.fixture
def driver(request):
    config.baseurl = request.config.getoption("--baseurl")
    config.browser = request.config.getoption("--browser").lower()

    if config.browser == "chrome":
        _driver_filename = 'chromedriver.exe' if platform.system() == 'Windows' else 'chromedriver'
        _chromedriver = os.path.join(os.path.dirname(os.getcwd()), 'vendor', _driver_filename)
        if os.path.isfile(_chromedriver):
            driver_ = webdriver.Chrome(_chromedriver)
        else:
            driver_ = webdriver.Chrome()
    elif config.browser == "firefox":
        _driver_filename = 'geckodriver.exe' if platform.system() == 'Windows' else 'geckodriver'
        _geckodriver = os.path.join(os.path.dirname(os.getcwd()), 'vendor', _driver_filename)
        print(_geckodriver)
        if os.path.isfile(_geckodriver):
            driver_ = webdriver.Firefox(executable_path=_geckodriver)
        else:
            driver_ = webdriver.Firefox()

    def quit():
        driver_.quit()

    request.addfinalizer(quit)
    return driver_
