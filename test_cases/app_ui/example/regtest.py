import os
import time
from page_objects.app_ui.android.home_screen import HomeScreen
from page_objects.app_ui.android.login_screen import LoginScreen
from common.app_ui.app import App
from common.app_ui.parmer import Parmer
from common.base import logger
from appium import webdriver
from common.base.path import Base_path

class regtest(Parmer):
    def __init__(self, parme,methodName='runTest'):
        super(regtest,self).__init__(methodName)
        self.capability = parme[0]
        self.app = self.capability["platformType"]
        self.device = self.capability["deviceType"]
        self.port = self.capability["port"]

    def setUp(self):
        """
        This method instantiates the appium driver
        """
        global desired_caps

        logger.info("Configuring desired capabilities")
        if self.app == 'ANDROID':
            desired_caps = self.android()

        logger.info("Initiating Appium driver")
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        logger.info('connect to device')

    def android(self):
        if self.device == 'SIMULATOR':
            return dict(platformName=self.capability["platformName"],
                        platformVersion=self.capability["platformVersion"],
                        deviceName=self.capability["deviceName"],
                        app=os.path.join(Base_path, self.capability["app"]),
                        noReset=True)
        elif self.device == 'real device':
            return dict(platformName='Android', platformVersion='', deviceName='PF',
                        app=f'{os.popen("pwd").read().rstrip()}/data/apps/Android-NativeDemoApp-0.2.1.apk',
                        noReset=True)

    def tearDown(self):
        """ tearDown  """
        logger.info('The test case has been executed and the test environment is being restored！')
        time.sleep(15)
        self.driver.quit()
    def test_login(self):
        App.click(self, HomeScreen.loginMenu)
        App.send_keys(self, LoginScreen.inputField, "johnsmith@gmail.com")
        App.send_keys(self, LoginScreen.passwordField, "password", index=0)
        App.tap(self, LoginScreen.inputField)