from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

class FirefoxBrowser:
    def __init__(self, username, code_default) -> None:
        self.username = username
        self.code_default = code_default

    def open(self) -> Firefox:
        profile_path = (
            'C:\\Users\\{}\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\{}.default-release'
        ).format(self.username, self.code_default)

        options = Options()
        options.set_preference('profile', profile_path)
        service = Service(r'C:\\WebDriver\\bin\\geckodriver.exe')

        self.driver = Firefox(service=service, options=options)
        return self.driver

    def close(self) -> Firefox:
        return self.driver.quit()

