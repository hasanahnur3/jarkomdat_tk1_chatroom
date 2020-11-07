import socket
from threading import Thread
import datetime

# megatur host dan port
host = "0.0.0.0"
port = 1234 

# list seluruh client
clients = set()

# membuat socket tcp
sock = socket.socket()
# membuat port reusable
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# memasangkan socket ke host dan port
sock.bind((host, port))
# listen for upcoming connections
sock.listen(10)
print("-- Server started listening --")

# method untuk melayani setiap client
def handle(client):
    while True:
        try:
            # menerima message dari client
            message = client.recv(1024).decode()
            print(message.split())
            print(message.split(" "))
            print("left" in message.split())
            if ("left" in message.split() and "the" in message.split() and "chatroom" in message.split() ):
                clients.remove(client)
                for c in clients:
                    c.send(message.encode())
                break
        except Exception as e:
            # error handler
            print(f"-- Error: {e} --")
            clients.remove(client)
        # broadcast ke seluruh client
        for c in clients:
            c.send(message.encode())

while True:
    # listening untuk connection baru
    client_socket, client_address = sock.accept()
    print(f"-- Connected with {client_address} --")
    # menambahkan client baru ke list
    clients.add(client_socket)
    # membuat thread baru untuk client tsb
    t = Thread(target=handle, args=(client_socket,))

    t.daemon = True
    t.start()

# menutup socket client
for c in clients:
    c.close()

# menutup socket server
sock.close()
