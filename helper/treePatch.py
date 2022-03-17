import xml.etree.ElementTree as ET
from copy import deepcopy


def findSubTree(root, subTreeName):
    subTreeRoot = root

    if len(subTreeName) > 1:
        indices = subTreeName[2 : len(subTreeName)].split("-")
        for index in indices:
            subTreeRoot = subTreeRoot[int(index)]

    return subTreeRoot


def findSubTreeParent(root, subTreeName):
    subTreeRoot = root

    if len(subTreeName) > 1:
        indices = subTreeName[2 : len(subTreeName)].split("-")
        for index in indices[0 : len(indices) - 1]:
            subTreeRoot = subTreeRoot[int(index)]

    return subTreeRoot


def insertSubTree(A, B, rootAName, subTreeBName, position):
    root = findSubTree(A, rootAName)
    subTree = findSubTree(B, subTreeBName)
    copySubTree = deepcopy(subTree)

    root.insert(position, copySubTree)


def deleteSubTree(A, subTreeAName):
    subTreeA = findSubTree(A, subTreeAName)
    parent = findSubTreeParent(A, subTreeAName)

    parent.remove(subTreeA)


def updateTag(A, B, subTreeAName, subTreeBName):
    subTreeA = findSubTree(A, subTreeAName)
    subTreeB = findSubTree(B, subTreeBName)
    subTreeA.tag = subTreeB.tag


def treePatch(A, B, editScript):
    for op in editScript:
        if op[0] == "Del":
            deleteSubTree(A, op[1])
        if op[0] == "Upd":
            updateTag(A, B, op[1], op[2])
        if op[0] == "Ins":
            insertSubTree(A, B, op[1], op[2], op[3])
