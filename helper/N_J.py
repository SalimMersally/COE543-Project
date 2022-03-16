from helper.costCalc import *
import xml.etree.ElementTree as ET


def TED (rootA, rootB):
    M=len(rootA) #number of children in A
    N=len(rootB) #number of children in B   
    
    Dist = [[0 for i in range (N+1)] for i in range (M+1)] 
    Dist[0][0] = costUpd(rootA,rootB)
    
    i=1
    j=1
    for child in rootA:
        Dist[i][0] = Dist[i-1][0] + costDelete(child,rootB)
        i+=1
        
    for child in rootB:
        Dist[0][j] = Dist[0][j-1] + costDelete(child,rootA)
        j+=1
        
        
    i=1
    j=1
    for childA in rootA:
        for childB in rootB:
            
            Dist[i][j] = min(
                Dist [i-1] [j-1] + TED(childA,childB),
                Dist [i-1] [j]   + costDelete(childA,rootB),
                Dist [i] [j-1]   + costInsert(childB,rootA)
            )
    return Dist[M][N]