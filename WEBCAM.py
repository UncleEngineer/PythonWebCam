import numpy as np
import cv2
from tkinter import *
from tkinter import ttk
#import tkinter as tk
from PIL import Image, ImageTk
import sys

window = Tk()  #Makes main window
window.overrideredirect(True)
window.wm_attributes("-topmost", True)
window.geometry("405x305+1515+0")
display1 = ttk.Label(window)
display1.grid(row=1, column=0, padx=0, pady=0)  #Display 1
cap = cv2.VideoCapture(0)

def show_frame():
    _, frame = cap.read()
    frame = cv2.resize(frame, (400,300))
    #frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(master = display1, image=img)
    display1.imgtk = imgtk #Shows frame for display 1
    display1.configure(image=imgtk)
    
    window.after(10, show_frame)



def CloseProgram(event=None):
	window.destroy()

global statemin
statemin = True
def Minimize(event=None):
    global statemin
    statemin = not statemin
    window.overrideredirect(statemin)


window.bind('<F1>',CloseProgram)
window.bind('<F2>',Minimize)
show_frame()
window.mainloop()
