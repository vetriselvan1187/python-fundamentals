import sys
import socket
from threading import Thread

# client program to connect receive message
def handle_request(socket, filepath):
    socket.connect(('', 80))
    filename = filepath
    socket.send(bytes(filename, 'utf-8'))
    msg = socket.recv(1024)
    print(msg)
    with open(filepath, 'rb') as f:
        while chunk := f.read(1024):
            socket.send(chunk)

for i in range(1):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        t = Thread(target=handle_request, args=[s, sys.argv[1]])
        t.start()
        t.join()

