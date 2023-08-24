
import socket
from threading import Thread

# simple python server
 
# handle client request
def handle_client_request(clientsocket):
    data = clientsocket.recv(1024)
    print(data)
    clientsocket.send(bytes('OK', 'utf-8'))
    filename = data.decode()
    with open('tmp_'+filename, 'wb') as f:
        while chunk := clientsocket.recv(1024):
            f.write(chunk)
            print('chunk written')


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


