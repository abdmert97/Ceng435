import socket
import datetime

r3Address = ("10.10.6.2", 30300)

bufferSize          = 1024

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
for i in range(1000):
    # Create a UDP socket at client side

    a = datetime.datetime.now()
    msgFromClient = str(a)
    bytesToSend         = str.encode(msgFromClient)
    UDPClientSocket.sendto(bytesToSend, r3Address)

    msgFromServer = UDPClientSocket.recvfrom(bufferSize)

    msg = "Message from Server {}".format(msgFromServer[0])
    #print(msg)
