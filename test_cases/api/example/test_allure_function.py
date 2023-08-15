import allure
import pytest

from common.base.config import conf

@allure.epic("this is allure epic")
@allure.feature("allure module feature")
@allure.suite("this is allure test suites")
class TestAllure():

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("allure story")
    @allure.title("test_allure_case1")
    @allure.description("test_allure_case1 description")
    @allure.link(url=eval(conf.get("api_env", "base_url")))  # access url
    @allure.testcase(url="ALLURE_001")  # bug link
    @allure.issue(url=eval(conf.get("api_env", "bug_url")))  # testcase link
    @allure.tag("this is allure tag")
    def test_allure_case1(self):
        pass

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("allure story")
    @allure.title("test_allure_case2")
    @allure.description("test_allure_case2 description")
    @allure.link(url=eval(conf.get("api_env", "base_url")))  # access url
    @allure.testcase(url="ALLURE_002")  # bug link
    @allure.issue(url=eval(conf.get("api_env", "bug_url")))  # testcase link
    @allure.tag("this is allure tag")
    def test_allure_case2(self):
        pass

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("allure story")
    @allure.title("test_allure_case3")
    @allure.description("test_allure_case3 description")
    @allure.link(url=eval(conf.get("api_env", "base_url")))  # access url
    @allure.testcase(url="ALLURE_003")  # bug link
    @allure.issue(url=eval(conf.get("api_env", "bug_url")))  # testcase link
    @allure.tag("this is api tag")
    def test_allure_case3(self):
        pass

    @allure.severity(allure.severity_level.MINOR)
    @allure.story("allure story")
    @allure.title("test_allure_case4")
    @allure.description("test_allure_case4 description")
    @allure.link(url=eval(conf.get("api_env", "base_url")))  # access url
    @allure.testcase(url="ALLURE_004")  # bug link
    @allure.issue(url=eval(conf.get("api_env", "bug_url")))  # testcase link
    @allure.tag("this is allure tag")
    def test_allure_case4(self):
        pass

    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.story("allure story")
    @allure.title("test_allure_case5")
    @allure.description("test_allure_case5 description")
    @allure.link(url=eval(conf.get("api_env", "base_url")))  # access url
    @allure.testcase(url="ALLURE_005")  # bug link
    @allure.issue(url=eval(conf.get("api_env", "bug_url")))  # testcase link
    @allure.tag("this is allure tag")
    @pytest.mark.skip("test skip function")
    def test_allure_case5(self):
        pass


