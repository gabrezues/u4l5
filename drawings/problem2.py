from turtle import *

sofi = Turtle()

def drawTri():
	for x in range(3):
		sofi.forward(100)
		sofi.left(120)

for x in range(12):
	drawTri()
	sofi.left(30)

mainloop()