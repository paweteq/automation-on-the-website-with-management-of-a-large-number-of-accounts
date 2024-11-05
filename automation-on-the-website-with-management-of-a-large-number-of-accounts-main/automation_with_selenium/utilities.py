import os

import undetected_chromedriver as uc

import logger
from paths import *

def create_driver(profile: str, load_extensions: bool = True):

    user_data_dir = f'{PROFILES_PATH}\\{profile}'

    if not profile_exists(profile): logger.error(f'Profile "{profile}" not found :(', True)

    opts = uc.ChromeOptions()

    extensions = ''
    for extension in os.listdir(EXTENTIONS_PATH): extensions = extensions + f'{EXTENTIONS_PATH}\\{extension},'
    if extensions and load_extensions: opts.add_argument(f'--load-extension={extensions}')

    driver = uc.Chrome(user_data_dir=user_data_dir, version_main=CHROME_VERSION, driver_executable_path='chromedriver.exe', options=opts)
    logger.log(f'Uruchomiono przegladarkę, PID: {driver.service.process.pid}', logger.colors.BLUE_BG)

    return driver

def profile_exists(profile: str): return profile and os.path.exists(f'{PROFILES_PATH}\\{profile}')

def get_chrome_cookies(profile: str):
    import json
    import sqlite3
    from base64 import b64decode
    from os.path import expandvars
    from win32.win32crypt import CryptUnprotectData
    from Crypto.Cipher.AES import new, MODE_GCM

    cookies_path = f'{PROFILES_PATH}\\{profile}\\{profile}\\Network\\Cookies'
    localstate_path = f'{PROFILES_PATH}\\{profile}\\Local State'

    db = expandvars(cookies_path)

    with open(localstate_path) as f: key = CryptUnprotectData(b64decode(json.load(f)['os_crypt']['encrypted_key'])[5:])[1]

    conn = sqlite3.connect(db)
    conn.create_function('decrypt', 1, lambda v: new(key, MODE_GCM, v[3:15]).decrypt(v[15:-16]).decode())
    cookies = dict(conn.execute("SELECT name, decrypt(encrypted_value) FROM cookies"))
    conn.close()
    return cookies

def extract_steamRefresh_steam(cookies: dict):
    if not 'steamRefresh_steam' in cookies.keys(): return None
    else: return cookies['steamRefresh_steam']