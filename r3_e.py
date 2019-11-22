import socket
import datetime

msgFromClient       = "testtesttest"

bytesToSend         = str.encode(msgFromClient)

r3Address = ("10.10.6.2", 30320)

bufferSize          = 1024

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
#UDPClientSocket.connect((serverAddressPort))
# Send to server using created UDP socket
UDPClientSocket.sendto(bytesToSend, r3Address)

msgFromServer = UDPClientSocket.recvfrom(bufferSize)
 
msg = "Message from Server {}".format(msgFromServer[0])
print(msg)
