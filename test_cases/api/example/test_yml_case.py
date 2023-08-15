import pytest
from common.base.yml_util import read_yml, write_yml
from common.base.config import conf
from common.api.requstsLib import Request
from common.base.assert_result import BaseTest
from common.base import logger


class TestYml:
    base_url = "https://qyapi.weixin.qq.com/cgi-bin"
    log_content = "this is api_data by reading yml file:{}"

    def test_yml_write(self):
        # read yml file
        api_data = read_yml("test_data/api/example/getAccessTokenData.yml")['cases'][0]
        logger.info(self.log_content.format(api_data))

        # set request info
        url = self.base_url + api_data['url']
        params = api_data['params']
        headers = eval(conf.get("api_env", "headers"))

        # send the request
        response = Request().get_request(url=url, headers=headers, params=params)
        access_token = response.json()['access_token']

        # write data to yml
        write_yml("test_data/api/example/token.yml", {"access_token": access_token})

    def test_get_api_yml(self):
        # read yml file
        api_data = read_yml("test_data/api/example/getAccessTokenData.yml")['cases'][0]
        logger.info(self.log_content.format(api_data))

        # set request info
        url = self.base_url + api_data['url']
        params = api_data['params']
        validations = api_data['validations']
        headers = eval(conf.get("api_env", "headers"))

        # send the request
        response = Request().get_request(url=url, headers=headers, params=params)

        # assert the request result
        try:
            BaseTest().equals(response.status_code, 200)
            BaseTest().contains(response.text,validations)
        except AssertionError as e:
            logger.error("api test_get_api_yml fail, fail info: {}".format(e))
            logger.exception(e)
            raise e
        else:
            logger.info("api test_get_api_yml pass")

    def test_post_api_yml(self):
        # read  yml file
        api_data = read_yml("test_data/api/example/postAddDepartmentData.yml", {'name': 'test'})['cases'][0]
        logger.info(self.log_content.format(api_data))
        access_token = read_yml("test_data/api/example/token.yml")['access_token']
        logger.info("this is access_token by reading yml file:{}".format(access_token))

        # set request info
        url = self.base_url + api_data['url'] + access_token
        body = api_data['params']
        headers = eval(conf.get("api_env", "headers"))

        # send the request
        response = Request().post_request(url=url, headers=headers, json=body)

        # assert the request result
        try:
            BaseTest().equals(response.status_code, 200)
        except AssertionError as e:
            logger.error("api test_post_api_yml fail, fail info: {}".format(e))
            logger.exception(e)
            raise e
        else:
            logger.info("api test_post_api_yml pass")

    @pytest.mark.parametrize("data", read_yml("test_data/api/example/getAccessTokenData.yml")['cases'])
    def test_parametrize(self, data):
        logger.info(self.log_content.format(data))

        # set request info
        url = self.base_url + data['url']
        params = data['params']
        validations = data['validations']
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
