from socket import *

serverPort = 1200
buffer_len = 2048
serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(('',serverPort))

while 1:
    message, address = serverSocket.recvfrom(buffer_len)

    print("message from: ", address)
    message = message.decode('utf-8')

    n_vowels = 0
    for v in ['a','e','i','o','u']:
        n_vowels += message.count(v)
    n_consonant = len(message) - n_vowels
    
    serverSocket.sendto(str(n_consonant).encode('utf-8'), address)
