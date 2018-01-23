import socket
import math

UDP_IP = "127.0.0.1"
UDP_PORT = 5008
clientSocket = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
clientSocket.bind((UDP_IP, UDP_PORT))
while True:
    data, addr = clientSocket.recvfrom(1024) # buffer size is 1024 bytes
    print "received message:", data
    n = math.factorial(int(data ))
    clientSocket.sendto(str(n),addr)
