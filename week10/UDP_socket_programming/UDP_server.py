from socket import socket, AF_INET, SOCK_DGRAM

s=socket(AF_INET,SOCK_DGRAM)
ip = '192.168.0.105' 
port=12345
s.bind((ip,port))    
print(f"The Server is Up and Listening at Port : { port } ")

while True:
    requestmsg,clientaddr = s.recvfrom(1024) 
    request=requestmsg.decode('utf-8')
    print(f"Hello Client {clientaddr}!")
    print(f"Request for contents of file : { request } has been received. ")
    try:
        with open(request,"r") as fd:
            contents=fd.read()
            print("Request Processed")
    except:
        contents="Request cannot be fulfilled. No such file exists."
        print("Request cannot be fulfilled")
    msg=contents  
    s.sendto(bytes(msg,'utf-8'),clientaddr) 
    print(f"Response Sent to Client { clientaddr }")
    print("Bye Client!")
    print("-"*10)