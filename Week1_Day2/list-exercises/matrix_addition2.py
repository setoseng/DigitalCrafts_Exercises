l1 = [1,3,4], [2,4,4]
l2 = [5,2,5], [1,0,5]
nl = [0,0,0], [0,0,0]
for x in range(len(l1)):
	for y in range(len(l1[0])):
		nl[x][y] = l1[x][y] + l2[x][y]
for z in nl:
	print(z)	