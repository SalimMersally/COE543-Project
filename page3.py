import json

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

from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets3")

TEDdict = {}
ES = {}


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def previousPage():
    window.destroy()
    import page2


# get distance method
def getTED():

    locA = ""
    locB = ""
    global TEDdict

    with open("locA.txt", "r") as myfile:
        locA = myfile.read()
    with open("locB.txt", "r") as myfile:
        locB = myfile.read()

    entry_3.delete(0, "end")
    entry_8.delete(0, "end")

    xmlFile1 = locA
    xmlFile2 = locB

    treeA = ET.parse(xmlFile1)  # xml to tree
    rootA = treeA.getroot()
    treeB = ET.parse(xmlFile2)  # xml to tree
    rootB = treeB.getroot()

    costDict = {}
    string = ""

    with open("InputCosts.txt", "r") as file:
        string = file.read()
    costDict = json.loads(string)

    for key in costDict:
        costDict[key] = int(costDict[key])

    if Combo.get() == "Only Tags":
        NJ1 = NJ_Tag(rootA, rootB, "A", "B", TEDdict, costDict)
        entry_3.insert(0, "Distance between A and B: " + str(NJ1) + "")
        sim = 1 - NJ1 / (
            nodeCounter_Tag(rootA, costDict["CostDel_Tag"])
            + nodeCounter_Tag(rootB, costDict["CostIns_Tag"])
        )
        sim = round(sim, 3)
        entry_8.insert(0, "Similarity  between A and B: " + str(sim) + "")
    elif Combo.get() == "Tags and Text":
        NJ1 = NJ_TagAndText(rootA, rootB, "A", "B", TEDdict, costDict)
        entry_3.insert(0, "Distance between A and B: " + str(NJ1) + "")
        sim = 1 - NJ1 / (
            nodeCounter_TagAndText(
                rootA, costDict["CostDel_Tag"], costDict["CostDel_Text"]
            )
            + nodeCounter_TagAndText(
                rootB, costDict["CostIns_Tag"], costDict["CostIns_Text"]
            )
        )
        sim = round(sim, 3)
        entry_8.insert(0, "Similarity  between A and B: " + str(sim) + "")
    elif Combo.get() == "Tags, Text, and Elements":
        NJ1 = NJ(rootA, rootB, "A", "B", TEDdict, costDict)
        entry_3.insert(0, "Distance between A and B: " + str(NJ1) + "")
        sim = 1 - NJ1 / (
            nodeCounter(
                rootA,
                costDict["CostDel_Tag"],
                costDict["CostDel_Text"],
                costDict["CostDel_attrib"],
            )
            + nodeCounter(
                rootB,
                costDict["CostIns_Tag"],
                costDict["CostIns_Text"],
                costDict["CostDel_attrib"],
            )
        )
        sim = round(sim, 3)
        entry_8.insert(0, "Similarity  between A and B: " + str(sim) + "")
    pprint(TEDdict["A/B"])


# Edit Script Method
def getES():

    entry_4.delete(0, "end")
    entry_2.delete(1.0, END)
    global ES

    if entry_5.get() != "":
        loc = entry_5.get()
        xmlFile = loc
        tree = ET.parse(xmlFile)
        root = tree.getroot()
        ES = XMLtoES(root)
        entry_2.insert(END, ES)
    else:

        locA = ""
        locB = ""

        with open("locA.txt", "r") as myfile:
            locA = myfile.read()
        with open("locB.txt", "r") as myfile:
            locB = myfile.read()

        with open("InputCosts.txt", "r") as file:
            string = file.read()
        costDict = json.loads(string)

        for key in costDict:
            costDict[key] = int(costDict[key])

        xmlFile1 = locA
        xmlFile2 = locB

        # dict = {}
        treeA = ET.parse(xmlFile1)  # xml to tree
        rootA = treeA.getroot()
        treeB = ET.parse(xmlFile2)  # xml to tree
        rootB = treeB.getroot()

        if Combo.get() == "Only Tags":
            ES = getTreeEditScript_Tag(TEDdict, rootA, rootB, "A", "B", costDict)
            ES = reverseArray(ES)
            ESRoot = EStoXML(ES)
            ET.ElementTree(ESRoot).write("ES.xml")
            entry_2.insert(END, ES)
            entry_4.insert(0, 'DONE !!! Check the "ES" XML file :)')
        elif Combo.get() == "Tags and Text":
            ES = getTreeEditScript_TagAndText(TEDdict, rootA, rootB, "A", "B", costDict)
            ES = reverseArray(ES)
            ESRoot = EStoXML(ES)
            ET.ElementTree(ESRoot).write("ES.xml")
            entry_2.insert(END, ES)
            entry_4.insert(0, 'DONE !!! Check the "ES" XML file :)')
        elif Combo.get() == "Tags, Text, and Elements":
            ES = getTreeEditScript(TEDdict, rootA, rootB, "A", "B", costDict)
            ES = reverseArray(ES)
            ESRoot = EStoXML(ES)
            ET.ElementTree(ESRoot).write("ES.xml")
            entry_2.insert(END, ES)
            entry_4.insert(0, 'DONE !!! Check the "ES" XML file :)')
    pprint(ES)


def patchA2B():
    locA = ""
    global ES

    with open("locA.txt", "r") as myfile:
        locA = myfile.read()

    entry_6.delete(0, "end")

    xmlFile1 = locA
    treeA = ET.parse(xmlFile1)  # xml to Tree
    rootA = treeA.getroot()
    if Combo.get() == "Only Tags":
        dictChanges = {}
        treePatch_Tag(rootA, ES, dictChanges)
        ET.ElementTree(rootA).write("Apacthed.xml")
        entry_6.insert(0, 'DONE !!! Check the "a" XML file :)')

    elif Combo.get() == "Tags and Text":
        dictChanges = {}
        treePatch_TagAndText(rootA, ES, dictChanges)
        ET.ElementTree(rootA).write("Apacthed.xml")
        entry_6.insert(0, 'DONE !!! Check the "a" XML file :)')

    elif Combo.get() == "Tags, Text, and Elements":
        dictChanges = {}
        treePatch(rootA, ES, dictChanges)
        ET.ElementTree(rootA).write("Apatched.xml")
        entry_6.insert(0, 'DONE !!! Check the "a" XML file :)')


def patchB2A():
    locB = ""
    global ES

    with open("locB.txt", "r") as myfile:
        locB = myfile.read()

    entry_7.delete(0, "end")

    xmlFile1 = locB

    treeB = ET.parse(xmlFile1)  # xml to Tree
    rootB = treeB.getroot()

    ESFlipped = flipES(ES)
    ESRoot = EStoXML(ESFlipped)
    ET.ElementTree(ESRoot).write("ESflipped.xml")

    if Combo.get() == "Only Tags":
        dictChanges = {}
        treePatch_Tag(rootB, ESFlipped, dictChanges)
        ET.ElementTree(rootB).write("Bpacthed.xml")
        entry_7.insert(0, 'DONE !!! Check the "b" XML file :)')

    elif Combo.get() == "Tags and Text":
        dictChanges = {}
        treePatch_TagAndText(rootB, ESFlipped, dictChanges)
        ET.ElementTree(rootB).write("Bpacthed.xml")
        entry_7.insert(0, 'DONE !!! Check the "b" XML file :)')

    elif Combo.get() == "Tags, Text, and Elements":
        dictChanges = {}
        treePatch(rootB, ESFlipped, dictChanges)
        ET.ElementTree(rootB).write("Bpacthed.xml")
        entry_7.insert(0, 'DONE !!! Check the "b" XML file :)')


def uploadES():
    entry_5.delete(0, "end")
    file = askopenfilename(filetypes=[("XML files", "*.xml"), ("All files", "*")])
    entry_5.insert(0, file)


window = Tk()

window.geometry("763x528")
window.configure(bg="#FFFFFF")
window.title("Similarity Machine")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=528,
    width=763,
    bd=0,
    highlightthickness=0,
    relief="ridge",
)

canvas.place(x=0, y=0)
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(381.0, 264.0, image=image_image_1)

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(130.0, 62.0, image=image_image_2)

canvas.create_rectangle(116.0, 145.0, 639.0, 208.0, fill="#B4D9FA", outline="")


vlist = ["Only Tags", "Tags and Text", "Tags, Text, and Elements"]

Combo = ttk.Combobox(window, values=vlist, state="readonly")
Combo.set("Pick an Option")
Combo.place(x=515.0, y=154.0, width=99.0, height=18.0)
Combo.config(font="Aerial 7", justify="center")


canvas.create_rectangle(116.0, 245.0, 639.0, 356.0, fill="#A8B6FF", outline="")


entry_2 = scrolledtext.ScrolledText(window, width=266, height=302, font=("Arial", 8))

entry_2.place(x=355.0, y=259.0, width=266.0, height=85.0)

entry_2.config(background="#dbe1e4", foreground="black", font="Arial 8 ", wrap="word")

canvas.create_rectangle(116.0, 392.0, 639.0, 469.0, fill="#869AFF", outline="")

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=patchB2A,
    relief="flat",
)
button_1.place(x=124.3125, y=434.0, width=106.875, height=23.0)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=getES,
    relief="flat",
)
button_2.place(x=128.0, y=252.0, width=106.875, height=23.0)

button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=uploadES,
    relief="flat",
)
button_3.place(x=130.0, y=300.0, width=103.0, height=23.0)

button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=getTED,
    relief="flat",
)
button_4.place(x=127.875, y=154.0, width=106.875, height=23.0)

button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=patchA2B,
    relief="flat",
)
button_5.place(x=124.3125, y=408.0, width=106.875, height=23.0)

canvas.create_rectangle(120.0, 133.0, 648.0, 143.0, fill="#174AFF", outline="")

canvas.create_rectangle(515.0, 115.0, 648.0, 138.0, fill="#174AFF", outline="")

canvas.create_rectangle(118.0, 380.0, 647.0, 390.0, fill="#0C2DA0", outline="")

canvas.create_rectangle(392.0, 364.0, 647.0, 385.0, fill="#0C2DA0", outline="")

canvas.create_rectangle(118.0, 233.0, 647.0, 243.0, fill="#133FDB", outline="")

canvas.create_rectangle(452.0, 217.0, 647.0, 238.0, fill="#133FDB", outline="")

canvas.create_text(
    529.0,
    119.0,
    anchor="nw",
    text="TED & Similarity",
    fill="#FFFFFF",
    font=("Arial BoldMT", 12 * -1),
)

canvas.create_text(
    565.0,
    221.0,
    anchor="nw",
    text="Edit Script",
    fill="#FFFFFF",
    font=("Arial BoldMT", 12 * -1),
)

canvas.create_text(
    576.0,
    369.0,
    anchor="nw",
    text="Patching",
    fill="#FFFFFF",
    font=("Arial BoldMT", 12 * -1),
)

entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(338.5, 164.0, image=entry_image_3)
entry_3 = Entry(bd=0, bg="#FFF9F9", highlightthickness=0)
entry_3.place(x=250.0, y=154.0, width=177.0, height=18.0)
entry_3.config(font="Arial 8")

entry_image_4 = PhotoImage(file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(238.0, 287.0, image=entry_image_4)
entry_4 = Entry(bd=0, bg="#FFF9F9", highlightthickness=0)
entry_4.place(x=137.0, y=277.0, width=202.0, height=18.0)
entry_4.config(font="Arial 8")


entry_image_5 = PhotoImage(file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(238.0, 336.0, image=entry_image_5)
entry_5 = Entry(bd=0, bg="#FFF9F9", highlightthickness=0)
entry_5.place(x=137.0, y=326.0, width=202.0, height=18.0)
entry_5.config(font="Arial 8")

entry_image_6 = PhotoImage(file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(351.0, 418.0, image=entry_image_6)
entry_6 = Entry(bd=0, bg="#FFF9F9", highlightthickness=0)
entry_6.place(x=250.0, y=408.0, width=202.0, height=18.0)
entry_6.config(font="Arial 8")

entry_image_7 = PhotoImage(file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(351.0, 445.0, image=entry_image_7)
entry_7 = Entry(bd=0, bg="#FFF9F9", highlightthickness=0)
entry_7.place(x=250.0, y=435.0, width=202.0, height=18.0)
entry_7.config(font="Arial 8")


entry_image_8 = PhotoImage(file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(338.5, 188.0, image=entry_image_8)
entry_8 = Entry(bd=0, bg="#FFFFFF", highlightthickness=0)
entry_8.place(x=250.0, y=179.0, width=177.0, height=16.0)
entry_8.config(font="Arial 8")

window.resizable(False, False)
window.mainloop()
