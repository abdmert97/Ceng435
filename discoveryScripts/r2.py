import socket
import datetime
from threading import Thread 


# SETTINGS
# Count of messages to be sent or received
msgCount = 1000
msgFromClient = "testtesttest"
bufferSize = 1024

# Count of client nodes to be started
clCount = 4

# Addresses of the server nodes to be connected
sAddress = ("10.10.2.2", 30020)
r1Address = ("10.10.4.1", 30120)
r3Address = ("10.10.6.2", 30320)
dAddress = ("10.10.5.2", 30420)

# INIT
# Averages of the RTT's
testResults = []
# Convert message to byte
bytesToSend = str.encode(msgFromClient)
serverAddressPorts = [sAddress , r1Address, r3Address, dAddress]
# Open the file to save link costs
f = open("link_costs.txt", "w")


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
for cl in clients: cl.join()
    
# Save the averages on the file after all messages are sent and close file
for i in range(clCount):
    f.write(str(i) + " - " + str(testResults[i]) + "\n")
f.close()
