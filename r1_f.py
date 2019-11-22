import socket
import datetime
from threading import Thread 


# SETTINGS
localIP     ="10.10.4.1"
localPorts   = [30120]
bufferSize  = 1024

clientCount = 2
serverCount = 1

msgCount = 1000
msgFromClient = "testtesttest"

sAddress = ("10.10.2.2", 30010)
dAddress = ("10.10.5.2", 30410)

# Init
bytesToSend = str.encode(msgFromClient)
serverAddressPorts = [sAddress, dAddress]
testResults = []
testAverages = []

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
    turnResults = []
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
        turnResults.append((c.microseconds)/1000.0)
    testResults.append(turnResults)
    UDPClientSocket.close()
    testAverages[i] = (totaltime/msgCount)/1000.0
    print(str((totaltime/msgCount)/1000.0) + "avg for " + str(i)) 

clients = [Thread(target=client, args=(i,)) for i in range(clientCount)]
for cl in clients: cl.start()
servers = [Thread(target=server, args=(i,)) for i in range(serverCount)]
for sv in servers: sv.start()
for sv in servers: sv.join()
for cl in clients: cl.join()
f = open("link_costs.txt", "w")
for i in range(clientCount):
    f.write("--- Individual Tests for" + str(i) + "  ---\n")
    for j in range(msgCount):
        f.write(str(i) + "->" + str(j) + " - " + str(testResults[i][j]) + "\n")
    f.write("--- Average Cost ---\n")
    f.write(str(i) + " - " + str(testAverages[i]) + "\n")
f.close()
