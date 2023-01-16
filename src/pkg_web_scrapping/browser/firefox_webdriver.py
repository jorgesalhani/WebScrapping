from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from .firefox_profile import FirefoxProfile
import os

class FirefoxBrowser:
    def __init__(self) -> None:
        self.driver = None

    def open(self) -> Firefox:
        profile = FirefoxProfile()
        profile_path = profile.get_profile_default_path()

        options = Options()
        options.set_preference('profile', profile_path)

        service_path = self.get_geckodriver_path(username=profile.username)
        if self.__check_file_exists(service_path):
            service = Service(service_path)
            self.driver = Firefox(service=service, options=options)
            
        return self.driver

    def close(self) -> Firefox:
        return self.driver.quit()

    def get_geckodriver_path(self, username: str) -> str:
        service_path = (
            "C:\\Users\\{}\\Downloads\\geckodriver-v0.32.0-win64\\geckodriver.exe"
            .format(username)
        )
        return service_path

    def __check_file_exists(self, path: str) -> bool:
        return os.path.exists(path)
