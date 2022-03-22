from function.costCalc import *
from function.treeEditDistance import *
from function.treePatch import *
from function.editScript import *
from function.dictEditDistance import *
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

costDict = {
    "CostIns_Tag": 1,
    "CostDel_Tag": 1,
    "CostUpd_Tag": 1,
    "CostIns_attrib": 1,
    "CostDel_attrib": 1,
    "CostUpd_attrib": 1,
    "CostIns_Text": 1,
    "CostDel_Text": 1,
    "CostUpd_Text": 1,
}


# Test only tags

# dict = {}
# NJ1 = NJ_Tag(rootA, rootB, "A", "B", dict, costDict)
# pprint(dict)
# print(NJ1)
# ES = getTreeEditScript_Tag(dict, rootA, rootB, "A", "B", costDict)
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
# NJ2 = NJ_Tag(rootA, rootB, "A", "B", dict, costDict)
# print(NJ2)

# # test tags and text

dict = {}
NJ1 = NJ_TagAndText(rootA, rootB, "A", "B", dict, costDict)
pprint(dict)
print(NJ1)

ES = getTreeEditScript_TagAndText(dict, rootA, rootB, "A", "B", costDict)
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
NJ2 = NJ_TagAndText(rootA, rootB, "A", "B", dict, costDict)
print(NJ2)

# test all

# dict = {}
# NJ1 = NJ(rootA, rootB, "A", "B", dict, costDict)
# pprint(dict)
# print(NJ1)

# ES = getTreeEditScript(dict, rootA, rootB, "A", "B", costDict)
# ES = reverseArray(ES)
# # pprint(ES)
# ESRoot = EStoXML(ES)
# ET.ElementTree(ESRoot).write("ES.xml")

# ESRoot = ET.parse("ES.xml").getroot()
# ES1 = XMLtoES(ESRoot)
# # pprint(ES1)

# ESflip = flipES(ES1)
# ESRoot = EStoXML(ESflip)
# ET.ElementTree(ESRoot).write("ESfliped.xml")

# ESRoot = ET.parse("ESfliped.xml").getroot()
# ES1 = XMLtoES(ESRoot)
# # pprint(ES1)

# treePatch(rootB, ES1, dictChanges={})
# ET.ElementTree(rootB).write("b.xml")

# dict = {}
# NJ2 = NJ(rootA, rootB, "A", "B", dict, costDict)
# print(NJ2)
