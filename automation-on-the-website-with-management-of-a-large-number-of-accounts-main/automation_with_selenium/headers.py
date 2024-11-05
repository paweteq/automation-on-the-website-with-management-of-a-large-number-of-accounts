
from paths import *

golden_code = {
    "authority": "url.com",
    "method": "POST",
    "path": "/pl/apiData/Bonus/gold_activation_code",
    "scheme": "https",
    "accept": "*/*",
    "accept-encoding": "gzip, deflate",
    "accept-language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "origin": "https://url.com",
    "pragma": "no-cache",
    "referer": "https://url.com/pl/",
    "sec-ch-ua": f'"Not.A/Brand";v="24", "Chromium";v="{CHROME_VERSION}", "Google Chrome";v="{CHROME_VERSION}"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "x-requested-with": "XMLHttpRequest",
    "User-Agent": USER_AGENT
}

deposit = {
    "authority": "url.com",
    "method": "POST",
    "path": "/pl/Pay/",
    "scheme": "https",
    "accept": "*/*",
    "accept-encoding": "gzip, deflate",
    "accept-language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7",
    "origin": "https://url.com",
    "Referer": "https://url.com/pl",
    "sec-ch-ua": f'"Google Chrome";v="{CHROME_VERSION}", "Not;A=Brand";v="8", "Chromium";v="{CHROME_VERSION}"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "User-Agent": USER_AGENT
}

deposit_history = {
    "authority": "url.com",
    "method": "GET",
    "path": "/pl/apiData/AccountHistory/deposit?perPage=10&page=0",
    "scheme": "https",
    "accept": "*/*",
    "accept-encoding": "gzip, deflate",
    "accept-language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7",
    "referer": "https://url.com/pl/panel/profil/settings",
    "sec-ch-ua": f'"Google Chrome";v="{CHROME_VERSION}", "Not;A=Brand";v="8", "Chromium";v="{CHROME_VERSION}"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "User-Agent": USER_AGENT
}

promo_code = {
    "authority": "url.com",
    "method": "POST",
    "path": "/pl/apiData/Bonus/promocode_activation_code",
    "scheme": "https",
    "accept": "*/*",
    "accept-encoding": "gzip, deflate",
    "accept-language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7",
    "origin": "https://url.com",
    "referer": "https://url.com/pl",
    "sec-ch-ua": f'"Google Chrome";v="{CHROME_VERSION}", "Not;A=Brand";v="8", "Chromium";v="{CHROME_VERSION}"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "x-requested-with": "XMLHttpRequest",
    "User-Agent": USER_AGENT
}

event_pass = {
    "authority": "url.com",
    "method": "POST",
    "path": "/pl/Event/Pass/claim",
    "scheme": "https",
    "accept": "*/*",
    "accept-encoding": "gzip, deflate",
    "accept-language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7",
    "origin": "https://url.com",
    "referer": "https://url.com/pl/planets-of-skins-event/event-pass",
    "sec-ch-ua": f'"Google Chrome";v="{CHROME_VERSION}", "Not;A=Brand";v="8", "Chromium";v="{CHROME_VERSION}"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "x-requested-with": "XMLHttpRequest",
    "User-Agent": USER_AGENT
}

event_coins_exchange = {
    "authority": "url.com",
    "method": "POST",
    "path": "/pl/Event/Scratch/exchange/",
    "scheme": "https",
    "accept": "*/*",
    "accept-encoding": "gzip, deflate",
    "accept-language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7",
    "origin": "https://url.com",
    "referer": "https://url.com/pl/planets-of-skins-event/machine",
    "sec-ch-ua": f'"Google Chrome";v="{CHROME_VERSION}", "Not;A=Brand";v="8", "Chromium";v="{CHROME_VERSION}"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "x-requested-with": "XMLHttpRequest",
    "User-Agent": USER_AGENT
}

balance = {
    "authority": "url.com",
    "method": "GET",
    "path": "/pl/balance",
    "scheme": "https",
    "accept": "*/*",
    "accept-encoding": "gzip, deflate",
    "accept-language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7",
    "referer": "https://url.com/pl/panel/profil",
    "sec-ch-ua": f'"Google Chrome";v="{CHROME_VERSION}", "Not;A=Brand";v="8", "Chromium";v="{CHROME_VERSION}"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "User-Agent": USER_AGENT
}

def generate_token(timestamp: int):
    return {
        "authority": "url.com",
        "method": "GET",
        "path": f"/pl/token?t={timestamp}",
        "scheme": "https",
        "accept": "*/*",
        "accept-encoding": "gzip, deflate",
        "accept-language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7",
        "referer": "https://url.com/pl",
        "sec-ch-ua": f'"Google Chrome";v="{CHROME_VERSION}", "Not;A=Brand";v="8", "Chromium";v="{CHROME_VERSION}"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "User-Agent": USER_AGENT
    }

def generate_wss_join_giveaway(authorization: str, giveaway_id: str):
    return {
        "authority": "wss-3003.site.com",
        "method": "PUT",
        "path": f"/v1/giveaway-user//join/{giveaway_id}",
        "scheme": "https",
        "accept": "*/*",
        "accept-encoding": "gzip, deflate",
        "accept-language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7",
        "authorization": f"Bearer {authorization}",
        "origin": "https://url.com",
        "referer": "https://url.com/",
        "sec-ch-ua": f'"Google Chrome";v="{CHROME_VERSION}", "Not;A=Brand";v="8", "Chromium";v="{CHROME_VERSION}"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "User-Agent": USER_AGENT
    }

def generate_wss_get_giveaway(authorization: str, giveaway_id: str):
    return {
        "authority": "wss-2071.site.com",
        "method": "GET",
        "path": f"/v1/giveaway-user//giveaway/{giveaway_id}",
        "scheme": "https",
        "accept": "*/*",
        "accept-encoding": "gzip, deflate",
        "accept-language": "pl-PL,pl;q=0.9",
        "authorization": f"Bearer {authorization}",
        "origin": "https://url.com",
        "referer": "https://url.com/",
        "sec-ch-ua": f'"Google Chrome";v="{CHROME_VERSION}", "Not;A=Brand";v="8", "Chromium";v="{CHROME_VERSION}"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "User-Agent": USER_AGENT,
        'X-Currency': 'PLN'
    }


steamid_headers =  {
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
	"Accept-Encoding": "gzip, deflate, br",
	"Accept-Language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7",
	'Connection': 'keep-alive',
	'Host': 'store.steampowered.com',
	"Sec-Fetch-Dest": "document",
	"Sec-Fetch-Mode": "navigate",
	"Sec-Fetch-Site": "none",
	"Sec-Fetch-User": "?1",
	"Upgrade-Insecure-Requests": "1",
	"sec-ch-ua": f'"Chromium";v="{CHROME_VERSION}", "Google Chrome";v="{CHROME_VERSION}", "Not=A?Brand";v="99"',
	"sec-ch-ua-mobile": "?0",
	"sec-ch-ua-platform": '"Windows"',
	'User-Agent': USER_AGENT
}

steam_login_headers =  {
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
	"Accept-Encoding": "gzip, deflate, br",
	"Accept-Language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7",
	'Connection': 'keep-alive',
	'Host': 'login.steampowered.com',
	"Sec-Fetch-Dest": "document",
	"Sec-Fetch-Mode": "navigate",
	"Sec-Fetch-Site": "none",
	"Sec-Fetch-User": "?1",
	"Upgrade-Insecure-Requests": "1",
	"sec-ch-ua": f'"Chromium";v="{CHROME_VERSION}", "Google Chrome";v="{CHROME_VERSION}", "Not=A?Brand";v="99"',
	"sec-ch-ua-mobile": "?0",
	"sec-ch-ua-platform": '"Windows"',
	'User-Agent': USER_AGENT
}

steam_steamid = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7",
    "sec-ch-ua": f'"Google Chrome";v="{CHROME_VERSION}", "Not;A=Brand";v="8", "Chromium";v="{CHROME_VERSION}"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
	'User-Agent': USER_AGENT
}
def generate_steam_tradeoffer(cookie: str):
    return {
        "User-Agent": USER_AGENT,
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://steamcommunity.com",
        "Referer": STEAM_TRADEURL,
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "sec-ch-ua": f'"Google Chrome";v="{CHROME_VERSION}", "Not;A=Brand";v="8", "Chromium";v="{CHROME_VERSION}"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "Referrer-Policy": "strict-origin-when-cross-origin",
        "cookie": cookie
    }

def generate_steam_avatar(steamid: str):
    return {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7",
        "Origin": "https://steamcommunity.com",
        "Referer": f"https://steamcommunity.com/profiles/{steamid}/edit/avatar", # id/ToNiePoli/edit/avatar
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "sec-ch-ua": f'"Chromium";v="{CHROME_VERSION}", "Google Chrome";v="{CHROME_VERSION}", "Not=A?Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        'User-Agent': USER_AGENT
    }
