import socket
import datetime
from threading import Thread 


# SETTINGS
localIP     ="10.10.4.1"
localPorts   = [30120]
bufferSize  = 1024

msgCount = 1000
msgFromClient = "testtesttest"

sAddress = ("10.10.2.2", 30010)
dAddress = ("10.10.5.2", 30410)

# Init
bytesToSend = str.encode(msgFromClient)
serverAddressPorts = [sAddress, dAddress]
f = open("link_costs.txt", "w")


def server(i):  
    UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    UDPServerSocket.bind((localIP, localPorts[i]))
    for x in range(msgCount):
        #print("UDP thread"+str(i)+" up and listening")
        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

        message = bytesAddressPair[0]
        address = bytesAddressPair[1]
        clientMsg = "Message from Client:{}".format(message)
        clientIP  = "Client IP Address:{}".format(address)
        #print(clientMsg)
        #print(clientIP)

        bytesToSend         = str.encode(str(message).upper())
        UDPServerSocket.sendto(bytesToSend, address)
    UDPServerSocket.close()


def client(i): 
    f.write("--- Individual Tests ---\n")
    totaltime = 0
    # Create a UDP socket at client side
    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    for x in range(msgCount):
        #UDPClientSocket.connect((serverAddressPorts[i]))
        # Send to server using created UDP socket
        UDPClientSocket.sendto(bytesToSend, serverAddressPorts[i])
        a = datetime.datetime.now()

        msgFromServer = UDPClientSocket.recvfrom(bufferSize)
        b = datetime.datetime.now()
        c = b - a
        totaltime += c.microseconds
        #print(c.microseconds/1000.0)
        msg = "Message from Server {}".format(msgFromServer[0])
        #print(msg)
        f.write(str(x) + " - " + str((c.microseconds)/1000.0) + "\n")
    UDPClientSocket.close()
    f.write("--- Average Cost ---\n")
    f.write(str(i) + " - " + str((totaltime/msgCount)/1000.0) + "\n")
    print(str((totaltime/msgCount)/1000.0) + "avg for " + str(i)) 

clients = [Thread(target=client, args=(i,)) for i in range(2)]
for cl in clients: cl.start()
servers = [Thread(target=server, args=(i,)) for i in range(1)]
for sv in servers: sv.start()
for sv in servers: sv.join()
for cl in clients: cl.join()
f.close()
