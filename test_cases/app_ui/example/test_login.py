import pytest
from common.app_ui.appiumdriver import Driver
from page_objects.app_ui.android.home_screen import HomeScreen
from page_objects.app_ui.android.login_screen import LoginScreen
from common.app_ui.app import App

class TestLogin(Driver):
    def __init__(self, driver):
        super().__init__(driver)

    def test_login(self):
        App.click(self, HomeScreen.loginMenu)
        App.send_keys(self, LoginScreen.inputField, "johnsmith@gmail.com")
        App.send_keys(self, LoginScreen.passwordField, "password", index=0)
        App.tap(self, LoginScreen.inputField)

