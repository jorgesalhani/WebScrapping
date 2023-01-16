from src.pkg_web_scrapping.browser.scrapping.firefox_auth import FirefoxAuth
import re

auth = FirefoxAuth(headless=True)

def test_google_page_healthcheck():
    driver = auth.access_google_page()
    google_url = driver.current_url
    driver.close()
    assert google_url == 'https://www.google.com/'

def test_google_login_button():
    button_content = auth.get_login_button_element()
    res = re.search('login', str(button_content[0]))
    assert bool(res)

def test_google_login_xpath():
    button_content = auth.get_login_button_element()
    xpath = auth.xpath_soup(button_content[0])
    assert xpath == "/html/body/div[1]/div[1]/div/div/div/div[2]/a"