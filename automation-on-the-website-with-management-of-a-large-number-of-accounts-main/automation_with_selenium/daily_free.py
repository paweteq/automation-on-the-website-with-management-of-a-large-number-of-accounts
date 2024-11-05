import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import autologin
import datetime

import threading
import paths
import manager
import pyautogui
import json
import os

screen_width, screen_height = pyautogui.size()


def daily_free(profile: str, thread_id: int):

    prefix = f'({profile})'

    user_data_dir = f'{paths.PROFILES_PATH}\\{profile}'
    driver = uc.Chrome(user_data_dir=user_data_dir, version_main=paths.CHROME_VERSION, driver_executable_path='chromedriver.exe')
    driver.set_window_size(screen_width // 2, screen_height // 2)
    
    if thread_id == 0: driver.set_window_position(0, 0)
    elif thread_id == 1: driver.set_window_position(screen_width // 2, 0)
    elif thread_id == 2: driver.set_window_position(0, screen_height // 2)
    elif thread_id == 3: driver.set_window_position(screen_width // 2, screen_height // 2)

    print(f'{prefix} Przeglądarka chodzi')
    print(f"{prefix} Loguję za pomocą steam'a...")
    driver.get(f"https://url.com/pl/daily-case")

    print(f'{prefix} Szukam przycisku logowania...')
    try:
            current_handle = driver.current_window_handle
            print('włączam kartę:',current_handle)
            try:
                zaloguj = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.button.max-w-full.bg-gold-400')))
                driver.close()
                autologin.login_via_selenium(profile, thread_id)
                time.sleep(2)
                driver.get(f"https://url.com/pl/daily-case")
                try:
                     colect_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.group.pb-3.pt-7.cursor-pointer')))
                     colect_button.click()
                     time.sleep(3)
                     value=WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'li.snap-center')))
                     values=value.text.split('\n')
                     price=values[1].replace('ZŁOTO','')
                     with open(f'memory\\dailyfree\\{datetime.datetime.now().strftime("%Y-%m-%d")}\\{profile}', 'w') as file:
                        file.write(str(price))
                     print(f'{prefix} Odebrał: {values[1]}')
                     site_cookies = driver.get_cookies()
                     cookies_ready = {}
                     for cookie in site_cookies: cookies_ready[cookie['name']] = cookie['value']
                     manager.site_cookies(profile, json.dumps(cookies_ready))
                     time.sleep(2)
                     driver.close()
                except:
                     try:
                        value=WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'li.snap-center')))
                        values=value.text.split('\n')
                        price=values[1].replace('ZŁOTO','')
                        with open(f'memory\\dailyfree\\{datetime.datetime.now().strftime("%Y-%m-%d")}\\{profile}', 'w') as file:
                            file.write(str(price))
                        print(f'{prefix} Odebrał: {values[1]}')
                        site_cookies = driver.get_cookies()
                        cookies_ready = {}
                        for cookie in site_cookies: cookies_ready[cookie['name']] = cookie['value']
                        manager.site_cookies(profile, json.dumps(cookies_ready))
                        time.sleep(2)
                        driver.close()

                     except:
                        print('nie wykryło przycisku')
                        time.sleep(1)
                        driver.close()
            except:
                try:
                     colect_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.group.pb-3.pt-7.cursor-pointer')))
                     colect_button.click()
                     time.sleep(3)
                     value=WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'li.snap-center')))
                     values=value.text.split('\n')
                     price=values[1].replace('ZŁOTO','')
                     with open(f'memory\\dailyfree\\{datetime.datetime.now().strftime("%Y-%m-%d")}\\{profile}', 'w') as file:
                        file.write(str(price))
                     print(f'{prefix} Odebrał: {values[1]}')
                     site_cookies = driver.get_cookies()
                     cookies_ready = {}
                     for cookie in site_cookies: cookies_ready[cookie['name']] = cookie['value']
                     manager.site_cookies(profile, json.dumps(cookies_ready))
                     time.sleep(2)
                     driver.close()
                except:
                     try:
                        value=WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'li.snap-center')))
                        values=value.text.split('\n')
                        price=values[1].replace('ZŁOTO','')
                        with open(f'memory\\dailyfree\\{datetime.datetime.now().strftime("%Y-%m-%d")}\\{profile}', 'w') as file:
                            file.write(str(price))
                        print(f'{prefix} Odebrał: {values[1]}')
                        keydrop_cookies = driver.get_cookies()
                        cookies_ready = {}
                        for cookie in keydrop_cookies: cookies_ready[cookie['name']] = cookie['value']
                        manager.set_cookies_keydrop(profile, json.dumps(cookies_ready))
                        time.sleep(2)
                        driver.close()

                     except:
                        print('nie wykryło przycisku')
                        time.sleep(1)
                        driver.close()
                
    except:
          print("błąd")
          driver.close()
def daily_threads(profiles: list):

    def daily_collect(profiles2: list, thread_id: int):
        for profile in profiles2: daily_free(profile, thread_id)

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
        thread = threading.Thread(target=daily_collect, args=(profiles_grops[i], i, ))
        threads.append(thread)

    for thread in threads: thread.start()
    for thread in threads: thread.join()

def roznica_list():
    lista = manager.get_enabled_profiles()
    odebrane=os.listdir(f'{paths.DAILYFREE_PATH}\\{datetime.datetime.now().strftime("%Y-%m-%d")}')
    return list(set(lista) - set(odebrane))
    

def main():
    output=roznica_list()
    if len(output)>30:
        print("Zmiejszam zbiór do 30 elementów")
        output=output[:30]
    daily_threads(output)
