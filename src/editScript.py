from src.costCalc import *
from src.arrayEditDistance import getEditScriptArray
from src.dictEditDistance import getEditScriptDict


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
            editScript.append(("Del", subTreeAName))
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
        editScript.append(("Del", subTreeAName))
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
            editScript.append(("Del", subTreeAName))
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
        editScript.append(("Del", subTreeAName))
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
            editScript.append(("Del", subTreeAName))
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
        editScript.append(("Del", subTreeAName))
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


# # def EStoXML(ES):
# #     top = Element("EditScript")
# #     for ele in ES:
# #         tag = SubElement(top, ele[0])
# #         if ele[0] == "Upd":
# #             tag.set("nameA", ele[1])
# #             tag.set("nameB", ele[2])
# #         if ele[0] == "Ins":
# #             tag.set("nameA", ele[1])
# #             tag.set("subTreeBName", ele[2])
# #             tag.set("col-1", str(ele[3]))
# #         if ele[0] == "Del":
# #             tag.set("subTreeAName", ele[1])

# #     tree = ElementTree(top)
# #     tree.write("ES.xml")
# #     return "XMl file created"


# # def XMLtoES(xmlFile):
# #     tree = ET.parse(xmlFile)
# #     root = tree.getroot()

# #     ES = []
# #     for child in root:
# #         tuple = ()
# #         tuple += (child.tag,)
# #         if child.tag == "Upd":
# #             tuple += (child.get("nameA"),)
# #             tuple += (child.get("nameB"),)
# #         if child.tag == "Del":
# #             tuple += (child.get("subTreeAName"),)
# #         if child.tag == "Ins":
# #             tuple += (child.get("nameA"),)
# #             tuple += (child.get("subTreeBName"),)
# #             tuple += (int(child.get("col-1")),)

# #         ES.append(tuple)

# #     print(ES)
# #     return ES
