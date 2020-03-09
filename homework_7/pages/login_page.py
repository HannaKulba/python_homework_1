from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.open_page()
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form is not displayed at page'

    def login(self):
        self.open_page()
        self.should_be_login_page()
        login_field = self.browser.find_element(*LoginPageLocators.LOGIN_FIELD)
        login_field.send_keys('anna_kulba')
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        password_field.send_keys('ich8yuR7')
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.click()
