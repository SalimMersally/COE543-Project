from pprint import pp, pprint


# the following method will compare two array of words following the
# Wagnar and Fisher algorithm (assuming the element to comapre are words and not
# character). the cost model is as follow:
#   - costDelWord = 1
#   - costInsWord = 1
#   - costUpdWord = 0 if same, 1 if different
# note that we assumed the comparision is case sensitive


def WF(A, B):

    tokenA = A.split()
    tokenB = B.split()

    M = len(tokenA)
    N = len(tokenB)

    Distance = [[None for i in range(N + 1)] for i in range(M + 1)]
    Distance[0][0] = 0

    for i in range(1, M + 1):
        Distance[i][0] = Distance[i - 1][0] + costDelWord()
    for j in range(1, N + 1):
        Distance[0][j] = Distance[0][j - 1] + costInsWord()

    for i in range(1, M + 1):
        for j in range(1, N + 1):
            Distance[i][j] = min(
                Distance[i - 1][j - 1] + costUpdWord(tokenA[i - 1], tokenB[j - 1]),
                Distance[i - 1][j] + costDelWord(),
                Distance[i][j - 1] + costInsWord(),
            )

    return Distance


def costUpdWord(A, B):
    if A == B:
        return 0
    return 1


def costInsWord():
    return 1


def costDelWord():
    return 1


def getEditScriptArray(matrix, A, B):

    tokenA = A.split()
    tokenB = B.split()

    row = len(matrix) - 1
    col = len(matrix[0]) - 1
    editScript = []

    while row > 0 and col > 0:
        if matrix[row][col] == (matrix[row - 1][col] + costDelWord()):
            editScript.append(("DelWord", row - 1, tokenA[row - 1]), col)
            row = row - 1
        elif matrix[row][col] == matrix[row][col - 1] + costInsWord():
            editScript.append(("InsWord", row, tokenB[col - 1], col - 1))
            col = col - 1
        elif costUpdWord(tokenA[row - 1], tokenB[col - 1]) != 0:
            editScript.append(
                ("UpdWord", row - 1, tokenA[row - 1], col - 1, tokenB[col - 1])
            )
            row = row - 1
            col = col - 1
        else:
            row = row - 1
            col = col - 1

    while row > 0:
        editScript.append(("DelWord", row - 1, tokenA[row - 1], col))
        row = row - 1

    while col > 0:
        editScript.append(("InsWord", row, tokenB[col - 1], col - 1))
        col = col - 1

    return editScript


def patchArray(strA, ES):
    arrA = strA.split()
    changes = 0
    for op in ES:
        if op[0] == "UpdWord":
            arrA[op[1] + changes] = op[4]
        if op[0] == "DelWord":
            arrA.pop(op[1] + changes)
            changes -= 1
        if op[0] == "InsWord":
            arrA.insert(op[1] + changes, op[2])
            changes += 1
    return " ".join(arrA)


# flip the ES so it can be used to patch B to A
def flipArrayES(arrayES):
    flipped = []
    for op in arrayES:
        tuple = ()
        if op[0] == "UpdWord":
            tuple = ("UpdWord", op[3], op[4], op[1], op[2])
        if op[0] == "DelWord":
            tuple = ("InsWord", op[3], op[2], op[1])
        if op[0] == "InsWord":
            tuple = ("DelWord", op[3], op[2], op[1])
        flipped.append(tuple)
    return flipped
