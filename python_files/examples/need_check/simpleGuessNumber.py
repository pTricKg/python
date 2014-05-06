import random
import time

answer = random.randint(1, 100)

print ("Guess my number")

time1 = time.time()

while True:
    choice = int(input())
    if choice < answer:
        print ("Higher")
    elif choice > answer:
        print ("Lower")
    elif choice == answer:
        break
print ("Correct!")

time2 = time.time()
total_time = str(int(time2 - time1))

print ("You guessed correct in " + total_time + " seconds!")
