import os
import unittest
from appium import webdriver
from common.base.variable import GetVariable as common
from common.app_ui import  apkInfo
from common.base.path import Base_path

# PATH = lambda p: os.path.abspath(
#     os.path.join(os.path.dirname(__file__), p)
# )


def appium_testcase(l_devices):
    apk_base = apkInfo.apkInfo(Base_path("/test_data/app_ui/Android-NativeDemoApp-0.2.1.apk"))
    desired_caps = {}
    desired_caps['platformName'] = l_devices["platformName"]
    desired_caps['platformVersion'] = l_devices["platformVersion"]
    desired_caps['deviceName'] = l_devices["deviceName"]
    desired_caps['appPackage'] = apk_base.get_apk_pkg()
    desired_caps['appActivity'] = apk_base.get_apk_activity()
    desired_caps['udid'] = l_devices["deviceName"]
    # desired_caps['app'] = PATH( '../img/t.apk')
    desired_caps["unicodeKeyboard"] = "True"
    desired_caps["resetKeyboard"] = "True"
    common.PACKAGE = apk_base.get_apk_pkg()
    remote = "http://127.0.0.1:" + str(l_devices["port"]) + "/wd/hub"
    driver = webdriver.Remote(remote, desired_caps)
    # common.DRIVER = driver
    # common.FLAG = False
    return driver

class TestInterfaceCase(unittest.TestCase):
    def __init__(self, methodName='runTest', l_devices=None):
        super(TestInterfaceCase, self).__init__(methodName)
        self.l_devices = l_devices
        # self.driver = ""

    def setUp(self):
        if self.l_devices["platformName"] == common.ANDROID:
            self.driver = appium_testcase(self.l_devices)

    def tearDown(self):
        # self.driver.close_app()
        # self.driver.quit()
        pass

    @staticmethod
    def tearDownClass():
        # driver.close_app()
        # driver.quit()
        print('tearDownClass')

    # @staticmethod
    # def parametrize(testcase_klass, l_devices=None):
    #     testloader = unittest.TestLoader()
    #     testnames = testloader.getTestCaseNames(testcase_klass)
    #     suite = unittest.TestSuite()
    #     for name in testnames:
    #         suite.addTest(testcase_klass(name, l_devices=l_devices[0]))
    #     return suite

