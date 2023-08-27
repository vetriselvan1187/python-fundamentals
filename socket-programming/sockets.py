
import socket

http_get = "GET / HTTP/1.1\r\nHost: www.google.com\r\nUser-Agent: mozilla/5.0\r\nAccept: */*\r\n\r\n"

http_get_request = "GET / HTTP/1.1\r\nAccept: */*\r\nSec-Fetch-Site: none\r\nAccept-Encoding: gzip, deflate\r\nUpgrade-Insecure-Requests: 1\r\nSec-Fetch-Mode: navigate\r\nHost: localhost:8000\r\nUser-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Safari/605.1.15\r\nAccept-Language: en-IN,en-GB;q=0.9,en;q=0.8\r\nSec-Fetch-Dest: document\r\nConnection: keep-alive\r\n"


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 8000))
s.send(bytes(http_get_request, 'utf-8'))
bytes_list = []
while chunk := s.recv(1024):
    bytes_list.append(chunk)
content = str(b''.join(bytes_list))
print(content)




# with socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('google.com', 80))
    s.send(bytes(http_get, 'utf-8'))
    bytes_list = []
    while chunk := s.recv(1024):
        bytes_list.append(chunk)
    content = str(b''.join(bytes_list))
    print(content)
    print(len(content))



# ssl socket
import socket, ssl

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.verify_mode = ssl.CERT_NONE
context.check_hostname = False
context.load_default_certs()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssl_sock = context.wrap_socket(s, server_hostname='www.verisign.com')
ssl_sock.connect(('www.verisign.com', 443))


# ssl socket


import socket
import ssl

hostname = 'developer.mozilla.org'
context = ssl.create_default_context()

with socket.create_connection((hostname, 443)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        print(ssock.version())
        ssock.send(bytes(http_get, 'utf-8'))
        bytes_list = []
        while chunk := ssock.recv(1024):
            bytes_list.append(chunk)
        content = str(b''.join(bytes_list))
        print(content)

