from math import dist
from unicodedata import name
from helper.costCalc import *
from helper.treePatch import *
import xml.etree.ElementTree as ET
import numpy as np

##note we used the inner functions to preserve the value of rootA and rootB when it comes to tree cost calculations
def NJ(A, B, nameA, nameB, matricesDic):

    subTreeA = findSubTree(A, nameA)
    subTreeB = findSubTree(B, nameB)

    M = len(subTreeA)  # number of first Level children in A
    N = len(subTreeB)  # number of first Level children in B

    Dist = [[None for i in range(N + 1)] for i in range(M + 1)]
    Dist[0][0] = costUpd(subTreeA, subTreeB)

    i = 1
    j = 1
    for childA in subTreeA:
        Dist[i][0] = Dist[i - 1][0] + costDelete(childA, B)
        i += 1

    for childB in subTreeB:
        Dist[0][j] = Dist[0][j - 1] + costInsert(childB, A)
        j += 1

    i = 1
    for childA in subTreeA:

        j = 1
        for childB in subTreeB:
            childAName = nameA + "-" + str(i - 1)
            childBName = nameB + "-" + str(j - 1)

            Dist[i][j] = min(
                (Dist[i - 1][j - 1] + NJ(A, B, childAName, childBName, matricesDic)),
                (Dist[i - 1][j] + costDelete(childA, B)),
                (Dist[i][j - 1] + costInsert(childB, A)),
            )
            j += 1
        i += 1

    matricesDic[nameA + "/" + nameB] = Dist
    return Dist[M][N]
