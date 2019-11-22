import socket
import datetime

# SETTINGS
# Destination IP and port
dAddress = ("10.10.5.2", 30430)

localIP ="10.10.6.2"
localPort = 30300

bufferSize = 1024
# Open UDP server socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# Bind UDP socket for server to localIP in localPort
UDPServerSocket.bind((localIP, localPort))
# Open UDP socket for client
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

for i in range(1000):
    # Wait until the message is received from server
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    # Get data from received package
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    # Convert client message into string format
    clientMsg = "Message from Client:{}".format(message)
    clientIP  = "Client IP Address:{}".format(address)
    # Send the response(received message)
    UDPClientSocket.sendto(message, dAddress)
    # Wait until the message is received from client
    msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    # Convert message into string format
    msg = "Message from Server {}".format(msgFromServer[0])
    # Send the response(received message)
    UDPServerSocket.sendto(msg, address)
# Close sockets
UDPServerSocket.close()
UDPClientSocket.close()
