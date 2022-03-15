from costCalc import *
script = ""

def getEditScript(dic , A, B):
    strA = A + ''
    strB = B + ''
    keyDic = strA + strB
    toReturn = []
    matrix = dic.get(keyDic)

    row = len(matrix) -1
    col = len(matrix[0])  -1
    ############add condition for matrix 1 of 1 

    while row>0 and col>0:
        if matrix[row][col] == matrix[row][col -1 ] + costDelete(A + row, B + col):
            toReturn.append("DelTree("+ strA +"-"+ row + ")")
        elif matrix[row][col] == matrix[row - 1][col] + costInsert(A + row, B + col):
            toReturn.append("InsTree("+ strB +"-"+ col + ")")
        else:
            strA = strA + "-" + row
            strB = strB + "-" + col
            # Here i need to fix the array to return 
            # else my output will have the below form
            # [Deltree#, [Deltree#,Instree#],Upd(A,B)]
            toReturn.append(getEditScript(dic , strA, strB))
        row = row - 1
        col = col - 1
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
        toReturn.append("InsTree("+ strA +"-"+ col + ")")
        col = col - 1
        if row == 0 and col == 0:
            if matrix[row][col] == 1:
                toReturn.append("Upd(" + strA + ","+strB)
        # end of the third loop    


    return toReturn