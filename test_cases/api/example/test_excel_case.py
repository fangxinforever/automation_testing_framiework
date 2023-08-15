import pytest
from common.base.excel_util import read_excel, write_excel
from common.base.config import conf
from common.api.requstsLib import Request
from common.base.assert_result import BaseTest
from common.base import logger


class TestExcel:
    base_url = "https://qyapi.weixin.qq.com/cgi-bin"
    log_content = "this is api_data by reading excel file:{}"

    def test_excel_write(self):
        # read excel file
        api_data = read_excel("test_data/api/example/getAccessTokenData.xlsx")[0]
        logger.info(self.log_content.format(api_data))

        # set request info
        url = self.base_url + api_data['Url']
        params = api_data['Params']
        headers = eval(conf.get("api_env", "headers"))

        # send the request
        response = Request().get_request(url=url, headers=headers, params=params)
        access_token = response.json()['access_token']

        # write data to excel
        write_excel("test_data/api/example/token.xlsx", {"access_token": access_token})

    def test_get_api_excel(self):
        # read excel file
        api_data = read_excel("test_data/api/example/getAccessTokenData.xlsx")[0]
        logger.info(self.log_content.format(api_data))

        # set request info
        url = self.base_url + api_data['Url']
        params = api_data['Params']
        validations = api_data['Validations']
        headers = eval(conf.get("api_env", "headers"))

        # send the request
        response = Request().get_request(url=url, headers=headers, params=params)

        # assert the request result
        try:
            BaseTest().equals(response.status_code, 200)
            BaseTest().contains( response.text,validations)
        except AssertionError as e:
            logger.error("api test_get_api_excel fail, fail info: {}".format(e))
            logger.exception(e)
            raise e
        else:
            logger.info("api test_get_api_excel pass")

    def test_post_api_excel(self):
        # read excel file
        api_data = read_excel("test_data/api/example/postAddDepartmentData.xlsx",
                              {'name': 'testName', 'name_en': 'test english name'})[0]
        logger.info(self.log_content.format(api_data))
        access_token = read_excel("test_data/api/example/token.xlsx")[0]['access_token']
        logger.info("this is access_token by reading excel file:{}".format(access_token))

        # set request info
        url = self.base_url + api_data['Url'] + access_token
        body = api_data['Params']
        headers = eval(conf.get("api_env", "headers"))

        # send the request
        response = Request().post_request(url=url, headers=headers, json=body)

        # assert the request result
        try:
            BaseTest().equals(response.status_code, 200)
        except AssertionError as e:
            logger.error("api test_post_api_excel fail, fail info: {}".format(e))
            logger.exception(e)
            raise e
        else:
            logger.info("api test_post_api_excel pass")

    @pytest.mark.parametrize("data", read_excel("test_data/api/example/getAccessTokenData.xlsx"))
    def test_parametrize(self, data):
        logger.info(self.log_content.format(data))

        # set request info
        url = self.base_url + data['Url']
        params = data['Params']
        validations = data['Validations']
        headers = eval(conf.get("api_env", "headers"))

        # send the request
        response = Request().get_request(url=url, headers=headers, params=params)

        # assert the request result
        try:
            BaseTest().equals(response.status_code, 200)
            BaseTest().contains(response.text,validations)
        except AssertionError as e:
            logger.error("api test_parametrize fail, fail info: {}".format(e))
            logger.exception(e)
            raise e
        else:
            logger.info("api test_parametrize pass")
