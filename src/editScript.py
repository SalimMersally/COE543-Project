from src.costCalc import *
from src.arrayEditDistance import getEditScriptArray
from src.dictEditDistance import getEditScriptDict
import xml.etree.ElementTree as ET


def reverseArray(array):
    result = []
    i = len(array) - 1
    while i >= 0:
        result.append(array[i])
        i -= 1
    return result


# After getting the edit matrices using NJ algorithm, the matrices
# are stored in a dictionary with their name as key
# using them will get the edit script by tranversing them back
# Note that the result should be flipped
# this method take into considaration only tags


def getTreeEditScript_Tag(matricesDic, A, B, nameA, nameB):

    keyDic = nameA + "/" + nameB
    editScript = []
    matrix = matricesDic.get(keyDic)

    row = len(matrix) - 1
    col = len(matrix[0]) - 1

    while row > 0 and col > 0:
        subTreeAName = nameA + "-" + str(row - 1)
        subTreeBName = nameB + "-" + str(col - 1)

        subTreeA = findSubTree(A, subTreeAName)
        subTreeB = findSubTree(B, subTreeBName)

        if matrix[row][col] == (matrix[row - 1][col] + costDelete_Tag(subTreeA, B)):
            editScript.append(("Del", subTreeAName , nameB, row -1))
            row = row - 1
        elif matrix[row][col] == matrix[row][col - 1] + costInsert_Tag(subTreeB, A):
            editScript.append(("Ins", nameA, subTreeBName, col - 1))
            col = col - 1
        else:
            editScript += getTreeEditScript_Tag(
                matricesDic, A, B, subTreeAName, subTreeBName
            )
            row = row - 1
            col = col - 1

    while row > 0:
        subTreeAName = nameA + "-" + str(row - 1)
        editScript.append(("Del", subTreeAName , nameB, row -1))
        row = row - 1

    while col > 0:
        subTreeBName = nameB + "-" + str(col - 1)
        editScript.append(("Ins", nameA, subTreeBName, col - 1))
        col = col - 1

    if matrix[row][col] == 1:
        editScript.append(("UpdTag", nameA, nameB))

    return editScript


# After getting the edit matrices using NJ algorithm, the matrices
# are stored in a dictionary with their name as key
# using them will get the edit script by tranversing them back
# Note that the result should be flipped
# this method take into considaration only tags


def getTreeEditScript_TagAndText(matricesDic, A, B, nameA, nameB):

    keyDic = nameA + "/" + nameB
    editScript = []
    matrix = matricesDic.get(keyDic)

    row = len(matrix) - 1
    col = len(matrix[0]) - 1

    while row > 0 and col > 0:
        subTreeAName = nameA + "-" + str(row - 1)
        subTreeBName = nameB + "-" + str(col - 1)

        subTreeA = findSubTree(A, subTreeAName)
        subTreeB = findSubTree(B, subTreeBName)

        if matrix[row][col] == (
            matrix[row - 1][col] + costDelete_TagAndText(subTreeA, B)
        ):
            editScript.append(("Del", subTreeAName, nameB, row -1))
            row = row - 1
        elif matrix[row][col] == matrix[row][col - 1] + costInsert_TagAndText(
            subTreeB, A
        ):
            editScript.append(("Ins", nameA, subTreeBName, col - 1))
            col = col - 1
        else:
            editScript += getTreeEditScript_TagAndText(
                matricesDic, A, B, subTreeAName, subTreeBName
            )
            row = row - 1
            col = col - 1

    while row > 0:
        subTreeAName = nameA + "-" + str(row - 1)
        editScript.append(("Del", subTreeAName, nameB, row -1))
        row = row - 1

    while col > 0:
        subTreeBName = nameB + "-" + str(col - 1)
        editScript.append(("Ins", nameA, subTreeBName, col - 1))
        col = col - 1

    rootA = findSubTree(A, nameA)
    rootB = findSubTree(B, nameB)

    if rootA.tag != rootB.tag:
        editScript.append(("UpdTag", nameA, nameB))

    dicKey = nameA + "/" + nameB + "/text"
    if dicKey in matricesDic:
        textA = rootA.text
        textB = rootB.text
        if textA is None:
            textA = ""
        if textB is None:
            textB = ""
        textMatrix = matricesDic[dicKey]
        if textMatrix[len(textA.split())][len(textB.split())] != 0:
            ESText = getEditScriptArray(textMatrix, textA, textB)
            editScript.append(("UpdText", nameA, nameB, reverseArray(ESText)))

    return editScript


# After getting the edit matrices using NJ algorithm, the matrices
# are stored in a dictionary with their name as key
# using them will get the edit script by tranversing them back
# Note that the result should be flipped
# this method take into considaration all tags,text and attributes


def getTreeEditScript(matricesDic, A, B, nameA, nameB):

    keyDic = nameA + "/" + nameB
    editScript = []
    matrix = matricesDic.get(keyDic)

    row = len(matrix) - 1
    col = len(matrix[0]) - 1

    while row > 0 and col > 0:
        subTreeAName = nameA + "-" + str(row - 1)
        subTreeBName = nameB + "-" + str(col - 1)

        subTreeA = findSubTree(A, subTreeAName)
        subTreeB = findSubTree(B, subTreeBName)

        if matrix[row][col] == (matrix[row - 1][col] + costDelete(subTreeA, B)):
            editScript.append(("Del", subTreeAName , nameB, row -1))
            row = row - 1
        elif matrix[row][col] == matrix[row][col - 1] + costInsert(subTreeB, A):
            editScript.append(("Ins", nameA, subTreeBName, col - 1))
            col = col - 1
        else:
            editScript += getTreeEditScript(
                matricesDic, A, B, subTreeAName, subTreeBName
            )
            row = row - 1
            col = col - 1

    while row > 0:
        subTreeAName = nameA + "-" + str(row - 1)
        editScript.append(("Del", subTreeAName , nameB, row -1))
        row = row - 1

    while col > 0:
        subTreeBName = nameB + "-" + str(col - 1)
        editScript.append(("Ins", nameA, subTreeBName, col - 1))
        col = col - 1

    rootA = findSubTree(A, nameA)
    rootB = findSubTree(B, nameB)

    if rootA.tag != rootB.tag:
        editScript.append(("UpdTag", nameA, nameB))

    textKey = nameA + "/" + nameB + "/text"
    if textKey in matricesDic:
        textA = rootA.text
        textB = rootB.text
        if textA is None:
            textA = ""
        if textB is None:
            textB = ""
        textMatrix = matricesDic[textKey]
        if textMatrix[len(textA.split())][len(textB.split())] != 0:
            ESText = getEditScriptArray(textMatrix, textA, textB)
            editScript.append(("UpdText", nameA, nameB, reverseArray(ESText)))

    attKey = nameA + "/" + nameB + "/attribute"
    if attKey in matricesDic:
        attMatrix = matricesDic[attKey]
        if attMatrix[len(attMatrix) - 1][len(attMatrix[0]) - 1] != 0:
            ESatt = getEditScriptDict(attMatrix, rootA.attrib, rootB.attrib)
            editScript.append(("UpdAttribute", nameA, nameB, reverseArray(ESatt)))

    return editScript


# The following method save the ES array into an XML


def EStoXML(ES):
    top = ET.Element("EditScript")
    for op in ES:
        opNode = ET.SubElement(top, op[0])

        if op[0] == "UpdTag":
            opNode.set("nameA", op[1])
            opNode.set("nameB", op[2])

        if op[0] == "Ins":
            opNode.set("nameA", op[1])
            opNode.set("subTreeBName", op[2])
            opNode.set("index", str(op[3]))

        if op[0] == "Del":
            opNode.set("subTreeAName", op[1])
            opNode.set("nameB", op[2])
            opNode.set("index", str(op[3]))
######################## NEED TO MODIFY DELETE HERE ##################################
        if op[0] == "UpdText":
            opNode.set("nameA", op[1])
            opNode.set("nameB", op[2])
            for opText in op[3]:
                opTextNode = ET.SubElement(opNode, opText[0])
                if opText[0] == "UpdWord":
                    opTextNode.set("index", str(opText[1]))
                    opTextNode.set("to", opText[2])
                if opText[0] == "DelWord":
                    opTextNode.set("index", str(opText[1]))
                if opText[0] == "InsWord":
                    opTextNode.set("index", str(opText[1]))
                    opTextNode.set("word", opText[2])

        if op[0] == "UpdAttribute":
            opNode.set("nameA", op[1])
            opNode.set("nameB", op[2])
            for opAtt in op[3]:
                opAttNode = ET.SubElement(opNode, opAtt[0])
                if opAtt[0] == "UpdAtt":
                    opAttNode.set("index", str(opAtt[1]))
                    opAttNode.set("Key", opAtt[2][0])
                    opAttNode.set("Value", opAtt[2][1])
                if opAtt[0] == "DelAtt":
                    opAttNode.set("index", str(opAtt[1]))
                if opAtt[0] == "InsAtt":
                    opAttNode.set("index", str(opAtt[1]))
                    opAttNode.set("Key", opAtt[2][0])
                    opAttNode.set("Value", opAtt[2][1])

    return top

######################### not modified yet ########################################
def XMLtoES(root):

    ES = []
    for child in root:
        tuple = ()
        if child.tag == "UpdTag":
            tuple = ("UpdTag", child.get("nameA"), child.get("nameB"))

        if child.tag == "Del":
            tuple = ("Del", child.get("subTreeAName"))

        if child.tag == "Ins":
            tuple = (
                "Ins",
                child.get("nameA"),
                child.get("subTreeBName"),
                int(child.get("index")),
            )

        if child.tag == "UpdText":
            textES = []
            for textChild in child:
                textTuple = ()
                if textChild.tag == "UpdWord":
                    textTuple = (
                        "UpdWord",
                        int(textChild.get("index")),
                        textChild.get("to"),
                    )
                if textChild.tag == "DelWord":
                    textTuple = ("DelWord", int(textChild.get("index")))
                if textChild.tag == "InsWord":
                    textTuple = (
                        "InsWord",
                        int(textChild.get("index")),
                        textChild.get("word"),
                    )
                textES.append(textTuple)
                # print(textChild.tag, textES)
            tuple = ("UpdText", child.get("nameA"), child.get("nameB"), textES)

        if child.tag == "UpdAttribute":
            attES = []
            for attChild in child:
                attTuple = ()
                if attChild.tag == "UpdAtt":
                    attTuple = (
                        "UpdAtt",
                        int(attChild.get("index")),
                        (attChild.get("Key"), attChild.get("Value")),
                    )
                if attChild.tag == "DelAtt":
                    attTuple = ("DelAtt", attChild.get("index"))
                if attChild.tag == "InsAtt":
                    attTuple = (
                        "InsAtt",
                        int(attChild.get("index")),
                        (attChild.get("Key"), attChild.get("Value")),
                    )
                attES.append(attTuple)
            tuple = ("UpdAttribute", child.get("nameA"), child.get("nameB"), attES)

        ES.append(tuple)

    return ES
