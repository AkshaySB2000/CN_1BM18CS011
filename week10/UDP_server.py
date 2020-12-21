import socket

localIP = "127.0.0.1"
localPort = 20001
bufferSize = 1024
serverMsg = "Hello UDP Client!"
bytesToSend = str.encode(serverMsg)

# Create a datagram socket
UDPServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))
print("The UDP server is up and listening!")

# Listen for incoming datagrams

while (True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientMsg = "The message from Client: {}".format(message)
    clientIP = "Client IP Address: {}".format(address)
    print(clientMsg)
    print(clientIP)
    # Sending a reply to client
    UDPServerSocket.sendto(bytesToSend, address)