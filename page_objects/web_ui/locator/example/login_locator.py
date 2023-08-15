from selenium.webdriver.common.by import By

class LoginLocator:
    email = By.ID, "email"
    password = By.ID, "pass"
    log_in_btn = By.NAME, "login"
