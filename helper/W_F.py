
def WF(A,B):
    
    tokenA = A.split()
    tokenB = B.split()
    
    M = len(tokenA)  
    N = len(tokenB)  
    
    Dist = [[None for i in range(N + 1)] for i in range(M + 1)]
    Dist[0][0]=0
    
    for i in range(1,M+1):
        Dist[i][0] = Dist[i-1][0] + costDelWord()
    for j in range(1,N+1):
        Dist[0][j] = Dist[0][j-1] + costInsWord()
        
    for i in range(1,M+1):
        for j in range(1,N+1):
            Dist[i][j]= min(
                Dist[i-1][j-1]+ costUpdWord(tokenA[i-1],tokenB[j-1]),
                Dist[i-1][j]+ costDelWord(),
                Dist[i][j-1]+ costInsWord()
            )
            
    
    return Dist


def costUpdWord(A,B):
    if A == B:
        return 0
    return 1

# keep those methods to later ask for user input
def costInsWord(): 
    return 1

def costDelWord():
    return 1

A="hello there are you hungry"
B="Hello here are you not very hungry"

print(WF(A,B))


def getEditScriptWF(matrix, A, B):
    
    tokenA = A.split()
    tokenB = B.split()
    
    row = len(matrix) - 1
    col = len(matrix[0]) - 1
    editScript = []
    
    while row > 0 and col > 0: 
        if matrix[row][col] == (matrix[row - 1][col] + costDelWord()):
            editScript.append(("Del", tokenA[row-1]))
            row = row - 1
        elif matrix[row][col] == matrix[row][col - 1] + costInsWord():
            editScript.append(("Ins", tokenB[col-1]))
            col = col - 1
        elif costUpdWord(tokenA[row-1],tokenB[col-1])!= 0:
            editScript.append(("Upd", tokenA[row-1],tokenB[col-1] ))  
            row = row - 1
            col = col - 1
        else:
            row = row - 1
            col = col - 1
            
    while row > 0:
        editScript.append(("Del", tokenA[row-1]))
        row = row - 1 
        
    while col > 0:
        editScript.append(("Ins", tokenB[col-1]))
        col = col-1
        
    return editScript
    
print(getEditScriptWF(WF(A,B),A,B))