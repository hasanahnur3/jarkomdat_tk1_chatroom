import socket
import random
from threading import Thread
from datetime import datetime
from colorama import Fore, init, Back

# mengatur warna untuk client
init()
colors = [Fore.CYAN, Fore.LIGHTBLACK_EX, 
    Fore.LIGHTCYAN_EX, Fore.LIGHTMAGENTA_EX, Fore.LIGHTWHITE_EX, 
    Fore.MAGENTA, Fore.YELLOW]
client_color = random.choice(colors)

# megatur host dan port
host = "192.168.0.106"
port = 1234

# membuat socket tcp
sock = socket.socket()
print("-- Connecting --")
# connect ke server
sock.connect((host, port))
print("-- Connected --")
# meminta username
name = input("Enter your name: ")


# thread baru untuk aktivitas menerima, karena thread parent digunakan untuk while input
def receive():
    while True:
        try:
            message = sock.recv(1024).decode()
            if message:
                print("\n" + message)
        except:
            print("-- Server Closed --")
            sock.close()
            break

t = Thread(target=receive)
t.daemon = True
t.start()

counter = 0
while True:
    if counter == 0:
        date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
        message = f"{client_color}[{date_now}] -- {name} joined the chatroom --{Fore.RESET}"
        sock.send(message.encode())

    # meminta input message
    message =  input()
    # exit program
    if message.lower() == 'exit':
        date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
        message = f"{client_color}[{date_now}] -- {name} left the chatroom --{Fore.RESET}"
        sock.send(message.encode())
        break
    # mengatur tanggal, waktu, dan warna
    date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
    message = f"{client_color}[{date_now}] {name}: {message}{Fore.RESET}"
    sock.send(message.encode())

# menutup socket
sock.close()