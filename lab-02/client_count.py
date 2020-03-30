from socket import *

serverName = 'localhost'
serverPort = 1200

clientSocket = socket(AF_INET, SOCK_DGRAM)

clientSocket.settimeout(5)

buffer_size = 2048

message = input("inserisci stringa: ")

clientSocket.sendto(message.encode('utf-8'),(serverName,serverPort))

try:
     consonantNumber, serverAddress = clientSocket.recvfrom(buffer_size)

     print("la stringa ", message, " contiene {} consonanti".format(consonantNumber.decode('utf-8')))

except Exception as e:
    print("error,",e)
finally:
    clientSocket.close()
    