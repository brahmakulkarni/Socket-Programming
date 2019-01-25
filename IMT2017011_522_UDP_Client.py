from socket import *

UDP_IP = '172.16.80.194'
UDP_PORT = 60001
BUFFER_SIZE = 4096

mysocket = socket(AF_INET,SOCK_DGRAM)
print "Provide the array of numbers by separating the elements with spaces:",
mysocket.sendto(raw_input(), (UDP_IP,UDP_PORT))
data = mysocket.recv(BUFFER_SIZE)
mysocket.close()
print "The sorted list is:", data
