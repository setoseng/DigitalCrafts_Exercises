from matplotlib import pyplot

def f(x):
	if (x%2)==0:
		return (-1)
	if (x%2)!=0:
		return 1
xs = list(range(-5,6))
ys = []
for x in xs:
	ys.append(f(x))
pyplot.bar(xs, ys)
pyplot.show()	