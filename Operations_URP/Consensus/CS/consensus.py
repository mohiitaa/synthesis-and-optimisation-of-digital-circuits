'''Consensus is a function belonging to the package CS
 that finds the consensus between a and b.

 To compute consensus we require AND and OR operations.
 op_or and op_and are present in the subpackage CS.Operations and
 the corressponding functions for OR and AND
'''

from CS.op_or import op_or
from CS.op_and import op_and


def consensus(a,b):
    n=len(a) # n gives the number of input variables
    con=[[ "00" for x in range(n)] for x in range(n)]
    i=0
    j=0
    consensus=[]
    flag=0
#-------------Computing the Consensus------------

    for i in range (n):
        
        flag=0
        for j in range(n):
            
            if i==j:
                
                con[i][j]=(op_or(a[j],b[j]))     # The digaonal elements of the consensus matrix is the result of OR operation between the corressponding variables 2 implicants

            else:
                
                con[i][j]=(op_and(a[j],b[j])) # Else its just AND operation
                if con[i][j]=="00":
    # All rows with "00" resulting from the AND operation are removed.
                    flag=1
        if flag!=1:
            
            consensus.append(con[i])
    return consensus   # The consenssu matrix containing the consensus is stored




    
    
