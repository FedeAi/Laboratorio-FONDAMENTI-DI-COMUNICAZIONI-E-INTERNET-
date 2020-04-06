from socket import *

# Specificare le generalità del Server (Welcome Socket)
serverName = 'localhost'
serverPort = 12000

# Aprire il socket lato client
clientSocket = socket(AF_INET, SOCK_STREAM)

# Richiedere la connessione
serverAddress = (serverName, serverPort)
clientSocket.connect(serverAddress) #3 way Handshahe
 
# Interazione con l'utente
message = input("inserisci il messaggio: ")

# Invio del messaggio al Server:
clientSocket.send(message.encode('utf-8')) # non dobbiamo specificare l'indirizzo server a differenza di sendTo (UDP)
# Il client già conosce l'indirizzo del connection_socket

#Attendere risposta dal Server
modifiedMessage = clientSocket.recv(1024)
modifiedMessage = modifiedMessage.decode('utf-8')
print('Dal Server: ', modifiedMessage)

# Chiusura del socket
clientSocket.close()
