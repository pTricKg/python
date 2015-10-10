# Receive
HOST = ""
PORT = PORT
import socket
s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
s.bind((HOST , PORT))
s.listen(1)
conn , addr = s.accept()
conn.recv()

# Send
HOST = "LocalHost"
PORT = PORT
import socket
s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
s.connect((HOST , PORT))
s.send()





