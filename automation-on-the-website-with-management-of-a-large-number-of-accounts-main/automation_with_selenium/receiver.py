import os
import json
import time
import requests
import threading

import colors
import logger
import manager
from paths import *

import headers

url = "https://bonus_code.com"

# GLOBAL VALUES

VIOSHIELD = ''

ERROR_WRONGCODE = False
ERROR_EXPIREDCODE = False

def collect_once(profile: str, code: str):
    
    global ERROR_WRONGCODE
    global ERROR_EXPIREDCODE

    if not os.path.exists(f'{COOKIES_KD_PATH}\\{profile}.json'):
        logger.error_profile(profile, f'{profile} ciasteczka nie istnieją')
        return 'no_cookies'

    logger.log_profile(profile, f'{profile} uruchomione', colors.LIGHT_BLUE)

    data = { "promoCode": code }
    cookies = manager.get_cookies_keydrop(profile)

    if not cookies:
        logger.error_profile(profile, f'{profile} ciasteczka nie istnieją')
        manager.set_as_login_required(profile)
        return 'no_cookies'

    if VIOSHIELD: cookies['__vioShield'] = VIOSHIELD

    with requests.Session() as session:

        session.headers.update({ "User-Agent": USER_AGENT })

        logger.log_profile(profile, f'{profile} wykonuję zapytanie...', colors.LIGHT_PURPLE)
        response = session.post(url, headers=headers.golden_code, cookies=cookies, json=data)

        if response.status_code == 200: # request OK

            res = json.loads(response.text)

            if res['status']:
                logger.log_profile(profile, f'Kod został odebrany ({code})', colors.LIGHT_GREEN)
                manager.set_code_received(profile, code, res['goldBonus'])
                print(f'{colors.YELLOW}Ilość golda: {colors.LIGHT_YELLOW}', res['goldBonus'], colors.RESET)
                return 'received'

            elif res['errorCode'] == 'notLoggedIn':
                logger.error_profile(profile, 'Trzeba się zalogować')
                manager.set_as_login_required(profile)

            elif res['errorCode'] == 'depositRequired':
                logger.error_profile(profile, 'Trzeba wpłacić na konto')
                manager.set_as_deposit_required(profile)

            elif res['errorCode'] == 'usedCode':
                logger.error_profile(profile, 'Kod już użyto')
                manager.set_code_received(profile, code)

            elif res['errorCode'] == 'wrongCode':
                ERROR_WRONGCODE = True
                logger.error_profile(profile, f'Kod jest błędny ({code})')

            elif res['errorCode'] == 'expiredCode':
                ERROR_EXPIREDCODE = True
                logger.error_profile(profile, f'Kod się skończył ({code})')

            elif res['errorCode'] == 'spamError':
                logger.error_profile(profile, f'Za często wykonujesz requesty, odpoczywam 3s')
                time.sleep(3)
            else:
                logger.error_profile(profile, f'Nieznany błąd: ' + response.text)

            return res['errorCode']

        else:
            logger.error_profile(profile, f'Wystąpił błąd podczas wykonywania requestu, sprawdź ciasteczka oraz wartość __vioShield {response.text}')
            return 'request_error'

def collect_group(profiles, code, second_run = False):

    try_again_profiles = []

    for profile in profiles:

        if ERROR_EXPIREDCODE or ERROR_WRONGCODE: break

        status = collect_once(profile, code)
        if status == 'spamError': try_again_profiles.append(profile)

        time.sleep(0.01) # BEFORE 1s

    if not second_run and len(try_again_profiles): collect_group(try_again_profiles, code, True)

def collect(profiles: list, code: str):

    global VIOSHIELD

    global ERROR_WRONGCODE
    global ERROR_EXPIREDCODE

    ERROR_WRONGCODE = False
    ERROR_EXPIREDCODE = False

    VIOSHIELD = manager.get_vioshield()

    profiles_grops = []
    groups_number = read_num()

    for _ in range(groups_number): profiles_grops.append([])

    n = 0
    for profile in profiles:
        profiles_grops[n].append(profile)
        if n >= groups_number - 1: n = 0
        else: n += 1

    threads = []
    for i in range(groups_number):
        thread = threading.Thread(target=collect_group, args=(profiles_grops[i], code))
        threads.append(thread)

    for thread in threads: thread.start()
    for thread in threads: thread.join()

    print('Zakończono odbieranie kodów!')

    return ERROR_EXPIREDCODE or ERROR_WRONGCODE

if __name__ == '__main__':
    code = 'A5CQBFJQMVIFFEQAJ'
    #collect_once('Profile 215', code)
    #profiles = manager.get_all_profiles()
    #profiles = manager.get_login_profiles() 
    #print(profiles)
    #profiles = ['Profile 215','Profile 216','Profile 217','Profile 218','Profile ']
    #collect(profiles, code)
