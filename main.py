from logging import root
from tkinter import *
from helper.costCalc import *
from helper.N_J import *
from helper.treePatch import *
from helper.editScript import *
import numpy as np
from pprint import pprint

dict1 = {
    "AB": [[0, 4, 5], [1, 4, 4], [2, 3, 4]],
    "A-0B-0": [[1, 2], [2, 3], [3, 4]],
    "A-0-0B-0-0": [[1, 2, 3]],
    "A-0-1B-0-0": [[1, 2, 3]],
    "A-0B-1": [[0, 1, 2], [1, 0, 1], [2, 1, 0]],
    "A-0-0B-1-0": [[0]],
    "A-0-0B-1-1": [[1]],
    "A-0-1B-1-0": [[1]],
    "A-0-1B-1-1": [[0]],
    "A-1B-0": [[1, 2]],
    "A-1B-1": [[1, 2, 3]],
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

# ES = getEditScript(dict1, rootA, rootB, "A", "B")
# print(np.flip(ES))

dict = {}
print(NJ(rootA, rootB, "A", "B", dict))
pprint(dict)

ES = getEditScript(dict, rootA, rootB, "A", "B")
print(reverseArray(ES))

treePatch(rootA, rootB, reverseArray(ES))
ET.ElementTree(rootA).write("a.xml")

# root = Tk()
# while True:
#     root.mainloop()
