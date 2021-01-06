import random as r

number=r.randint(0,1000)

attempts=0

while True:

	input_number=int(input("Guess the number (Between 1 and 1000): "))	attempts +=1

	if input_number ==number :

		print(" Yes, your guess is correct! ")

		break

	if input_number>number:

		print(" Incorrect ! please try to guess a smaller number. ")

	else:

		print(" Incorrect ! please try to guess a large number.")

print("You tried",attempts,"times to find the correct number. ")
