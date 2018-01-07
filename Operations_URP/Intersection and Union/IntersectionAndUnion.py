## This is a code for INTERSECTION and UNION.

# A few test case examples which cover all combinations of resultant cubes are:
# These test cases can have any number of variables. But we've taken 3 variables for examples shown below:
# 1) Intersection : Void. Union : Tautology => Cube 1 = [10 01 01] and Cube 2 = [11 10 10].
# 2) Intersection and Union : Tautology => Cube 1 = [11 11 11] and Cube 2 = [11 11 11].
# 3) Intersection and Union : Void => Cube 1 = [00 00 00] and CUbe 2 = [00 00 00].
# 4) Intersection : Void and Union : a resultant cube. => Cube 1 = [01 10 01] and Cube 2 = [10 10 11]
# 5) Intersection and Union : a resultant cube. => Cube 1 = [01 11 11] and Cube 2 = [01 11 10]
# 6) Intersection and Union : another resultant cube. => Cube 1 = [01 01 10] and cube 2 = [01 11 10]
# 7) Intersection and Union : another resultant cube. => Cube 1 = [01 11 10] and cube 2 = [01 11 11]
# Similarly works for any set of input combinations given.

## Code begins:

#User input:
v=input("Enter the number of variables of the function")
L1=[11]*v
L2=[11]*v
print "Enter the first cube in PCN"
for i in range (v):
	L1[i]=raw_input()
	i+=1
	
i=0
print "Enter the second cube in PCN"
for i in range (v):
	L2[i]=raw_input()
	i+=1

#Initialising the resultant cube.
j=0
L3=["00"]*v

#Code for intersection.(Prints void is any variable results a 00, otherwise gives the intersection).
for j in range (v):
	if L1[j]=="00" or L2[j]=="00":
		print "Intersection gives Void"
		break
	elif (L1[j]=="10" and L2[j]=="01") or (L1[j]=="01" and L2[j]=="10"):
		print "Intersection gives Void"
		break
	elif L1[j]=="11":
		L3[j]=L2[j]
		if j==v-1:
			print "The Intersection is: ",L3
	elif L2[j]=="11":
		L3[j]=L1[j]
		if j==v-1:
			print "The Intersection is: ",L3
	elif L1[j]==L2[j]:
		L3[j]=L1[j]
		if j==v-1:
			print "The Intersection is: ",L3
	j+=1
#End of intersection

#Code for union:

#Initialising resultant cube
L4=["00"]*v

j=0
for j in range (v):
	if L1[j]=="11" or L2[j]=="11" or (L1[j]=="10" and L2[j]=="01") or (L1[j]=="01" and L2[j]=="10"):
		L4[j]="11"
	elif L1[j]=="00":
		L4[j]=L2[j]
	elif L2[j]=="00":
		L4[j]=L1[j]
	elif L1[j]==L2[j]:
		L4[j]=L1[j]
	j+=1
print "The Union is: ",L4

# End of code.