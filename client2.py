# Import socket module
import socket			

# Create a socket object
s = socket.socket()		

# Define the port on which you want to connect
port = 55555			

# connect to the server on local computer
s.connect(('192.168.59.44', port))

# receive data from the server and decoding to get the string.
print (s.recv(1024).decode())
data=''
angle =10
while(data != "stop"):
    print("what angle buddy:\n")
    angle = input()
#    s.send(str(angle).encode('utf8'))
    data = str(angle).encode('utf8')
    s.send(data)
# close the connection
s.close()	
	

