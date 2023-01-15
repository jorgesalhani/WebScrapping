import requests
import bs4

def req():
    return requests.get("https://www.google.com")

if __name__ == "__main__":
    print(req())