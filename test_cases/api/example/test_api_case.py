from common.base.config import conf
from common.api.requstsLib import Request
from common.base.assert_result import BaseTest
from common.base import logger

class TestOne():

    def test_api_case1(self):
        """
        test api case1
        """
        # request address
        url = eval(conf.get("api_env", "base_url"))
        # request header
        headers = eval(conf.get("api_env", "headers"))
        # send the request
        response = Request().get_request(url=url, headers=headers)
        # assert the request result
        try:
            BaseTest().equals(response.status_code, 200)
        except AssertionError as e:
            logger.error("api testcase1 fail, fail info: {}".format(e))
            logger.exception(e)
            raise e
        else:
            logger.info("api testcase1 pass")
