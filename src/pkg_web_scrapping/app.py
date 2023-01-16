import requests
import bs4


from browser.firefox_profile import FirefoxProfile

def req():
    return requests.get("https://www.google.com")

if __name__ == "__main__":
    profile = FirefoxProfile()
    print(profile.get_profile_code_default())