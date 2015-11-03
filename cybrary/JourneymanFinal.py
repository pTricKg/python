import socket
'''
1.5) Python Journeyman: Write a Python server which:
	receives a connection from the included client (JourneymanFinal.py)
	stores received data in a file, then adds the file to a list
	returns the data from the file when requested
	deals with errors and missing files
'''

def load_data(conn, fname):
	fobject = file(fname , "r+")
	conn.send(fobject.read())
	conn.close()
	fobject.close()
	return fobject

def save_data(conn):
	fname = conn.recv(1024)
	fobject = file(fname , "w+")
	data = conn.recv(1024)
	print "f%s %s" % (fname , data)
	fobject.write(data)
	file_list.append(fname)
	fobject.close()
	conn.close()
	return fname

def main():
	HOST = ''
	PORT = 50001
	options = ['SAVE' , 'LOAD']
	file_list = []
	while(True):
		s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
		s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		s.bind((HOST , PORT))
		s.listen(1)
		conn , addr = s.accept()
		conn.recv(1024)
		if conn.recv(1024) == options[0]:
			file_list.append(save_data(conn))
		if conn.recv(1024) == options[1]:
			fname = conn.recv(1024)
			load_data(conn.fname)
main()
