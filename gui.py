from ctypes.wintypes import SIZE
import tkinter
from tkinter import *
from turtle import color 

#Define window
root = tkinter.Tk()
root.title("Similarity Machine")
#icon of the app
root.iconbitmap('Pixelkit-Flat-Jewels-Tree.ico')
#width and height
root.geometry("700x500+400+150")
#wno resize (in x and y direction)
root.resizable(1,1)
root.config(bg = "grey")

#define label
label = tkinter.Label(root, text="Choose your XML files", font="Arial" )
label.grid(row=0, column=1, padx=100)

#define layout
chooseA_bt = tkinter.Button(root, text="Choose File A", bg="#00ffff", activebackground="#ff000f", borderwidth=5)
chooseA_bt.grid(row=1,column=0, pady=10)

chooseB_bt = tkinter.Button(root, text="Choose File B", bg="black",fg="white", activebackground="#455005", borderwidth=5)
chooseB_bt.grid(row=1,column=3)

#last line of my code
root.mainloop()