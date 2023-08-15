import pytest
from selenium.webdriver import Chrome
from selenium import webdriver
from page_objects.web_ui.pages.example.login_page import LoginPage
from page_objects.web_ui.pages.example.index_page import IndexPage
from common.base.config import conf


def create_driver():
    """
    Open browser，create driver object
    :return:
    """
    # read configuration if headless mode is used
    if conf.getboolean('run', 'headless'):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(options=options)
    else:
        driver = Chrome()
    return driver


@pytest.fixture(scope='class')
def login_setup():
    """
    login precondition：open browser，redirect login page
    :return:
    """
    driver = create_driver()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(conf.get('ui_env', 'base_url'))
    login_page = LoginPage(driver)
    index_page = IndexPage(driver)
    yield login_page, index_page
    # login teardown，quit browser
    driver.quit()
