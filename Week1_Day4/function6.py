from matplotlib import pyplot
from numpy import arange
import math

def f(x):
	return math.sin(x)
xs = arange(-5,6,0.1)
ys = []
for x in xs:
	ys.append(f(x))
pyplot.plot(xs, ys)
pyplot.show()	