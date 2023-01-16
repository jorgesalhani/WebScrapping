import os
from src.pkg_web_scrapping.browser.firefox_webdriver import FirefoxBrowser
from src.pkg_web_scrapping.browser.firefox_profile import FirefoxProfile

profile = FirefoxProfile()


def test_username_healthcheck():
    assert profile.username == 'jorge'

def test_firefox_full_path_existence():
    full_path = 'C:\\Users\\{}\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles'.format(profile.username)
    assert os.path.exists(full_path)

def test_code_default_existence():
    code_default = profile.get_profile_code_default()
    assert code_default != ''

