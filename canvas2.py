#draw three squares, randomly color each square, produce sound when red is generated, use keyboard to color the last square
import random
import winsound
from Tkinter import *
master = Tk()

def fgreen(event):
    w.create_rectangle(100,100,200,200, fill = "green")

def fred(event):
    w.create_rectangle(100,100,200,200, fill = "red")
    
def fredtone(event):
	winsound.Beep(275, 1000)
    
def forange(event):
    w.create_rectangle(100,100,200,200, fill = "orange")

def fyellow(event):
    w.create_rectangle(100,100,200,200, fill = "yellow")

def fblue(event):
    w.create_rectangle(100,100,200,200, fill = "blue")

def fviolet(event):
    w.create_rectangle(100,100,200,200, fill = "violet")

def mouseclick(event):
    w.focus_set()

w = Canvas(master, width = 200, height = 200)

#click in canvas and then use keyboard to color the fourth square
w.bind("<g>", fgreen)
w.bind("<r>", fred, add="+")
w.bind("<r>", fredtone, add="+")
w.bind("<o>", forange)
w.bind("<y>", fyellow)
w.bind("<b>", fblue)
w.bind("<v>", fviolet)
w.bind("<Button-1>", mouseclick)
w.pack()

#choose random colors from color list 
color = ["red", "orange", "yellow", "green", "blue", "violet"]
c1 = random.choice(color)
c2 = random.choice(color)
c3 = random.choice(color)

#draw three more squares
w.create_rectangle(0,0,100,100, fill = c1)
w.create_rectangle(100,0,200,100, fill = c2)
w.create_rectangle(0,100,100,200, fill = c3)

#add text
w.create_text(150,125,text = "Click on canvas.")
w.create_text(150,150,text = "and use keyboard")
w.create_text(150,175,text = "to choose color.")

#play tone when a red square is generated (but not if red is chosen by clicking 'r' key)
if c1 == "red" or c2 == "red" or c3 == "red":
    winsound.Beep(275, 1000)

master.mainloop()
