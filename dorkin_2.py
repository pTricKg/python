c = ""
s = []

ur_list = raw_input("give me things to add to list: ")

if ur_list is not "":
	for l in ur_list:
		s.append(l)
		print s
		#c = l
		c = c + l
print "this is string " + c
print "this is list " + str(s)
