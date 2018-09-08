import time
import random
from tkinter import Tk, Canvas

tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()

def random_triangle():
	x1 = random.randrange(400)
	y1 = random.randrange(400)
	x2 = random.randrange(400)
	y2 = random.randrange(400)
	x3 = random.randrange(400)
	y3 = random.randrange(400)
	canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill='', outline='black')

for x in range(10):
    random_triangle()
    tk.update()

tk.mainloop()