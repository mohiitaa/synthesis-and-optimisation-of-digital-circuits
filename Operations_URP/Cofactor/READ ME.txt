##Given a function f of n variables and consisiting of m implicants,
## The following code finds the cofactor of all the m implicants
## with respect to a implicant beta also of n variables.
##
## op_cofactor is a function that finds the cofactor of 2
## implicants given as arguments.
## It is a function belonging to the user defined
## package "Cofactor".

## Also to compute cofactor, OR and AND are needed as well and
## they are present in the Cofactor Package

## ---------To execute impl_cofactor------------------

## >> Enter the number of variables in the function
## <Input by user> some non-zero integer
## >>Enter the number of implicants in the function
## <Input by user> some non-zero integer
## >> Enter the function(f) in PCN notation
## <Input by user>  In PCN Format. If "00" entered, a message stating that Invalid Input Occurs. The
##                 same message occurs when other characters are used.

##Note: After entering the PCN value for each variable, the next value has to be entered in a new line







from Cofactor.op_cofactor import op_cofactor


#--------------Taking Input(F and beta) from the User----------------------- '''
n=input("Enter the number of variables in the function")
m=input("Enter the number of implicants in the function")
a=[[ "00" for x in range(n)] for x in range(m)] # a will be a mxn matrix . a is the function.
b=["00"]*n
valid_in=["01","10","11"]
print "Enter the function(f) in PCN notation"
for i in range(m):
    
    for j in range(n):
        
        while (1):
            
# While kept because the user has to keep giving input, unless and until its valid '''
            a[i][j]=raw_input()
            if a[i][j] in valid_in:  
                
                break
            else:
                
                print("Invalid Input.Please enter the previous variable correctly")  # "00" isn't accepted
    print ("*")


print "Now, enter the implicant with respect to which you want to take the cofactor also in PCN notation i.e enter beta"
for j in range(n):
    flag=0
    while (1):
        
        b[j]=raw_input()  
        if b[j] in valid_in:
            break
        else:
            print("Invalid Input. Please enter the previous variable correctly")
cofact_mat=[]
#cofact_mat stores the cofactor result
#Finding the cofactor of the implicants of f with respect to beta 
for i in range(m):
    temp=op_cofactor(a[i],b)
    if temp!=[]:
        cofact_mat.append(temp)
   
    else:
        print "Cofactor between",str(a[i]),"and",str(b), "is void"
#If the 2 implicants don't intersect,the cofactor is void
        

if cofact_mat!=[]:
    print "Cofactor matrix is:\n "
    print cofact_mat
else:
    print "Cofactor is void since the intersection of the implicant with respect to all the implicants in the function is null"

    

