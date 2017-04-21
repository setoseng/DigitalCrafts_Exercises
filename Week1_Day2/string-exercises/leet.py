text_stuff = "LEET HACKER MAN"
for i in range (0,len(text_stuff)):
	if text_stuff[i]=="A":
		text_stuff = text_stuff.replace(text_stuff[i],"4")
	if text_stuff[i]=="E":
		text_stuff = text_stuff.replace(text_stuff[i],"3")
	if text_stuff[i]=="G":
		text_stuff = text_stuff.replace(text_stuff[i],"6")
	if text_stuff[i]=="I":
		text_stuff = text_stuff.replace(text_stuff[i],"1")
	if text_stuff[i]=="O":
		text_stuff = text_stuff.replace(text_stuff[i],"0")
	if text_stuff[i]=="S":
		text_stuff = text_stuff.replace(text_stuff[i],"5")
	if text_stuff[i]=="T":
		text_stuff = text_stuff.replace(text_stuff[i],"7")					
print(text_stuff)
