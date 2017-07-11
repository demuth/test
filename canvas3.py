#User must be on a Windows machine
#first you have to enter your name (in reality, the operator will scan a barcode on their helmet maybe) 
#fourteen boxes pop up in a window with the operator name
#clicking on boxes represents scanning a barcode for now and "barcode number" appears (will be the actual number when there is a barcode scanner)
#color of box (green, yellow, or red) is randomly chosen for now (in reality, red and yellow will be for errors) 
#if yellow, an error window pops up
#if red, a tone plays, error is displayed on the box, and an error window pops up 

#Need to figure out database connection 

import time
import random
import winsound
import mysql.connector
from Tkinter import *

#FUNCTIONS:
#this is a giant function that governs all the clicking on the screen that represents scanning a barcode for now 
#    I'm sure there's probably a way to cut this down because everything is repeated for each rectangle 
def mouseclick(event):
    w.focus_set()
    if event.x >50 and event.x < 300 and event.y > 25 and event.y < 725: #this if statement is on necessary since we're modeling a barcode scan with a click
        print "clicked at", event.x, event.y #this line is basically unnecessary 
        print(str(time.strftime("%Y/%m/%d %H:%M:%S"))) #will eventually write the date/time to the database instead of printing 
    if event.x > 50 and event.x < 300 and event.y > 25 and event.y < 75:
        color = ["red", "yellow", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green"]
        k1 = random.choice(color) #the color will actually be triggered by an error, not a random choice 
        w.create_rectangle(50,25,300,75, fill = k1)
        w.create_text(175,50,)
        if k1=="red":
            winsound.Beep(275,1000)
            w.create_text(175, 50, font = ("Courier", 20), text = "ERROR") #will also write error to the file, along with the date/time, etc. 
            errorbox=Toplevel()
            errorbox.title("Error Information")
            msg = Message(errorbox, text = "Error information from database")
            msg.pack()
        elif k1 == "yellow":
            w.create_text(175, 50, font = ("Courier", 20), text = "barcode number")
            errorbox=Toplevel()
            errorbox.title("Caution") #not sure exactly what yellow signifies 
            msg = Message(errorbox, text = "Error information from database")
            msg.pack()
        else:
            w.create_text(175, 50, font = ("Courier", 20), text = "barcode number") #ultimately name will be pulled from database after bar code is scanned
    elif event.x > 50 and event.x < 300 and event.y > 75 and event.y < 125:
        color = ["red", "yellow", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green"]
        k2 = random.choice(color)
        w.create_rectangle(50,75,300,125,fill=k2)
        if k2=="red":
            winsound.Beep(275,1000)
            w.create_text(175, 100, font = ("Courier", 20), text = "ERROR")
            errorbox=Toplevel()
            errorbox.title("Error Information")
            msg = Message(errorbox, text = "Error information from database")
            msg.pack()
        elif k2 == "yellow":
            w.create_text(175, 100, font = ("Courier", 20), text = "barcode number")
            errorbox=Toplevel()
            errorbox.title("Caution")
            msg = Message(errorbox, text = "Error information from database")
            msg.pack()
        else: 
            w.create_text(175, 100, font = ("Courier", 20), text = "barcode number")
    elif event.x > 50 and event.x < 300 and event.y > 125 and event.y < 175:
        color = ["red", "yellow", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green"]
        k3 = random.choice(color)
        w.create_rectangle(50,125,300,175, fill = k3)
        if k3=="red":
            winsound.Beep(275,1000)
            w.create_text(175, 150, font = ("Courier", 20), text = "ERROR")
            errorbox=Toplevel()
            errorbox.title("Error Information")
            msg = Message(errorbox, text = "Error information from database")
            msg.pack()
        elif k3 == "yellow":
            w.create_text(175, 150, font = ("Courier", 20), text = "barcode number")
            errorbox=Toplevel()
            errorbox.title("Caution")
            msg = Message(errorbox, text = "Error information from database")
            msg.pack()
        else: 
            w.create_text(175, 150, font = ("Courier", 20), text = "barcode number")
    elif event.x > 50 and event.x < 300 and event.y > 175 and event.y < 225: 
        color = ["red", "yellow", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green"]
        k4 = random.choice(color)
        w.create_rectangle(50,175,300,225, fill = k4)
        if k4=="red":
            winsound.Beep(275,1000)
            w.create_text(175, 200, font = ("Courier", 20), text = "ERROR")
            errorbox=Toplevel()
            errorbox.title("Error Information")
            msg = Message(errorbox, text = "Error information from database")
            msg.pack()
        elif k4 == "yellow":
            w.create_text(175, 200, font = ("Courier", 20), text = "barcode number")
            errorbox=Toplevel()
            errorbox.title("Caution")
            msg = Message(errorbox, text = "Error information from database")
            msg.pack()
        else: 
            w.create_text(175, 200, font = ("Courier", 20), text = "barcode number")
    elif event.x > 50 and event.x < 300 and event.y > 225 and event.y < 275:
        color = ["red", "yellow", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green"]
        k5 = random.choice(color)
        w.create_rectangle(50,225,300,275, fill = k5)
        if k5=="red":
            winsound.Beep(275,1000)
            w.create_text(175, 250, font = ("Courier", 20), text = "ERROR")
            errorbox=Toplevel()
            errorbox.title("Error Information")
            msg = Message(errorbox, text = "Error information from database")
            msg.pack()
        elif k5 == "yellow":
            w.create_text(175, 250, font = ("Courier", 20), text = "barcode number")
            errorbox=Toplevel()
            errorbox.title("Caution")
            msg = Message(errorbox, text = "Error information from database")
            msg.pack()
        else: 
            w.create_text(175, 250, font = ("Courier", 20), text = "barcode number")
    elif event.x > 50 and event.x < 300 and event.y > 275 and event.y < 325:
        color = ["red", "yellow", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green"]
        k6 = random.choice(color)
        w.create_rectangle(50,275,300,325, fill = k6)
        if k6=="red":
            winsound.Beep(275,1000)
            w.create_text(175, 300, font = ("Courier", 20), text = "ERROR")
            errorbox=Toplevel()
            errorbox.title("Error Information")
            msg = Message(errorbox, text = "Error information from database")
            msg.pack()
        elif k6 == "yellow":
            w.create_text(175, 300, font = ("Courier", 20), text = "barcode number")
            errorbox=Toplevel()
            errorbox.title("Caution")
            msg = Message(errorbox, text = "Error information from database")
            msg.pack()
        else:
            w.create_text(175, 300, font = ("Courier", 20), text = "barcode number")
    elif event.x > 50 and event.x < 300 and event.y > 325 and event.y < 375:
        color = ["red", "yellow", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green"]
        k7 = random.choice(color)
        w.create_rectangle(50,325,300,375, fill = k7)
        if k7=="red":
            winsound.Beep(275,1000)
            w.create_text(175, 350, font = ("Courier", 20), text = "ERROR")
            errorbox=Toplevel()
            errorbox.title("Error Information")
            msg = Message(errorbox, text = "Error information from database")
            msg.pack()
        elif k7 == "yellow":
            w.create_text(175, 350, font = ("Courier", 20), text = "barcode number")
            errorbox=Toplevel()
            errorbox.title("Caution")
            msg = Message(errorbox, text = "Error information from database")
            msg.pack()
        else: 
            w.create_text(175, 350, font = ("Courier", 20), text = "barcode number")
    elif event.x > 50 and event.x < 300 and event.y > 375 and event.y < 425:
        color = ["red", "yellow", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green"]
        k8 = random.choice(color)
        w.create_rectangle(50,375,300,425, fill = k8)
        if k8=="red":
            winsound.Beep(275,1000)
            w.create_text(175, 400, font = ("Courier", 20), text = "ERROR")
            errorbox=Toplevel()
            errorbox.title("Error Information")
            msg = Message(errorbox, text = "Error information from database")
            msg.pack()
        elif k8 == "yellow":
            w.create_text(175, 400, font = ("Courier", 20), text = "barcode number")
            errorbox=Toplevel()
            errorbox.title("Caution")
            msg = Message(errorbox, text = "Error information from database")
            msg.pack()
        else: 
            w.create_text(175, 400, font = ("Courier", 20), text = "barcode number")
    elif event.x > 50 and event.x < 300 and event.y > 425 and event.y < 475:
        color = ["red", "yellow", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green"]
        k9 = random.choice(color)
        w.create_rectangle(50,425,300,475, fill = k9)
        if k9=="red":
            winsound.Beep(275,1000)
            w.create_text(175, 450, font = ("Courier", 20), text = "ERROR")
            errorbox=Toplevel()
            errorbox.title("Error Information")
            msg = Message(errorbox, text = "Error information from database")
            msg.pack()
        elif k9 == "yellow":
            w.create_text(175, 450, font = ("Courier", 20), text = "barcode number")
            errorbox=Toplevel()
            errorbox.title("Caution")
            msg = Message(errorbox, text = "Error information from database")
            msg.pack()
        else: 
            w.create_text(175, 450, font = ("Courier", 20), text = "barcode number")
    elif event.x > 50 and event.x < 300 and event.y > 475 and event.y < 525:
        color = ["red", "yellow", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green"]
        k10 = random.choice(color)
        w.create_rectangle(50,475,300,525, fill = k10)
        if k10=="red":
            winsound.Beep(275,1000)
            w.create_text(175, 500, font = ("Courier", 20), text = "ERROR")
            errorbox=Toplevel()
            errorbox.title("Error Information")
            msg = Message(errorbox, text = "Error information from database")
            msg.pack()
        elif k10 == "yellow":
            w.create_text(175, 500, font = ("Courier", 20), text = "barcode number")
            errorbox=Toplevel()
            errorbox.title("Caution")
            msg = Message(errorbox, text = "Error information from database")
            msg.pack()
        else: 
            w.create_text(175, 500, font = ("Courier", 20), text = "barcode number")
    elif event.x > 50 and event.x < 300 and event.y > 525 and event.y < 575:
        color = ["red", "yellow", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green"]
        k11 = random.choice(color)
        w.create_rectangle(50,525,300,575, fill = k11)
        if k11=="red":
            winsound.Beep(275,1000)
            w.create_text(175, 550, font = ("Courier", 20), text = "ERROR")
            errorbox=Toplevel()
            errorbox.title("Error Information")
            msg = Message(errorbox, text = "Error information from database")
            msg.pack()
        elif k11 == "yellow":
            w.create_text(175, 550, font = ("Courier", 20), text = "barcode number")
            errorbox=Toplevel()
            errorbox.title("Caution")
            msg = Message(errorbox, text = "Error information from database")
            msg.pack()
        else: 
            w.create_text(175, 550, font = ("Courier", 20), text = "barcode number")
    elif event.x > 50 and event.x < 300 and event.y > 575 and event.y < 625:
        color = ["red", "yellow", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green"]
        k12 = random.choice(color)
        w.create_rectangle(50,575,300,625, fill = k12)
        if k12=="red":
            winsound.Beep(275,1000)
            w.create_text(175, 600, font = ("Courier", 20), text = "ERROR")
            errorbox=Toplevel()
            errorbox.title("Error Information")
            msg = Message(errorbox, text = "Error information from database")
            msg.pack()
        elif k12 == "yellow":
            w.create_text(175, 600, font = ("Courier", 20), text = "barcode number")
            errorbox=Toplevel()
            errorbox.title("Caution")
            msg = Message(errorbox, text = "Error information from database")
            msg.pack()
        else: 
            w.create_text(175, 600, font = ("Courier", 20), text = "barcode number")
    elif event.x > 50 and event.x < 300 and event.y > 625 and event.y < 675:
        color = ["red", "yellow", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green"]
        k13 = random.choice(color)
        w.create_rectangle(50,625,300,675, fill = k13)
        if k13=="red":
            winsound.Beep(275,1000)
            w.create_text(175, 650, font = ("Courier", 20), text = "ERROR")
            errorbox=Toplevel()
            errorbox.title("Error Information")
            msg = Message(errorbox, text = "Error information from database")
            msg.pack()
        elif k13 == "yellow":
            w.create_text(175, 650, font = ("Courier", 20), text = "barcode number")
            errorbox=Toplevel()
            errorbox.title("Caution")
            msg = Message(errorbox, text = "Error information from database")
            msg.pack()
        else: 
            w.create_text(175, 650, font = ("Courier", 20), text = "barcode number")
    elif event.x > 50 and event.x < 300 and event.y > 675 and event.y < 725:
        color = ["red", "yellow", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green"]
        k14 = random.choice(color)
        w.create_rectangle(50,675,300,725, fill = k14)
        if k14=="red":
            winsound.Beep(275,1000)
            w.create_text(175, 700, font = ("Courier", 20), text = "ERROR")
            errorbox=Toplevel()
            errorbox.title("Error Information")
            msg = Message(errorbox, text = "Error information from database")
            msg.pack()
        elif k14 == "yellow":
            w.create_text(175, 700, font = ("Courier", 20), text = "barcode number")
            errorbox=Toplevel()
            errorbox.title("Caution")
            msg = Message(errorbox, text = "Error information from database")
            msg.pack()
        else: 
            w.create_text(175, 700, font = ("Courier", 20), text = "barcode number")


#START GUI
master = Tk()

#creates a canvas 
w = Canvas(master, width = 600, height = 750)
w.bind("<Button-1>", mouseclick)
w.pack()

#operator will actually scan a bar code on their helmet and may only have access to certain tasks
name= raw_input("Enter name: ")
w.create_text(450,25,font=("Courier", 14), text = "Operator Name:")
w.create_text(450,50,font=("Courier", 14), text = name)
#will also write operator name to the database? 

#draw 14 stacked gray boxes on the left side of the screen 
#FIGURE OUT HOW TO DO THIS IN INCREMENTS WITH A LOOP
w.create_rectangle(50,25,300,75,fill = "gray")
w.create_rectangle(50,75,300,125,fill= "gray")
w.create_rectangle(50,125,300,175,fill="gray")
w.create_rectangle(50,175,300,225,fill="gray")
w.create_rectangle(50,225,300,275,fill="gray")
w.create_rectangle(50,275,300,325,fill="gray")
w.create_rectangle(50,325,300,375,fill="gray")
w.create_rectangle(50,375,300,425,fill="gray")
w.create_rectangle(50,425,300,475,fill="gray")
w.create_rectangle(50,475,300,525,fill="gray")
w.create_rectangle(50,525,300,575,fill="gray")
w.create_rectangle(50,575,300,625,fill="gray")
w.create_rectangle(50,625,300,675,fill="gray")
w.create_rectangle(50,675,300,725,fill="gray")

master.mainloop()
