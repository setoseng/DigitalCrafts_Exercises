from turtle import *
from shapes import *
import random
bgcolor("black")
color("white")
for x in range(50):
	up()
	goto(random.randint(-200,200),random.randint(-200,200))
	for i in range(5):
		down()
		begin_fill()
		forward(30)
		right(144)
mainloop()