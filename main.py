import webbrowser
import colorama
from colorama import Fore
import time
import os
import discord
import threading
import webbrowser
import keyboard
import string
import random
import sys
import requests
from os import system
colorama.init()

system("title " + "Lunar Tool,   Made By Reaper#1234,   Github: github.com/ReaperSkid")

banner = (Fore.LIGHTBLUE_EX + """                                                       
 ██▓     █    ██  ███▄    █  ▄▄▄       ██▀███     ▄▄▄█████▓ ▒█████   ▒█████   ██▓          | Discord Tools                  | IP Tools
▓██▒     ██  ▓██▒ ██ ▀█   █ ▒████▄    ▓██ ▒ ██▒   ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒          | [1] Mass DM all friends        | [5] Basic IP Puller  
▒██░    ▓██  ▒██░▓██  ▀█ ██▒▒██  ▀█▄  ▓██ ░▄█ ▒   ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░          | [2] Find Your Token            | [6] IP Tracer
▒██░    ▓▓█  ░██░▓██▒  ▐▌██▒░██▄▄▄▄██ ▒██▀▀█▄     ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░          | [3] Discord Nitro Generator    | [7] IP Pinger
░██████▒▒▒█████▓ ▒██░   ▓██░ ▓█   ▓██▒░██▓ ▒██▒     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒      | [4] Token Gen (COMING SOON)    | 
░ ▒░▓  ░░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒  ▒▒   ▓▒█░░ ▒▓ ░▒▓░     ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░      |                                | 
░ ░ ▒  ░░░▒░ ░ ░ ░ ░░   ░ ▒░  ▒   ▒▒ ░  ░▒ ░ ▒░       ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░      |                                | 
  ░ ░    ░░░ ░ ░    ░   ░ ░   ░   ▒     ░░   ░      ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░         |                                | 
    ░  ░   ░              ░       ░  ░   ░                     ░ ░      ░ ░      ░  ░      |                                |                                          
""" + Fore.LIGHTBLUE_EX)
print(banner)

Choice = int(input("Option [-->]: "))

if Choice == 1:
    client = discord.Client()
    colorama.init()

    Token = input("Token [-->]: ")
    Message = input("What Do You Want To Mass DM [-->]: ")
    thread_amount = int(input("How Many Threads [-->]: "))
    used_threads = thread_amount * 100000

    @client.event
    async def on_connect():
        for user in client.user.friends:
            try:
                await user.send(Message)
                print(Fore.GREEN)
                print(f"message: {user.name}")
            except:
                print(Fore.RED)
                print(f"unable to message: {user.name}")
    def run():
        client.run("YOUR TOKEN HERE", bot=False)
    
    threads = []
    
    for i in range(thread_amount):
        t = threading.Thread(target=run())
        t.daemon = False
        threads.append(t)
    
    for i in range(thread_amount):
        threads[i].start()
    
    for i in range(thread_amount):
        threads[i].join()

if Choice == 2:
    webbrowser.open("https://www.youtube.com/watch?v=YEgFvgg7ZPI&ab_channel=GaugingGadgets")

if Choice == 3:
    Hotkey = input("Keybind to start program [-->]: ")
    thread_amount = int(input("How many threads do you want to use? "))
    used_threads = thread_amount * 100000
    print(f"Press {Hotkey} to activate")
    while True:
        if keyboard.is_pressed(Hotkey):
            while True:
                def generate():
                    while True:
                        code = ('').join(random.choices(string.ascii_letters + string.digits,
                                            k=16))
                        r = requests.get(
                        f"https://discordapp.com/api/v6/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"
                        )
                        if r.status_code == 200:
                            print(Fore.BLUE)
                            print(f"[+] Valid | discord.gift/{code}")
                            sys.write(f"discord.gift/{code}\n")
                            webbrowser.open("https://discord.gg/WdaZy28xkB%22")
                        else:
                            print(Fore.RED)
                            print(f"[-] Invalid | https://discord.gift/{code}")

                threads = []

                for i in range(thread_amount):
                    t = threading.Thread(target=generate())
                    t.daemon = False
                    threads.append(t)

                for i in range(thread_amount):
                    threads[i].start()

                for i in range(thread_amount):
                    threads[i].join()

if Choice == 4:
    print("Coming soon lmao")
    exit()

if Choice == 5:
    webbrowser.open("https://iplogger.org/")

if Choice == 6:
    ip = str(input("Enter IP: "))
    response = requests.post("http://ip-api.com/batch", json=[
    {"query": str(ip)},
    ]).json()
    for ip_info in response:
        for k,v in ip_info.items():
            print(Fore.LIGHTBLUE_EX)
            print(k,v)
            print(" \n \r ")
        time.sleep(120)

if Choice == 7:
    print(Fore.LIGHTBLUE_EX)
    ip_list = input("Enter kids IP: ")
    pingtimes = int(input(f"How many times do you want to ping {ip_list}?: "))
    response = os.popen(f"ping {ip_list}").read()
    if "Received = 4" in response:
        for i in range (pingtimes):
            print(f"KID IS ONLINE")
            time.sleep(0.1)
    else:
        for i in range (pingtimes):
            print(f"KID IS OFFLINE")
            time.sleep(0.1)

