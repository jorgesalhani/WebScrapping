from ..firefox_webdriver import FirefoxBrowser
from bs4 import BeautifulSoup
import itertools

class FirefoxAuth:
    def __init__(self, headless=False) -> None:
        self.driver = None
        self.headless = headless

    def access_google_page(self):
        firefox = FirefoxBrowser(headless=self.headless)
    
        driver = firefox.open()
        driver.get("https://www.google.com")

        return driver

    def get_login_button_element(self) -> list:
        driver_google = self.access_google_page()
        self.driver = driver_google

        soup_google = BeautifulSoup(self.driver.page_source, features="html.parser")
        login_button = soup_google.find_all(
            lambda tag: len(tag.find_all()) == 0 and "login" in tag.text
        )
        return login_button

    def xpath_soup(self, element):
        """
        Generate xpath of soup element
        :param element: bs4 text or node
        :return: xpath as string
        """
        components = []
        child = element if element.name else element.parent
        for parent in child.parents:
            """
            @type parent: bs4.element.Tag
            """
            previous = itertools.islice(parent.children, 0, parent.contents.index(child))
            xpath_tag = child.name
            xpath_index = sum(1 for i in previous if i.name == xpath_tag) + 1
            components.append(xpath_tag if xpath_index == 1 else '%s[%d]' % (xpath_tag, xpath_index))
            child = parent
        components.reverse()
        return '/%s' % '/'.join(components)