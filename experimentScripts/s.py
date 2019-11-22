import socket
import datetime


# SETTINGS
# Addresses of the server nodes to be connected
r3Address = ("10.10.6.2", 30300)

bufferSize = 1024


# Initialize the client socket
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# Messaging procedure
for i in range(1000):
    # Record the clock at the send time
    sendTime  = datetime.datetime.now()
    # Time in string format 
    msgFromClient = str(sendTime)
    # Encode send time string
    bytesToSend   = str.encode(msgFromClient)
    # Send the message to server
    UDPClientSocket.sendto(bytesToSend, r3Address)
    # Wait until the response is received from server
    msgFromServer = UDPClientSocket.recvfrom(bufferSize) 
# Close the client socket
UDPClientSocket.close()
