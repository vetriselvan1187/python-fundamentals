
import socket
import threading
from threading import Thread

# simple python server
 
# handle client request
def handle_client_request(clientsocket):
    with clientsocket:
        data = clientsocket.recv(1024)
        threading.Event().wait(5)
        clientsocket.send(data)
        print('clientsocket closed')

# create and bind server on port 80
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serversocket:
    serversocket.bind(('', 80))
    serversocket.listen(50)
    
    while True:
        (clientsocket, address) = serversocket.accept()
        print(clientsocket,' ', address)
        client_thread = Thread(target=handle_client_request, args=[clientsocket])
        client_thread.start()


