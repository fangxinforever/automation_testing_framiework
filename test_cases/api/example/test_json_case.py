from common.base.json_operator import JsonOperation
from common.base.logger import LogFileOperation
from common.base.assert_result import BaseTest
from common.api.requstsLib import Request
from common.base.path import Base_path
from common.base.config import conf
import os
import pytest

logger = LogFileOperation().logger
json_operator = JsonOperation()
requestor = Request()
assertion = BaseTest()


class TestJson(object):
    json_get_file = os.path.join(Base_path, 'test_data/api/example/getAccessTokenData.json')
    json_post_file = os.path.join(Base_path, 'test_data/api/example/postAddDepartmentData.json')
    token_file = os.path.join(Base_path, 'test_data/api/example/token.json')

    def test_get_api_json(self):
        # read json file and # setup request payload
        url = json_operator.get_value_from_jsonfile_parameter(self.json_get_file, 'url', 1, {'host': 'qyapi.weixin.qq.com', 'port': '443'})
        params = json_operator.get_value_from_jsonfile_parameter(self.json_get_file, 'params', 1, {'corpid': 'ww152ef7dc359ff01b', 'corpsecret': '47oKWL-bBaEvV4JG8wVXtbDb9StnL-ZqQldaztU9CJo'})
        validations = json_operator.get_value_from_jsonfile_parameter(self.json_get_file, 'validations', 1, {'validations': '"errcode":0,"errmsg":"ok"'})
        headers = eval(conf.get("api_env", "headers"))

        # send request
        try:
            response = requestor.get_request(url, headers=headers, params=params)
            # assert the response
            assertion.equals(response.status_code, 200)
            assertion.contains(response.text,validations)
            logger.info("api test_get_api_json pass")
        except Exception as e:
            logger.exception("test_get_api_json occurred exception {}".format(e))

    def test_post_api_json(self):
        # read json file and # setup request payload
        access_token = json_operator.get_value_from_jsonfile(self.token_file, 'access_token', 0)
        url = json_operator.get_value_from_jsonfile_parameter(self.json_post_file, 'url', 1, {'host': 'qyapi.weixin.qq.com', 'port': '443'}) + access_token
        body = json_operator.get_value_from_jsonfile_parameter(self.json_post_file, 'payload', 1, {'name':'广州', 'name_en': 'test'})
        headers = eval(conf.get("api_env", "headers"))

        # send request
        try:
            response = requestor.post_request(url, headers=headers, json=body)
            # assert the response
            assertion.equals(response.status_code, 200)
            logger.info("api test_post_api_json pass")
        except Exception as e:
            logger.exception("test_post_api_json occurred exception {}".format(e))

    def test_json_write(self):
        # get token
        url = json_operator.get_value_from_jsonfile_key(self.json_get_file, 'url', key_dict={'id': '001'})
        params = json_operator.get_value_from_jsonfile_key(self.json_get_file, 'params', key_dict={'id': '001'})
        headers = eval(conf.get("api_env", "headers"))
        response = requestor.get_request(url, headers=headers, params=params)
        assertion.equals(response.status_code, 200)
        json_operator.write_json_file(response.json(), self.token_file)

    @pytest.mark.parametrize("api_data", json_operator.get_value_from_jsonfile(json_get_file, 'cases'))
    def test_parametrize(self, api_data):
        url = api_data["url"]
        params = api_data["params"]
        validations = api_data['validations']
        headers = eval(conf.get("api_env", "headers"))
        if '$' not in url:
            response = requestor.post_request(url, headers=headers, params=params)
            assertion.equals(response.status_code, 200)
            assertion.contains(response.text,validations)
        else:
            print("This case don't execute!")


