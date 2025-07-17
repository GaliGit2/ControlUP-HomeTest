from HomeTest.config import USERNAME, PASSWORD
from HomeTest.locators import USERNAME_INPUT, PASSWORD_INPUT, LOGIN_BUTTON
from HomeTest.helpers.ui_helpers import wait_and_send_keys, wait_and_click

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self):
        wait_and_send_keys(self.driver, *USERNAME_INPUT, USERNAME)
        wait_and_send_keys(self.driver, *PASSWORD_INPUT, PASSWORD)
        wait_and_click(self.driver, *LOGIN_BUTTON)

