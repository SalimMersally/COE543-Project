# import xml.etree.ElementTree as ET
from cmath import cos
from function.dictEditDistance import WF_Dict
from function.arrayEditDistance import *


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


def nodeCounter_Tag(root, cost):
    counter = 0

    if root is None:
        return counter

    counter += cost
    for child in root:
        counter += nodeCounter_Tag(child, cost)

    return counter


def costInsert_Tag(subTreeB, A, dictCost):
    if isSubTree_Tag(subTreeB, A):
        return 1
    else:
        return nodeCounter_Tag(subTreeB, dictCost["CostIns_Tag"])


def costDelete_Tag(subTreeA, B, dictCost):
    if isSubTree_Tag(subTreeA, B):
        return 1
    else:
        return nodeCounter_Tag(subTreeA, dictCost["CostDel_Tag"])


def costUpd_Tag(rootA, rootB, dictCost):
    if rootA.tag == rootB.tag:
        return 0
    else:
        return dictCost["CostUpd_Tag"]


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


def nodeCounter_TagAndText(root, costTag, costText):
    counter = 0

    if root is None:
        return counter

    counter += costTag

    if root.text is not None:
        counter += costText * len(root.text.split())

    for child in root:
        counter += nodeCounter_TagAndText(child, costTag, costText)

    return counter


def costInsert_TagAndText(subTreeB, A, costDict):
    if isSubTree_TagAndText(subTreeB, A):
        return 1
    else:
        return nodeCounter_TagAndText(
            subTreeB, costDict["CostIns_Tag"], costDict["CostIns_Text"]
        )


def costDelete_TagAndText(subTreeA, B, costDict):
    if isSubTree_TagAndText(subTreeA, B):
        return 1
    else:
        return nodeCounter_TagAndText(
            subTreeA, costDict["CostDel_Tag"], costDict["CostDel_Text"]
        )


def costUpd_TagAndText(rootA, rootB, nameA, nameB, matricesDic, costDict):
    cost = 0

    if rootA.tag != rootB.tag:
        cost += costDict["CostUpd_Tag"]

    if (rootA.text is not None) or (rootB.text is not None):
        textA = rootA.text
        textB = rootB.text
        if textA is None:
            textA = ""
        if textB is None:
            textB = ""
        distanceOfText = WF(textA, textB, costDict)
        matricesDic[nameA + "/" + nameB + "/text"] = distanceOfText
        cost += distanceOfText[len(textA.split())][len(textB.split())]

    return cost


# The following method are used to calculate the cost of operation on trees
# these method will take into consideration all Tags, attributes, and text
# the cost model for it is:
#   - DelTree = 1 if subtree available in B, else sum of nodes + words + att
#   - InsTree = 1 if subtree available in A, else sum of nodes + words + att
#   - UpdTag = 1 if tags are diffent, 0 if same + cost of upd text + cost of upd att


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


def nodeCounter(root, costTag, costText, costAtt):
    counter = 0

    if root is None:
        return counter

    counter += costTag

    if root.text is not None:
        counter += costText * len(root.text.split())

    if root.attrib != {}:
        counter += costAtt * (len(root.attrib.keys()) + len(root.attrib.values()))

    for child in root:
        counter += nodeCounter(child, costTag, costText, costAtt)

    return counter


def costInsert(subTreeB, A, costDict):
    if isSubTree(subTreeB, A):
        return 1
    else:
        return nodeCounter(
            subTreeB,
            costDict["CostIns_Tag"],
            costDict["CostIns_Text"],
            costDict["CostIns_attrib"],
        )


def costDelete(subTreeA, B, costDict):
    if isSubTree(subTreeA, B):
        return 1
    else:
        return nodeCounter(
            subTreeA,
            costDict["CostDel_Tag"],
            costDict["CostDel_Text"],
            costDict["CostDel_attrib"],
        )


def costUpd(rootA, rootB, nameA, nameB, matricesDic, costDict):
    cost = 0

    if rootA.tag != rootB.tag:
        cost += costDict["CostUpd_Tag"]

    if (rootA.text is not None) or (rootB.text is not None):
        textA = rootA.text
        textB = rootB.text
        if textA is None:
            textA = ""
        if textB is None:
            textB = ""
        distanceOfText = WF(textA, textB, costDict)
        matricesDic[nameA + "/" + nameB + "/text"] = distanceOfText
        cost += distanceOfText[len(textA.split())][len(textB.split())]

    if (rootA.attrib != {}) or (rootB.attrib != {}):
        distanceOfAtt = WF_Dict(rootA.attrib, rootB.attrib, costDict)
        matricesDic[nameA + "/" + nameB + "/attribute"] = distanceOfAtt
        cost += distanceOfAtt[len(distanceOfAtt) - 1][len(distanceOfAtt[0]) - 1]

    return cost
