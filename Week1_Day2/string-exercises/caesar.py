alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
message = "lbh zhfg hayrnea jung lbh unir yrnearq"
st = list(message)
new_message = []
tempz =0
z = 0
for y in range (0,len(st)):

	if st[y] != " ":
		for i in range(0,26):
			if st[y] == alpha[i]:
				tempz = i
		
		z = (tempz -13) % 26 
		new_message.append(alpha[z])

	else:
		new_message.append(" ")

print ("".join(new_message))