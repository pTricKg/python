

def letter_count():
	count = 1
	given = raw_input("Give word and I'll count the letters: ")
	for l in given:
		print l + " makes " + str(count)
		count += 1
	print "You gave " + str(given) + " and it has " + str(count - 1) + " letters."
letter_count()

def vowels_count():
	count = 0
	lst = []
	given = raw_input("Give word and I'll count the vowels: ")
	for l in given:
		if l in "aeiouAEIOU":
			print l + " is vowel."
			count += 1
		
		lst.append(l)
	print given + " has " + str(count) + " vowels."
	print lst
vowels_count()	
