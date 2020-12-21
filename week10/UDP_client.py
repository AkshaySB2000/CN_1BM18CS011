import socket

clientMsg = "Hello UDP Server!"
bytesToSend = str.encode(clientMsg)
serverAddressPort = ("127.0.0.1", 20001)
bufferSize = 1024

# Create a UDP socket at client side
UDPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send to server using created UDP socket
UDPClientSocket.sendto(bytesToSend, serverAddressPort)

serverMsg = UDPClientSocket.recvfrom(bufferSize)
msg = "The message from Server: {}".format(serverMsg[0])
print(msg)