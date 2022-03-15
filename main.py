from pydoc import Helper
from tkinter import *
from helper.costCalc import *

xmlFile = "sample/onlyTag/sampleA.xml"
xmlFile2 = "sample/onlyTag/sampleB.xml"

treeA = ET.parse(xmlFile)  # xml to tree
rootA = treeA.getroot()
treeB = ET.parse(xmlFile2)  # xml to tree
rootB = treeB.getroot()

print(isTreeIdentical(rootA, rootB))
print(isTreeIdentical(rootA[0], rootB[1]))

print(isSubTree(rootA, rootB))
print(isSubTree(rootA[0], rootB))

# root = Tk()
# while True:
#     root.mainloop()
