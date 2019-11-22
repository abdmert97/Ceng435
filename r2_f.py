import socket
import datetime
from threading import Thread 


# SETTINGS
msgCount = 1000
msgFromClient = "testtesttest"
bufferSize = 1024

sAddress = ("10.10.2.2", 30020)
r1Address = ("10.10.4.1", 30120)
r3Address = ("10.10.6.2", 30320)
dAddress = ("10.10.5.2", 30420)

# Init
bytesToSend = str.encode(msgFromClient)
serverAddressPorts = [sAddress , r1Address, r3Address, dAddress]
f = open("link_costs.txt", "w")

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

clients = [Thread(target=client, args=(i,)) for i in range(4)]
for cl in clients: cl.start()
for cl in clients: cl.join()
f.close()
