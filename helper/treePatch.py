from textwrap import indent
import xml.etree.ElementTree as ET
from copy import deepcopy


def findSubTree(root, subTreeName):
    subTreeRoot = root

    if len(subTreeName) > 1:
        indices = subTreeName[2 : len(subTreeName)].split("-")
        for index in indices:
            subTreeRoot = subTreeRoot[int(index)]

    return subTreeRoot


def findSubTreeChange(root, subTreeName, dictChanges):
    subTreeRoot = root
    parentsName = subTreeName[0]

    if len(subTreeName) > 1:
        indices = subTreeName[2 : len(subTreeName)].split("-")
        for i in range(0, len(indices)):
            print(parentsName)
            if i != 0:
                parentsName += "-" + indices[i - 1]
            if not parentsName in dictChanges:
                subTreeRoot = subTreeRoot[int(indices[i])]
            else:
                subTreeRoot = subTreeRoot[int(indices[i]) + dictChanges[parentsName]]

    return subTreeRoot


def insertSubTree(A, B, rootAName, subTreeBName, position, dictChanges):
    root = findSubTreeChange(A, rootAName, dictChanges)
    subTree = findSubTreeChange(B, subTreeBName, dictChanges)
    copySubTree = deepcopy(subTree)

    if not rootAName in dictChanges:
        root.insert(position, copySubTree)
        dictChanges[rootAName] = 1
    else:
        root.insert(position + dictChanges[rootAName] + 1, copySubTree)
        dictChanges[rootAName] += 1


def deleteSubTree(A, subTreeAName, dictChanges):
    array = subTreeAName.split("-")
    parentName = "-".join(array[0 : len(array) - 1])
    parent = findSubTreeChange(A, parentName, dictChanges)

    subTreeA = findSubTreeChange(A, subTreeAName, dictChanges)

    print(parentName)
    parent.remove(subTreeA)

    if not parentName in dictChanges:
        dictChanges[parentName] = -1
    else:
        dictChanges[parentName] -= 1


def updateTag(A, B, subTreeAName, subTreeBName, dictChanges):
    subTreeA = findSubTreeChange(A, subTreeAName, dictChanges)
    subTreeB = findSubTreeChange(B, subTreeBName, dictChanges)
    subTreeA.tag = subTreeB.tag


def patch(A, B, editScript, dictChanges):
    for op in editScript:
        print(dictChanges)
        if op[0] == "Del":
            deleteSubTree(A, op[1], dictChanges)
        if op[0] == "Upd":
            updateTag(A, B, op[1], op[2], dictChanges)
        if op[0] == "Ins":
            insertSubTree(A, B, op[1], op[2], op[3], dictChanges)


def treePatch(A, B, editScript):
    dictChanges = {}
    patch(A, B, editScript, dictChanges)
