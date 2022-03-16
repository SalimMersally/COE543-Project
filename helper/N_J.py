from helper.costCalc import *
import xml.etree.ElementTree as ET
import copy

##note we used the inner functions to preserve the value of rootA and rootB when it comes to tree cost calculations
def NJ(rootA0,rootB0):
    rootA = copy.deepcopy(rootA0)
    rootB = copy.deepcopy(rootB0)
    def TED (rootA, rootB):
   
        M=len(rootA) #number of first Level children in A
        N=len(rootB) #number of first Level children in B   
    
        Dist = [[None for i in range (N+1)] for i in range (M+1)] 
        Dist[0][0] = costUpd(rootA,rootB)
    
    
        i=1
        j=1
        for childA in rootA:
            Dist[i][0] = (Dist[i-1][0] + costDelete(childA,rootB0))             
            i+=1
        
        for childB in rootB:
            Dist[0][j] = (Dist[0][j-1] + costInsert(childB,rootA0))
            j+=1
        
        i=1
        for childA in rootA:
        
            j=1
            for childB in rootB:
                print(Dist)
                Dist[i][j] = min(
                    (Dist [i-1] [j-1] + TED(childA,childB)),
                    (Dist [i-1] [j]   + costDelete(childA,rootB0)),
                    (Dist [i] [j-1]   + costInsert(childB,rootA0))
                )
                j+=1
            i+=1
        
        print(Dist)
        return Dist[M][N]
    
    return TED(rootA,rootB)