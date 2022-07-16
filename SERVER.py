import socket

Server=socket.socket()

print("Socket created.")

Server.bind(('localhost',9283))

Server.listen(10)

print('Waiting for the Connections . . .')

while True:

    C,address=Server.accept()

    client_name=C.recv(1024).decode()

    inp=C.recv(1024).decode()

    size_of_string=len(inp)

    X=str(size_of_string)

    print("Connection established with : ",address,"\nClient Name : ",client_name)

    C.send(bytes(X,'utf-8'))

    C.close()


