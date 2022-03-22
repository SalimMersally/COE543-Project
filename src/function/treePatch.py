import xml.etree.ElementTree as ET
from src.function.dictEditDistance import patchDict
from src.function.arrayEditDistance import patchArray
from copy import deepcopy

# the following method are used as helper to all the patch methods


def findSubTreeChange(root, subTreeName, dictChanges):
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


def insertSubTree(A, rootAName, subTreeB, position, dictChanges):
    root = findSubTreeChange(A, rootAName, dictChanges)

    if not rootAName in dictChanges:
        root.insert(position, subTreeB)
        dictChanges[rootAName] = 1
    else:
        root.insert(position, subTreeB)
        dictChanges[rootAName] += 1


def deleteSubTree(A, subTreeAName, dictChanges):
    array = subTreeAName.split("-")
    parentName = "-".join(array[0 : len(array) - 1])
    parent = findSubTreeChange(A, parentName, dictChanges)
    subTreeA = findSubTreeChange(A, subTreeAName, dictChanges)

    parent.remove(subTreeA)

    if not parentName in dictChanges:
        dictChanges[parentName] = -1
    else:
        dictChanges[parentName] -= 1


def updateNode(A, subTreeAName, tagB, dictChanges):
    subTreeA = findSubTreeChange(A, subTreeAName, dictChanges)
    subTreeA.tag = tagB


# the following method is used to patch a tree into another one
# using the edit script taking into considartion only tags
# note that a dictionary should be given as argument to the patch funtion so
# values of change are stored in recursive calls


def treePatch_Tag(A, editScript, dictChanges):
    for op in editScript:
        if op[0] == "UpdTag":
            updateNode(A, op[1], op[4], dictChanges)
        if op[0] == "Del":
            deleteSubTree(A, op[1], dictChanges)
        if op[0] == "Ins":
            insertSubTree(A, op[1], op[3], op[4], dictChanges)


# the following methods are used to patch a tree into another one
# using the edit script taking into considartion only tags and text
# note that a dictionary should be given as argument to the patch funtion so
# values of change are stored in recursive calls


def updateText(A, subTreeAName, textES, dictChanges):
    subTreeA = findSubTreeChange(A, subTreeAName, dictChanges)
    subTreeAText = subTreeA.text
    if subTreeAText is None:
        subTreeAText = ""
    subTreeAUpdatedText = patchArray(subTreeAText, textES)
    subTreeA.text = subTreeAUpdatedText


def treePatch_TagAndText(A, editScript, dictChanges):
    for op in editScript:
        if op[0] == "UpdTag":
            updateNode(A, op[1], op[4], dictChanges)
        if op[0] == "Del":
            deleteSubTree(A, op[1], dictChanges)
        if op[0] == "Ins":
            insertSubTree(A, op[1], op[3], op[4], dictChanges)
        if op[0] == "UpdText":
            updateText(A, op[1], op[3], dictChanges)


# the following methods are used to patch a tree into another one
# using the edit script taking into considartion all tags, att and text
# note that a dictionary should be given as argument to the patch funtion so
# values of change are stored in recursive calls


def updateAttribute(A, subTreeAName, attES, dictChanges):
    subTreeA = findSubTreeChange(A, subTreeAName, dictChanges)
    subTreeAAtt = subTreeA.attrib
    subTreeAUpdatedAtt = patchDict(subTreeAAtt, attES)
    subTreeA.attrib = subTreeAUpdatedAtt


def treePatch(A, editScript, dictChanges):
    for op in editScript:
        if op[0] == "UpdTag":
            updateNode(A, op[1], op[4], dictChanges)
        if op[0] == "Del":
            deleteSubTree(A, op[1], dictChanges)
        if op[0] == "Ins":
            insertSubTree(A, op[1], op[3], op[4], dictChanges)
        if op[0] == "UpdText":
            updateText(A, op[1], op[3], dictChanges)
        if op[0] == "UpdAttribute":
            updateAttribute(A, op[1], op[3], dictChanges)
