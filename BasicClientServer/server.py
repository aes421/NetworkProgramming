import socket

PORT = 8080
BUFF = 1024

server = socket.socket()
server.bind(('127.0.0.1', PORT))

server.listen(0)
print("Server listening on {0}".format(PORT))

while True:
    (conn, address) = server.accept()
    response = b""
    while True:
        data = conn.recv(BUFF)
        response += data
        if(len(data) < BUFF):
            break
        
    print("Recieved {0} from client".format(response.decode()))
    print("Echoing {0} from server".format(response.decode()))
    conn.send(response)