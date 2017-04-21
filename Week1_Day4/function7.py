from matplotlib import pyplot
from numpy import arange
import math

def f(x):
	x+1
	return x
c = int(input("Celcius "))	
xs = list(range(c,int(c*9/5+32)))
ys = []
for x in xs:
	ys.append(f(x))
pyplot.plot(xs, ys)
pyplot.show()	