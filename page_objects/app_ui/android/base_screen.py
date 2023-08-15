from appium.webdriver.common.mobileby import MobileBy
from common.app_ui.appiumdriver import Driver


class BaseScreen(Driver):
    """
    common screen locators
    """

    def __init__(self, driver):
        super().__init__(driver)