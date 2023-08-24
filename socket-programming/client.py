
import socket
from threading import Thread

# client program to connect receive message
def handle_request(socket):
    socket.connect(('', 80))
    msg = socket.recv(1024)
    print(msg)

for i in range(10):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        t = Thread(target=handle_request, args=[s])
        t.start()
        t.join()

