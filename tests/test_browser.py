import os
from src.pkg_web_scrapping.browser.firefox_profile import FirefoxProfile
from src.pkg_web_scrapping.browser.firefox_webdriver import FirefoxBrowser

profile = FirefoxProfile()

def test_username_healthcheck():
    assert profile.username == os.getlogin()

def test_firefox_full_path_existence():
    full_path = 'C:\\Users\\{}\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles'.format(profile.username)
    assert os.path.exists(full_path)

def test_code_default_existence():
    code_default = profile.get_profile_default_path()
    assert code_default != ''

def test_geckodriver_firefox_service():
    driver = FirefoxBrowser()
    gecko_path = driver.get_geckodriver_path(profile.username)
    assert os.path.exists(gecko_path)
    