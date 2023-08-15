from page_objects.web_ui.locator.example.index_locator import IndexLocator as loc
from common.web_ui.base_page import BasePage
from common.base.logger import LogFileOperation

log = LogFileOperation().logger


class IndexPage(BasePage):
    def is_login(self):
        """
        whether the login successfully jumps to the home page
        :return:
        """
        try:
            self.wait_element_visible(loc.home_logo, 'Facebook home logo')
            log.info('Login Successfully')
        except Exception as e:
            log.error(e)
            return False
        else:
            return True
