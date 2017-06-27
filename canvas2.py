#Version of canvas2 06/09/2017
#initially draws 4 squares on a canvas and randomly colors them 
#upon clicking on the canvas, the keyboard can be used to change the color of a random square
    # r key for red, o key for orange, y key for yellow, g key for green, b key for blue, or v key for violet 
#tone plays when red is randomly generated initially or when red is chosen using the r key on the keyboard 
#writes the last color chosen using the keyboard and the date/time of the selection to canvas.db file 

#Issues of this version: (1) randomly chooses which square will be colored instead of the user being able to click on the desired square
#    (2) writes only the last selection to the file i.e. appears to overwrite previous selections 

#Benefits of this version: (1) user selects color using the keyboard 

import os, sys
import random
import time
import winsound
from Tkinter import *
master = Tk()

#if the g key is pressed for green
def fgreen(event):
    s1 = [0,0,100,100]
    s2 = [100,0,200,100]
    s3 = [0,100,100,200]
    s4 = [100,100,200,200]
    s = [s1, s2, s3, s4]
    w.create_rectangle(random.choice(s), fill = "green")
    filename = "C:\\Users\\Olivia\\Desktop\\DUNE\\Python\\canvas.db"
    dirname = os.path.dirname(filename)
    if not os.path.exists(dirname):
        os.makedirs(dirname, 755)
    f = open(filename, 'w')
    f.write("green " + str(time.strftime("%Y/%m/%d %H:%M:%S")))
    f.close()

#if the r key is pressed for red
def fred(event):
    s1 = [0,0,100,100]
    s2 = [100,0,200,100]
    s3 = [0,100,100,200]
    s4 = [100,100,200,200]
    s = [s1, s2, s3, s4]
    w.create_rectangle(random.choice(s), fill = "red")
    winsound.Beep(275, 1000) #play tone if keyboard is used to create a red square
    filename = "C:\\Users\\Olivia\\Desktop\\DUNE\\Python\\canvas.db"
    dirname = os.path.dirname(filename)
    if not os.path.exists(dirname):
        os.makedirs(dirname, 755)
    f = open(filename, 'w')
    f.write("red " + str(time.strftime("%Y/%m/%d %H:%M:%S")))
    f.close()
    
#if the o key is pressed for orange
def forange(event):
    s1 = [0,0,100,100]
    s2 = [100,0,200,100]
    s3 = [0,100,100,200]
    s4 = [100,100,200,200]
    s = [s1, s2, s3, s4]
    w.create_rectangle(random.choice(s), fill = "orange")
    filename = "C:\\Users\\Olivia\\Desktop\\DUNE\\Python\\canvas.db"
    dirname = os.path.dirname(filename)
    if not os.path.exists(dirname):
        os.makedirs(dirname, 755)
    f = open(filename, 'w')
    f.write("orange " + str(time.strftime("%Y/%m/%d %H:%M:%S")))
    f.close()

#if the y key is pressed for yellow
def fyellow(event):
    s1 = [0,0,100,100]
    s2 = [100,0,200,100]
    s3 = [0,100,100,200]
    s4 = [100,100,200,200]
    s = [s1, s2, s3, s4]
    w.create_rectangle(random.choice(s), fill = "yellow")
    filename = "C:\\Users\\Olivia\\Desktop\\DUNE\\Python\\canvas.db"
    dirname = os.path.dirname(filename)
    if not os.path.exists(dirname):
        os.makedirs(dirname, 755)
    f = open(filename, 'w')
    f.write("yellow " + str(time.strftime("%Y/%m/%d %H:%M:%S")))
    f.close()

#if the b key is pressed for blue
def fblue(event):
    s1 = [0,0,100,100]
    s2 = [100,0,200,100]
    s3 = [0,100,100,200]
    s4 = [100,100,200,200]
    s = [s1, s2, s3, s4]
    w.create_rectangle(random.choice(s), fill = "blue")
    filename = "C:\\Users\\Olivia\\Desktop\\DUNE\\Python\\canvas.db"
    dirname = os.path.dirname(filename)
    if not os.path.exists(dirname):
        os.makedirs(dirname, 755)
    f = open(filename, 'w')
    f.write("blue " + str(time.strftime("%Y/%m/%d %H:%M:%S")))
    f.close()

#if the v key is pressed for violet 
def fviolet(event):
    s1 = [0,0,100,100]
    s2 = [100,0,200,100]
    s3 = [0,100,100,200]
    s4 = [100,100,200,200]
    s = [s1, s2, s3, s4]
    w.create_rectangle(random.choice(s), fill = "violet")
    filename = "C:\\Users\\Olivia\\Desktop\\DUNE\\Python\\canvas.db"
    dirname = os.path.dirname(filename)
    if not os.path.exists(dirname):
        os.makedirs(dirname, 755)
    f = open(filename, 'w')
    f.write("violet " + str(time.strftime("%Y/%m/%d %H:%M:%S")))
    f.close()

#user has to click the canvas with the mouse before they can use the keyboard 
def mouseclick(event):
    w.focus_set()

w = Canvas(master, width = 200, height = 200)

#click in canvas and then use keyboard to color a random square
w.bind("<Button-1>", mouseclick)
w.bind("<g>", fgreen)
w.bind("<r>", fred)
w.bind("<o>", forange)
w.bind("<y>", fyellow)
w.bind("<b>", fblue)
w.bind("<v>", fviolet)
w.pack()

#choose random colors from color list
color = ["red", "orange", "yellow", "green", "blue", "violet"]
c1 = random.choice(color)
c2 = random.choice(color)
c3 = random.choice(color)
c4 = random.choice(color)

#draw four squares, colored initially by the random selections made in lines 124-127
w.create_rectangle(0,0,100,100, fill = c1)
w.create_rectangle(100,0,200,100, fill = c2)
w.create_rectangle(0,100,100,200, fill = c3)
w.create_rectangle(100,100,200,200, fill = c4)

#add text instructions in bottom right square
w.create_text(150,125,text = "Click on canvas.")
w.create_text(150,150,text = "and use keyboard")
w.create_text(150,175,text = "to choose color.")

#play tone when a red square is randomly generated
if c1 == "red" or c2 == "red" or c3 == "red" or c4 == "red":
    winsound.Beep(275, 1000)

master.mainloop()
