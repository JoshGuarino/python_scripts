import socket 
ip = socket.gethostbyname('192.168.0.1')
#print (ip)

IP1 = socket.gethostbyname(socket.gethostname()) # local IP adress of your computer
#IP2 = socket.gethostbyname('Nicholas-PC') # IP adress of remote computer

print(IP1)
#print(IP2)
