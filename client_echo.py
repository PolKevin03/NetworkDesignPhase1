from socket import *

#server info
serverName ="localhost"
serverPort =12000

clientSocket =socket(AF_INET,SOCK_DGRAM) #makes UDP socket

message ="HELLO" #send this text

clientSocket.sendto(message.encode(),(serverName, serverPort)) #send text to server

modifiedMessage,serverAddress=clientSocket.recvfrom(2048) #grabs the message

print("Received:",modifiedMessage.decode()) #prints in terminal

clientSocket.close() #ends socket