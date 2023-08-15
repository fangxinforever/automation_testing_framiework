from page_objects.web_ui.locator.example.login_locator import LoginLocator as loc
from common.web_ui.base_page import BasePage
from common.base.logger import LogFileOperation
from common.base.config import conf

log = LogFileOperation().logger


class LoginPage(BasePage):
    def login(self):
        """
        login operations
        :return:
        """
        # input account
        self.input_data(loc.email, value=conf.get('ui_account', 'email'),loc_desc='account')
        # input password
        self.input_data(loc.password, value=conf.get('ui_account', 'password'), loc_desc='password')
        # click login
        self.click_element(loc.log_in_btn, loc_desc='Login In')

    def get_login_page(self):
        """
        get login page
        :return:
        """
        self.driver.get(conf.get('ui_env', 'base_url'))

    def is_logout(self):
        """
        whether log out
        :return:
        """
        try:
            self.wait_element_visible(loc.log_in_btn, 'login button')
            log.info('Logout Successfully')
        except Exception as e:
            log.error(e)
            return False
        else:
            return True