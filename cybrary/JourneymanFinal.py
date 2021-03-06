import socket
'''
1.5) Python Journeyman: Write a Python server which:
	receives a connection from the included client (JourneymanFinal.py)
	stores received data in a file, then adds the file to a list
	returns the data from the file when requested
	deals with errors and missing files
'''

def load_data(conn, fname):
	print "Load file"
	fobject = file(fname , "r+")
	data = fobject.read()
	conn.send(data)
	conn.close()
	fobject.close()
	return

def save_data(conn):
	print "Save file"
	fname = conn.recv(1024)
	fobject = file(fname , "w+")
	data = conn.recv(1024)
	print "%s:\t%s" % (fname , data)
	fobject.write(data)
	file_list.append(fname)
	fobject.close()
	conn.close()
	return fname

def main():
	HOST = ''
	PORT = 50001
		
	options = ['SAVE\n' , 'LOAD\n']
	file_list = []

	s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	s.bind((HOST , PORT))
	
	while(True):
		
		s.listen(1)
		conn , addr = s.accept()
		d = conn.recv(1024)

		print d
		if d == options[0]:
			file_list.append(save_data(conn))
		elif d == options[1]:
			if fname not in file_list:
				conn.send("File Not Found")
				conn.close()
			else:
				fname = conn.recv(1024)
				load_data(conn, fname)
		else:
			print "What the heck!"
main()
