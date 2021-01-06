import random
number=random.randint(1,1000)
x=0
low=1
high=1000
while True:
	print("Guess the number (between 1 and 1000): ")
	input_number=(low+high)//2
	print(" My guess is",input_number)
	x+=1
	if input_number ==number :
		print("Yes,your guess is Correct ! ")
		break
	if input_number>number:
		print(" Incorrect! Please try to guess a smaller number.")
		high=input_number-1
	else:
		print("Incorrect! Please try to guess large number.")
		low=input_number+1
print("You tried",x,"times to find the correct number.")