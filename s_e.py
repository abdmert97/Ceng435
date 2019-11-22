import socket
import datetime

# r3 IP and port
r3Address = ("10.10.6.2", 30300)

bufferSize          = 1024
# Open UDP socket
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
for i in range(1000):
    # Get current time
    a = datetime.datetime.now()
    # Time in string format 
    msgFromClient = str(a)
    # Encode time string
    bytesToSend   = str.encode(msgFromClient)
    # Send message to r3 route
    UDPClientSocket.sendto(bytesToSend, r3Address)
    # Wait until message is received and read message
    msgFromServer = UDPClientSocket.recvfrom(bufferSize) 
