from common.base import logger


class BaseTest:
    def equals(self, actual, expected):
        """
        assert if it is equal
        :param actual:
        :param expected:
        :return:
        """
        try:
            assert actual == expected
            logger.info("assert successful,actual value：{} is equal to expected value：{}".format(actual, expected))
        except AssertionError:
            logger.error("assert fail,actual value：{} isn't equal to expected value：{}".format(actual, expected))
            raise AssertionError

    def assert_true(self, actual):
        """
        assert if it is true
        :param actual:
        :return:
        """
        try:
            assert actual is True
            logger.info("assert successful,actual value：{} is true".format(actual))
        except AssertionError:
            logger.error("assert fail,actual value：{} is false".format(actual))
            raise AssertionError

    def contains(self, content, target):
        """
        assert if contains text
        :param content: actual text
        :param target: contains text
        :return:
        """
        try:
            assert target in content
            logger.info("assert successful,actual texts：{} contains texts：{}".format(content, target))
        except AssertionError:
            logger.error("assert fail,actual texts：{} don't contain texts：{}".format(content, target))
            raise AssertionError

    def exists(self, actual):
        """
        assert if field exists
        :param actual: field name
        :return:
        """
        try:
            assert actual is not None
            logger.info("assert successful,field exist:{}".format(actual))
        except AssertionError:
            logger.error("assert failed,field doesn't exist:{}".format(actual))
            raise AssertionError
