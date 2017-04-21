from turtle import *

def triangle(size,fill,colour):
	color(colour)
	if fill=="yes":
		begin_fill()
	forward(size)
	left(120)
	forward(size)
	left(120)
	forward(size)
	end_fill()

def square(size,fill,colour):
	color(colour)
	if fill=="yes":
		begin_fill()
	forward(size)
	left(90)
	forward(size)
	left(90)
	forward(size)
	left(90)
	forward(size)
	end_fill()

def pentagon(size,fill,colour):
	color(colour)
	if fill=="yes":
		begin_fill()
	forward(size)
	left(72)
	forward(size)
	left(72)
	forward(size)
	left(72)
	forward(size)
	left(72)
	forward(size)
	end_fill()

def hexagon(size,fill,colour):
	color(colour)
	if fill=="yes":
		begin_fill()
	forward(size)
	left(60)
	forward(size)
	left(60)
	forward(size)
	left(60)
	forward(size)
	left(60)
	forward(size)
	left(60)
	forward(size)
	end_fill()

def octagon(size,fill,colour):
	color(colour)
	if fill=="yes":
		begin_fill()
	forward(size)
	left(45)
	forward(size)
	left(45)
	forward(size)
	left(45)
	forward(size)
	left(45)
	forward(size)
	left(45)
	forward(size)
	left(45)
	forward(size)
	left(45)
	forward(size)
	end_fill()

def star(size,fill,colour):
	if fill=="yes":
		begin_fill()
	color(colour)
	for i in range (5):
		forward(size)
		right(144)
	end_fill()
		
def circles(size,fill,colour):
	if fill=="yes":
		begin_fill()
	color(colour)
	width(5)
	circle(size)
	end_fill()

