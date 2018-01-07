#THIS CODE USES URP TO FIND THE COMPLEMENT OF A FUNCTION
'''
The termination conditions of recursion check for a tautology or a void cube.
If that's not satisfied,we see if it is a single implIcant and then use De morgan's law to find the complement at that level.
Else,shannon's expansion is done on the function with respect to the most binate variable.
And as the recursion returns,shannon's expressions at each level are combined.

FUNCTIONS USED FROM 'Cofactor' PACKAGE:
1.The "op_cofactor" function which finds cofactor with respect to an impicant
2.The "op_and" function which does basic anding operation
->Both these functions are used for computation of shannons expression.


TEST CASES: (each test case checks each respective termination condition,also traverses all possible paths in the code)
1.A null function
2.1st implicant=['11','11','01'], 2nd implicant=['11','11','10']
3.A function with row of 11's(PCN)
4.1st implicant=['01','11','11'], 2nd implicant=['11','01','01']
5.1st implicant=['01','01','01'], 2nd implicant=['10','10','10'], 3rd implicant=['01','10','11']

'''   

#############################################################################################################################################


from Cofactor.op_cofactor import op_cofactor
from Cofactor.op_and import op_and
import copy


#------------------------------function for performing OR operation(to sum the products in shannon expression)-------------------------------

def op_or(a,b):
    if a=="11" or b=="11":
        s="11"
    elif a==b:
        s=a
    else:
        s="11"
    return s

    
#---------------------function to check if the expression depends on a single variable and if yes, is it a tautology------------------------
    
def single_var_tauto(cube1,n1,c1):
    singlevartauto=0 
    colcount=0
    for i in range(n1):
        onecount=0
        for j in range(c1):
            if cube1[j][i]=="11":
                onecount=onecount+1
            else:
                dependentcol=i
                break
        if onecount==c1:    #check if this variable has as a column of "11"s
            colcount=colcount+1
    
    if colcount==n1-1:  #check if there are n-1 columns of "11"s. If yes, it depends on one variable
        for i in range(c1-1):
            if cube1[i][dependentcol]!=cube[i+1][dependentcol]:    #checking if that one variable is unate or binate
                singlevartauto=1                                   #if binate, the function is a tautology and singlevartauto=1 , else singlevartauto=0
                break
    return singlevartauto


#-------------------------Function for De morgan's operation on a single implicant---------------------------------------------------------------
def demorgan(cube2,n2):
        demorg_comp=list()
        
        for i in range(n2):
                taut2=["11" for x in range(n2)]
                if cube2[0][i]!="11":
                        if cube[0][i]=="01":
                                taut2[i]="10"
                                
                        else:
                                taut2[i]="01"
                        demorg_comp.append(taut2)
        return demorg_comp                             #Example: if cube2=bc=[['11','01','01']], demorg_comp=b!+c!=[['11','10','11'],['11','11','01']

    
#------------------------------------------Function to find the most binate variable-----------------------------------------------------------------

def binate_var(Main,n,cnew):
    print("Binate Function")
    diff=["00" for  x in range(n)]
    count01=0
    count10=0
    for j in range(n):
        count01=0
        count10=0
        for i in range(cnew):
            if Main[i][j]=="01":
                count01=count01+1
            elif Main[i][j]=="10":
                count10=count10+1
        diff[i]=max(count01,count10)-min(count01,count10)  #finding the amount of binateness
    (m,i) = max((diff,i) for i,v in enumerate(diff))
    return i                                               #returns the index of most binate variable
                
    

#--------------------------------------------------------------------------------------------------------------------------

#-------------------------------------Complementation function-------------------------------------------------------------  


def complementation(Main,index,n,cnew):
      
        print("recurr of ",index)

        taut=["11" for x in range(n)]
        void=["00" for x in range(n)]

        #------termination conditions
        if taut in Main:                     
            return void
        elif single_var_tauto(Main,n,cnew)==1:
            return void
        elif Main==[]:
            return taut
        elif len(Main)==1:
                #complementation using demorgan's Law
                comp=demorgan(Main,n)
                return comp

        splitvar=binate_var(Main,n,cnew)  #finding the most binate variable to split
        lcofac[splitvar]="10"             #implicant with respect to which we are cofactoring

        for i in range(cnew):             #cofactoring
                temp=op_cofactor(Main[i],lcofac)
                if temp!=[]:
                        leftcofactor.append(temp)
                        
        lcnew=len(leftcofactor)
    
        leftshannon=complementation(leftcofactor,index+1,n,lcnew) #calling left recursion
        lshanexp=op_and(lcofac,leftshannon)               #left half of shannon's expression
        
        rcofac[splitvar]="01"               #implicant with respect to which we are cofactoring

        for i in range(cnew):               #cofactoring
                temp=op_cofactor(Main[i],rcofac)
                if temp!=[]:
                        rightcofactor.append(temp)

        rcnew=len(rightcofactor)

        rightshannon=complementation(rightcofactor,index+1,n,rcnew)  #calling right recursion
        rshanexp=op_and(rcofac,rightshannon)                        #right half of shannon's expression
        print("rshanexp=",rshanexp)

        #combing shannon's expression
        shannonexp.append(lshanexp)
        shannonexp.append(rshanexp)

        return shannonexp
                
                
        

#---------------------------------------------------------------------------------------------------------


#--------------------------------------------PROGRAM BEGINS-----------------------------------------------

n=0
c=0
n = int(input("Enter the number of variables in the function:"))
c = int(input("Enter the number of cubes in the function:"))

cnew=copy.deepcopy(c)
nnew=copy.deepcopy(n)

dc=0
tautology=0
flag=0
lol="00"
cube=[["00" for x in range(n)] for x in range(c)] #-----------the PCN input list

print("Enter the cubes in PCN(in order):")

#-------This part takes input and removes null cubes and checks for don't care cubes Ex:['11','11','11']

for i in range(c):
    for j in range(n):
        cube[i-flag][j]=input()
        if cube[i-flag][j]=="11":
            dc=dc+1
        if cube[i-flag][j]=="00":
#      print("That was a redundant cube.Enter the next cube.")
            for k in range(n-j-1):
                lol=input()
            cube.pop(i-flag)
            flag=flag+1
            dc=0
            break
    if dc==n:
        cube.pop(i-flag)
        tautology=tautology+1
        dc=0
        flag=flag+1
    dc=0
    print("*")


#--------our new c is the number of cubes left after removing null and don't care cubes
c=c-flag
if tautology==0:
    tautology=single_var_tauto(cube,n,c)

if tautology!=0:
    print("The entered function is a TAUTOLOGY and hence the complement is VOID \n F!=0")
    
elif c==0:
    print("The entered function is VOID and hence the complement is a TAUTOLOGY \n F!=1")
    
else:
    print("reduced input:",cube)
    rec=list()
    #------rec is a list of list of lists to store cubes at different levels
    lcofac=["11" for x in range(n)]
    rcofac=["11" for x in range(n)]
    leftcofactor=list()
    rightcofactor=list()
    shannonexp=list()
    final=complementation(cube,0,n,cnew)
    print("complement=",final)

    
    
#---------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------PROGRAM END-----------------------------------------------------------------
