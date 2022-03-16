from pydoc import Helper
from tkinter import *
from helper.costCalc import *
from helper.N_J import *

xmlFile = "sample/onlyTag/sampleA.xml"
xmlFile2 = "sample/onlyTag/sampleB.xml"
xmlFile3 = "sample/onlyTag/sampleC.xml"


treeA = ET.parse(xmlFile)  # xml to tree
rootA = treeA.getroot()
treeB = ET.parse(xmlFile2)  # xml to tree
rootB = treeB.getroot()
treeC = ET.parse(xmlFile3)  # xml to tree
rootC = treeC.getroot()
len(rootA)
print(NJ(rootA,rootB))
# root = Tk()
# while True:
#     root.mainloop()
