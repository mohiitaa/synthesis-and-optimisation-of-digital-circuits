
# The package Cofactor has the function op_cofactor,
# that finds the cofactor between a and b,given as its arguments.
# For finding the cofactor the following steps are followed
#   1. The intersection between the 2 implicants is taken.
#   2.If the 2 implicants don't intersect, we don't proceed ahead. Cofactor is null.
#     Else cofactor is given by:
#         [ a1+b1' a2+b2' a3+b3'.......    an+bn']

# Cofactor requires 2 basic functions: "and" and "or" with the 2nd variable complemented.
# op_and and op_notor are the respective functions for these. They are placed in the
# package Cofactor



from Cofactor.op_notor import op_notor
from Cofactor.op_and import op_and

def op_cofactor(a,b):

    n=len(a)
    flag=0
    '''#Checking for intersection between the 2 implicants    '''
    for j in range(n):
        
        s=op_and(a[j],b[j])
        if s=="00": # If no intersection,don't proceed ahead
            
            flag=1
            break
    
    
    if flag!=1:
        
        cofact=[0]*n
        for j in range(n):
            cofact[j]=op_notor(a[j],b[j])

    else:
        cofact=[]
  
       

    return cofact  
       
