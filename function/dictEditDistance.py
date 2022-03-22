# the following method are used to get the edit distance, edit script, and
# patch a dictionary (to be used for attribute and value of trees)
# the algorithm follow wagnar and fisher approach but with tuples of 2 words
# instead of one. the cost model is as follow:
#   - InsAtt = 2
#   - DelAtt = 2
#   - UpdAtt = 0 if same, 1 if same but diff value, 2 if att and val diff


def WF_Dict(dictA, dictB, costDict):

    listA = list(dictA.items())
    listB = list(dictB.items())

    M = len(listA)
    N = len(listB)

    Distance = [[None for i in range(N + 1)] for i in range(M + 1)]
    Distance[0][0] = 0

    for i in range(1, M + 1):
        Distance[i][0] = Distance[i - 1][0] + costDelAtt(costDict)
    for j in range(1, N + 1):
        Distance[0][j] = Distance[0][j - 1] + costInsAtt(costDict)

    for i in range(1, M + 1):
        for j in range(1, N + 1):
            Distance[i][j] = min(
                Distance[i - 1][j - 1]
                + costUpdAtt(listA[i - 1], listB[j - 1], costDict),
                Distance[i - 1][j] + costDelAtt(costDict),
                Distance[i][j - 1] + costInsAtt(costDict),
            )

    return Distance


def costUpdAtt(A, B, costDict):
    if A[0] == B[0] and A[1] == B[1]:
        return 0
    elif A[0] == B[0]:
        return costDict["CostUpd_attrib"]
    else:
        return 2 * costDict["CostUpd_attrib"]


def costInsAtt(costDict):
    return 2 * costDict["CostIns_attrib"]


def costDelAtt(costDict):
    return 2 * costDict["CostDel_attrib"]


def getEditScriptDict(matrix, dictA, dictB, costDict):

    listA = list(dictA.items())
    listB = list(dictB.items())

    row = len(matrix) - 1
    col = len(matrix[0]) - 1
    editScript = []

    while row > 0 and col > 0:
        if matrix[row][col] == (matrix[row - 1][col] + costDelAtt(costDict)):
            editScript.append(("DelAtt", row - 1, listA[row - 1], col))
            row = row - 1
        elif matrix[row][col] == matrix[row][col - 1] + costInsAtt(costDict):
            editScript.append(("InsAtt", row, listB[col - 1], col - 1))
            col = col - 1
        elif costUpdAtt(listA[row - 1], listB[col - 1], costDict) != 0:
            editScript.append(
                ("UpdAtt", row - 1, listA[row - 1], col - 1, listB[col - 1])
            )
            row = row - 1
            col = col - 1
        else:
            row = row - 1
            col = col - 1

    while row > 0:
        editScript.append(("DelAtt", row - 1, listA[row - 1], col))
        row = row - 1

    while col > 0:
        editScript.append(("InsAtt", row, listB[col - 1], col - 1))
        col = col - 1

    return editScript


def patchDict(dictA, ES):
    listA = list(dictA.items())
    changes = 0
    for op in ES:
        if op[0] == "UpdAtt":
            listA[op[1] + changes] = op[4]
        if op[0] == "DelAtt":
            listA.pop(op[1] + changes)
            changes -= 1
        if op[0] == "InsAtt":
            listA.insert(op[1] + changes, op[2])
            changes += 1
    return dict(listA)


# flip the ES so it can be used to patch B to A
def flipDictES(arrayES):
    flipped = []
    for op in arrayES:
        tuple = ()
        if op[0] == "UpdAtt":
            tuple = ("UpdAtt", op[3], op[4], op[1], op[2])
        if op[0] == "DelAtt":
            tuple = ("InsAtt", op[3], op[2], op[1])
        if op[0] == "InsAtt":
            tuple = ("DelAtt", op[3], op[2], op[1])
        flipped.append(tuple)
    return flipped
