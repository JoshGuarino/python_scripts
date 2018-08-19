import socket 

host_name = input('Enter the host name or IP address: \n')
status = False
while status == False:
    try:
        ip = socket.gethostbyname(host_name) #IP address of host
        status = True
    except:
        print("Error 404 not found.")
        host_name = input('Enter the host name or IP address: \n')
        
ip_local = socket.gethostbyname(socket.gethostname()) # local IP address of your computer
print('host IP: ' + ip)
print('local IP: ' + ip_local)




