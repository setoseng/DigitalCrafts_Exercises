file_name = input("Please input a file name you want to open: ")
file_stuff = input("What you want in this?")
file_handle = open(file_name,'w')
file_handle.write(file_stuff)
file_handle.close()
file_handle = open(file_name,'r')
content = file_handle.read()
print(content)
file_handle.close()