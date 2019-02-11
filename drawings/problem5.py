from turtle import *

sofi = Turtle()

def drawStar():
	for x in range(5):
		sofi.forward(50)
		sofi.left(144)

drawStar()

mainloop()