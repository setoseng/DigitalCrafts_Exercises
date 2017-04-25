file_name = input("Please input a file name you want to open: ")
file_handle = open(file_name,'r')
content = file_handle.read()
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
word = content
d = {}
print(word)
for y in word:
	for x in alphabet:
		if y == x:
			if x in d:
				d[y] += 1
			else:
				d[y]=1			
print (d)
print(content)
file_handle.close()