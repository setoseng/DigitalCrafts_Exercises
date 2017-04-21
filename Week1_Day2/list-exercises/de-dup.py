dump = [1,2,2,1,3,"kappa","kappa"]
nl = []
for x in dump:
	if x not in nl:
		nl.append(x)
print(nl)