import socket
import datetime
from threading import Thread 


# SETTINGS
localIP     ="10.10.6.2"
localPorts   = [30320]
bufferSize  = 1024

# Count of server and client nodes to be started
svCount = 2
clCount = 1

# Count of messages to be sent or received
msgCount = 1000
msgFromClient = "testtesttest"

# Addresses of the server nodes to be connected
sAddress = ("10.10.2.2", 30030)
dAddress = ("10.10.5.2", 30430)

# INIT
# Convert message to byte
bytesToSend = str.encode(msgFromClient)
serverAddressPorts = [sAddress, dAddress]
# Open the file to save link costs
f = open("link_costs.txt", "w")
# Averages of the RTT's
testResults = []



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


def client(i): 
    # The total time taken(in microseconds) for all messages in this connection
    totaltime = 0
    # Initialize the client socket
    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    # Messaging procedure of client
    for x in range(msgCount):
        # Send the message to server
        UDPClientSocket.sendto(bytesToSend, serverAddressPorts[i])
        # Record the clock at the send time
        sendTime = datetime.datetime.now()
        # Wait until the response is received from server
        msgFromServer = UDPClientSocket.recvfrom(bufferSize)
        # Record the clock at the send time
        receiveTime = datetime.datetime.now()
        # Delay is the difference of clocks at send and receive times
        delay = receiveTime - sendTime
        totaltime += delay.microseconds
        # Write result of this message to the file 
        f.write(str(i) + "->" + str(x) + " - " + str((delay.microseconds)/1000.0) + "\n")
    # Close the client socket
    UDPClientSocket.close()
    # Save the average results to the testResults
    testResults.append((totaltime/msgCount)/1000.0)
    
    
# Run the client threads
clients = [Thread(target=client, args=(i,)) for i in range(clCount)]
for cl in clients: cl.start()
    
# Run the server threads
servers = [Thread(target=server, args=(i,)) for i in range(svCount)]
for sv in servers: sv.start()
for sv in servers: sv.join()
for cl in clients: cl.join()
    
# Save the averages on the file after all messages are sent and close file
for i in range(clCount):
    f.write(str(i) + " - " + str(testResults[i]) + "\n")
f.close()
