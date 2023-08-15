import globals as glb
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.ie.service import Service as IEService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager, EdgeChromiumDriverManager
from common.base import logger


class Driver:
    """
        Selenium webdriver wrapper
    """

    def __init__(self):
        """
        Initial driver, start browser
        """
        self.driver = None
        self.browser_name = glb.options.get("platform").lower()

    def get_driver(self):
        try:
            logger.info(f'Getting webdriver based on this string: {self.browser_name}')
            if self.browser_name == 'chrome':
                self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
            elif self.browser_name == 'firefox':
                self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
            elif self.browser_name == 'edge':
                self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
            elif self.browser_name == 'ie':
                self.driver = webdriver.Ie(service=IEService(IEDriverManager().install()))
            elif self.browser_name == 'safari':
                self.driver = webdriver.Safari()
            else:
                raise Exception("Please check the testing browser name {}".format(self.browser_name))
        except WebDriverException as wde:
            logger.error(f'Could not instantiate WebDriver from the search string {self.browser_name}')
            logger.error(wde)
            raise wde
        self.driver.maximize_window()
        return self.driver
    #
    # def get(self, url):
    #     """
    #     Loads a web page
    #     :param url: open the url
    #     """
    #     logger.info('Open url {}'.format(url))
    #     self.driver.get(url)
    #
    # def find_element(self, by, value):
    #     """
    #     Find an element given a By strategy and locator.
    #
    #     :param by: By.xpath, By.CSS, By.ID....
    #     :param value:
    #     :return: WebElement
    #     """
    #     try:
    #         logger.info('Find element by {}, value {}'.format(by, value))
    #         return self.driver.find_element(by, value)
    #     except Exception as e:
    #         logger.error('Cannot find the element')
    #         raise e
    #
    # def find_elements(self, by, value):
    #     """
    #     Find elements given a By strategy and locator.
    #
    #     :param by: By.xpath, By.CSS, By.ID....
    #     :param value:
    #     :return: WebElements
    #     """
    #     try:
    #         logger.info('Find element by {}, value {}'.format(by, value))
    #         return self.driver.find_elements(by, value)
    #     except Exception as e:
    #         logger.error('Cannot find the elements')
    #         raise e
    #
    # def wait_for_element(self, by, locator, waiting_time=10):
    #     """
    #     Explicit wait, find element given a By strategy and locator in waiting time
    #     :param by: By.xpath, By.CSS, By.ID...
    #     :param locator:
    #     :param waiting_time: default 10s
    #     :return: WebElement
    #     """
    #     try:
    #         return WebDriverWait(self.driver, waiting_time).until(
    #             expected_conditions.presence_of_element_located((by, locator)))
    #     except Exception as e:
    #         logger.error('Cannot find the element in {}s'.format(waiting_time))
    #         raise e
    #
    # def exit(self):
    #     """
    #     Exit browser
    #     """
    #     logger.info('exit() called - exiting')
    #     self.driver.quit()
    #     self.driver = None
