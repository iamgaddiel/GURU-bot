from os import pread
import time
from mechanicalsoup import StatefulBrowser
import mechanicalsoup
import requests
import random
import string


def create_referral(username, counter) -> None:
    try:
        letters = string.ascii_uppercase
        random_word: str = ''.join(random.choice(letters) for i in range(10))

        sign_up_data = {
            'name': f'{random_word}',
            'username': f'{random_word}',
            'email': f'{random_word}@email.com',
            'password': f'{random_word}',
            'password_confirmation': f'{random_word}',
            'check': True,
        }

        url: str = f"https://ref.moneyguru.co/{username}"
        browser = StatefulBrowser()
        browser.open(url)
        if browser.url == "https://moneyguru.co":
            browser.open(browser.url)
            browser.follow_link('/register')
            browser.select_form('form[action="/register"]')
            browser['name'] = sign_up_data['name']
            browser['username'] = sign_up_data['username']
            browser['email'] = sign_up_data['email']
            browser['password'] = sign_up_data['password']
            browser['password_confirmation'] = sign_up_data['password_confirmation']
            browser['check'] = sign_up_data['check']
            response = browser.submit_selected()

            # check for successful form submission
            page = browser.page
            ref_label = page.find('div', class_="widget-title opacity-5 text-uppercase")
            if ref_label:
                print(f"{ref_label.text}: {counter}")

    except requests.exceptions.ConnectionError:
        print('You have network connection problem')
    except mechanicalsoup.LinkNotFoundError as e:
        print("I can't find your link", e)
    except mechanicalsoup.InvalidFormMethod as e:
        print("invalid form method", e)


counter: int = 1
referral_link: str = input('Enter username: ')
while True:
    time.sleep(1.00)
    create_referral(referral_link, counter)
    counter += 1

# test_referral(username, counter)
