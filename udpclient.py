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
host = "127.0.01"
port = 3330

# membuat socket tcp
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
name = input("Enter your name: ")


# thread baru untuk aktivitas menerima, karena thread parent digunakan untuk while input

message = f"{client_color}{name}: joined the chatroom"
sock.sendto(message.encode(),(host, port))

def receive():
    while True:
        data, addr = sock.recvfrom(4096)
        print("\n" + str(data.decode('utf=8')))
t = Thread(target=receive)
t.daemon = True
t.start()

counter=0
while True:
    if counter == 0:
        date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
        message = f"{client_color}[{date_now}] -- {name} joined the chatroom --{Fore.RESET}"
        sock.sendto(message.encode('utf-8'),(host, port))

    # meminta input message
    message =  input()

    # exit program
    if message.lower() == 'exit':
        date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
        message = f"{client_color}[{date_now}] -- {name} left the chatroom --{Fore.RESET}"
        sock.sendto(message.encode('utf-8'),(host, port))
        break
    
    # mengatur tanggal, waktu, dan warna
    date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
    message = f"{client_color}[{date_now}] {name}: {message}{Fore.RESET}"
    sock.sendto(message.encode('utf-8'),(host, port))
    counter+=1

# menutup socket
sock.close()