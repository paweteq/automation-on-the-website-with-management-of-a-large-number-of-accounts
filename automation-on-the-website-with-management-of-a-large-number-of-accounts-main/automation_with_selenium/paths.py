import os
from datetime import date
import configparser

def read_config():
    config = configparser.ConfigParser()
    config.read('config.ini',encoding='utf-8')

    chrome_path = config.get('Config', 'CHROME_PATH')
    chrome_version = config.getint('Config', 'CHROME_VERSION')

    return chrome_path, chrome_version

def read_ip():
    config = configparser.ConfigParser()
    config.read('config.ini',encoding='utf-8')
    ip = str(config.get('Config', 'IP'))
    return ip

def read_num():
    config = configparser.ConfigParser()
    config.read('config.ini',encoding='utf-8')
    ip = int(config.getint('Config', 'GROUP_NUM'))
    return ip

TODAY = date.today()

# ==================================================
# MEMORY PATH
# ==================================================

MEMORY_PATH = 'memory'

if not os.path.exists(MEMORY_PATH): os.makedirs(MEMORY_PATH)

# ==================================================
# CODES PATHS (DAILYFREE is in working on mode)
# ==================================================

RECEIVED_CODES_PATH = f'{MEMORY_PATH}\\received_codes'
RECEIVED_CODES_BY_DATE_PATH = f'{MEMORY_PATH}\\received_codes_by_date'
CODES_AMOUNT_PATH = f'{MEMORY_PATH}\\received_codes_amounts'
DAILYFREE_PATH = f'{MEMORY_PATH}\\dailyfree'
TODAY_DAILYFREE_PATH = f'{MEMORY_PATH}\\dailyfree\\{TODAY}'

if not os.path.exists(RECEIVED_CODES_PATH): os.makedirs(RECEIVED_CODES_PATH)
if not os.path.exists(RECEIVED_CODES_BY_DATE_PATH): os.makedirs(RECEIVED_CODES_BY_DATE_PATH)
if not os.path.exists(CODES_AMOUNT_PATH): os.makedirs(CODES_AMOUNT_PATH)
if not os.path.exists(DAILYFREE_PATH): os.makedirs(DAILYFREE_PATH)
if not os.path.exists(TODAY_DAILYFREE_PATH): os.makedirs(TODAY_DAILYFREE_PATH)

# ==================================================
# COOKIES PATHS
# ==================================================

COOKIES_PATH = f'{MEMORY_PATH}\\cookies'
COOKIES_KD_PATH = f'{COOKIES_PATH}\\keydrop'
COOKIES_STEAM_PATH = f'{COOKIES_PATH}\\steam'

if not os.path.exists(COOKIES_PATH): os.makedirs(COOKIES_PATH)
if not os.path.exists(COOKIES_KD_PATH): os.makedirs(COOKIES_KD_PATH)
if not os.path.exists(COOKIES_STEAM_PATH): os.makedirs(COOKIES_STEAM_PATH)

# ==================================================
# PROFILES AND CHROME PATHS
# ==================================================

PROFILES_PATH = f'{os.getcwd()}\\profiles' # WARNING: Make sure to follow the OS correct directories
CHROME_PATH = read_config()[0]

EXTENTIONS_PATH = f'{os.getcwd()}\\extentions' # WARNING: Make sure to follow the OS correct directories

if not os.path.exists(PROFILES_PATH): os.makedirs(PROFILES_PATH)
if not os.path.exists(EXTENTIONS_PATH): os.makedirs(EXTENTIONS_PATH)

# ==================================================
# PROFILES STATUS PATHS
# ==================================================

ENABLED_PROFILES_PATH = f'{MEMORY_PATH}\\enabled_profiles'
LOGIN_REQUIRED_PATH = f'{MEMORY_PATH}\\login_required'
DEPOSIT_REQUIRED_PATH = f'{MEMORY_PATH}\\deposit_required'

if not os.path.exists(ENABLED_PROFILES_PATH): os.makedirs(ENABLED_PROFILES_PATH)
if not os.path.exists(LOGIN_REQUIRED_PATH): os.makedirs(LOGIN_REQUIRED_PATH)
if not os.path.exists(DEPOSIT_REQUIRED_PATH): os.makedirs(DEPOSIT_REQUIRED_PATH)

# ==================================================
# GIFTCARDS PATHS
# ==================================================

GIFTCARDS_PATH = f'{MEMORY_PATH}\\giftcards'

if not os.path.exists(GIFTCARDS_PATH): os.makedirs(GIFTCARDS_PATH)

# ==================================================
# LOGS PATHS
# ==================================================

LOGS_PATH = f'{MEMORY_PATH}\\logs\\{TODAY}' # WARNING - Be careful, it's better for logs to be in 'TODAY' folder
LOGS_PROFILES_PATH = f'{LOGS_PATH}\\profiles_logs'

if not os.path.exists(LOGS_PATH): os.makedirs(LOGS_PATH)
if not os.path.exists(LOGS_PROFILES_PATH): os.makedirs(LOGS_PROFILES_PATH)

# ==================================================
# LISTENER PATHS
# ==================================================

LISTENER_PATH = f'{MEMORY_PATH}\\listener'
LISTENER_CODES_PATH = f'{LISTENER_PATH}\\codes'
LISTENER_SOUNDS_PATH = f'{LISTENER_PATH}\\sounds'

if not os.path.exists(LISTENER_PATH): os.makedirs(LISTENER_PATH)
if not os.path.exists(LISTENER_CODES_PATH): os.makedirs(LISTENER_CODES_PATH)
if not os.path.exists(LISTENER_SOUNDS_PATH): os.makedirs(LISTENER_SOUNDS_PATH)

# ==================================================
# STEAM PROFILES DATA PATHS
# ==================================================

STEAM_PATH = f'{MEMORY_PATH}\\steam'
STEAM_IDS_PATH = f'{STEAM_PATH}\\ids'

if not os.path.exists(STEAM_PATH): os.makedirs(STEAM_PATH)
if not os.path.exists(STEAM_IDS_PATH): os.makedirs(STEAM_IDS_PATH)

# ==================================================
# ACCOUNTS CREATED BY AI PATHS
# ==================================================

AI_PATH = f'{MEMORY_PATH}\\ai'
AI_BRAIN = f'{AI_PATH}\\brain'
AI_CREATED_ACCOUNTS_PATH = f'{AI_PATH}\\created_account'
AI_PROFILES_INFO_PATH = f'{AI_PATH}\\profiles_info'

if not os.path.exists(AI_PATH): os.makedirs(AI_PATH)
if not os.path.exists(AI_BRAIN): os.makedirs(AI_BRAIN)
if not os.path.exists(AI_CREATED_ACCOUNTS_PATH): os.makedirs(AI_CREATED_ACCOUNTS_PATH)
if not os.path.exists(AI_PROFILES_INFO_PATH): os.makedirs(AI_PROFILES_INFO_PATH)

# ==================================================
# FIREBASE CONFIG
# ==================================================

FIREBASE_SERVICE_PATH = f'{MEMORY_PATH}\\service.json'

# ==================================================
# DISCORD/NOTIFICATIONS TOKEN
# ==================================================

DISCORD_TOKEN = ''
NOTIF_TOKEN = ''

# ==================================================
# REQUESTS CONFIG
# ==================================================

CHROME_VERSION = read_config()[1]
USER_AGENT = f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{CHROME_VERSION}.0.0.0 Safari/537.36'

# ==================================================
# YOUR STEAM
# ==================================================

STEAM_ID = 76561198265082098
STEAM_TRADEURL = 'https://steamcommunity.com/tradeoffer/new/?partner={tradepartner}'
STEAM_TRADEOFFER_TOKEN = '{token_trade}'

TRADEOFFER_CONFIRM_REQUIRED_PATH = f'{MEMORY_PATH}\\tradeoffer_confirm_required'

if not os.path.exists(TRADEOFFER_CONFIRM_REQUIRED_PATH): os.makedirs(TRADEOFFER_CONFIRM_REQUIRED_PATH)
