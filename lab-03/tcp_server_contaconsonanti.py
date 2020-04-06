from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
binding = ('',serverPort)
serverSocket.bind(binding)

# Welcome Socket in ascolto
serverSocket.listen(1)  # n = numero di client in attesa + 1 accettabili

print('Server pronto a ricevere')
vocali = ['A','E','I','O','U',' ']

while 1:
    connectionSocket, clientAddres = serverSocket.accept()
    print('Connesso con: ', clientAddres)

    message = connectionSocket.recv(2048)
    message = message.decode('utf-8')
    message = message.upper()

    numero = len(message)
    for voc in vocali:
        numero = numero - message.count(voc)
    # Risposta
    numero = str(numero).encode('utf-8')
    connectionSocket.send(numero)

    # Active Close
    connectionSocket.close()