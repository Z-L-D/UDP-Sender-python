import socket

command = b"Hello from Python"
address = "127.0.0.1"
port = 5500

socket_object = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM)
socket_object.sendto(command, (address, port))