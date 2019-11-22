import socket
from threading import Thread 

# SETTINGS
localIP     ="10.10.5.2"
localPorts   = [30410, 30420, 30430]

msgCount = 1000
bufferSize  = 1024
msgFromClient = "testtesttest"

# Init
bytesToSend = str.encode(msgFromClient)



def server(i):  
    UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    UDPServerSocket.bind((localIP, localPorts[i]))
    for x in range(msgCount):
        print("UDP thread"+str(i)+" up and listening")
        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

        message = bytesAddressPair[0]
        address = bytesAddressPair[1]
        clientMsg = "Message from Client:{}".format(message)
        clientIP  = "Client IP Address:{}".format(address)
        print(clientMsg)
        print(clientIP)

        bytesToSend         = str.encode(str(message).upper())
        UDPServerSocket.sendto(bytesToSend, address)
    UDPServerSocket.close()
    
servers = [Thread(target=server, args=(i,)) for i in range(3)]
for sv in servers: sv.start()
