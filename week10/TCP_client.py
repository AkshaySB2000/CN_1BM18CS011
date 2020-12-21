import socket

serverName = '127.0.0.1'
serverPort = 12345

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((serverName,serverPort))
payload='Hello TCP Server!'
try:
    while True:
        client_socket.send(payload.encode('utf-8'))
        data = client_socket.recv(1024)
        print(str(data))
        more = input('Do you wish to send more data to the Server?\n')
        if more.lower() == 'y':
            payload = input("Enter the payload\n")
        else:
            break
except KeyboardInterrupt:
    print("User Exit!")
client_socket.close()