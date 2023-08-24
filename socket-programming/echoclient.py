
import socket
import sys
from threading import Thread

# client program to connect receive message
def make_request(message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('', 80))
        s.send(bytes(message, 'utf-8'))
        msg = s.recv(1024)
        print(msg)

for i in range(10):
    t = Thread(target=make_request, args=[sys.argv[1]])
    t.start()

