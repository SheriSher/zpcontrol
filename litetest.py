from tkinter import *

def motion(e):
	x = e.x
	y = e.y
	root.title(f"{str(x)}:{str(y)}")
	cv.coords(oval, x-5,y-5,x+5,y+5)


root = Tk()
cv = Canvas(root)
oval = cv.create_oval((10,10,20,20), fill="black")
cv.pack(expand=1, fill="both")
print()

cv.bind("<Motion>", motion)
root.mainloop()
