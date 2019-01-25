from socket import *

TCP_IP = ''
TCP_PORT = 5001
BUFFER_SIZE = 4096

print "Connection established! Waiting to receive array..."
mysocket = socket(AF_INET,SOCK_STREAM)
mysocket.bind((TCP_IP,TCP_PORT))
mysocket.listen(1)

# print connection, address
while 1:
    connection, address = mysocket.accept()
    a = connection.recv(BUFFER_SIZE)
    print a,"Blah"
    data = map(int,a.split())
    if not data: break
    data.sort()
    #print TCP_IP, "Hello"
    s = ''
    for i in data:s+=str(i)+" "
    connection.send(s)
    connection.close()
print "Sorted array has been sent back to the client. Connection is closing."
