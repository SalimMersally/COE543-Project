from fileinput import filename
from traceback import format_tb
from function.costCalc import *
from function.treeEditDistance import *
from function.treePatch import *
from function.editScript import *
from pprint import pprint
import xml.etree.ElementTree as ET

from ctypes.wintypes import SIZE
import tkinter
from tkinter.filedialog import *
from tkinter import *

from turtle import color 
from tkinter import filedialog
from tkinter import ttk
from tkinter import scrolledtext

# Define window
root = tkinter.Tk()
root.title("Similarity Machine")

#icon of the app
root.iconbitmap('tree.ico')
#width and height
root.geometry("1000x500+300+150")
# resize (in x and y direction)
root.resizable(1,1)
root.config(bg = "grey")
#Frame
frame = Frame(width=700, height=50, bg="brown", colormap="new")
frame.pack(fill =BOTH,expand=True)
but_frame = Frame(width=700, height=100, bg="white", colormap="new")
but_frame.pack(fill =BOTH,expand=True)
ted_frame = Frame(width=700, height=100, bg="white", colormap="new")
ted_frame.pack(fill =BOTH,expand=True)
es_frame = Frame(width=700, height=100, bg="brown", colormap="new")
es_frame.pack(fill =BOTH,expand=True)
patch_frame = Frame(width=700, height=100, bg="white", colormap="new")
patch_frame.pack(fill =BOTH,expand=True)
# COSTS 
costDict = {
    "CostIns_Tag": 1,
    "CostDel_Tag": 1,
    "CostUpd_Tag": 1,
    "CostIns_attrib": 1,
    "CostDel_attrib": 1,
    "CostUpd_attrib": 1,
    "CostIns_Text": 1,
    "CostDel_Text": 1,
    "CostUpd_Text": 1,
}

#method choosing file
fileA = ""
fileB = ""
def choose_file(arg) :
    
    if arg == 1 :
        locA.delete(0, "end")
        fileA = askopenfilename(filetypes = [('XML files', '*.xml'),('All files','*')])
        locA.insert(0,fileA)
        #print("You have selected : %s" % fileA)
        #filepathA = filedialog.asksaveasfilename()
    if arg == 2 :
        locB.delete(0, "end")
        fileB = askopenfilename(filetypes = [('XML files', '*.xml'),('All files','*')])
        locB.insert(0,fileB)
        #print("You have selected : %s" % fileB)
        #filepathB = filedialog.asksaveasfilename()
#get distance method
def getTED() :
    
    dis_text.delete(0, "end")
    sim_text.delete(0, "end")
    xmlFile1 = locA.get()
    xmlFile2 = locB.get()
    
    dict = {}
    treeA = ET.parse(xmlFile1)  # xml to tree
    rootA = treeA.getroot()
    treeB = ET.parse(xmlFile2)  # xml to tree
    rootB = treeB.getroot()
    if Combo.get() == "Only Tags" :
        NJ1 = NJ_Tag(rootA, rootB, "A", "B", dict, costDict)
        dis_text.insert(0,'Distance between A and B: ' +str(NJ1) + ''  )
        sim = 1 - NJ1/(nodeCounter_Tag(rootA,costDict["CostDel_Tag"])+ nodeCounter_Tag(rootB,costDict["CostIns_Tag"]))
        sim = round(sim,3)
        sim_text.insert(0,'Similarity  between A and B: ' + str(sim) + ''  )
    elif Combo.get() == "Tags and Text" :
        NJ1 = NJ_TagAndText(rootA, rootB, "A", "B", dict, costDict)
        dis_text.insert(0,'Distance between A and B: ' +str(NJ1) + ''  )
        sim = 1 - NJ1/(nodeCounter_TagAndText(rootA,costDict["CostDel_Tag"],costDict["CostDel_Text"])+ nodeCounter_TagAndText(rootB,costDict["CostIns_Tag"],costDict["CostIns_Text"]))
        sim = round(sim,3)
        sim_text.insert(0,'Similarity  between A and B: ' + str(sim) + ''  )
    elif Combo.get() == "Tags, Text, and Elements": 
        NJ1 = NJ(rootA, rootB, "A", "B", dict, costDict)
        dis_text.insert(0,'Distance between A and B: ' +str(NJ1) + ''  )
        sim = 1 - NJ1/(nodeCounter(rootA,costDict["CostDel_Tag"],costDict["CostDel_Text"],costDict["CostDel_attrib"])+ nodeCounter(rootB,costDict["CostIns_Tag"],costDict["CostIns_Text"],costDict["CostDel_attrib"]))
        sim = round(sim,3)
        sim_text.insert(0,'Similarity  between A and B: ' + str(sim) + ''  )
# Edit Script Method 
def getES():
    es_entry.delete(0, "end")
    scroll.delete(1.0,END)
    xmlFile1 = locA.get()
    xmlFile2 = locB.get()

    
    dict = {}
    treeA = ET.parse(xmlFile1)  # xml to tree
    rootA = treeA.getroot()
    treeB = ET.parse(xmlFile2)  # xml to tree
    rootB = treeB.getroot()
    
    if Combo.get() == "Only Tags" :
        NJ1 = NJ_Tag(rootA, rootB, "A", "B", dict, costDict)
        ES = getTreeEditScript_Tag(dict, rootA, rootB, "A", "B", costDict)
        ES = reverseArray(ES)
        ESRoot = EStoXML(ES)
        ET.ElementTree(ESRoot).write("ES.xml")
        scroll.insert(END,ES) 
        es_entry.insert(0,"DONE !!! Check the \"ES\" XML file :)")
    elif Combo.get() == "Tags and Text" :
        NJ1 = NJ_TagAndText(rootA, rootB, "A", "B", dict, costDict)
        ES = getTreeEditScript_TagAndText(dict, rootA, rootB, "A", "B", costDict)
        ES = reverseArray(ES)
        ESRoot = EStoXML(ES)
        ET.ElementTree(ESRoot).write("ES.xml")
        scroll.insert(END,ES)
        es_entry.insert(0,"DONE !!! Check the \"ES\" XML file :)")
    elif Combo.get() == "Tags, Text, and Elements": 
        NJ1 = NJ(rootA, rootB, "A", "B", dict, costDict)
        ES = getTreeEditScript(dict, rootA, rootB, "A", "B", costDict)
        ES = reverseArray(ES)
        ESRoot = EStoXML(ES)
        ET.ElementTree(ESRoot).write("ES.xml")
        scroll.insert(END,ES)
        es_entry.insert(0,"DONE !!! Check the \"ES\" XML file :)")

# Patch A
def patchA():
    p_entry.delete(0, "end")
    xmlFile1 = locA.get()
    xmlFile2 = locB.get()

    
    dict = {}
    treeA = ET.parse(xmlFile1)  # xml to Tree
    rootA = treeA.getroot()
    treeB = ET.parse(xmlFile2)  # xml to Tree
    rootB = treeB.getroot() 
    
    if Combo.get() == "Only Tags" :
        
        NJ1 = NJ_Tag(rootA, rootB, "A", "B", dict, costDict)
        ES = getTreeEditScript_Tag(dict, rootA, rootB, "A", "B", costDict)
        # ES = reverseArray(ES)
        # ESRoot = EStoXML(ES)
        # ET.ElementTree(ESRoot).write("ES.xml")

        ESRoot = ET.parse("ES.xml").getroot()
        ES1 = XMLtoES(ESRoot)
        dictChanges = {}
        treePatch_Tag(rootA, ES1, dictChanges)
        ET.ElementTree(rootA).write("a.xml")
        p_entry.insert(0,"DONE !!! Check the \"a\" XML file :)")
    elif Combo.get() == "Tags and Text" :
        
        NJ1 = NJ_TagAndText(rootA, rootB, "A", "B", dict, costDict)
        ES = getTreeEditScript_TagAndText(dict, rootA, rootB, "A", "B", costDict)
        # ES = reverseArray(ES)
        # ESRoot = EStoXML(ES)
        # ET.ElementTree(ESRoot).write("ES.xml")
        ESRoot = ET.parse("ES.xml").getroot()
        ES1 = XMLtoES(ESRoot)
        dictChanges = {}
        treePatch_TagAndText(rootA, ES1, dictChanges)
        ET.ElementTree(rootA).write("a.xml")
        
        p_entry.insert(0,"DONE !!! Check the \"a\" XML file :)")
    
    elif Combo.get() == "Tags, Text, and Elements": 
        
        NJ1 = NJ(rootA, rootB, "A", "B", dict, costDict)
        ES = getTreeEditScript(dict, rootA, rootB, "A", "B", costDict)
        # ES = reverseArray(ES)
        # ESRoot = EStoXML(ES)
        # ET.ElementTree(ESRoot).write("ES.xml")
        ESRoot = ET.parse("ES.xml").getroot()
        ES1 = XMLtoES(ESRoot)
        dictChanges = {}
        treePatch(rootA, ES1, dictChanges)
        ET.ElementTree(rootA).write("a.xml")
        p_entry.insert(0,"DONE !!! Check the \"a\" XML file :)")

# Patch B
def patchB():
    p_entry.delete(0, "end")
    xmlFile1 = locA.get()
    xmlFile2 = locB.get()

    
    dict = {}
    treeA = ET.parse(xmlFile1)  # xml to Tree
    rootA = treeA.getroot()
    treeB = ET.parse(xmlFile2)  # xml to Tree
    rootB = treeB.getroot() 
    
    if Combo.get() == "Only Tags" :
        
        NJ1 = NJ_Tag(rootA, rootB, "A", "B", dict, costDict)
        ES = getTreeEditScript_Tag(dict, rootA, rootB, "A", "B", costDict)
        ESRoot = ET.parse("ES.xml").getroot()
        ES1 = XMLtoES(ESRoot)
        ESflip = flipES(ES1)
        ESRoot = EStoXML(ESflip)
        ET.ElementTree(ESRoot).write("ESfliped.xml")
        ESRoot = ET.parse("ESfliped.xml").getroot()
        ES1 = XMLtoES(ESRoot)
        treePatch_Tag(rootB, ES1, dictChanges={})
        ET.ElementTree(rootB).write("b.xml")
        p_entryB.insert(0,"DONE !!! Check the \"b\" XML file :)")
    elif Combo.get() == "Tags and Text" :
        
        NJ1 = NJ_TagAndText(rootA, rootB, "A", "B", dict, costDict)
        ES = getTreeEditScript_TagAndText(dict, rootA, rootB, "A", "B", costDict)
        ESRoot = ET.parse("ES.xml").getroot()
        ES1 = XMLtoES(ESRoot)
        ESflip = flipES(ES1)
        ESRoot = EStoXML(ESflip)
        ET.ElementTree(ESRoot).write("ESfliped.xml")
        ESRoot = ET.parse("ESfliped.xml").getroot()
        ES1 = XMLtoES(ESRoot)
        treePatch_TagAndText(rootB, ES1, dictChanges={})
        ET.ElementTree(rootB).write("b.xml")
        p_entryB.insert(0,"DONE !!! Check the \"b\" XML file :)")
    
    elif Combo.get() == "Tags, Text, and Elements": 
        
        NJ1 = NJ(rootA, rootB, "A", "B", dict, costDict)
        ES = getTreeEditScript(dict, rootA, rootB, "A", "B", costDict)
        ESRoot = ET.parse("ES.xml").getroot()
        ES1 = XMLtoES(ESRoot)
        ESflip = flipES(ES1)
        ESRoot = EStoXML(ESflip)
        ET.ElementTree(ESRoot).write("ESfliped.xml")
        ESRoot = ET.parse("ESfliped.xml").getroot()
        ES1 = XMLtoES(ESRoot)
        treePatch(rootB, ES1, dictChanges={})
        ET.ElementTree(rootB).write("b.xml")
        p_entryB.insert(0,"DONE !!! Check the \"b\" XML file :)")

#define label
label = tkinter.Label(frame, text="Choose your XML files", font=("Arial",18), bg="brown", fg="white" )
label.grid(row=0, column=1, padx=365, pady=15)
# button frame 
#define layout
chooseA_bt = tkinter.Button(but_frame, text="Choose File A", bg="grey", activebackground="#00ffff", borderwidth=5, command= lambda: choose_file(1))
chooseA_bt.grid(row=0,column=0, pady=10)
locA = Entry(but_frame, width=40, borderwidth=5)
locA.grid(row=1, column=0, padx=50)

chooseB_bt = tkinter.Button(but_frame, text="Choose File B", bg="grey", activebackground="#00ffff", borderwidth=5, command= lambda: choose_file(2))
chooseB_bt.grid(row=0,column=1)
locB = Entry(but_frame, width=40, borderwidth=5)
locB.grid(row=1, column=1, padx=20)
# Combo box
vlist = ["Only Tags", "Tags and Text", "Tags, Text, and Elements"]
 
Combo = ttk.Combobox(but_frame, values = vlist, state="readonly")
Combo.set("Pick an Option")
Combo.grid(row=0,column=2, padx=170)

# TED Frame             \\ ted_frame
ted_bt = tkinter.Button(ted_frame, text="Get TED", bg="grey", activebackground="#00ffff", borderwidth=5, command= getTED)
ted_bt.grid(row=0,column=0, pady=10, padx=30)
dis_text = Entry(ted_frame, width=50, borderwidth=5)
dis_text.grid(row=0, column=1, padx=20)
sim_text = Entry(ted_frame, width=50, borderwidth=5)
sim_text.grid(row=0, column=2, padx=20)

# ES Frame 
es_bt = tkinter.Button(es_frame, text="Get ES", bg="grey", activebackground="#00ffff", borderwidth=5, command=getES)
es_bt.grid(row=0,column=0, pady=10, padx=30)
scroll = scrolledtext.ScrolledText(es_frame,width=100,height=2 , font= ("Arial",8))
scroll.grid(column=1, row=0, padx=20)
scroll.config(background="light grey", foreground="black",
                 font='times 12 bold', wrap='word')
es_entry = Entry(es_frame, width=50, borderwidth=4)
es_entry.grid(row=1, column=1, padx=20)

# Patching Frame 
patch_bt = tkinter.Button(patch_frame,text="Patching A to B", bg="grey", activebackground="#00ffff", borderwidth=5, command=patchA)
patch_bt.grid(row=0,column=0, pady=10, padx=30)
p_entry = Entry(patch_frame, width=50, borderwidth=4)
p_entry.grid(row=0, column=1, padx=20)
patchB_bt = tkinter.Button(patch_frame,text="Patching B to A", bg="grey", activebackground="#00ffff", borderwidth=5,command=patchB)
patchB_bt.grid(row=1,column=0, pady=10, padx=30)
p_entryB = Entry(patch_frame, width=50, borderwidth=4)
p_entryB.grid(row=1, column=1, padx=20)
# last line of my code
root.mainloop()
