
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
            
    
    return Dist[M][N]


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
