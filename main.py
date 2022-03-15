from pydoc import Helper
from tkinter import *
from helper.costCalc import *

xmlFile = "sample/onlyTag/sampleA.xml"
xmlFile2 = "sample/onlyTag/sampleB.xml"
xmlFile3 = "sample/onlyTag/sampleC.xml"


treeA = ET.parse(xmlFile)  # xml to tree
rootA = treeA.getroot()
treeB = ET.parse(xmlFile2)  # xml to tree
rootB = treeB.getroot()
treeC = ET.parse(xmlFile3)  # xml to tree
rootC = treeC.getroot()

print(isTreeIdentical(rootA, rootB))
print(isTreeIdentical(rootA[0], rootB[1]))

print(isSubTree(rootA, rootB))
print(isSubTree(rootA[0], rootB))

print(nodeCounter(rootA))
print(nodeCounter(rootB))
print(nodeCounter(rootC))

print(costDelete(rootA, rootB))
print(costDelete(rootA[0], rootB[1]))

print(costInsert(rootA, rootB))
print(costInsert(rootA[0], rootB[1]))

# root = Tk()
# while True:
#     root.mainloop()
