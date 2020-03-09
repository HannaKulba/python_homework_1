from .base_page import BasePage
from .locators import HomePageLocators


class HomePage(BasePage):
    def should_be_home_page(self):
        self.should_be_home_url()
        self.should_be_profile()

    def should_be_profile(self):
        assert self.is_element_present(*HomePageLocators.PROFILE), 'No profile on home page'

    def should_be_home_url(self):
        home_url = 'https://senla-portal.secure.force.com/portal/BasicPage?currentApp=Home'
        assert home_url == self.browser.current_url, 'This is not home page'
