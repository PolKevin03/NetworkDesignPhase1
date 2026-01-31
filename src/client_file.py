from socket import *
import sys #py system 

#server info
serverName ="localhost"
serverPort =13000

CHUNK =1024

if len(sys.argv) <2:
    print("Usage: python client_file.py <file.bmp>")
    sys.exit(1)

filePath =sys.argv[1]

clientSocket =socket(AF_INET, SOCK_DGRAM) #makes the socket
clientSocket.settimeout(2)

with open(filePath,"rb") as file: #open file 
    while True:
        message =file.read(CHUNK)
        if not message:
            break

        while True: #send file into chunks
            clientSocket.sendto(message,(serverName, serverPort))
            try:
                modifiedMessage,serverAddress =clientSocket.recvfrom(2048)
                if modifiedMessage ==b"ACK":
                    break
            except timeout:
                print("Resending chunk.")

while True: #tell the end
    clientSocket.sendto(b"END",(serverName, serverPort))
    try:
        modifiedMessage, serverAddress =clientSocket.recvfrom(2048)
        if modifiedMessage ==b"ACK_END":
            break
    except timeout:
        print("Resending END...")

clientSocket.close()
print("Done sending.")