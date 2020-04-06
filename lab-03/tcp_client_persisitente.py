from socket import *

# Generalità del welcome socket
serverName = 'localhost'
serverPort = 12000

# Creiamo il client socket
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
while True:
    message = input('Inserisci lettere (. per fermare): ')
    clientSocket.send(message.encode('utf-8'))

    if message =='.':
        break
    modifiedMessage = clientSocket.recv(1024)
    modifiedMessage = modifiedMessage.decode('utf-8')
    print('Dal Server: ', modifiedMessage)

# Chiudere la connessione (l' utente ha inserito un '.')
clientSocket.close()

