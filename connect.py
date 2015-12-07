import socket

HOST = ''
PORT = 50001


s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST , PORT))
s.listen(1)
conn , addr = s.accept()
conn.recv(1024)
#s.close()
