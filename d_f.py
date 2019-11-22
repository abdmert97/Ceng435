import socket
from threading import Thread 

# SETTINGS
localIP     ="10.10.5.2"
localPorts   = [30410, 30420, 30430]

# Count of server nodes to be started
svCount = 0

# Count of messages to be sent
msgCount = 1000
bufferSize  = 1024


def server(i):   
    # Initialize the server socket and bind to localip&localport
    UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    UDPServerSocket.bind((localIP, localPorts[i]))
    # Messaging procedure of server
    for x in range(msgCount):
        # Wait until the message is received from client
        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
        # Get data from received package
        message = bytesAddressPair[0]
        address = bytesAddressPair[1]
        # Send the response(upper case version of received message)
        bytesToSend         = str.encode(str(message).upper())
        UDPServerSocket.sendto(bytesToSend, address)
    # Close the server socket
    UDPServerSocket.close()
    
    
# Run the server threads
servers = [Thread(target=server, args=(i,)) for i in range(svCount)]
for sv in servers: sv.start()
for sv in servers: sv.join()
