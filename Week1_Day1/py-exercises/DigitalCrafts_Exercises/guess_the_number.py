import random
secret_number = random.randint(1,10)
print("I am thinking of a number between 1 and 10.")
count = 5
while count>0:
	count -=1
	num = int(input("What's the number? "))
	if num == secret_number:
		print("Yes! You Win!")
		break
	elif num<secret_number:
		print(num,"is too low.")
		print("You have ",count,"guesses left")
	elif num>secret_number:
		print(num,"is too high.")
		print("You have ",count,"guesses left")
	if count == 0:
		print("You ran out of guesses!")	
