# the following method are used to get the edit distance, edit script, and
# patch a dictionary (to be used for attribute and value of trees)
# the algorithm follow wagnar and fisher approach but with tuples of 2 words
# instead of one. the cost model is as follow:
#   - InsAtt = 2
#   - DelAtt = 2
#   - UpdAtt = 0 if same, 1 if same but diff value, 2 if att and val diff


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


def getEditScriptDict(matrix, dictA, dictB):

    listA = list(dictA.items())
    listB = list(dictB.items())

    row = len(matrix) - 1
    col = len(matrix[0]) - 1
    editScript = []

    while row > 0 and col > 0:
        if matrix[row][col] == (matrix[row - 1][col] + costDelAtt()):
            editScript.append(("DelAtt", row - 1, listA[row - 1], col))
            row = row - 1
        elif matrix[row][col] == matrix[row][col - 1] + costInsAtt():
            editScript.append(("InsAtt", row, listB[col - 1], col - 1))
            col = col - 1
        elif costUpdAtt(listA[row - 1], listB[col - 1]) != 0:
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
