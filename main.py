from src.costCalc import *
from src.treeEditDistance import *
from src.treePatch import *
from src.editScript import *
from pprint import pprint

# xmlFile1 = "sample/onlyTag/Sample1/SampleDoc1.xml"
# xmlFile2 = "sample/onlyTag/Sample1/SampleDoc2.xml"
xmlFile1 = "sample/onlyTag/Huge/employee1.xml"
xmlFile2 = "sample/onlyTag/Huge/employee2.xml"

treeA = ET.parse(xmlFile1)  # xml to tree
rootA = treeA.getroot()
treeB = ET.parse(xmlFile2)  # xml to tree
rootB = treeB.getroot()

dict = {}
NJ1 = NJ_Tag(rootA, rootB, "A", "B", dict)
# pprint(dict)
print(NJ1)

ES = getTreeEditScript_Tag(dict, rootA, rootB, "A", "B")
print(reverseArray(ES))

dictChanges = {}
treePatch_Tag(rootA, rootB, reverseArray(ES), dictChanges)
ET.ElementTree(rootA).write("a.xml")

dict = {}
NJ2 = NJ_Tag(rootA, rootB, "A", "B", dict)
print(NJ2)
