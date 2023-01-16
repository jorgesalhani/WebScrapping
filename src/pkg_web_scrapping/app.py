import requests
import bs4
from browser.firefox_webdriver import FirefoxBrowser

if __name__ == "__main__":
    driver = FirefoxBrowser()
    
    firefox = driver.open()
    firefox.get("https://www.google.com")

    driver.close()

    