import socket
from threading import Thread

# megatur host dan port
host = "127.0.0.1"
port = 3330 

addrs =[]

# membuat socket tcp
sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# memasangkan socket ke host dan port
sock.bind((host, port))

print("-- Server is ready --")

while True:
    # try:
        # menerima message dari client
        data, addr = sock.recvfrom(4096)
        message = str(data.decode('utf=8'))
        if ("left" in message.split() and "the" in message.split() and "chatroom" in message.split()):
            addrs.remove(addr)
            for c in addrs:
                sock.sendto(message.encode('utf-8'), c)
            continue

        print(message)
        if (addr not in addrs):
            addrs.append(addr)
        for c in addrs:
            sock.sendto(message.encode('utf-8'), c)
    # except Exception as e:
        # error handler
        # print(f"-- Error: {e} --")
        # broadcast ke seluruh client

# menutup socket server
sock.close()
