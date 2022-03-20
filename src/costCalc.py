# import xml.etree.ElementTree as ET
from src.arrayEditDistance import *


def findSubTree(root, subTreeName):
    subTreeRoot = root

    if len(subTreeName) > 1:
        indices = subTreeName[2 : len(subTreeName)].split("-")
        for index in indices:
            subTreeRoot = subTreeRoot[int(index)]

    return subTreeRoot


# The following method are used to calculate the cost of operation on trees
# these method will take into consideration only Tags
# the cost model for it is:
#   - DelTree = 1 if subtree available in B, else sum of nodes
#   - InsTree = 1 if subtree available in A, else sum of nodes
#   - UpdTag = 1 if tags are diffent, 0 if same


def isTreeIdentical_Tag(root1, root2):
    if root1 == None and root2 == None:
        return True
    if root1 == None or root2 == None:
        return False
    if root1.tag != root2.tag:
        return False
    if len(root1) != len(root2):
        return False
    for i in range(0, len(root1)):
        if not isTreeIdentical_Tag(root1[i], root2[i]):
            return False
    return True


def isSubTree_Tag(root1, root2):
    if root1 is None:
        return True

    if root2 is None:
        return False

    if isTreeIdentical_Tag(root1, root2):
        return True

    for i in range(0, len(root2)):
        if isSubTree_Tag(root1, root2[i]):
            return True

    return False


def nodeCounter_Tag(root):
    counter = 0

    if root is None:
        return counter

    counter += 1
    for child in root:
        counter += nodeCounter_Tag(child)

    return counter


def costInsert_Tag(subTreeB, A):
    if isSubTree_Tag(subTreeB, A):
        return 1
    else:
        return nodeCounter_Tag(subTreeB)


def costDelete_Tag(subTreeA, B):
    if isSubTree_Tag(subTreeA, B):
        return 1
    else:
        return nodeCounter_Tag(subTreeA)


def costUpd_Tag(rootA, rootB):
    if rootA.tag == rootB.tag:
        return 0
    else:
        return 1


# The following method are used to calculate the cost of operation on trees
# these method will take into consideration only Tags and text
# the cost model for it is:
#   - DelTree = 1 if subtree available in B, else sum of nodes + words
#   - InsTree = 1 if subtree available in A, else sum of nodes + words
#   - UpdTag = 1 if tags are diffent, 0 if same + cost of upd text


def isTreeIdentical_TagAndText(root1, root2):
    if root1 == None and root2 == None:
        return True
    if root1 == None or root2 == None:
        return False
    if root1.tag != root2.tag:
        return False
    if root1.text != root2.text:
        return False
    if len(root1) != len(root2):
        return False
    for i in range(0, len(root1)):
        if not isTreeIdentical_TagAndText(root1[i], root2[i]):
            return False
    return True


def isSubTree_TagAndText(root1, root2):
    if root1 is None:
        return True

    if root2 is None:
        return False

    if isTreeIdentical_TagAndText(root1, root2):
        return True

    for i in range(0, len(root2)):
        if isSubTree_TagAndText(root1, root2[i]):
            return True

    return False


def nodeCounter_TagAndText(root):
    counter = 0

    if root is None:
        return counter

    if root.text is not None:
        counter += 1 + len(root.text.split())

    for child in root:
        counter += nodeCounter_TagAndText(child)

    return counter


def costInsert_TagAndText(subTreeB, A):
    if isSubTree_TagAndText(subTreeB, A):
        return 1
    else:
        return nodeCounter_TagAndText(subTreeB)


def costDelete_TagAndText(subTreeA, B):
    if isSubTree_TagAndText(subTreeA, B):
        return 1
    else:
        return nodeCounter_TagAndText(subTreeA)


def costUpd_TagAndText(rootA, rootB, nameA, nameB, matricesDic):
    cost = 0

    if rootA.tag != rootB.tag:
        cost += 1

    if (rootA.text is not None) and (rootB.text is not None):
        textA = rootA.text.strip()
        textB = rootB.text.strip()
        distanceOfText = WF(textA, textB)
        matricesDic[nameA + "/" + nameB + "/text"] = distanceOfText
        cost += distanceOfText[len(textA.split())][len(textB.split())]

    return cost


# The following method are used to calculate the cost of operation on trees
# these method will take into consideration all Tags, attributes, and text
# the cost model for it is:
#   - DelTree = 1 if subtree available in B, else sum of nodes + words
#   - InsTree = 1 if subtree available in A, else sum of nodes + words
#   - UpdTag = 1 if tags are diffent, 0 if same + cost of upd text    

def isTreeIdentical(root1, root2):
    if root1 == None and root2 == None:
        return True
    if root1 == None or root2 == None:
        return False
    if root1.tag != root2.tag:
        return False
    if root1.text != root2.text:
        return False
    if root1.attrib != root2.attrib:
        return False
    if len(root1) != len(root2):
        return False
    for i in range(0, len(root1)):
        if not isTreeIdentical(root1[i], root2[i]):
            return False
    return True


def isSubTree(root1, root2):
    if root1 is None:
        return True

    if root2 is None:
        return False

    if isTreeIdentical(root1, root2):
        return True

    for i in range(0, len(root2)):
        if isSubTree(root1, root2[i]):
            return True

    return False

##needs to be changed to account for cost input: an approach can include 
##adding inputs to the functions (cost for root, tag, attribute) --> those can change depending on methods
def nodeCounter(root):
    counter = 0

    if root is None:
        return counter

    if root.text is not None:
        counter += 1 + len(root.text.split())
    if root.attrib is not None:
        counter += 1 + len(root.attrib.keys()) + len(root.attrib.values())
    for child in root:
        counter += nodeCounter(child)

    return counter


def costInsert(subTreeB, A):
    if isSubTree(subTreeB, A):
        return 1
    else:
        return nodeCounter(subTreeB)


def costDelete(subTreeA, B):
    if isSubTree(subTreeA, B):
        return 1
    else:
        return nodeCounter(subTreeA)


def costUpd(rootA, rootB, nameA, nameB, matricesDic):
    cost = 0

    if rootA.tag != rootB.tag:
        cost += 1

    if (rootA.text is not None) and (rootB.text is not None):
        textA = rootA.text.strip()
        textB = rootB.text.strip()
        distanceOfText = WF(textA, textB)
        matricesDic[nameA + "/" + nameB + "/text"] = distanceOfText
        cost += distanceOfText[len(textA.split())][len(textB.split())]
        
    if (rootA.attrib is not None) and (rootB.attrib is not None):
        keysA = " ".join(list(rootA.attrib.keys()))
        keysB = " ".join(list(rootB.attrib.keys()))
        valuesA = " ".join(list(rootA.attrib.values()))
        valuesB = " ".join(list(rootB.attrib.values()))
        
        distKeys = WF(keysA,keysB)
        distValues = WF(valuesA,valuesB)
        distanceOfAttributes = distKeys[len(keysA.split())][len(keysB.split())] + distValues[len(valuesA.split())][len(valuesB.split())]
        matricesDic[nameA + "/" + nameB + "/attribute"] = distanceOfText
        cost+= distanceOfAttributes
        

    return cost
