import socket
import datetime

dAddress = ("10.10.5.2", 30430)

localIP ="10.10.6.2"
localPort = 30301

bufferSize = 1024


UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))

bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
message = bytesAddressPair[0]
address = bytesAddressPair[1]
clientMsg = "Message from Client:{}".format(message)
clientIP  = "Client IP Address:{}".format(address)
print(clientMsg)
print(clientIP)

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPClientSocket.sendto(message, dAddress)

msgFromServer = UDPClientSocket.recvfrom(bufferSize)
 
msg = "Message from Server {}".format(msgFromServer[0])
print(msg)
UDPServerSocket.sendto(bytesToSend, address)
