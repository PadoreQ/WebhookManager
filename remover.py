import discord
import requests
import time
import os
from discord import Webhook, RequestsWebhookAdapter

def menu():
    print("[1] Delete Webhook")
    print("[2] Send Message")
    print("[3] Webhook Spammer")

menu()
option = int(input("Option:"))

while option != 0:
    if option == 1:

        webhook1 = input("Webhook:")
        requests.delete(webhook1)
        print("[+] Webhook has been removed.")
        time.sleep(3)
        os.system("exit")

    elif option == 2:
        webhooklink = input("Webhook:")
        webhookmessage = input("Message:")
        webhook = Webhook.from_url(webhooklink, adapter=RequestsWebhookAdapter())
        webhook.send(webhookmessage)
        print("[+] Message sent.")
        time.sleep(3)
        os.system("exit")
    elif option == 3:



        webhooklink = input("Webhook:")
        webhookmessage = input("Spam Message:")
        messages = int(input("How many messages to send:"))
        messagedelay = int(input("Message delay:"))
        webhook = Webhook.from_url(webhooklink, adapter=RequestsWebhookAdapter())
        num = messages
        for x in range(num):
            webhook.send(webhookmessage)
            time.sleep(messagedelay)
            print("[+] Message sent.")
        time.sleep(3)
        os.system("exit")

    else:
        print("Error")

print()
menu()
