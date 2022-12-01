# A biblioteca socket é necessária para a construção 
# da comunicaçãi entre o listener e o cliente
import socket
import time

# Informar HOST e PORT

HOST = 'localhost'
PORT = 3000

# Criação do socket

s = socket.socket()

# Bind para conectar HOST e PORT
s.bind((HOST, PORT))
print(f'Aguardando conexão na porta: {PORT}')

s.listen(5)

# Guarda-se o accept em duas variáveis, pois o accept retorna uma tupla
conn, address = s.accept()
print(f'Recebendo solicitação de {address}')

messages = [
    'Mensagem A',
    'Mensagem C',
    'Mensagem B',
]

for message in messages:
    # Conversão para Bytes
    message = bytes(message, 'utf-8')
    # O listener envia a mensagem para o cliente
    conn.send(message)
    # Tempo para as mensagens não aparecerem de uma vez só
    time.sleep(4)
