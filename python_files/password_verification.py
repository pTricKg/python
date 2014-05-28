#-----------------------------------------------
#password_test.py
#   example of if/else, lists, assignments,raw_input,
#   comments and evaluations
#-----------------------------------------------
# Assign the users and passwords
users = [input('Create your username => ')]
passwords = [input('Create your password => ')]
users = ['Patrick','Jenica','Cauy','Abrielle','JJim']
passwords = ['access','dog','12345','kids','qwerty']
#-----------------------------------------------
# Get username and password
usrname =(input('Enter your username => '))
pwd =(input('Enter your password => '))
#-----------------------------------------------
# Check to see if user is in the list
if usrname in users:
    position = users.index(usrname) #Get the position in the list of the users
    if pwd == passwords[position]:  #Find the password at position
#   if pwd == passwords[]: 
        print('Hi there, %s. Access granted.' % usrname)
    else:
        print('Password incorrect. Access denied.')
else:
    print("Sorry...I don't recognize you. Access denied.")
