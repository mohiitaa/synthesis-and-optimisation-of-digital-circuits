## The following code finds the consensus between 2 implicants.
## Consensus between 2 implicants is an indication of the distance
## between them. If Consensus is null, the distance is greater than
## or equal to 2.
##
## The function consensus is kept in the package CS. The 2 implicants
## are passed on as its arguments.

## To compute consensus we require AND and OR operations.
## op_or and op_and are present in the subpackage CS.Operations and
## the corressponding functions for OR and AND.



## To find the consensus between 2 implicants the code "impl_consensus" has to be run. It takes input in PCN format.
## ---------To execute imp_consensus------------------

## >> Enter the number of variables
## <Input by user> some non-zero integer
## >>Enter the Implicants in PCN Notation
## <Input by user> Can be any 2 implicants in PCN Format. If "00" entered, a message stating that Invalid Input Occurs. The
##                 same message occurs when other characters are used.

##Note: After entering the PCN value for each variable, the next value has to be entered in a new line              

from CS.consensus import consensus

# ----- Taking the input from the user-------------------- 
n=input("Enter the number of variables")
a=["00"]*n
b=["00"]*n
valid_in=["11","01","10"]  # List of Valid Input

print "Enter the first implicant in PCN notation"
for j in range(n):
    
# While kept because the user has to keep giving input, unless and until its valid
    while(1):
        
        a[j]=raw_input()
            
      
        if a[j] not in valid_in:
            
            print("Invalid Input.Please enter the previous variable correctly")
        # "00"  or any other char input not  in valid_in are not accepted and the user has to enter the PCN value of the variable again
        else:
            break

print "Now, enter the 2nd implicant also in PCN notation."
for j in range(n):
    flag=0
    while (1):
        
        b[j]=raw_input()
        
        if b[j] not in valid_in:
            print("Invalid Input. Please enter the previous variable correctly")
        else:
            break

            
con=consensus(a,b) #Computing the consensus between a and b
if con==[]:
    print "The Consensus is void. Hence the distance between them is greater than or equal to 2"
else:
    print "The Consensus is:"
    print con



