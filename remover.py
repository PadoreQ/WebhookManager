import discord
import requests
import time
import os

webhook = input("Webhook:")
requests.delete(webhook)

print("[+] Webhook has been removed.")
time.sleep(3)
os.system("exit")


