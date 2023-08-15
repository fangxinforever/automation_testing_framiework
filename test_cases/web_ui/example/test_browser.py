import time

from selenium.webdriver.common.by import By

from common.base import logger
import globals as glb
from common.web_ui.base_page import BasePage
from common.web_ui.driver import Driver


class TestBrowser:

    def test_option(self):
        logger.info("test_option")
        logger.info("Testing platform: {}".format(glb.get("platform")))

    def test_browser(self):
        logger.info("starting browsers...")
        driver = Driver().get_driver()
        base_page = BasePage(driver)
        base_page.get("https://www.baidu.com")
        input_loc = (By.ID, 'kw')
        base_page.find_element(input_loc, "search input box")
        time.sleep(5)
        driver.close()
        base_page.quit()
