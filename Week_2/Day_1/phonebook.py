#Menu
print("Electronic Phone Book")
print("======================")
print("1. Look up an entry")
print("2. Set an entry")
print("3. Delete an entry")
print("4. List all entries")
print("5. Quit")
dial = int(input("What would you like to do (1-5)? "))
if dial == 1:
	name_entry = input("What is the person's name you would like to look up?")
	file_handle = open('phonebook.txt','r')
	content = file_handle.read()
	print(content.find(name_entry))
