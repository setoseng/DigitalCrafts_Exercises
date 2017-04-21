def play():
	while True:
		c = input("Do you want to play again? (Y/N)?")
		if c == "Y":
			return True
		elif c == "N":
			return False
		else:
			print("Invalid Input")
	
play()		