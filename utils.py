import requests
import datetime

url = "https://api.starlingbank.com/api/v2"


def get_account(personal_access_token):
    r = requests.get(url + "/accounts", headers={"Authorization": "Bearer " + personal_access_token})
    return r.json()["accounts"][0]["accountUid"]


def get_default_category(personal_access_token):
    r = requests.get(url + "/accounts", headers={"Authorization": "Bearer " + personal_access_token})
    return r.json()["accounts"][0]["defaultCategory"]


def get_balance(personal_access_token):
    balance = requests.get(url + "/accounts/" + (get_account(personal_access_token)) + "/balance", headers={"Authorization": "Bearer " + personal_access_token})
    return balance.json()["effectiveBalance"]["minorUnits"] / 100


def get_transactions(personal_access_token, amount):
    # print(get_account(personal_access_token))
    # print(get_default_category(personal_access_token))
    datefrom = (datetime.datetime.now() - datetime.timedelta(days=30)).strftime("%Y-%m-%d") + "T00:00:00Z"
    feeditems = requests.get(url + "/feed/account/" + (get_account(personal_access_token)) + "/category/" + (get_default_category(personal_access_token)) + "?changesSince=" + datefrom, headers={"Authorization": "Bearer " + personal_access_token})
    return feeditems.json()["feedItems"][:10]
