from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    _login_button = {"by": By.ID, "value": "login2"}
    _username_input = {"by": By.ID, "value": "loginusername"}
    _password_input = {"by": By.ID, "value": "loginpassword"}
    _submit_button = {"by": By.XPATH, "value": "//button[normalize-space()='Log in']"}
    _success_message = {"by": By.ID, "value": "nameofuser"}
    _failure_message = {"by": By.CSS_SELECTOR, "value": ".flash.error"}
    _login_form = {"by": By.ID, "value": "logInModal"}

    def __init__(self, driver):
        self.driver = driver
        self._visit("/")
        assert self._get_title() == 'STORE'

    def with_(self, username, password):
        self._click(self._login_button)
        self._is_displayed(self._login_form, 5)
        self._type(self._username_input, username)
        self._type(self._password_input, password)
        self._click(self._submit_button)

    def success_message_present(self):
        return self._is_displayed(self._success_message, 5)

    def failure_message_present(self):
        return self._get_alert_text() in ('User does not exist.', 'Wrong password.')

    def test_invalid_credentials(self, login):
        login.with_("tomsmith", "bad password")
        assert login.failure_message_present()
