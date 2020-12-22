from socket import socket, AF_INET, SOCK_STREAM

s=socket(AF_INET,SOCK_STREAM)
HEADERSIZE=10   
ip = '192.168.0.105' 
port = 12345
s.bind((ip,port))  
s.listen(4)   
print(f"The Server is Up and Listening at Port : { port } ")

while True:
    clientsocket, clientaddr= s.accept()   
    print(f"Hello Client {clientaddr}!")
    request=clientsocket.recv(1024) 
    request=request.decode('utf-8')
    print(f"Client Request for contents of file : { request } has been received. ")
    try:
        with open(request,"r") as fd:
            contents=fd.read()
            print("Request has been processed")
    except:
        contents="Request cannot be fulfilled. No such file exists."
        print("Request cannot be fulfilled!")
    msg=f"{len(contents):<{HEADERSIZE}}"+contents   
    clientsocket.send(bytes(msg,'utf-8')) 
    print(f"Response Sent to Client { clientaddr }")
    print("Bye Client!")
    print("-"*10)