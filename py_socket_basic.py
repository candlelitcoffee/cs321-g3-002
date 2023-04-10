our_socket = socket(AF_INET, SOCK_DGRAM) # Open socket
our_socket.sendto(<<packet>>, <<server name and port combo>>)
msg = our_socket.recvfrom(<<port number to receive from>>)
our_socket.close() # Close socket
