import json
import os
from string import Template

from jsonpath import jsonpath

from common.api import variables

from common.base.assert_result import BaseTest
from common.base.config import conf
from common.base.json_operator import JsonOperation
from common.base.path import Base_path
from common.base.yml_util import read_yml
from common.base import logger

base_test = BaseTest()


class TestCaseDataHandle:

    def url_handle(self, url):
        """
        handle url from csv file
        :param url: request url ,can be full path or relative path
        :return:
        """
        url_after = ""
        if url.startswith('http'):
            url_after = url
        elif url.startswith('/'):
            url_after = eval(conf.get("api_env", "base_url")) + url
        return url_after

    def validation_handle(self, response_data, validation_data):
        """
        handle validation from csv file
        :param response_data: api response data
        :param validation_data: including jsonpath and expected value
        :return:
        """
        if validation_data == "":
            return
        validation_list = []
        for k, v in json.loads(validation_data).items():
            validation_list.append((k, v))
        for validation in validation_list:
            json_path = validation[0]
            actual_value = jsonpath(response_data, json_path)[0]
            logger.info("actual_values is :{}".format(actual_value))

            if str(validation[1]).find("(") == -1:
                assert_type = "equals"
                expect_value = validation[1]
            else:
                assert_type = str(validation[1]).split("(")[0]
                expect_value = str(validation[1]).split("(")[1].split(")")[0]
            try:
                assert_func = getattr(BaseTest(), assert_type)
                if expect_value == "":
                    assert_func(actual_value)
                else:
                    assert_func(actual_value, expect_value)
            except AttributeError:
                logger.error("There is no such assert type:{}".format(assert_type))
                raise AttributeError

    def var_handle(self, var_data, response_data):
        """
        set variables from response data
        :param var_data: including variable name and variable jsonpath
        :param response_data: api response
        :return:
        """
        if var_data == "":
            return
        for k, v in json.loads(var_data).items():
            variables.set_value(k, jsonpath(response_data, v)[0])
        logger.info("variables:{}".format(variables.get_items()))

    def var_replace(self, request_data, replace_var):
        """
        replace variables in request body or request params
        :param request_data: request body or request params
        :param replace_var: global variables
        :return:
        """
        if "$" in request_data:
            return Template(request_data).safe_substitute(replace_var)
        else:
            return request_data

    def request_payload_handle(self, request_data):
        """
        handle request payload,if it is a file path,then read data from files
        :param request_data: RequestPayload from test_data files
        :return:
        """
        if '.json' in request_data:
            return json.dumps(JsonOperation().read_json_file(os.path.join(Base_path, request_data)))
        elif '.yml' in request_data:
            return json.dumps(read_yml(request_data))
        else:
            return request_data
