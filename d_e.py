import socket
import datetime
localIP     ="10.10.5.2"
localPort   = 30430
bufferSize  = 1024


UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))

bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

message = bytesAddressPair[0]
address = bytesAddressPair[1]

raw_message = "{}".format(message)
sendtime = datetime.datetime.strptime(raw_message, "%Y-%m-%d %H:%M:%S.%f")
print("formatted: " + str(sendtime.microsecond))
clientMsg = "Message from Client:{}".format(message)
clientIP  = "Client IP Address:{}".format(address)
print(clientMsg)
print(clientIP)

UDPServerSocket.sendto(message, address)
