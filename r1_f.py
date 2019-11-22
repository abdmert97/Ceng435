import socket
import datetime
from threading import Thread 


# SETTINGS
localIP     ="10.10.4.1"
localPorts   = [30120]
bufferSize  = 1024

svCount = 1
clCount = 2
msgCount = 1000
msgFromClient = "testtesttest"

sAddress = ("10.10.2.2", 30010)
dAddress = ("10.10.5.2", 30410)

# Init
bytesToSend = str.encode(msgFromClient)
serverAddressPorts = [sAddress, dAddress]
f = open("link_costs.txt", "w")
testResults = []


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
        f.write(str(i) + "->" + str(x) + " - " + str((c.microseconds)/1000.0) + "\n")
    UDPClientSocket.close()
    testResults.append((totaltime/msgCount)/1000.0)
    print(str((totaltime/msgCount)/1000.0) + "avg for " + str(i)) 

clients = [Thread(target=client, args=(i,)) for i in range(clCount)]
for cl in clients: cl.start()
servers = [Thread(target=server, args=(i,)) for i in range(svCount)]
for sv in servers: sv.start()
for sv in servers: sv.join()
for cl in clients: cl.join()
for i in range(clCount):
    f.write(str(i) + " - " + testResults[i] + "\n")
f.close()
