from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_dollar_rate(url):
    options = Options()
    options.add_argument('--start-maximized')
    browser = webdriver.Chrome('./chromedriver/chromedriver.exe', options=options)
    browser.get(url)
    dollar_rate = browser.find_element_by_id('currency-informer').text
    print(dollar_rate)
    browser.quit()


if __name__ == '__main__':
    get_dollar_rate('https://www.onliner.by/')
