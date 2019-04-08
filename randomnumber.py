import math

myGuess = int(input("Type a number from 1 to 6: "))

import random

value = random.randint(1, 6)

if value == myGuess:
	print ("Correct!")
	print (" ")
	print ("Please play again!")
else:
	print ("Wrong answer")
	print (" ")
	print ("The correct answer was...")
	print ( value )