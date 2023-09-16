import os
import sys
import colorama
import pystyle
import time
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

[1] Crack PIN       [2] Close

""")
choice = input("[>] Select : ")

if choice =="1":
    cookie = input("Input Cookie > ")
    print("Cracking PIN...")
    time.sleep(5)
    print("Succsesfully cracked cookie! Pin Is 3481")
    time.sleep(4)

if choice =="2":
    print("Closing PIN CRACKER")
