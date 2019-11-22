import socket
import datetime
from threading import Thread 

msgFromClient = "Hello UDP Server"

bytesToSend = str.encode(msgFromClient)
sAddressPort = ("10.10.2.2", 30020)
r1AddressPort = ("10.10.4.1", 30120)
r3AddressPort = ("10.10.6.2", 30320)
dAddressPort = ("10.10.5.2", 30420)
serverAddressPorts = [sAddressPort , r1AddressPort, r3AddressPort, dAddressPort]
f = open("link_costs.txt", "w")
bufferSize = 1024
def client(i): 
    f.write("--- Individual Tests ---\n")
    totaltime = 0
    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    for x in range(1000):
        # Create a UDP socket at client side
        #UDPClientSocket.connect((serverAddressPorts[i]))
        # Send to server using created UDP socket
        UDPClientSocket.sendto(bytesToSend, serverAddressPorts[0])
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
    f.write(str(i) + " - " + str((totaltime/1000)/1000.0) + "\n")
    print(str((totaltime/1000)/1000.0) + "avg for " + str(i)) 

clients = [Thread(target=client, args=(i,)) for i in range(4)]
for cl in clients: cl.start()
for cl in clients: cl.join()
f.close()
