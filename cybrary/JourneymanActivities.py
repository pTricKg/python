import socket

'''1.1) Take two arguments, a list and an integer. The list is a series 
of strings; one of those strings will be the filename, the others will 
be the file contents. The integer is the location in the list of the file 
name. (Write each string to a separate line)

list:
a 0 <-contents
b 1 <-contents
c 2 <-contents
d 3 <-contents
e 4 <- filename
f 5 <-contents

item:
4

'''
def journeyman1(str_list , item):
    filename = str(str_list[item])
    f = open(filename, 'w+')
    for i in str_list:
        if i != str_list[item]:
            f.write(i)
    f.close()     
    return


'''1.2) Write a function which takes a single integer as an argument and 
returns the sum of every integer up to and including that number, use a 
generator.'''

def sum_generator(final_num):
    current_num = 0
    
    while(current_num <= final_num):
        yield current_num # output witout return or end
        current_num += 1
        
    # return range_sum #(Make this a yield)

def journeyman2(final_num):
    #return sum(range(final_num+1))
    range_sum = sum(sum_generator(final_num))
    return range_sum


'''1.3) Write a python script which connects to the included server 
on port 50001 and returns the message it receives.'''
def journeyman3():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create socket
    s.connect(('127.0.0.1',50001))
    received_string = s.recv(1024)
    s.close()
    return received_string


'''1.4) Create a class called person, with height, weight, hair color, 
and eye color fields, then implement it to describe yourself.'''
def journeyman4():
    class Person:
        
        def __init__(self, height, weight, hair, eye):
            #initalize
            self.height = 0
            self.weight = 0
            self.hair = ''
            self.eye = ''
            
            self.height = height
            self.weight = weight
            self.hair = hair
            self.eye = eye

            

    Me = Person(6, 190, 'Black', 'Black')
    print Me.height
    print Me.weight
    print Me.hair
    print Me.eye
    return
    


