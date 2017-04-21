count = 0
print ("You have",count,"coins")
while True:
	answer = input("Do you want another? (yes/no)")
	if answer == "yes":
		count +=1
	else:
		print("Bye")
		break
	print("You have ",count,"coins")
