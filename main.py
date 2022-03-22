from src.function.costCalc import *
from src.function.treeEditDistance import *
from src.function.treePatch import *
from src.function.editScript import *
from src.function.dictEditDistance import *
from pprint import pprint
import xml.etree.ElementTree as ET

xmlFile1 = "sample/everything/Sample1/SampleDoc1.xml"
xmlFile2 = "sample/everything/Sample1/SampleDoc2.xml"
# xmlFile1 = "sample/onlyTag/small/sampleB.xml"
# xmlFile2 = "sample/onlyTag/small/sampleE.xml"
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
# ES = reverseArray(ES)
# pprint(ES)

# ESRoot = EStoXML(ES)
# ET.ElementTree(ESRoot).write("ES.xml")

# ESRoot = ET.parse("ES.xml").getroot()
# ES1 = XMLtoES(ESRoot)
# pprint(ES1)

# dictChanges = {}
# treePatch_Tag(rootA, ES1, dictChanges)
# ET.ElementTree(rootA).write("a.xml")
# dict = {}
# NJ2 = NJ_Tag(rootA, rootB, "A", "B", dict)
# print(NJ2)

# # test tags and text

dict = {}
NJ1 = NJ_TagAndText(rootA, rootB, "A", "B", dict)
# pprint(dict)
print(NJ1)

ES = getTreeEditScript_TagAndText(dict, rootA, rootB, "A", "B")
ES = reverseArray(ES)
# pprint(ES)

ESRoot = EStoXML(ES)
ET.ElementTree(ESRoot).write("ES.xml")

ESRoot = ET.parse("ES.xml").getroot()
ES1 = XMLtoES(ESRoot)
# pprint(ES1)

dictChanges = {}
treePatch_TagAndText(rootA, ES1, dictChanges)
ET.ElementTree(rootA).write("a.xml")
dict = {}
NJ2 = NJ_TagAndText(rootA, rootB, "A", "B", dict)
print(NJ2)

# test all

# dict = {}
# NJ1 = NJ(rootA, rootB, "A", "B", dict)
# pprint(dict)
# print(NJ1)

# ES = getTreeEditScript(dict, rootA, rootB, "A", "B")
# ES = reverseArray(ES)
# pprint(ES)
# ESRoot = EStoXML(ES)
# ET.ElementTree(ESRoot).write("ES.xml")

# ESRoot = ET.parse("ES.xml").getroot()
# ES1 = XMLtoES(ESRoot)
# pprint(ES1)

# dictChanges = {}
# treePatch(rootA, ES1, dictChanges)
# ET.ElementTree(rootA).write("a.xml")

# dict = {}
# NJ2 = NJ_TagAndText(rootA, rootB, "A", "B", dict)
# print(NJ2)
