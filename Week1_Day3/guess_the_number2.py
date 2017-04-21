print("Think of a number between 1-100")
bottom = 0
top = 100
guess = 0
while True:
	guess +=1	
	middle = int((bottom+top)/2)
	print(middle)
	answer = input("higher,lower, or correct?")
	if answer=="correct":
		print("The number was:",middle)
		print("Number of Guesses:",guess)
		break
	elif answer=="higher" :
		bottom = int(middle + 1)
	else:
		top = int(middle - 1)