from os import pipe
import time
from mechanicalsoup import StatefulBrowser
import requests


def click_ref_link(username: str, counter: int):
    try:
        url: str = f"https://ref.moneyguru.co/{username}"
        browser = StatefulBrowser()
        browser.open(url)
        if browser.url == "https://moneyguru.co":
            print(f'{counter}: clicked', url)
    except requests.exceptions.ConnectionError:
        print('You have network connection problem')

counter: int = 1
username: str = input('Enter your username: ')
while True:
    time.sleep(1.00)
    click_ref_link(username, counter)
    counter += 1
