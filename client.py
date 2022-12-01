import socket
import time

HOST = 'localhost'
PORT = 3000

s = socket.socket()
# Conecta o HOST e a PORT
s.connect((HOST, PORT))

while True:
    # 1024 - número de bytes
    data = s.recv(1024)
    print(data.decode('utf-8'))
    time.sleep(2)
