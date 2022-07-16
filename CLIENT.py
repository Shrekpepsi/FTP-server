import socket

Client=socket.socket()

Client.connect(('localhost',9283))

client_name=input("Enter your name : ")

Client.send(bytes(client_name,'utf-8'))

inp=input("Enter your string : ")

Client.send(bytes(inp,'utf-8'))

print('Your input has ',Client.recv(1024).decode(),' characters')





















