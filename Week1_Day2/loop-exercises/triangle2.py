def triangle(n):
	k = 2*n-5
	for i in range(0,n):
		for j in range(0,k):
			print(end=" ")
		k = k - 1
		for j in range(0,i+1):
			print("* ", end="")
		print("\r")
n = int(input("Height?"))
triangle(n)