import socket

serverName = '127.0.0.1'
serverPort = 12345

#create server
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#bind server 
server_socket.bind((serverName, serverPort ))

#listen
server_socket.listen(5)

while True:
    print("The Server is waiting for connection")
    client_socket, addr = server_socket.accept()
    print("The Client has been connected from",addr)
    while True:
        data = client_socket.recv(1024)
        if not data or data.decode('utf-8') == 'END':
            break
        print("Received from Client : %s"%data.decode("utf-8"))
        try:
            client_socket.send(bytes('Hello TCP Client!', 'utf-8'))
        except:
            print("User Exit!")
    client_socket.close()