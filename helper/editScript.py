from helper.costCalc import *
from helper.treePatch import *
import numpy as np
from xml.etree.ElementTree import *

dict1 = {
    "AB": [[0, 4, 5], [1, 4, 4], [2, 3, 4]],
    "A-1B-1": [[1, 2], [2, 3], [3, 4]],
    "A-1-1B-1-1": [[1, 2, 3]],
    "A-1-2B-1-1": [[1, 2, 3]],
    "A-1B-2": [[0, 1, 2], [1, 0, 1], [2, 1, 0]],
    "A-1-1B-2-1": [[0]],
    "A-1-1B-2-2": [[1]],
    "A-1-2B-2-1": [[1]],
    "A-1-2B-2-2": [[0]],
    "A-2B-1-1": [[1, 2]],
    "A-2B-2": [[1, 2, 3]],
}


def getEditScript(matricesDic, A, B, nameA, nameB):

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
            editScript += getEditScript(matricesDic, A, B, subTreeAName, subTreeBName)
            row = row - 1
            col = col - 1
    # end of first while loop

    while row > 0:
        subTreeAName = nameA + "-" + str(row - 1)
        editScript.append(("Del", subTreeAName))
        row = row - 1
    # end of the second loop

    while col > 0:
        subTreeBName = nameB + "-" + str(col - 1)
        editScript.append(("Ins", nameA, subTreeBName, col - 1))
        col = col - 1
    # end of the third loop

    if row == 0 and col == 0:
        if matrix[row][col] == 1:
            editScript.append(("Upd", nameA, nameB))

    return editScript


def reverseArray(array):
    result = []
    i = len(array) - 1
    while i >= 0:
        result.append(array[i])
        i -= 1
    return result

def EStoXML(ES):
    top = Element('EditScript')
    for ele in ES: 
        tag = SubElement(top,ele[0])
        if ele[0] == 'Upd':
            tag.__setattr__('nameA: ',ele[1])
            tag.__setattr__('nameB: ',ele[2])
        if ele[0] == 'Ins':
            tag.__setattr__('nameA: ', ele[1])
            tag.__setattr__('subTreeBName: ', ele[2])   
            tag.__setattr__('col-1: ', ele[3])   
        if ele[0] == 'Del':
            tag.__setattr__('subTreeAName: ', ele[1]) 
            
    tree = ET.ElementTree("top")
    tree.write("ES.xml")        
    