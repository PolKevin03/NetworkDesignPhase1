from socket import *

#server info
serverPort =13000
CHUNK =1024

serverSocket =socket(AF_INET, SOCK_DGRAM) #make UDP socket

serverSocket.bind(("", serverPort)) #combine

print("The server is ready to receive file") #print in terminal

outFile =open("received.bmp","wb")

while True: #loop grabbing packets
    message, clientAddress =serverSocket.recvfrom(CHUNK +10)

    if message ==b"END":
        serverSocket.sendto(b"ACK_END",clientAddress)
        break

    outFile.write(message)
    serverSocket.sendto(b"ACK",clientAddress)

outFile.close()
serverSocket.close()

print("Saved as received.bmp")