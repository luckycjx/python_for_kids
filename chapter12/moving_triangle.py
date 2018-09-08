import time
import random
from tkinter import Tk, Canvas

tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
id = canvas.create_polygon(10, 10, 10, 60, 50, 35)

for x in range(60):
	canvas.move(id, 5, 0)
	tk.update()
	time.sleep(0.05)

for x in range(60):
	canvas.move(id, 0, 5)
	tk.update()
	time.sleep(0.05)

	
for x in range(60):
	canvas.move(id, -5, 0)
	tk.update()
	time.sleep(0.05)

	
for x in range(60):
	canvas.move(id, 0, -5)
	tk.update()
	time.sleep(0.05)