import socket

HOST = '127.0.0.1'
PORT = 50001

file_list = []

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.connect((HOST, PORT))

s.send("Test")
usr = raw_input(" Type something ")
print usr
s.send(usr)
s.close()
