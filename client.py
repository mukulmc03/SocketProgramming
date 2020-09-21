import socket

c = socket.socket()     #Client Socket

c.connect(('localhost', 9999))

name = input("Enter Your Name")
c.send(bytes(name, 'utf-8'))

print(c.recv(1024).decode())     #1024 is buffer size to recieve response from server and decode() to decode byte format