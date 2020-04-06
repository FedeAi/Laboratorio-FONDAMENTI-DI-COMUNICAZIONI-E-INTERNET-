from socket import *

serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName,serverPort))

clientSocket.settimeout(5) # [s]

message = input('Inserire lettere: ')
clientSocket.send(message.encode('utf-8'))

try:
    response = clientSocket.recv(2048)
    response = response.decode('utf-8')
    print('Il numero di consonanti è: ', response )
except:
    print("Server non raggiungibile, prova più tardi")
finally:
    clientSocket.close()