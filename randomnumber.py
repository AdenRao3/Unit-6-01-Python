# Created by: Aden Rao
# Created on: April 7, 2019
# This program randomly picks a number between 1 and 6 and then it lets the user enter a number and then it will let you know if it is right.

# Imports math
import math

# Input for the user to enter a number and it tells them to enter a number
myGuess = int(input("Type a number from 1 to 6: "))

# Imports random function
import random

# Value of the correct number
value = random.randint(1, 6)

# If statement for if the user's answer is equal to the number to guess
if value == myGuess:
	print ("Correct!")
	print (" ")
	print ("Please play again!")
else:
	print ("Wrong answer")
	print (" ")
	print ("The correct answer was...")
	print ( value )
