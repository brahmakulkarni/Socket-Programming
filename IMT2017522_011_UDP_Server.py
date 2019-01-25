from socket import *

UDP_IP = ''
UDP_PORT = 60001

sock = socket(AF_INET,SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1000) # buffer size is 1000 bytes
    print "addr: ",addr
    data1 = map(int,data.split())
    if not data:break
    print "Recieved! Calculating..."
    data1.sort()
    data1.reverse()
    s = ''
    for i in data1:s+=str(i)+" "
    print "Sending.."
    print s
    sock.sendto(s,addr)
sock.close()
