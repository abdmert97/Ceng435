import socket
import datetime
localIP     ="10.10.5.2"
localPort   = 30430
bufferSize  = 1024

f = open("end_to_end_20ms.txt", "w")

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))
totaltime = 0
for i in range(1000):
  bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

  message = bytesAddressPair[0]
  address = bytesAddressPair[1]

  raw_message = "{}".format(message)
  sendtime = datetime.datetime.strptime(raw_message, "%Y-%m-%d %H:%M:%S.%f")
  delay = (datetime.datetime.now()-sendtime).microseconds/1000.0
  totaltime += delay
  f.write(str(delay) + "\n")
  #print(str(delay))
  clientMsg = "Message from Client:{}".format(message)
  clientIP  = "Client IP Address:{}".format(address)
  #print(clientMsg)
  #print(clientIP)

  UDPServerSocket.sendto(message, address)
print("avg: " + str(totaltime/1000.0))
f.write("avg: " + str(totaltime/1000.0))
f.close()
