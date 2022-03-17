from logging import root
from tkinter import *
from helper.costCalc import *
from helper.N_J import *
from helper.treePatch import *
from helper.editScript import *
dict1 = {
    "AB" : [[0,4,5],[1,4,4],[2,3,4]],
    "A-1B-1" : [[1,2],[2,3],[3,4]],
    "A-1-1B-1-1" : [[1,2,3]],
    "A-1-2B-1-1" : [[1,2,3]],
    "A-1B-2" : [[0,1,2],[1,0,1],[2,1,0]],
    "A-1-1B-2-1" : [[0]],
    "A-1-1B-2-2" : [[1]],
    "A-1-2B-2-1" : [[1]],
    "A-1-2B-2-2" : [[0]],
    "A-2B-1-1" : [[1,2]],
    "A-2B-2" : [[1,2,3]]
}

xmlFile = "sample/onlyTag/sampleA.xml"
xmlFile2 = "sample/onlyTag/sampleB.xml"
xmlFile3 = "sample/onlyTag/sampleC.xml"


treeA = ET.parse(xmlFile)  # xml to tree
rootA = treeA.getroot()
treeB = ET.parse(xmlFile2)  # xml to tree
rootB = treeB.getroot()
treeC = ET.parse(xmlFile3)  # xml to tree
rootC = treeC.getroot()

print(getEditScript(dict1,rootA,rootB,"A","B"))

# len(rootA)
# print(NJ(rootA, rootB))

test = [
    ("Del", "A-0"),
    ("Upd", "A-0", "B-0"),
    ("Ins", "A-0", "B-0-0", 0),
    ("Ins", "A", "B-1", 1),
]
treePatch(rootA, rootB, test)
ET.ElementTree(rootA).write("a.xml")

# root = Tk()
# while True:
#     root.mainloop()
