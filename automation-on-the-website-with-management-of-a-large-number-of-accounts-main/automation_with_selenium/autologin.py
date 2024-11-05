import os
import time
import json
import requests
import pyautogui
import threading



import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from paths import *
import manager

screen_width, screen_height = pyautogui.size()

def login_via_requests(profile: str, thread_id: int):

    url = "https://url.com/"
    prefix = f'({profile})'

    steam_cookies_path = f'{COOKIES_STEAM_PATH}\\{profile}.json'

    print(f'{prefix} Rozpoczynam proces logowania do konta')

    if not os.path.exists(steam_cookies_path):
        print(f'{prefix} Brak ciasteczek steam, muszę zalogować się za pomocą selenium i je wygenerować')
        login_via_selenium(profile, thread_id)
        return

    print(f'{prefix} Posiadam ciasteczka steam, loguję się za pomocą requestów')
    cookies = {}

    with open(steam_cookies_path, 'r') as file:
        text = file.read()
        if text: cookies = json.loads(text)

    with requests.Session() as session:

        response = session.get(url, allow_redirects=True)

        print(f"{prefix} Status odpowiedzi:", response.status_code)

        if response.status_code == 200:

            print(f'{prefix} Wykonuję drugi request do steam')
            response2 = session.get(response.url, cookies=cookies)

def login_via_selenium(profile: str, thread_id: int, login_link = ''):

    prefix = f'({profile})'

    print(f'{prefix} Loguję za pomocą selenium...')

    user_data_dir = f'{PROFILES_PATH}\\{profile}'
    driver = uc.Chrome(user_data_dir=user_data_dir, version_main=CHROME_VERSION, driver_executable_path='chromedriver.exe')
    driver.set_window_size(screen_width // 2, screen_height // 2)
    
    if thread_id == 0: driver.set_window_position(0, 0)
    elif thread_id == 1: driver.set_window_position(screen_width // 2, 0)
    elif thread_id == 2: driver.set_window_position(0, screen_height // 2)
    elif thread_id == 3: driver.set_window_position(screen_width // 2, screen_height // 2)

    print(f'{prefix} Przeglądarka chodzi')

    if login_link:
        print(f'{prefix} Loguję za pomocą linku...')
        driver.get(login_link)
    else:
        print(f"{prefix} Loguję za pomocą steam'a...")
        driver.get("https://url.com/")

        print(f'{prefix} Szukam przycisku logowania...')

        #try:
        button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn_green_white_innerfade')))
        #except Exception as e:
            #print('Error 1' ,e)
            #return False

        print(f'{prefix} Pobieram ciasteczka steam...')
        steam_cookies = driver.get_cookies()
        print('pobrano:', steam_cookies)
        
        steam_cookies_ready = {}
        for cookie in steam_cookies: steam_cookies_ready[cookie['name']] = cookie['value']

        manager.set_cookies_steam(profile, json.dumps(steam_cookies_ready))

        print(f'{prefix} Klikam przycisk...')
        button.click()

        try: key_drop_loaded = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.block')))
        except: return False

    time.sleep(3) # TO CHANGE
    driver.refresh()
    time.sleep(2)
    site_cookies = driver.get_cookies()

    cookies_ready = {}
    for cookie in site_cookies: cookies_ready[cookie['name']] = cookie['value']

    manager.set_cookies(profile, json.dumps(cookies_ready))
    manager.set_vioshield(cookies_ready['__vioShield']))

    manager.set_as_logged_in(profile)
    driver.close()

def autologin_once(profile: str, thread_id: int):
    login_via_selenium(profile, thread_id)

def autologin_threads(profiles: list):

    def collect_group(profiles2: list, thread_id: int):
        for profile in profiles2: autologin_once(profile, thread_id)

    profiles_grops = []
    number_of_threads = 4

    for _ in range(number_of_threads): profiles_grops.append([])

    n = 0
    for profile in profiles:
        profiles_grops[n].append(profile)
        if n >= number_of_threads - 1: n = 0
        else: n += 1

    threads = []

    for i in range(number_of_threads):
        thread = threading.Thread(target=collect_group, args=(profiles_grops[i], i, ))
        threads.append(thread)

    for thread in threads: thread.start()
    for thread in threads: thread.join()

if __name__ == '__main__':
    for i in range(271,301):
        autologin_once(f'Profile {i}', 0)
