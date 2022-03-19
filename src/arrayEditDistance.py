def reverseArray(array):
    result = []
    i = len(array) - 1
    while i >= 0:
        result.append(array[i])
        i -= 1
    return result


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


A = "hello there are you hungry dude"
B = "Hello here are you not very hungry"

# print(WF(A, B))


def getEditScriptWF(matrix, A, B):

    tokenA = A.split()
    tokenB = B.split()

    row = len(matrix) - 1
    col = len(matrix[0]) - 1
    editScript = []

    while row > 0 and col > 0:
        if matrix[row][col] == (matrix[row - 1][col] + costDelWord()):
            editScript.append(("DelWord", tokenA[row - 1]))
            row = row - 1
        elif matrix[row][col] == matrix[row][col - 1] + costInsWord():
            editScript.append(("InsWord", tokenB[col - 1]))
            col = col - 1
        elif costUpdWord(tokenA[row - 1], tokenB[col - 1]) != 0:
            editScript.append(("UpdWord", tokenA[row - 1], tokenB[col - 1]))
            row = row - 1
            col = col - 1
        else:
            row = row - 1
            col = col - 1

    while row > 0:
        editScript.append(("DelWord", tokenA[row - 1]))
        row = row - 1

    while col > 0:
        editScript.append(("InsWord", tokenB[col - 1]))
        col = col - 1

    return editScript


# print(reverseArray(getEditScriptWF(WF(A, B), A, B)))
