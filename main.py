from src.costCalc import *
from src.treeEditDistance import *
from src.treePatch import *
from src.editScript import *
from src.dictEditDistance import *
from pprint import pprint
import xml.etree.ElementTree as ET

xmlFile1 = "C:/Users/ahmad/OneDrive/Desktop/IDPA Project/COE543-Project/sample/everything/Sample3/SampleDoc1.xml"
xmlFile2 = "C:/Users/ahmad/OneDrive/Desktop/IDPA Project/COE543-Project/sample/everything/Sample3/SampleDoc2.xml"
# xmlFile1 = "sample/everything/small/sampleA.xml"
# xmlFile2 = "sample/everything/small/sampleB.xml"
# xmlFile1 = "sample/tagAndText/Huge/employee1.xml"
# xmlFile2 = "sample/tagAndText/Huge/employee2.xml"

treeA = ET.parse(xmlFile1)  # xml to tree
rootA = treeA.getroot()
treeB = ET.parse(xmlFile2)  # xml to tree
rootB = treeB.getroot()

# Test only tags


# dict = {}
# NJ1 = NJ_Tag(rootA, rootB, "A", "B", dict)
# pprint(dict)
# print(NJ1)
# ES = getTreeEditScript_Tag(dict, rootA, rootB, "A", "B")
# print(reverseArray(ES))
# dictChanges = {}
# treePatch_Tag(rootA, rootB, reverseArray(ES), dictChanges)
# ET.ElementTree(rootA).write("a.xml")
# dict = {}
# NJ2 = NJ_Tag(rootA, rootB, "A", "B", dict)
# print(NJ2)

# # test tags and text

# dict = {}
# NJ1 = NJ_TagAndText(rootA, rootB, "A", "B", dict)
# # pprint(dict)
# print(NJ1)
# ES = getTreeEditScript_TagAndText(dict, rootA, rootB, "A", "B")
# pprint(reverseArray(ES))
# dictChanges = {}
# treePatch_TagAndText(rootA, rootB, reverseArray(ES), dictChanges)
# ET.ElementTree(rootA).write("a.xml")
# dict = {}
# NJ2 = NJ_TagAndText(rootA, rootB, "A", "B", dict)
# print(NJ2)

# test all

dict = {}
NJ1 = NJ(rootA, rootB, "A", "B", dict)
#pprint(dict)
#print(NJ1)

ES = getTreeEditScript(dict, rootA, rootB, "A", "B")
ES = reverseArray(ES)
ESRoot = EStoXML(ES)
ET.ElementTree(ESRoot).write("ES.xml")

ESRoot = ET.parse("ES.xml").getroot()
ES1 = XMLtoES(ESRoot)
pprint(ES1)

dictChanges = {}
treePatch(rootA, rootB, ES1, dictChanges)
ET.ElementTree(rootA).write("a.xml")

dict = {}
NJ2 = NJ_TagAndText(rootA, rootB, "A", "B", dict)
print(NJ2)

# print(len(ES), len(ES1))
# for i in range(0, len(ES)):
#     print(ES[i], ES1[i])
#     if ES[i] != ES1[i]:
#         print("break")
#         break
