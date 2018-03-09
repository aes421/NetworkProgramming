import socket

PORT = 8080
BUFF = 2048

server = socket.socket()
server.bind(('127.0.0.1', PORT))

server.listen(0)
print("Server listening on {0}".format(PORT))

(conn, address) = server.accept()
while True:
    response = b""
    while True:
        data = conn.recv(BUFF)
        response += data
        if(len(data) < BUFF):
            break

    if(response.decode() == 'FIN'):
        print("Goodbye")
        conn.close()
        break
    print("Recieved {0} from client".format(response.decode()))
    print("Echoing {0} from server".format(response.decode()))
    conn.send(response)