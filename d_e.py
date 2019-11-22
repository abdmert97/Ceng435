import socket
import datetime

# SETTINGS
localIP     ="10.10.5.2"
localPort   = 30430
bufferSize  = 1024

# Count of messages to be sent or received
msgCount = 1000

# Open the file to save end-to-end delays
f = open("end_to_end.txt", "w")

# Initialize the server socket and bind to localip&localport
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))
# The total time taken(in milliseconds) for all messages in this connection
totaltime = 0
# Messaging procedure
for i in range(msgCount):
  # Wait until the message is received from client
  bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
  # Get data from received package
  message = bytesAddressPair[0]
  address = bytesAddressPair[1]
  # Convert message into string format
  raw_message = "{}".format(message)
  # Decode the sendtime received as message
  sendtime = datetime.datetime.strptime(raw_message, "%Y-%m-%d %H:%M:%S.%f")
  # Calculate the delay
  delay = (datetime.datetime.now()-sendtime).microseconds/1000.0
  totaltime += delay
  # Write end to end delay of current message to file
  f.write(str(delay) + "\n")

# Send the response(received message)
UDPServerSocket.sendto(message, address)
# Close the server socket
UDPServerSocket.close()
# Save the average on the file after all messages are sent and close file
f.write("avg: " + str(totaltime/1000.0))
f.close()
