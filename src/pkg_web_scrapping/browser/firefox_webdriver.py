from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from .firefox_profile import FirefoxProfile
import os

class FirefoxBrowser:
    def __init__(self, headless=False) -> None:
        self.driver = None
        self.headless = headless

    def open(self) -> webdriver.Firefox:
        profile = FirefoxProfile()
        profile_path = profile.get_profile_default_path()

        options = Options()
        options.set_preference('profile', profile_path)
        if self.headless: options.add_argument("--headless")

        service_path = self.get_geckodriver_path(username=profile.username)
        if self.__check_file_exists(service_path):
            service = Service(service_path)
            self.driver = webdriver.Firefox(service=service, options=options)
            
        return self.driver

    def close(self) -> webdriver.Firefox:
        return self.driver.quit()

    def get_geckodriver_path(self, username: str) -> str:
        service_path = (
            "C:\\Users\\{}\\Downloads\\geckodriver-v0.32.0-win64\\geckodriver.exe"
            .format(username)
        )
        return service_path

    def __check_file_exists(self, path: str) -> bool:
        return os.path.exists(path)
