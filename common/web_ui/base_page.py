import os
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.base.path import screenshot_dir
from common.base import logger


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get(self, url):
        """
        Loads a web page
        :param url: open the url
        """
        logger.info('Open url {}'.format(url))
        self.driver.get(url)

    def quit(self):
        """
        Exit browser
        """
        logger.info('exit() called - exiting')
        self.driver.quit()
        self.driver = None

    def page_save_screenshot(self, filename='', page_desc=''):
        """
        page screenshot
        :param filename: file name
        :param page_desc: page description
        :return:
        """
        try:
            file_path = os.path.join(screenshot_dir, filename)
            self.driver.save_screenshot(file_path)
        except Exception as e:
            logger.error('get-[{}]-page screenshot successfully'.format(page_desc))
            logger.exception(e)
            raise e
        else:
            logger.info('get-[{}]-page screenshot successfully，picture was saved as {}'.format(page_desc, filename))

    def click_element(self, loc, loc_desc=''):
        """
        click element
        :param loc: element locator
        :param loc_desc: element description
        :return:
        """
        try:
            self.driver.find_element(*loc).click()
        except Exception as e:
            logger.error("click element -[{}]--fail".format(loc_desc))
            logger.exception(e)
            self.page_save_screenshot(loc_desc)
            raise e
        else:
            logger.info("click element-[{}]--successfully".format(loc_desc))

    def get_element_text(self, loc, loc_desc=''):
        """
        get element text
        :param loc: element locator -->:(BY.xxx,'expression')
        :param loc_desc: element description
        :return: element text
        """
        try:
            text = self.driver.find_element(*loc).text
        except Exception as e:
            logger.error("get element -[{}]-- text fail".format(loc_desc))
            logger.exception(e)
            self.page_save_screenshot(loc_desc)
            raise e
        else:
            logger.info("get element -[{}]--text successfully: {}".format(loc_desc, text))
            return text

    def find_element(self, loc, loc_desc=''):
        """
        query element
        :param loc:  element locator -->:(BY.xxx,'expression')
        :param loc_desc: element description
        :return:
        """
        try:
            ele = self.driver.find_element(*loc)
        except Exception as e:
            logger.error("query element -[{}]--fail".format(loc_desc))
            logger.exception(e)
            self.page_save_screenshot(loc_desc)
            raise e
        else:
            logger.info("query element-[{}]--successfully".format(loc_desc))
            return ele

    def get_element_attr(self, loc, attr, loc_desc=''):
        """
        get element attribute
        :param loc: element locator -->:(BY.xxx,'expression')
        :param attr: element attribute
        :param loc_desc: element description
        :return: element attribute
        """
        try:
            text = self.driver.find_element(*loc).get_attribute(attr)
        except Exception as e:
            logger.error("get element attribute-[{}]--fail".format(loc_desc))
            logger.exception(e)
            self.page_save_screenshot(loc_desc)
            raise e
        else:
            logger.info("get element attribute-[{}]--successfully".format(loc_desc))
            return text

    def wait_element_visible(self, loc, loc_desc, timeout=20, poll_time=0.5):
        """
        wait element is visible
        :param loc:  element locator -->:(BY.xxx,'expression')
        :param loc_desc: element description
        :param timeout: timeout
        :param poll_time: wait poll_time
        :return: located element
        """
        try:
            ele = WebDriverWait(self.driver, timeout, poll_time).until(
                EC.visibility_of_element_located(loc)
            )
        except Exception as e:
            logger.error("wait element -[{}]- visible timeout".format(loc_desc))
            logger.exception(e)
            self.page_save_screenshot(loc_desc)
            raise e
        else:
            logger.info("wait element -[{}]- visible successfully".format(loc_desc))
            return ele

    def wait_element_presence(self, loc, loc_desc='', timeout=20, poll_time=0.5):
        """
        wait element presence
        :param loc: loc: element locator -->:(BY.xxx,'expression')
        :param loc_desc: loc_desc: element description
        :param timeout:
        :param poll_time:
        :return: located element
        """
        try:
            ele = WebDriverWait(self.driver, timeout, poll_time).until(
                EC.presence_of_element_located(loc)
            )
        except Exception as e:
            logger.error("wait element -[{}]--presence timeout".format(loc_desc))
            logger.exception(e)
            self.page_save_screenshot(loc_desc)
            raise e
        else:
            logger.info("ait element -[{}]--presence successfully".format(loc_desc))
            return ele

    def wait_element_clickable(self, loc, loc_desc='', timeout=20, poll_time=0.5):
        """
        wait element clickable
        :param loc: loc: element locator-->:(BY.xxx,'expression')
        :param loc_desc: loc_desc: element desciption
        :param timeout:
        :param poll_time:
        :return: located element
        """
        try:
            ele = WebDriverWait(self.driver, timeout, poll_time).until(
                EC.element_to_be_clickable(loc)
            )
        except Exception as e:
            logger.error("wait element clickable-[{}]--timeout".format(loc_desc))
            logger.exception(e)
            self.page_save_screenshot(loc_desc)
            raise e
        else:
            logger.info("wait element clickable-[{}]-- successfully".format(loc_desc))
            return ele

    def input_data(self, loc, value, loc_desc=''):
        """
        input data in the input element
        :param loc: input locator -->:(BY.xxx,'expression')
        :param value: input value
        :param loc_desc: element description
        :return:
        """
        try:
            ele = self.driver.find_element(*loc)
            ele.clear()
            ele.send_keys(value)
        except Exception as e:
            logger.error("input data-[{}]--fail".format(loc_desc))
            logger.exception(e)
            self.page_save_screenshot(loc_desc)
            raise e
        else:
            logger.info("input data-[{}]--successfully".format(loc_desc))
