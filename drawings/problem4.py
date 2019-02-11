from turtle import *

sofi = Turtle()

def drawHexa(side):
	for x in range(6):
		sofi.forward(side)
		sofi.left(60)

drawHexa(50)
drawHexa(60)
drawHexa(70)
drawHexa(80)
drawHexa(90)
drawHexa(100)

mainloop()