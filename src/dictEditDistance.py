from pprint import pprint

dict1 = {
    "at1": "val1",
    "at2": "val2",
    "at3": "val3",
    "at4": "val4",
    "at5": "val5",
    "at6": "val6",
}

dict2 = {
    "at2": "val2",
    "at3": "val3",
    "at4": "val4",
    "at5": "val4",
    "at6": "val6",
    "at7": "val7",
}


def WF_Dict(dictA, dictB):

    listA = list(dictA.items())
    listB = list(dictB.items())

    M = len(listA)
    N = len(listB)

    Distance = [[None for i in range(N + 1)] for i in range(M + 1)]
    Distance[0][0] = 0

    for i in range(1, M + 1):
        Distance[i][0] = Distance[i - 1][0] + costDelAtt()
    for j in range(1, N + 1):
        Distance[0][j] = Distance[0][j - 1] + costInsAtt()

    for i in range(1, M + 1):
        for j in range(1, N + 1):
            Distance[i][j] = min(
                Distance[i - 1][j - 1] + costUpdAtt(listA[i - 1], listB[j - 1]),
                Distance[i - 1][j] + costDelAtt(),
                Distance[i][j - 1] + costInsAtt(),
            )

    return Distance


def costUpdAtt(A, B):
    if A[0] == B[0] and A[1] == B[1]:
        return 0
    elif A[0] == B[0]:
        return 1
    else:
        return 2


def costInsAtt():
    return 2


def costDelAtt():
    return 2


distance = WF_Dict(dict1, dict2)
pprint(distance)


def getEditScriptDict(matrix, dictA, dictB):

    listA = list(dictA.items())
    listB = list(dictB.items())

    row = len(matrix) - 1
    col = len(matrix[0]) - 1
    editScript = []

    while row > 0 and col > 0:
        if matrix[row][col] == (matrix[row - 1][col] + costDelAtt()):
            editScript.append(("DelAtt", row - 1))
            row = row - 1
        elif matrix[row][col] == matrix[row][col - 1] + costInsAtt():
            editScript.append(("InsAtt", row, listB[col - 1]))
            col = col - 1
        elif costUpdAtt(listA[row - 1], listB[col - 1]) != 0:
            editScript.append(("UpdAtt", row - 1, listB[col - 1]))
            row = row - 1
            col = col - 1
        else:
            row = row - 1
            col = col - 1

    while row > 0:
        editScript.append(("DelAtt", row - 1))
        row = row - 1

    while col > 0:
        editScript.append(("InsAtt", row, listB[col - 1]))
        col = col - 1

    return editScript


def reverseArray(array):
    result = []
    i = len(array) - 1
    while i >= 0:
        result.append(array[i])
        i -= 1
    return result


ES = getEditScriptDict(distance, dict1, dict2)
pprint(reverseArray(ES))


def patchDict(dictA, ES):
    listA = list(dictA.items())
    changes = 0
    for op in ES:
        print(listA)
        if op[0] == "UpdAtt":
            listA[op[1] + changes] = op[2]
        if op[0] == "DelAtt":
            listA.pop(op[1] + changes)
            changes -= 1
        if op[0] == "InsAtt":
            listA.insert(op[1] + changes, op[2])
            changes += 1
    return dict(listA)


pprint(patchDict(dict1, reverseArray(ES)))
