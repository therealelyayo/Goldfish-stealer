import os
import sys
import colorama
import pystyle
import time
import subprocess
from subprocess import call
from colorama import Fore
from colorama import *
from pystyle import *
os.system("cls")

version = "3.9.7"
def logo():
    print("""

   _____   ____  __.__________  __________.___ _______    ___________________    _____  _________  ____  __._____________________ 
  /  _  \ |    |/ _|\____    /  \______   \   |\      \   \_   ___ \______   \  /  _  \ \_   ___ \|    |/ _|\_   _____/\______   \ 
 /  /_\  \|      <    /     /    |     ___/   |/   |   \  /    \  \/|       _/ /  /_\  \/    \  \/|      <   |    __)_  |       _/
/    |    \    |  \  /     /_    |    |   |   /    |    \ \     \___|    |   \/    |    \     \___|    |  \  |        \ |    |   \ 
\____|__  /____|__ \/_______ \   |____|   |___\____|__  /  \______  /____|_  /\____|__  /\______  /____|__ \/_______  / |____|_  /
        \/        \/        \/                        \/          \/       \/         \/        \/        \/        \/         \/ 

""")

 
logo()
print(Fore.LIGHTRED_EX + version + """

[1] Make File       [2] Close

""")
choice = input("[>] Select : ")

if choice =="1":
    call('START utils/upx.exe', shell=True)
    cookie = input("Input Webhook > ")
    print("Please wait...")
    time.sleep(5)
    print("Please wait")
    time.sleep(4)

if choice =="2":
    print("Closing")
