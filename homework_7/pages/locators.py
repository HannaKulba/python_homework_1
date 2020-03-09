from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FORM = (By.CLASS_NAME, 'pbBody')
    LOGIN_FIELD = (By.CSS_SELECTOR, '#loginValue > input')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '#passwordValue > input')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '.btn.btn--large.btn--colored')


class HomePageLocators:
    PROFILE = (By.CLASS_NAME, 'user-account')
