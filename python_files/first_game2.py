message = "Hello, welcome to your practice interview."
print (message)
message2 = "Here we will practice some of the more difficult questions posed at today's interview. "
print (message2)
print "Shall we begin?"

answer0 = raw_input()
no = 1
yes = 1
if answer0 == 'no':
    print ( answer0 + "!" + "Well, thanks anyway for trying!"+ "Good-Bye!!")
else:
    print "I'm glad to hear it!  What is your name?"
##
##answer0 = raw_input()
##if answer0 == no:
##    print "Well, thanks anyway for trying!"
##    print "Good-Bye!"
##else:
##    print ("Can you tell me your name, please?")
    
answer1 = raw_input()
print ("Hello, " + answer1 + "." + "  How did you here about us?")
answer2 = raw_input()
print ( answer2 + ", OK." + "  What attracted you to this company?")
answer3 = raw_input()
print ( answer3 + ", That is a solid reason. Did you check out what we do?")
answer4 = raw_input()
no = 1
yes = 1
if answer4 == 'no':
    print ( answer4 + ", it seems you don't really want this job!  Please tell me why you bothered showing up?")
else:
    print ( answer4 + ", that is great!  Please tell me how your skills fit what we are looking for?")
answer5 = raw_input()
print ( answer5 + ", Really?")
print ("Would you like to talk more about that!")
answer6 = raw_input()
no = 1
yes = 1
if answer6 == 'no':
    print ( answer6 + "!" + "I'm sorry for asking")
##else:
##    print "I'm glad to hear it!  Please tell me what you disliked most about living there."

##why does this not work? I added else command, not sure why it works now like i want it. dont forget :
    ##yes = 1
    ##if yes:
        ##print "I'm glad to hear it!  Please tell me what you disliked most about living there."




    
