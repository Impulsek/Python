import math
import random
count=0
while True:
	print("Guess the number between 1-100")
	number=random.randint(1,100)
	while True:
		guess=int(input("Your guess: "))
		count=count+1
		if(number==guess):
			print("You guessed right! You needed",count,"attempts")
			break
		elif(number>guess):
			print("Your number is lower")
		elif(number<guess):
			print("Your number is higher")
	menu=input("You want to continue? Y-yes N-no: ")
	if(menu=="N" or menu=="n"):
		break;

