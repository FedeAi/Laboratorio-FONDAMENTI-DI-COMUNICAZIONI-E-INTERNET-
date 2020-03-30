from socket import *

#serverName = 'localhost'
serverPort = 12000

serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(('',serverPort))

while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    message = message.decode('utf-8')
    print('Message from: ', clientAddress)
    modifiedMessage = message.upper()

    serverSocket.sendto(modifiedMessage.encode('utf-8'), clientAddress)