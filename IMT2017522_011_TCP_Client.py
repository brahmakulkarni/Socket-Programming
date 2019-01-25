from socket import *
TCP_IP = '172.16.82.34'
TCP_PORT = 5001
BUFFER_SIZE = 4096
l = raw_input("Enter the array with space separated integers\n")
s = socket(AF_INET,SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(l)
data = s.recv(BUFFER_SIZE)
s.close()
print "The sorted array is: ", data
