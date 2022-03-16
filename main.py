from tkinter import *
from helper.costCalc import *
from helper.N_J import *
from helper.treePatch import *

xmlFile = "sample/onlyTag/sampleA.xml"
xmlFile2 = "sample/onlyTag/sampleB.xml"
xmlFile3 = "sample/onlyTag/sampleC.xml"


treeA = ET.parse(xmlFile)  # xml to tree
rootA = treeA.getroot()
treeB = ET.parse(xmlFile2)  # xml to tree
rootB = treeB.getroot()
treeC = ET.parse(xmlFile3)  # xml to tree
rootC = treeC.getroot()
# len(rootA)
# print(NJ(rootA, rootB))

# insertSubTree(rootA, rootB, "A-0-1", "B", 0)
# ET.ElementTree(rootA).write("a.xml")

# deleteSubTree(rootA, "A-0-1-0")
# ET.ElementTree(rootA).write("b.xml")

# updateTag(rootA, rootB, "A-0-1", "B-0")
# ET.ElementTree(rootA).write("c.xml")

# root = Tk()
# while True:
#     root.mainloop()
