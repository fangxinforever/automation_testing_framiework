import json

import requests

from common.api import variables
from common.api.test_case_data_handle import TestCaseDataHandle
from common.api.test_case_entity import TestCaseEntity
from common.base.assert_result import BaseTest
from common.base.logger import LogFileOperation
from json import dumps

logger = LogFileOperation().logger
test_case_handle = TestCaseDataHandle()


class Request(requests.Session):
    request_e_log = "Interface requests an exception,reason：{}"

    def get_request(self, url, headers=None, params=None, cookies=None):
        """
        get method
        :param url:
        :param headers:
        :param params:
        :param cookies:
        :return:
        """
        try:
            res = self.request('GET', url, headers=headers, params=params, cookies=cookies, verify=False)
            self.api_log('GET', url, headers=headers, params=params, cookies=cookies,
                         code=res.status_code, res_text=res.text, res_header=res.headers)
            assert res.status_code == 200
            return res
        except Exception as e:
            logger.error(self.request_e_log.format(e))
            raise e

    def post_request(self, url, headers=None, data=None, json=None, params=None, cookies=None):
        """
        post method
        :param url:
        :param headers:
        :param data:
        :param json:
        :param params:
        :param cookies:
        :return:
        """
        try:
            res = self.request('POST', url, headers=headers, params=params, data=data,
                               json=json, cookies=cookies, verify=False)
            self.api_log('POST', url, headers=headers, params=params, json=json, data=data, cookies=cookies,
                         code=res.status_code, res_text=res.text, res_header=res.headers)
            return res

        except Exception as e:
            logger.error(self.request_e_log.format(e))
            raise e

    def put_request(self, url, headers=None, data=None, json=None, params=None, cookies=None):
        """
        put method
        :param url:
        :param headers:
        :param data:
        :param json:
        :param params:
        :param cookies:
        :return:
        """
        try:
            res = self.request('PUT', url, headers=headers, params=params, data=data,
                               json=json, cookies=cookies, verify=False)
            self.api_log('PUT', url, headers=headers, params=params, json=json, data=data, cookies=cookies,
                         code=res.status_code, res_text=res.text, res_header=res.headers)
            return res

        except Exception as e:
            logger.error(self.request_e_log.format(e))
            raise e

    def delete_request(self, url, headers=None, data=None, json=None, params=None, cookies=None):
        """
        delete method
        :param url:
        :param headers:
        :param data:
        :param json:
        :param params:
        :param cookies:
        :return:
        """
        try:
            res = self.request('DELETE', url, headers=headers, params=params, data=data,
                               json=json, cookies=cookies, verify=False)
            self.api_log('DELETE', url, headers=headers, params=params, json=json, data=data, cookies=cookies,
                         code=res.status_code, res_text=res.text, res_header=res.headers)
            return res

        except Exception as e:
            logger.error(self.request_e_log.format(e))
            raise e

    def api_log(self, method, url, headers=None, params=None, json=None, data=None, cookies=None, file=None, code=None,
                res_text=None, res_header=None):
        """
        api log detail
        :param method:
        :param url:
        :param headers:
        :param params:
        :param json:
        :param cookies:
        :param file:
        :param code:
        :param res_text:
        :param res_header:
        :return:
        """
        logger.info("request method====>{}".format(method))
        logger.info("request address====>{}".format(url))
        logger.info("request header====>{}".format(dumps(headers, indent=4)))
        logger.info("request parameter====>{}".format(dumps(params, indent=4)))
        logger.info("request body json====>{}".format(dumps(json, indent=4)))
        logger.info("request body data====>{}".format(dumps(data, indent=4)))
        logger.info("upload file======>{}".format(file))
        logger.info("Cookies====>{}".format(dumps(cookies, indent=4)))
        logger.info("response status code====>{}".format(code))
        logger.info("response header====>{}".format(res_header))
        logger.info("response body====>{}".format(res_text))

    def send_request(self, request_data: TestCaseEntity):
        """
        send any type of request
        :param method: request method
        :param request_data: should be TestCaseEntity
        :return:
        """
        method = request_data.method.upper()
        url = test_case_handle.var_replace(test_case_handle.url_handle(request_data.url), variables.get_items())
        # replace params or body variables
        headers = eval(test_case_handle.var_replace(request_data.headers, variables.get_items()))
        params = test_case_handle.var_replace(request_data.params, variables.get_items())
        request_payload = test_case_handle.request_payload_handle(request_data.request_payload)
        body_data = test_case_handle.var_replace(request_payload, variables.get_items())
        try:
            res = self.request(method=method, headers=headers, url=url, params=params, data=body_data)
            self.api_log(method=method, headers=headers, url=url, params=params, data=body_data,
                         code=res.status_code, res_text=res.text, res_header=res.headers)
        except Exception as e:
            logger.error(self.request_e_log.format(e))
            raise e
        if res is not None:
            BaseTest().equals(res.status_code, request_data.http_code)
            test_case_handle.validation_handle(dict(res.headers), request_data.response_header_validations)
            test_case_handle.var_handle(var_data=request_data.response_header_variables,
                                        response_data=dict(res.headers))
            test_case_handle.validation_handle(res.json(), request_data.validations)
            test_case_handle.var_handle(var_data=request_data.variables, response_data=res.json())
