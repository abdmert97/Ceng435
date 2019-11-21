import socket
from threading import Thread 
import datetime

msgFromClient = "Hello UDP Server"

bytesToSend = str.encode(msgFromClient)

serverAddressPort = ("10.10.5.1", 30211)

bufferSize = 1024
def client(): 
    for i in range(0,1):
        # Create a UDP socket at client side
        UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        #UDPClientSocket.connect((serverAddressPort))
        # Send to server using created UDP socket
        UDPClientSocket.sendto(bytesToSend, serverAddressPort)
        a = datetime.datetime.now()

        msgFromServer = UDPClientSocket.recvfrom(bufferSize)
        b = datetime.datetime.now()
        c = b - a
        print(c.milliseconds)
        msg = "Message from Server {}".format(msgFromServer[0])
        #print(msg)

clients = [Thread(target=client, args=()) for i in range(5)]
for cl in clients: cl.start()
