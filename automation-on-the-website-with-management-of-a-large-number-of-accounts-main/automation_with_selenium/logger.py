from datetime import datetime

import colors
from paths import *

def log(text: str, color: str = colors.RESET):
    log_time = datetime.now().strftime("%H:%M:%S")
    with open(f'{LOGS_PATH}\\today.txt', 'a', encoding='utf-8') as file: file.write(log_time + ' > ' + text + '\n')
    print(f'{color}{text}{colors.RESET}')

def warn(text: str): log(text, colors.YELLOW)

def error(text: str, fatal: bool = False):
    log_time = datetime.now().strftime("%H:%M:%S")
    with open(f'{LOGS_PATH}\\today.txt', 'a', encoding='utf-8') as file: file.write('Error occured -> ' + log_time + ' > ' + text + '   <<<   ERROR\n')
    print(f'{colors.RED}(error): {colors.LIGHT_RED}' + text + f'{colors.RESET}')
    if fatal: raise Exception(text)

def log_profile(profile: str, text: str, color: str = colors.RESET):
    log_time = datetime.now().strftime("%H:%M:%S")
    with open(f'{LOGS_PROFILES_PATH}\\{profile}.txt', 'a', encoding='utf-8') as file: file.write(log_time + ' > ' + text + '\n')
    print(f'{color}{text}{colors.RESET}')

def error_profile(profile: str, text: str):
    log_time = datetime.now().strftime("%H:%M:%S")
    with open(f'{LOGS_PROFILES_PATH}\\{profile}.txt', 'a', encoding='utf-8') as file: file.write('Error occured -> ' + log_time + ' > ' + text + '   <<<   ERROR\n')
    print(f'{colors.RED}(error): {colors.LIGHT_RED}' + text + f'{colors.RESET}')


def no_profile(profile: str): warn(f'({profile}) nie istnieje taki profil')
def no_cookies(profile: str): warn(f'({profile}) brak ciasteczek')
def no_authorization(profile: str): warn(f'({profile}) błąd podczas pobierania tokenu autoryzacji')
def deposit_not_allowed(profile: str): warn(f'({profile}) ma zakaz wpłat')
def login_required(profile: str): warn(f'({profile}) wymaga zalogowania się')

