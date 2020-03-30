from socket import *

serverName = 'localhost' #127.0.0.1
serverPort = 12000 # numero di porta del processo server arbitrario, deve essre >1023 perchè gli altri sono well known

#creare il socket client

clientSocket = socket(AF_INET, SOCK_DGRAM)  #AF_INET -> IPv4, SOCK_DIGRAM --> UDP
clientSocket.settimeout(2) #in secondi
message = input("inserisci lettere: ")

clientSocket.sendto(message.encode('utf-8'), (serverName,serverPort))

try: 
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048) #2048 = lunghezza buffer

    modifiedMessage = modifiedMessage.decode('utf-8') #decode

    print(modifiedMessage)

except Exception as e:
    print("Server error,", e)

finally:
    clientSocket.close()
