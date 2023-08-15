import pytest
import unittest
import os
from datetime import datetime
from appium import webdriver
from common.base import logger
from pytest_html_reporter import attach

# class appiumServer():
#     def __init__(self,devices):
#         self.server = server.AppiumServer(devices)
class Driver(unittest.TestCase):

    def __init__(self, driver):
        super().__init__(driver)

    def setUp(self):
        """
        This method instantiates the appium driver
        """
        global desired_caps

        logger.info("Configuring desired capabilities")
        if self.app == 'ios':
            desired_caps = self.ios()

        elif self.app == 'android':
            desired_caps = self.android()
            print(desired_caps)

        logger.info("Initiating Appium driver")
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

        # set waits
        self.driver.implicitly_wait(5)  # waits 5 seconds

    def android(self):
        if self.device == 'emulator':
            return dict(platformName='Android', platformVersion='10.0.0', deviceName='emulator-5554',
                        app=f'/Users/tom_li/sourcecode/python/python_automation_framework/test_data/app_ui/Android-NativeDemoApp-0.2.1.apk', noReset=True)
        elif self.device == 'real device':
            return dict(platformName='Android', platformVersion='', deviceName='PF',
                        app=f'{os.popen("pwd").read().rstrip()}/data/apps/Android-NativeDemoApp-0.2.1.apk', noReset=True)

    def ios(self):
        if self.device == 'simulator':
            return dict(platformName='iOS', platformVersion='13.3', deviceName='iPhone 11',
                        app=f'{os.popen("pwd").read().rstrip()}/data/apps/iOS-Simulator-NativeDemoApp-0.2.1.app',
                        automationName='XCUITest')
        # elif self.device == 'real device':
        #     return dict(platformName='iOS', platformVersion='14.0', deviceName='iPhone X',
        #                 udid=f'{UDID}', useNewWDA=True,
        #                 app=f'{os.popen("pwd").read().rstrip()}/data/apps/iOS-RealDevice-NativeDemoApp-0.2.1.ipa',
        #                 automationName='XCUITest')
        elif self.device == 'bitrise':
            return dict(platformName='iOS', platformVersion='13.0', deviceName='iPhone-11',
                        udid='E04A6F53-4C3B-4810-B210-DD2015D0D064', useNewWDA=True,
                        app=f'{os.popen("pwd").read().rstrip()}/data/apps/iOS-Simulator-NativeDemoApp-0.2.1.app', automationName='XCUITest')

    def tearDown(self):
        Driver.screenshot_on_failure(self)
        attach(data=self.driver.get_screenshot_as_png())
        self.driver.quit()

    def screenshot_on_failure(self):
        today = datetime.now()
        now = today.strftime('%Y-%m-%d_%H-%M-%S')
        test_name = self._testMethodName
        for self._testMethodName, error in self._outcome.errors:
            if error:
                self.logger.error("Taking screenshot on failure")
                if not os.path.exists('screenshots'):
                    os.makedirs('screenshots')

                self.driver.save_screenshot(f"screenshots/{test_name}_{now}.png")

    @pytest.fixture(autouse=True)
    def cli(self, app, device):
        self.app = 'android'
        self.device = device

    def wda_port(self):
        return 8100

    def android_device_name(self):
        return 'emulator-5554'
