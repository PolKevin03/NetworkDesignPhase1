from socket import *

#server info
serverPort =12000
BUFFER_SIZE =2048

serverSocket = socket(AF_INET, SOCK_DGRAM) #make UDP socket
serverSocket.bind(("", serverPort)) #combine

print("The server is ready to receive") #print in terminal

while True: #loop grabbing packets
    message, clientAddress = serverSocket.recvfrom(BUFFER_SIZE) #grabs message
    print("Received:", message.decode()) #prints in terminal

    serverSocket.sendto(message, clientAddress) #send back to client