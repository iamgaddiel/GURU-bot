from os import pipe
import time
from mechanicalsoup import StatefulBrowser
import requests

# time.sleep(2.00)


def click_ref_link(username):
    try:
        counter: int = 1
        url: str = f"https://ref.moneyguru.co/{username}"
        browser = StatefulBrowser()
        browser.open(url)
        
        if browser.url == "https://moneyguru.co":
            print(f'{counter}: clicked', url)

    except requests.exceptions.ConnectionError:
        print('You have network connection problem')


username: str = input('Enter your username: ')
while True:
    time.sleep(1.00)
    click_ref_link(username)
    