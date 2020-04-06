from socket import *
from threading import Thread

def handler(connenctionSocket):
    while True:
        message = connenctionSocket.recv(1024)
        message = message.decode('utf-8')
        if message == '.':
            break
        modifiedMessage = message.upper()
        connenctionSocket.send(modifiedMessage.encode('utf-8'))

    connenctionSocket.close()

# Creaiamo il Welcome socket
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) # abilitare il MT

serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('Server pronto a ricevere')
while True:
    newSocket, clientAddr = serverSocket.accept()
    thread = Thread(target = handler, args=(newSocket,))
    print('connessione con: ', clientAddr)
    thread.start()


