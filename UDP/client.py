import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5008
#MESSAGE = "8"

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
#print "message:", MESSAGE
#ผมใช้อีกวิธีนะครับ
EN = raw_input('Number is: ')

clientSocket = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
clientSocket.sendto(EN, (UDP_IP, UDP_PORT))

data, servere = clientSocket.recvfrom(1024)
print "Answer = ",data
