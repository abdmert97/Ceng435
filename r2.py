import config

from socket import *

#Port of this server.
localServerPort = 30212

#IP of Broker.
brokerServerName = '10.10.2.1'

#Port of Broker.
brokerServerPort = 30211

#Initialize localSocket and listen to localServerPort.
localSocket = socket(AF_INET, SOCK_DGRAM)
localSocket.bind(('10.10.1.2', localServerPort))

#Initialize brokerSocket and connect to Broker.
brokerSocket = socket(AF_INET, SOCK_DGRAM)
brokerSocket.connect((brokerServerName, brokerServerPort))

while True:
    (dataFDest, addrDest) = localSocket.recvfrom(config.msg_size)
    #Forward the sentence to Broker.
    brokerSocket.send(dataFDest)

localSocket.close()
brokerSocket.close()
