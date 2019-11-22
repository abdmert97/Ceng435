import socket
import datetime
from threading import Thread 

msgFromClient = "Hello UDP Server"

bytesToSend = str.encode(msgFromClient)
sAddressPort = ("10.10.2.2", 30200)
r1AddressPort = ("10.10.4.1", 30210)
r3AddressPort = ("10.10.6.2", 30230)
dAddressPort = ("10.10.5.2", 30340)
serverAddressPorts = [r1AddressPort, r2AddressPort, r3AddressPort]

bufferSize = 1024
def client(i): 
    totaltime = 0
    for x in range(1000):
        # Create a UDP socket at client side
        UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
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
    print(str((totaltime/1000)/1000.0) + "avg for " + str(i)) 

clients = [Thread(target=client, args=(i,)) for i in range(3)]
for cl in clients: cl.start()
