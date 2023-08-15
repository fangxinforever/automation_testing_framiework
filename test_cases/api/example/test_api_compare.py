from common.api.requstsLib import Request
from common.base.json_compare import JsonCompare
from common.base import logger
from common.api.test_case_entity import TestCaseEntity
requestor = Request()
comparer = JsonCompare()
test_case_entity = TestCaseEntity()


class TestCompareJson:

    # def test_two_apis(self):
    #     data = test_case_entity.read_file_to_test_case("test_data/api/example/testAPICompare.csv")
    #     api1_data = Request().send_request(data[0]).json()
    #     api2_data = Request().send_request(data[1]).json()
    #     diff = comparer.compare(api1_data, api2_data)
    #     logger.info("result for comparing two apis is {}".format(diff))

    def test_two_strings(self):
        expect = """
          {
             "add": "haha",
             "name": "Andy",
             "age": 23,
             "family": ["mary"],
             "job": {
              "city": ["成都","苏州"],
              "location": "宽窄巷子",
              "company": "银泰心中"
             }
            }
            """
        actual = """
            {
             "content": null,
             "name": "Andy",
             "age": "23",
             "family": ["lucy","cindy"],
             "job": {
              "city": ["苏州","成都"],
              "location": "宽窄巷子",
              "company": "银泰中心"
             }
            }
            """
        diff = comparer.compare(expect, actual)
        logger.info("result for comparing two strings is {}".format(diff))


class TestCompareJson2:
    def test_two_strings(self):
        expect = """
          {
             "add": "haha",
             "name": "Andy",
             "age": 23,
             "family": ["mary"],
             "job": {
              "city": ["成都","苏州"],
              "location": "宽窄巷子",
              "company": "银泰心中"
             }
            }
            """
        actual = """
            {
             "content": null,
             "name": "Andy",
             "age": "23",
             "family": ["lucy","cindy"],
             "job": {
              "city": ["苏州","成都"],
              "location": "宽窄巷子",
              "company": "银泰中心"
             }
            }
            """
        diff = comparer.compare(expect, actual)
        logger.info("result for comparing two strings is {}".format(diff))