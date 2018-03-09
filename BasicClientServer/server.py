import socket

PORT = 8080

server = socket.socket()
server.bind(('127.0.0.1', PORT))

server.listen(0)
print("Server listening on {0}".format(PORT))

while True:
    (conn, address) = server.accept()
    response = conn.recv(4096)
    print("Recieved {0} from client".format(response.decode()))
    print("Echoing {0} from server".format(response.decode()))
    conn.send(response)