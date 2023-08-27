
import socket
from threading import Thread

# simple python server
 
# handle client request
def handle_client_request(clientsocket):
    message = 'This is a message returned by server'
    message_bytes = bytes(message, 'UTF-8')
    clientsocket.send(message_bytes)

# create and bind server on port 80
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serversocket:
    serversocket.bind(('', 80))
    serversocket.listen(5)
    while True:
        (clientsocket, address) = serversocket.accept()
        with clientsocket:
            client_thread = Thread(target=handle_client_request, args=[clientsocket])
            client_thread.start()  
            client_thread.join()


