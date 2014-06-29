#My Credits by pTricKg
#demonstrates escape sequences

#\t = tab
print("\t\t\tpTricKg Credits")

#double backslash is how to print backslash without program erroring.
print("\t\t\t \\ \\ \\ \\ \\ \\ \\")
print("\t\t\t\tby")
print("\t\t\tPatrick Gorman")
print("\t\t\t \\ \\ \\ \\ \\ \\ \\")

print("\nI am learning Python") #use \ before quotes inside string
print("\nI believe \'I like\' Java a lot more but \"need\" to learn Python too")

#\a = system bell, sound system bell
#trying following code to get sound to work

##mixer.init() #you must initialize the mixer
alert=mixer.Sound('bell.wav')
alert.play()

print('\a')
print('\a')
print('\a')
print('\a')
print('\a')

input("\n\nPress enter to exit")
