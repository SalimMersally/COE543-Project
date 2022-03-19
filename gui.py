from fileinput import filename
from src.costCalc import *
from src.treeEditDistance import *
from src.treePatch import *
from src.editScript import *
from pprint import pprint
import xml.etree.ElementTree as ET

from ctypes.wintypes import SIZE
import tkinter
from tkinter.filedialog import *
from tkinter import *

from turtle import color 
from tkinter import filedialog
from tkinter import ttk


# Define window
root = tkinter.Tk()
root.title("Similarity Machine")

#icon of the app
root.iconbitmap('tree.ico')
#width and height
root.geometry("1000x500+300+150")
#wno resize (in x and y direction)
root.resizable(1,1)
root.config(bg = "grey")
#Frame
frame = Frame(width=700, height=50, bg="white", colormap="new")
frame.pack(fill =BOTH,expand=True)
but_frame = Frame(width=700, height=100, bg="red", colormap="new")
but_frame.pack(fill =BOTH,expand=True)
ted_frame = Frame(width=700, height=100, bg="blue", colormap="new")
ted_frame.pack(fill =BOTH,expand=True)
es_frame = Frame(width=700, height=100, bg="yellow", colormap="new")
es_frame.pack(fill =BOTH,expand=True)
patch_frame = Frame(width=700, height=100, bg="green", colormap="new")
patch_frame.pack(fill =BOTH,expand=True)


#method choosing file
fileA = ""
fileB = ""
def choose_file(arg) :
    
    if arg == 1 :
        locA.delete(0, "end")
        fileA = askopenfilename(filetypes = [('XML files', '*.xml'),('All files','*')])
        locA.insert(0,fileA)
        print("You have selected : %s" % fileA)
        #filepathA = filedialog.asksaveasfilename()
    if arg == 2 :
        locB.delete(0, "end")
        fileB = askopenfilename(filetypes = [('XML files', '*.xml'),('All files','*')])
        locB.insert(0,fileB)
        print("You have selected : %s" % fileB)
        #filepathB = filedialog.asksaveasfilename()
#get distance method
def getTED() :
    
    dis_text.delete(0, "end")
    sim_text.delete(0, "end")
    xmlFile1 = locA.get()
    xmlFile2 = locB.get()
    xmlFile1 = xmlFile1[60:]
    xmlFile2 = xmlFile2[60:]
    
    dict = {}
    treeA = ET.parse(xmlFile1)  # xml to tree
    rootA = treeA.getroot()
    treeB = ET.parse(xmlFile2)  # xml to tree
    rootB = treeB.getroot()
    if Combo.get() == "Only Tags" :
        NJ1 = NJ_Tag(rootA, rootB, "A", "B", dict)
        dis_text.insert(0,'Distance between A and B: ' +str(NJ1) + ''  )
        sim = 1/(1+NJ1)
        sim_text.insert(0,'Similarity  between A and B: ' + str(sim) + ''  )
    elif Combo.get() == "Tags and Text" :
        NJ1 = NJ_TagAndText(rootA, rootB, "A", "B", dict)
        dis_text.insert(0,'Distance between A and B: ' +str(NJ1) + ''  )
        sim = 1/(1+NJ1)
        sim_text.insert(0,'Similarity  between A and B: ' + str(sim) + ''  )
    elif Combo.get() == "Tags, Text, and Elements": 
        dis_text.insert(0,'Distance between A and B: NOT DONE YET'  )
        sim_text.insert(0,'Similarity  between A and B: NOT DONE YET'  )
#define label
label = tkinter.Label(frame, text="Choose your XML files", font="Arial" )
label.grid(row=0, column=1, padx=100)
# button frame 
#define layout
chooseA_bt = tkinter.Button(but_frame, text="Choose File A", bg="#00ffff", activebackground="#ff000f", borderwidth=5, command= lambda: choose_file(1))
chooseA_bt.grid(row=0,column=0, pady=10)
locA = Entry(but_frame, width=40)
locA.grid(row=1, column=0, padx=50)

chooseB_bt = tkinter.Button(but_frame, text="Choose File B", bg="black",fg="white", activebackground="#455005", borderwidth=5, command= lambda: choose_file(2))
chooseB_bt.grid(row=0,column=1)
locB = Entry(but_frame, width=40)
locB.grid(row=1, column=1, padx=20)
# Combo box
vlist = ["Only Tags", "Tags and Text", "Tags, Text, and Elements"]
 
Combo = ttk.Combobox(but_frame, values = vlist)
Combo.set("Pick an Option")
Combo.grid(row=0,column=2, padx=170)

# TED Frame             \\ ted_frame
ted_bt = tkinter.Button(ted_frame, text="Get TED", bg="#00ffff", activebackground="#ff000f", borderwidth=5, command= getTED)
ted_bt.grid(row=0,column=0, pady=10)
dis_text = Entry(ted_frame, width=50)
dis_text.grid(row=0, column=1, padx=20)
sim_text = Entry(ted_frame, width=50)
sim_text.grid(row=0, column=2, padx=20)
# last line of my code
root.mainloop()
