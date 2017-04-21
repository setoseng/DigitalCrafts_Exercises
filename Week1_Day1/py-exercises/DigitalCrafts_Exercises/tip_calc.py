total = int(input("Total bill amount? "))
service = input("Level of service? (good,fair, or bad) ")
if service == "good":
	tip = total * .2
elif service == "fair":
	tip = total * .15
elif service == "bad":
	tip = total * .10
print ("Tip Amount: ${0:.2f}".format(tip))
print ("Total bill amount: $", total+tip)