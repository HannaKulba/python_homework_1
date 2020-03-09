from homework_7.pages.login_page import LoginPage
from homework_7.pages.home_page import HomePage
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function')
def browser():
    options = Options()
    options.add_argument('--start-maximized')
    print('\nstart browser...')
    browser = webdriver.Chrome('../../selenium/chromedriver/chromedriver.exe', options=options)
    yield browser
    print('\nquit browser...')
    browser.quit()


def test_login_to_senla_portal(browser):
    url = 'https://senla-portal.secure.force.com/portal/BasicPage'
    login_page = LoginPage(browser, url)
    login_page.login()
    home_page = HomePage(browser, browser.current_url)
    home_page.should_be_home_page()
