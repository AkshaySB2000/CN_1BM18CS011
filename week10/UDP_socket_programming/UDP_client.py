from socket import socket, AF_INET, SOCK_DGRAM
def main():
    s = socket(AF_INET,SOCK_DGRAM)
    ip = '192.168.0.105' 
    port = 12345 
    socket_addr = (ip,port)
    print("Hello UDP Server!")
    request=input("Enter Filename : ") 
    s.sendto(bytes(request,'utf-8'),socket_addr)  
    print(f"Request for contents of File : {request} has been sent to the Server.")
    response,addr = s.recvfrom(2048) 
    response = response.decode('utf-8')
    if addr == (ip,port) :
        print("-"*10)
        print(response)
        print("-"*10)
        print("Response has been received.")
        print("Bye Server!")
main()