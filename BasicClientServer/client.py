import socket

PORT = 8080

client = socket.socket()
client.connect(('127.0.0.1', PORT))
msg = b"Hello!"
print("Sending from {0} client".format(msg.decode()))
client.send(msg)
print("Recieved {0} from server".format((client.recv(4096)).decode()))