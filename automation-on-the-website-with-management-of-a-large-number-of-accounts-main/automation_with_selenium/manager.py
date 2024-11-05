import os
import time
import json
import random
import subprocess
import pygetwindow

import colors
from paths import *

# ==================================================
# Codes
# ==================================================

def get_today_number_of_codes(_date = TODAY):

    path = f'{RECEIVED_CODES_BY_DATE_PATH}\\{_date}'
    if not os.path.exists(path): return 0
    return len(os.listdir(path))

def set_code_received(profile: str, code: str, gold_amount: int = 0):

    rc_path = f'{RECEIVED_CODES_PATH}\\{code}'
    rcdate_path = f'{RECEIVED_CODES_BY_DATE_PATH}\\{TODAY}'

    if not os.path.exists(rc_path): 
        try: os.makedirs(rc_path)
        except: pass

    if not os.path.exists(rcdate_path):
        try: os.makedirs(rcdate_path)
        except: pass

    with open(f'{rcdate_path}\\{code}', 'a', encoding='utf-8') as file: pass
    with open(f'{rc_path}\\{profile}', 'a', encoding='utf-8') as file: pass
    
    if gold_amount: set_code_amount(code, gold_amount)

    print(f'{colors.GREEN}(code received) {colors.LIGHT_GREEN}{profile}{colors.RESET} odebrał kodzik -> {colors.YELLOW}{code}')

def set_code_amount(code: str, amount: int, force_update: bool = False):
    try:
        if not os.path.exists(f'{CODES_AMOUNT_PATH}\\{code}') or force_update:
            with open(f'{CODES_AMOUNT_PATH}\\{code}', 'w', encoding='utf-8') as file: file.write(amount)
    except: pass

def get_code_amount(code: str):

    if not os.path.exists(f'{CODES_AMOUNT_PATH}\\{code}'): return 0

    with open(f'{CODES_AMOUNT_PATH}\\{code}', 'r', encoding='utf-8') as file:
        try:
            gold_amount = int(file.read())
            return gold_amount
        except: return 0

# ==================================================
# Dailyfree
# ==================================================

def get_dailyfree_failed_profiles():
    profiles = get_all_profiles()
    received_profiles = os.listdir(f'{TODAY_DAILYFREE_PATH}')

    output = []
    for profile in profiles:
        if not profile in received_profiles: output.append(profile)

    return output

def set_dailyfree_received(profile: str):
    with open(f'{TODAY_DAILYFREE_PATH}\\{profile}', 'a') as file: pass

# ==================================================
# Cookies
# ==================================================

def extract_cookies(driver, link: str = ''):
    if link:
        driver.get(link)
        time.sleep(2)
    cookies = driver.get_cookies()
    return prepare_cookies(cookies)

def prepare_cookies(cookies: list):
    cookies_ready = {}
    for cookie in cookies: cookies_ready[cookie['name']] = cookie['value']
    return cookies_ready

def set_cookies_site(profile: str, cookies: str):
    with open(f'{COOKIES_KD_PATH}\\{profile}.json', 'w', encoding='utf-8') as file: file.write(cookies)

def set_cookies_steam(profile: str, cookies: str):
    with open(f'{COOKIES_STEAM_PATH}\\{profile}.json', 'w', encoding='utf-8') as file: file.write(cookies)

def set_vioshield(vioshield: str):
    with open(f'{MEMORY_PATH}\\vioshield', 'w', encoding='utf-8') as file: file.write(vioshield)

def get_cookies_site(profile: str):
    path = f'{COOKIES_KD_PATH}\\{profile}.json'
    if not os.path.exists(path): return None
    with open(path, 'r') as file: return json.loads(file.read())

def get_cookies_steam(profile: str):
    path = f'{COOKIES_STEAM_PATH}\\{profile}.json'
    if not os.path.exists(path): return None
    with open(path, 'r') as file: return json.loads(file.read())

def get_vioshield():
    with open(f'{MEMORY_PATH}\\vioshield', 'r') as file: return file.read()

def get_cookies_site_with_vioshield(profile: str):
    cookies = get_cookies_site(profile)
    if not cookies: return None
    cookies['__vioShield'] = get_vioshield()
    return cookies

# ==================================================
# Login / Deposit
# ==================================================

def set_as_login_required(profile: str):
    with open(f'{LOGIN_REQUIRED_PATH}\\{profile}', 'a') as file: pass

def set_as_logged_in(profile: str):
    if os.path.exists(f'{LOGIN_REQUIRED_PATH}\\{profile}'): os.remove(f'{LOGIN_REQUIRED_PATH}\\{profile}')

def set_as_deposit_required(profile: str):
    with open(f'{DEPOSIT_REQUIRED_PATH}\\{profile}', 'a') as file: pass

def set_as_paid(profile: str):
    if os.path.exists(f'{DEPOSIT_REQUIRED_PATH}\\{profile}'): os.remove(f'{DEPOSIT_REQUIRED_PATH}\\{profile}')

# ==================================================
# Gift Cards
# ==================================================

def add_giftcard(gift_code: str):
    with open(f'{GIFTCARDS_PATH}\\{gift_code}', 'a') as file: pass

def remove_giftcard(gift_code: str):
    if os.path.exists(f'{GIFTCARDS_PATH}\\{gift_code}'): os.remove(f'{GIFTCARDS_PATH}\\{gift_code}')

def get_random_giftcard():
    giftcards = os.listdir(GIFTCARDS_PATH)
    if len(giftcards): return random.choice(giftcards)
    return None

# ==================================================
# Trade Offers
# ==================================================

def set_as_tradeoffer_confirm_required(profile: str):
    with open(f'{TRADEOFFER_CONFIRM_REQUIRED_PATH}\\{profile}', 'a') as file: pass

def set_as_tradeoffer_confirmed(profile: str):
    if os.path.exists(f'{TRADEOFFER_CONFIRM_REQUIRED_PATH}\\{profile}'): os.remove(f'{TRADEOFFER_CONFIRM_REQUIRED_PATH}\\{profile}')

# ==================================================
# Steam Ids
# ==================================================

def set_steamid(profile: str, steam_id: str):
    with open(f'{STEAM_IDS_PATH}\\{profile}', 'w', encoding='utf-8') as file: file.write(steam_id)

def get_steamid(profile: str):
    path = f'{STEAM_IDS_PATH}\\{profile}'
    if not os.path.exists(path): return None
    with open(path, 'r') as file: return file.read()

# ==================================================
# Profiles
# ==================================================

def get_all_profiles(): return os.listdir(PROFILES_PATH)
def get_login_profiles(): return os.listdir(LOGIN_REQUIRED_PATH)
def get_deposit_profiles(): return os.listdir(DEPOSIT_REQUIRED_PATH)

def get_enabled_profiles():
    profiles = get_all_profiles()
    enabled_profiles = os.listdir(ENABLED_PROFILES_PATH)
    login_profiles = get_login_profiles()
    deposit_profiles = get_deposit_profiles()

    output = []

    for profile in profiles:
        if profile in enabled_profiles and not profile in login_profiles and not profile in deposit_profiles: output.append(profile)

    return output

def get_failed_profiles(code: str):
    try: profiles = os.listdir(f'{RECEIVED_CODES_PATH}\\{code}')
    except: profiles = []
    enabled_profiles = get_enabled_profiles()

    output = []

    for profile in enabled_profiles:
        if not profile in profiles: output.append(profile)

    return output

def enable_profile(profile: str):
    with open(f'{ENABLED_PROFILES_PATH}\\{profile}', 'a') as file: pass

def disable_profile(profile: str):
    if os.path.exists(f'{ENABLED_PROFILES_PATH}\\{profile}'): os.remove(f'{ENABLED_PROFILES_PATH}\\{profile}')

def run_profile(profile: str):

        profile_folder = f'{PROFILES_PATH}\\{profile}'
        user_data_dir = f'--user-data-dir="{profile_folder}"'

        cmd = f'{CHROME_PATH} {user_data_dir} --profile-directory="{profile}"'

        extentions = ''
        for extention in os.listdir(EXTENTIONS_PATH): extentions = extentions + f'{EXTENTIONS_PATH}\\{extention},'
        if extentions: cmd = cmd + f' --load-extension="{extentions}"'

        windows_before = pygetwindow.getWindowsWithTitle("Google Chrome")

        process = subprocess.Popen(cmd)
        windows_after = pygetwindow.getWindowsWithTitle("Google Chrome")

        for i in range(30):
            if not len(windows_before) == len(windows_after): break
            windows_after = pygetwindow.getWindowsWithTitle("Google Chrome")
            time.sleep(0.1)

        chrome_window = None

        for window in windows_after:
            if not window in windows_before: chrome_window = window

        if not chrome_window: return

        chrome_window.activate()
        chrome_window.maximize()

        return process

def get_first_enabled_profile():
    lists=get_enabled_profiles()

    if len(lists): 
        print(lists[0])
        return lists[0]
    else:
        return False
def if_enable(profile: str):
    if os.path.exists(f'{ENABLED_PROFILES_PATH}\\{profile}'): return True
    else:return False
def if_login_required(profile: str):
    if os.path.exists(f'{LOGIN_REQUIRED_PATH}\\{profile}'): return True
    else:return False
def if_deposit_required(profile: str):
    if os.path.exists(f'{DEPOSIT_REQUIRED_PATH}\\{profile}'): return True
    else:return False

if __name__ == '__main__':

    run_profile('Profile 3')
