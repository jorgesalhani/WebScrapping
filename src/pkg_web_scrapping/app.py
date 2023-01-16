from browser.firefox_webdriver import FirefoxBrowser
from browser.scrapping.firefox_auth import FirefoxAuth
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

if __name__ == "__main__":
    firefox_auth = FirefoxAuth()
    login_button = firefox_auth.get_login_button_element()
    print(login_button)

    firefox_auth.driver.close()
    