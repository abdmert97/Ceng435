import socket
from threading import Thread 

localIP     ="10.10.4.1"
localPort   = 30211
bufferSize  = 1024

msgFromClient = "Hello UDP Server"

bytesToSend = str.encode(msgFromClient)

serverAddressPort = ("10.10.4.1", 30211)



def server(i):  
    UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    UDPServerSocket.bind((localIP, localPort))
    while(True):
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
servers = [Thread(target=server, args=(i,)) for i in range(5)]
for sv in servers: sv.start()


def client(): 
    for i in range(0,5):
        # Create a UDP socket at client side
        UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        #UDPClientSocket.connect((serverAddressPort))
        # Send to server using created UDP socket
        UDPClientSocket.sendto(bytesToSend, serverAddressPort)

        msgFromServer = UDPClientSocket.recvfrom(bufferSize)
        
        msg = "Message from Server {}".format(msgFromServer[0])
        print(msg)

clients = [Thread(target=client, args=()) for i in range(5)]
for cl in clients: cl.start()
