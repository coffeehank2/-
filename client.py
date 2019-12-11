import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ("localhost", 1313)
print("Connecting to %s:%s" % server_address)
sock.connect(server_address)

message = b"To Infinity ... "
print('Client send"%s"' % message.decode())
sock.sendall(message)

reply = sock.recv(11)
print('Client received "%s"' % reply.decode())

sock.close()
