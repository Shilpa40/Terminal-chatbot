import socket 

port = 3000
CHUNK = 65535 # receive atmost these bytes of data at once

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # create a socket object
#socket.socket(family,type)
#AF_INET: family of ip4 ip adresses.
#type : udp, SOCK_STREAM: Tcp

#Need some ip addresses that the server will listen to when message comes
hostname = '127.0.0.1' # ip address. at local machine, same for everyone 
#aka.home, there is no place like 127.0.0.1

s.bind((hostname,port)) # bind the socket with the host machine and on port 3000

print(f"server is live on {s.getsockname()}")

# Run this server infinitely, till i stop it manually. 

while True: # infinite loop
    data.clientAdd = s.recvfrom(CHUNK)
    message  = data.decode('ascii') #by default data travels in bytes
    print(f"Rajat: {message} ")
    message_send = input("Reply: ")
    data = message_send.encode('ascii')
    # send data to the ip address that sent me the data.
    s.sendto(data,clientAdd)
