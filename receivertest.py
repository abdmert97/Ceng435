import socket
import Thread from threading

localIP     ="10.10.4.1"
localPort   = 30211
bufferSize  = 1024

msgFromServer       = "Hello UDP Client"
bytesToSend         = str.encode(msgFromServer)
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))

def server():  
    print("UDP thread up and listening")
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientMsg = "Message from Client:{}".format(message)
    clientIP  = "Client IP Address:{}".format(address)
    print(clientMsg)
    print(clientIP)

    UDPServerSocket.sendto(bytesToSend, address)
servers = [Thread(target=server, args=()) for i in range(5)]
for sv in servers: sv.start()
