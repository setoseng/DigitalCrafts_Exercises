from matplotlib import pyplot

def f(x):
	return x * x
xs = list(range(-100,100))
ys = []
for x in xs:
	ys.append(f(x))
pyplot.plot(xs, ys)
pyplot.show()	