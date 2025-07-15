
# 🧠 LaynC2 - Remote Access via Discord (Python)

> ⚠️ **[EN/PT-BR] Educational use only. Do not use this on any system without permission.**
> ⚠️ **Uso exclusivamente educacional. Não utilize sem permissão expressa do dono do sistema.**

---

## 📌 Description / Descrição

**[EN]**  
This is a Python-based Remote Access Tool (RAT) that uses a Discord bot as a Command & Control server (C2). It provides full remote control of infected machines via Discord commands, with features ranging from webcam capture to file exfiltration, process control, and ransomware-like behavior.

**[PT-BR]**  
Este é um RAT (Remote Access Tool) escrito em Python que utiliza o Discord como servidor de C2 (comando e controle). Ele oferece controle completo da máquina infectada, com comandos enviados via bot do Discord — incluindo captura de tela, webcam, execução de comandos e ransomware.

---

## 🎯 Features / Funcionalidades

✅ Full command execution (`cmd`)  
✅ Screenshot and webcam capture (`screenshot`, `webcam`)  
✅ Process listing and killing (`process`, `killproc`)  
✅ Remote shell access (`revshell`)  
✅ Microphone recording (`recordmic`)  
✅ File upload/download (`upload`, `download`)  
✅ Keylogger with webhook exfiltration (`keylog`)  
✅ Telegram, Discord, credentials, browser history and cookies extraction  
✅ Crypto wallet and clipper functionality (`wallets`, `cryptoclip`)  
✅ Persistence, self-delete, ransomware functions (`persistencia`, `ranso`)  

---

## 🚀 How to Use / Como Usar

1. Setup your Discord bot (create one at https://discord.com/developers).
2. Insert the token in `main.py` (`BOT_TOKEN = "..."`).
3. Run `main.py` on the target machine.
4. Control the bot using commands from your Discord server.

---

## 🧪 Example Commands / Exemplos de Comandos

```bash
/interact 1
/cmd whoami
/screenshot
/keylog start 60
/cryptoclip
/ranso
/unranso
/excluir
```

---

## 📂 Structure / Estrutura

- `main.py`: Main bot logic and command handling
- `libraries/`: Modules for specific functions (cam, mic, persistence, etc.)
- Discord bot integration (`discord.ext.commands`)
- Slash + prefix commands supported

---

## ✅ Requirements / Requisitos

- OS: **Windows only**
- Python 3.10+
- Modules: `discord.py`, `cv2`, `pyautogui`, `sounddevice`, `psutil`, `pywin32`, etc.

```bash
pip install -r requirements.txt
```

---

## ⚖️ Legal Disclaimer / Aviso Legal

**[EN]**  
This code is provided for educational and ethical hacking research purposes only. You are fully responsible for any misuse. The authors assume no liability.

**[PT-BR]**  
Este código é fornecido apenas para fins educacionais e pesquisa em segurança ofensiva. Você é totalmente responsável por qualquer uso indevido. Os autores não se responsabilizam.

---

## 🌐 International Use / Uso Internacional

This project was designed for global use:  
✅ English-friendly command naming  
✅ Comments and documentation bilingual  
✅ Compatible with Discord servers worldwide

---

## 🛡️ Ethical Reminder / Lembrete Ético

Only use this on machines you **own** or **have explicit permission** to test.  
Use apenas em máquinas que **você possui** ou **tem permissão clara** para testar.

---

**📁 Educational tool made for Red Team labs and ethical research.**
