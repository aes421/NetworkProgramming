import socket

PORT = 8080
BUFF = 2048

client = socket.socket()
client.connect(('127.0.0.1', PORT))
print("Enter messages to be sent to server.  Type quit when you're done.")

while True:
    msg = input()
    if (msg == "quit"):
        client.shutdown(socket.SHUT_WR)
    else:
        msg = msg.encode()
        print("Sending from {0} client".format(msg.decode()))
        client.send(msg)

    #recieve server response
    response = b""
    while True:
        data = client.recv(BUFF)
        response += data
        if(len(data) < BUFF):
            break

    if (response.decode() == ''):
        print("Goodbye")
        client.close()
        break
    else:
        print("Recieved {0} from server".format(response.decode()))