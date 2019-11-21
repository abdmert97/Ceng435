import socket
import datetime
from threading import Thread 

localIP     ="10.10.4.1"
localPorts   = [30100]
bufferSize  = 1024

msgFromClient = "Hello UDP Server"

bytesToSend = str.encode(msgFromClient)



def server(i):  
    UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    UDPServerSocket.bind((localIP, localPorts[i]))
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
servers = [Thread(target=server, args=(i,)) for i in range(1)]
for sv in servers: sv.start()


serverAddressPorts = [("10.10.5.1", 30210), ("10.10.5.2", 30410)]

def client(i): 
    for x in range(0,5):
        # Create a UDP socket at client side
        UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        #UDPClientSocket.connect((serverAddressPorts[i]))
        # Send to server using created UDP socket
        UDPClientSocket.sendto(bytesToSend, serverAddressPorts[i])
        a = datetime.datetime.now()

        msgFromServer = UDPClientSocket.recvfrom(bufferSize)
        b = datetime.datetime.now()
        c = b - a
        print(c.microseconds/1000.0)
        msg = "Message from Server {}".format(msgFromServer[0])
        #print(msg)

clients = [Thread(target=client, args=(i,)) for i in range(2)]
for cl in clients: cl.start()
