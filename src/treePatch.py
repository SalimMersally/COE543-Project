from textwrap import indent
import xml.etree.ElementTree as ET
from copy import deepcopy

# the following methods are used to patch a tree into another one
# using the edit script taking into considartion only tags
# note that a dictionary should be given as argument to the patch funtion so
# values of change are stored in recursive calls


def findSubTreeChange_Tag(root, subTreeName, dictChanges):
    subTreeRoot = root
    parentsName = subTreeName[0]

    if len(subTreeName) > 1:
        indices = subTreeName[2 : len(subTreeName)].split("-")
        for i in range(0, len(indices)):
            if i != 0:
                parentsName += "-" + indices[i - 1]
            if not parentsName in dictChanges:
                subTreeRoot = subTreeRoot[int(indices[i])]
            else:
                subTreeRoot = subTreeRoot[int(indices[i]) + dictChanges[parentsName]]

    return subTreeRoot


def insertSubTree_Tag(A, B, rootAName, subTreeBName, position, dictChanges):
    root = findSubTreeChange_Tag(A, rootAName, dictChanges)
    subTree = findSubTreeChange_Tag(B, subTreeBName, dictChanges)
    copySubTree = deepcopy(subTree)

    if not rootAName in dictChanges:
        root.insert(position, copySubTree)
        dictChanges[rootAName] = 1
    else:
        root.insert(position, copySubTree)
        dictChanges[rootAName] += 1


def deleteSubTree_Tag(A, subTreeAName, dictChanges):
    array = subTreeAName.split("-")
    parentName = "-".join(array[0 : len(array) - 1])
    parent = findSubTreeChange_Tag(A, parentName, dictChanges)
    subTreeA = findSubTreeChange_Tag(A, subTreeAName, dictChanges)

    parent.remove(subTreeA)

    if not parentName in dictChanges:
        dictChanges[parentName] = -1
    else:
        dictChanges[parentName] -= 1


def updateNode_Tag(A, B, subTreeAName, subTreeBName, dictChanges):
    subTreeA = findSubTreeChange_Tag(A, subTreeAName, dictChanges)
    subTreeB = findSubTreeChange_Tag(B, subTreeBName, dictChanges)
    subTreeA.tag = subTreeB.tag


def treePatch_Tag(A, B, editScript, dictChanges):
    for op in editScript:
        if op[0] == "Del":
            deleteSubTree_Tag(A, op[1], dictChanges)
        if op[0] == "UpdTag":
            updateNode_Tag(A, B, op[1], op[2], dictChanges)
        if op[0] == "Ins":
            insertSubTree_Tag(A, B, op[1], op[2], op[3], dictChanges)
