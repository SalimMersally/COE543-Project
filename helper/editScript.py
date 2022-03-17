from helper.costCalc import *
from helper.treePatch import *
#dictionary example
print('Try Dictionar')
dict1 = {
    "AB" : [[0,4,5],[1,4,4],[2,3,4]],
    "A-1B-1" : [[1,2],[2,3],[3,4]],
    "A-1-1B-1-1" : [[1,2,3]],
    "A-1-2B-1-1" : [[1,2,3]],
    "A-1B-2" : [[0,1,2],[1,0,1],[2,1,0]],
    "A-1-1B-2-1" : [[0]],
    "A-1-1B-2-2" : [[1]],
    "A-1-2B-2-1" : [[1]],
    "A-1-2B-2-2" : [[0]],
    "A-2B-1-1" : [[1,2]],
    "A-2B-2" : [[1,2,3]]
}


#End of the example 

def getEditScript(dic , A, B, strA, strB):
    
    keyDic = strA + strB
    # ! ! ! 
    toReturn = []
    matrix = dic.get(keyDic)

    row = len(matrix) -1
    col = len(matrix[0])  -1
    ############add condition for matrix 1 of 1 ###############

    while row>0 and col>0:
        print("1")
        if matrix[row][col] == (matrix[row - 1][col] + costDelete(findSubTree(A,(strA +"-"+ str(row))) ,findSubTree( B,(strB +"-"+ str(col))))):
            toReturn.append("DelTree("+ strA +"-"+ row + ")")
            row = row - 1
        elif matrix[row][col] == matrix[row][col - 1] + costInsert(findSubTree(A,(strA +"-"+ str(row))) ,findSubTree( B,(strB +"-"+ str(col)))):
            toReturn.append("InsTree("+ strB +"-"+ col + ")")
            col = col - 1
        else:
            subtreeA = strA + "-" + row
            subtreeB = strB + "-" + col
            # Here i need to fix the array to return 
            # else my output will have the below form
            # [Deltree#, [Deltree#,Instree#],Upd(A,B)]
            toReturn.append(getEditScript(dic , A,B,subtreeA, subtreeB))
            row = row - 1
            col = col - 1
        # Here i guess it should be or so when we have the case of 0-0 it will check for update 
        # ! ! !
        if row == 0 and col == 0:
            if matrix[row][col] == 1:
                toReturn.append("Upd(" + strA + ","+strB)
    # end of first while loop
    
    while row > 0 :
        toReturn.append("DelTree("+ strA +"-"+ row + ")")
        row = row - 1
        if row == 0 and col == 0:
            if matrix[row][col] == 1:
                toReturn.append("Upd(" + strA + ","+strB)
    # end of the second loop
    
    while col > 0 :
        toReturn.append("InsTree("+ strB +"-"+ col + ")")
        col = col - 1
        if row == 0 and col == 0:
            if matrix[row][col] == 1:
                toReturn.append("Upd(" + strA + ","+strB)
    # end of the third loop    


    return toReturn

