from function.costCalc import *

# the following method will calculate the Edit Distance Matrices
# to transform treeA into treeB following Nermin and Jagadish algorithm
# this method take into considiration only tag


def NJ_Tag(A, B, nameA, nameB, matricesDic, costDict):

    subTreeA = findSubTree(A, nameA)
    subTreeB = findSubTree(B, nameB)

    M = len(subTreeA)  # number of first Level children in A
    N = len(subTreeB)  # number of first Level children in B

    Distance = [[None for i in range(N + 1)] for i in range(M + 1)]
    Distance[0][0] = costUpd_Tag(subTreeA, subTreeB, costDict)

    i = 1
    j = 1
    for childA in subTreeA:
        Distance[i][0] = Distance[i - 1][0] + costDelete_Tag(childA, B, costDict)
        i += 1

    for childB in subTreeB:
        Distance[0][j] = Distance[0][j - 1] + costInsert_Tag(childB, A, costDict)
        j += 1

    i = 1
    for childA in subTreeA:

        j = 1
        for childB in subTreeB:
            childAName = nameA + "-" + str(i - 1)
            childBName = nameB + "-" + str(j - 1)

            Distance[i][j] = min(
                (
                    Distance[i - 1][j - 1]
                    + NJ_Tag(A, B, childAName, childBName, matricesDic, costDict)
                ),
                (Distance[i - 1][j] + costDelete_Tag(childA, B, costDict)),
                (Distance[i][j - 1] + costInsert_Tag(childB, A, costDict)),
            )
            j += 1
        i += 1

    matricesDic[nameA + "/" + nameB] = Distance
    return Distance[M][N]


# the following method will calculate the Edit Distance Matrices
# to transform treeA into treeB following Nermin and Jagadish algorithm
# this method take into considiration only tag and text


def NJ_TagAndText(A, B, nameA, nameB, matricesDic, costDict):

    subTreeA = findSubTree(A, nameA)
    subTreeB = findSubTree(B, nameB)

    M = len(subTreeA)  # number of first Level children in A
    N = len(subTreeB)  # number of first Level children in B

    Distance = [[None for i in range(N + 1)] for i in range(M + 1)]
    Distance[0][0] = costUpd_TagAndText(
        subTreeA, subTreeB, nameA, nameB, matricesDic, costDict
    )

    i = 1
    j = 1
    for childA in subTreeA:
        Distance[i][0] = Distance[i - 1][0] + costDelete_TagAndText(childA, B, costDict)
        i += 1

    for childB in subTreeB:
        Distance[0][j] = Distance[0][j - 1] + costInsert_TagAndText(childB, A, costDict)
        j += 1

    i = 1
    for childA in subTreeA:

        j = 1
        for childB in subTreeB:
            childAName = nameA + "-" + str(i - 1)
            childBName = nameB + "-" + str(j - 1)

            Distance[i][j] = min(
                (
                    Distance[i - 1][j - 1]
                    + NJ_TagAndText(A, B, childAName, childBName, matricesDic, costDict)
                ),
                (Distance[i - 1][j] + costDelete_TagAndText(childA, B, costDict)),
                (Distance[i][j - 1] + costInsert_TagAndText(childB, A, costDict)),
            )
            j += 1
        i += 1

    matricesDic[nameA + "/" + nameB] = Distance
    return Distance[M][N]


# the following method will calculate the Edit Distance Matrices
# to transform treeA into treeB following Nermin and Jagadish algorithm
# this method take into considiration all tags, text and attributes


def NJ(A, B, nameA, nameB, matricesDic, costDict):

    subTreeA = findSubTree(A, nameA)
    subTreeB = findSubTree(B, nameB)

    M = len(subTreeA)  # number of first Level children in A
    N = len(subTreeB)  # number of first Level children in B

    Distance = [[None for i in range(N + 1)] for i in range(M + 1)]
    Distance[0][0] = costUpd(subTreeA, subTreeB, nameA, nameB, matricesDic, costDict)

    i = 1
    j = 1
    for childA in subTreeA:
        Distance[i][0] = Distance[i - 1][0] + costDelete(childA, B, costDict)
        i += 1

    for childB in subTreeB:
        Distance[0][j] = Distance[0][j - 1] + costInsert(childB, A, costDict)
        j += 1

    i = 1
    for childA in subTreeA:

        j = 1
        for childB in subTreeB:
            childAName = nameA + "-" + str(i - 1)
            childBName = nameB + "-" + str(j - 1)

            Distance[i][j] = min(
                (
                    Distance[i - 1][j - 1]
                    + NJ(A, B, childAName, childBName, matricesDic, costDict)
                ),
                (Distance[i - 1][j] + costDelete(childA, B, costDict)),
                (Distance[i][j - 1] + costInsert(childB, A, costDict)),
            )
            j += 1
        i += 1

    matricesDic[nameA + "/" + nameB] = Distance
    return Distance[M][N]
