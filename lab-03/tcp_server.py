from socket import *

# Creare il Welcome Socket
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
binding = (('', serverPort))
serverSocket.bind(binding)

# Specificare che si tratta di Welcome Socket, e mettersi in ascolto di richieste
serverSocket.listen(1)  # n = numero di client in attesa + 1 accettabili

print('Il server è pronto a ricevere')

while 1:
    # Instaurare la connessione con il client
    connectionSocket, clientAddres = serverSocket.accept()
    print('Connesso con: ', clientAddres)

    # Attendere messaggi applicativi
    message = connectionSocket.recv(1024)
    message = message.decodep('utf-8')
    modifiedMessage = message.upper()

    # Inviare la risposta dal Server
    connectionSocket.send(modifiedMessage.encode('utf-8'))
    connectionSocket.close()
    
