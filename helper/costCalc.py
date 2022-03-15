from operator import truediv
from tarfile import ENCODING
import xml.etree.ElementTree as ET
from array import *

xmlFile = "sampleA.xml"
xmlFile2 = "sampleB.xml"

treeA = ET.parse(xmlFile) #xml to tree
rootA = treeA.getroot()
treeB = ET.parse(xmlFile2) #xml to tree
rootB = treeB.getroot()

def isTreeIdentical(root1,root2):
    if (root1 == None and root2 == None):
        return True
    if (root1 == None or root2 == None):
        return False
    if (root1.tag != root2.tag):
        return False
    if(len(root1) != len(root2)):
        return False
    for i in range(0, len(root1)):
        if(not isTreeIdentical(root1[i], root2[i])):
            return False
    return True

print(isTreeIdentical(rootA,rootB))
print(isTreeIdentical(rootA[0],rootB[1]))

def isSubTree (root1,root2):
    #print(root1, root2)
    if root1 is None:
        return True
 
    if root2 is None:
        return False
 
    if (isTreeIdentical(root1, root2)):
        return True
    
    for i in range(0, len(root2)):
        if(isSubTree(root1, root2[i])):
            return True
        
    return False
    
print(isSubTree(rootA,rootB))
print(isSubTree(rootA[0],rootB))
