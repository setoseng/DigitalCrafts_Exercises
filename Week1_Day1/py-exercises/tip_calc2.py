total = int(input("Total bill amount? "))
service = input("Level of service? (good,fair, or bad) ")
people = int(input("Split how many ways?"))
if service == "good":
	tip = total * .2
elif service == "fair":
	tip = total * .15
elif service == "bad":
	tip = total * .10
totalCost = total+tip
split = totalCost / people
print ("Tip Amount: ${0:.2f}".format(tip))
print ("Total bill amount: $", totalCost)
print ("Amount per person: $",split)