from socket import socket, AF_INET, SOCK_STREAM
def main():
    s = socket(AF_INET,SOCK_STREAM)
    HEADERSIZE=10  
    ip = '192.168.0.105' 
    port = 12345
    s.connect((ip,port))  
    print("Hello TCP Server!")
    request = input("Enter the filename: ") 
    s.send(bytes(request,'utf-8'))  
    print(f"Requesting the server for contents of file : {request} sent.")
    serverMsg = True
    fullMsg = ''
    while True:    
        response = s.recv(50)  
        response = response.decode('utf-8')
        if serverMsg:
            msglen= int(response[:HEADERSIZE])  
            serverMsg = False
        fullMsg += response
        if len(fullMsg)-HEADERSIZE == msglen : 
            print("-"*10)
            print(fullMsg[HEADERSIZE:])
            print("-"*10)
            print("Response from Server has been received.")
            s.close()
            print("Bye Server!")
            break
main()