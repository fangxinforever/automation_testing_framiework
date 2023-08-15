from appium.webdriver.common.mobileby import MobileBy
from common.app_ui.appiumdriver import Driver


class LoginScreen(Driver):
    """
    login screen locators
    """
    inputField = (MobileBy.XPATH, '//android.widget.EditText[@content-desc="input-email"]')
    passwordField = (MobileBy.ACCESSIBILITY_ID, 'input-password')
    loginButton = (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="button-LOGIN"]/android.view.ViewGroup')

    def __init__(self, driver):
        super().__init__(driver)