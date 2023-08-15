from common.base.assert_result import BaseTest
from common.base import logger


class TestHomePage:

    def test_login_pass(self, login_setup):
        """
        Login Successfully
        :param login_setup:
        :return:
        """
        login_page, index_page = login_setup
        login_page.get_login_page()
        login_page.login()
        res = index_page.is_login()
        try:
            BaseTest().assert_true(res)
        except AssertionError as e:
            logger.error("Login fail, fail info: {}".format(e))
            logger.exception(e)
            raise e
        else:
            logger.info("Login successfully")
