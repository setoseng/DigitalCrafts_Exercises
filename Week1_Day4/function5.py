from matplotlib import pyplot
import math

def f(x):
	return math.sin(x)
xs = list(range(-5,6))
ys = []
for x in xs:
	ys.append(f(x))
pyplot.plot(xs, ys)
pyplot.show()	