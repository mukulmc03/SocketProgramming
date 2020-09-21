import socket

s = socket.socket()     #Server socket
print("Socket Created")

s.bind(('localhost', 9999))       # To bind socket with port no.

s.listen(3)     #To limit clients
print("Waiting for connection")

while True:
    c, addr = s.accept()        #C for client and its address
    name = c.recv(1024).decode()
    print("Connected with", addr, name)

    c.send(bytes('Welcome Client','utf-8'))