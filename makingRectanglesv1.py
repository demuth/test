from Tkinter import *

i=0
k=14 #this is where we would read in the number of rectangles needed
leftx=50; lefty=25; rightx=300; righty=75#coordinates for the rectangle to be used in the w.create
#left refers to the top left corner of the rectangle, right refers to the bottom right corner

master=Tk();

w=Canvas(master, width=600, height=750)
w.pack()


while (i<k):
    if righty>=600:#if the first column of rectangles goes lower than y=600
        leftx=leftx+250; rightx=rightx+250; lefty=25; righty=75#this starts a new column of rectangles
    w.create_rectangle(leftx, lefty, rightx, righty)
    lefty=lefty+50; righty=righty+50
    i=i+1

master.mainloop()
