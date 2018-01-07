######This is the code for PROJECT 1--OBDD,ROBDD & ITE expression

'''
1.Enter the function
2.If you want to quit press "q", else specify the splitting order
3.If you didn't quit,output(OBDD leaf node values,ROBDD tree and ITE expression) appears for the given splittng order.
4.Go to step 2.
Hence you can see output for any splitting order you want in one running of the code.

***The code also does ERROR HANDLING.It allows only valid inputs.

'''


'''
TEST CASES:
1.All null cubes.
2.A tatutology.
3.PCN=[['01','01','01'],['10','01','01']]-->gives an asymmetric tree
4.PCN=[['01','01','01'],['10','10','10']]-->gives a symmetric tree
5.PCN=[['01','11','11']]-->Function dependent on a single variable
'''



#----------------------------------------------------------------------------------------------------

import graphviz as gv
import numpy as np
import copy

#--------------------------------a function for ERROR HANDLING in user input--------------------------

def checkinput(ip,varr):
        ans = "xx"
        while ans=="xx":
            try:
                    ans = input()
                    if ip==1:
                            if ans not in ("11","01","10","00"):  #-------takes in only PCN notation
                                raise ValueError
                    elif ip==2:
                            if ans not in varr:  #----checking if variables specified for splitting order are present in original variable list
                                    raise ValueError
                    elif ip==3:
                            int(ans)   #--------takes in only integers
                            
            except ValueError:
                    ans = "xx"
                    print("That's not a valid input! Please enter that part again.")
                
        return ans


#----------------------------a shortcut function for and-ing the cubes-------------------------------

def Op_and(cp,c_mat):
	if c_mat == "11" or c_mat == cp:
		s = "11"
	else:
		s = "00" 
		
	return s

#-------------------------------------------------------------------------------------------------------

#------------------------------The recursion function for OBDD------------------------------------------	
var3=list()

def OBDD(reclist,index,col,ar,var3):
	global expp
	Main=copy.deepcopy(reclist[index])
	#print("index=",index,"col=",col,"\n \n")
	if index == n:
		#print ("Entered base condition")
		test=["11" for x in range(n)]
		if Main[0]==test:
			ar.append(1)
			#---------for ite expression------------
			expp=expp+",1"
			#-----pop the stored cubes of this level since they are no more needed
			reclist.pop(index)
			return
		elif "00" in Main[0]:
			ar.append(0)
			#---------for ite expression------------
			expp=expp+",0"
			#------pop the stored cubes of this level since they are no more needed
			reclist.pop(index)
			return 
	else:
		Left = copy.deepcopy(reclist[index])

		#-----and operation for left child
		for i in range(col):
			Left[i][index] = Op_and("10",Main[i][index])
			

		lc = len(Left)
		i=0

		#-----removing null cubes
		if lc!=1:
			while i<lc:
				if "00" in Left[i]:
					Left.pop(i)
					lc = lc-1
					if lc==1:
						break
				else:
					i=i+1
	
		#---------for ite expression------------
		if index!=0:
			expp=expp+",ite("+var3[index]
		else:
			expp=expp+"ite("+var3[index]

		#------appending the cubes of this level to reclist
		reclist.append(Left)

		#-----calling the recursion for left child
		OBDD(reclist,index+1,lc,ar,var3)

		
		Right= copy.deepcopy(reclist[index])

		#-----and operation for right child
		i=0
		for i in range(col):
			Right[i][index] = Op_and("01",Main[i][index])
	
		lc = len(Right)
		i=0
		
		#-----removing null cubes
		if lc!=1:	
			while i<lc:
				if "00" in Right[i]:
					Right.pop(i)
					lc = lc-1
					if lc==1:
						break
				else:
					i = i+1	

		#------appending the cubes of this level to reclist
		reclist.append(Right)

		#------calling the recursion for right child
		OBDD(reclist,index+1,lc,ar,var3)
		
		#---------for ite expression------------
		expp=expp+")"
		
		#------pop the stored cubes of this level since they are no more needed
		reclist.pop(index)

		#print("end")
		return
	

#-----------------------------------------------------------------------------------------------------

#-------------------------------------------ROBDD PART------------------------------------------------

def ROBDD(a,var):
	p=len(a)
	tt=len(a)
	no=len(var)

	k=2 
	f=0
	foundindic=0

	dic=list()

	#------------Robdd is made using the leaf node array got from the OBDD function

	while p>1:
		no=no-1
		uff=0
		f=0

		for i in range(0,p-1,2):
			foundindic=0
			if i!=0 or p!=tt:
				if p!=tt:
					#-----if left and right child are both 0 or 1,parent id will be 0 or 1 respectively
					if a[i]==a[i+1] and (a[i]==0 or a[i]==1):
						#print("same id")
						if a[i]==0:
							dic.append({'id':0,'l':0,'r':0,'lev':var[no]})
						elif a[i]==1:
							dic.append({'id':1,'l':1,'r':1,'lev':var[no]})
						a[f]=a[i]
						f=f+1
						foundindic=1
						
					#-----checking if other ids have same children(non leaf node levels)
					else:
						for j in range(len(dic)-uff,len(dic),1):
							if dic[j]['l']==a[i] and dic[j]['r']==a[i+1]:
								#print("old id non-last level")
								dic.append({'id':dic[j]['id'],'l':a[i],'r':a[i+1],'lev':var[no]})
								a[f]=dic[j]['id']
								foundindic=1
								f=f+1
								break

				#-----checking if other ids have same children(for leaf node level)
				else:
					for j in range(len(dic)-uff,len(dic),1):
						if dic[j]['l']==a[i] and dic[j]['r']==a[i+1]:
							#print("old id last level")
							dic.append({'id':dic[j]['id'],'l':a[i],'r':a[i+1],'lev':var[no]})
							a[f]=dic[j]['id']
							foundindic=1
							f=f+1
							break

				#-------assigning new ids in case they aren't found in the old id list
				if foundindic!=1:
					#print("new id")
					if p==tt:
						if a[i]==0 and a[i+1]==0:
							dic.append({'id':0,'l':0,'r':0,'lev':var[no]})
						elif a[i]==1 and a[i+1]==1:
							dic.append({'id':1,'l':1,'r':1,'lev':var[no]})
						else:
							dic.append({'id':k,'l':a[i],'r':a[i+1],'lev':var[no]})
							k=k+1 
					else:
						dic.append({'id':k,'l':a[i],'r':a[i+1],'lev':var[no]})
						k=k+1
					
					a[f]=dic[len(dic)-1]['id']
					f=f+1
					foundindic=0

			else:
				#print("for first element")
				if a[i]==0 and a[i+1]==0:
					dic.append({'id':0,'l':0,'r':0,'lev':var[no]})
				elif a[i]==1 and a[i+1]==1:
					dic.append({'id':1,'l':1,'r':1,'lev':var[no]})
				else:
					dic.append({'id':k,'l':a[i],'r':a[i+1],'lev':var[no]})
					k=k+1 
				a[f]=dic[0]['id']
				f=f+1
				
			uff=uff+1	

		p=int(p/2)

	#print("dic=",dic)
	dic2=list()
	dic2.append(dic[len(dic)-1])

	#--------reducing the dictionary of ids such that there's only one element with a particular id
	#--------it is done from top to bottom.Top variables are stored first in the dictionary list
	for i in range(len(dic)-2,-1,-1):
		just=0
		for j in dic2:
			if dic[i]['id']==j['id']:
				break
			else:
				just=just+1
		if just==len(dic2):
			dic2.append(dic[i])

	print("\nReduced ROBDD dictionary of ids=",dic2,"\n")

#----------------------------------------------------------------------------------------------------

#------------------------------------------GRAPHVIZ PART---------------------------------------------

	rbd = gv.Digraph(format='png')

	#-----traversing the reduced dictionary
	for i in range(0,len(dic2),1):

		#------if left child = right child 
		if dic2[i]['l']==dic2[i]['r'] and dic2[i]['l']==0:
			if len(dic2)!=1:
				rbd.node(str(dic2[i]['id']),str(0))
			else:
				rbd.edge(dic2[i]['lev'],str(0))
		elif dic2[i]['l']==dic2[i]['r'] and dic2[i]['l']==1:
			if len(dic2)!=1:
				rbd.node(str(dic2[i]['id']),str(1))
			else:
				rbd.edge(dic2[i]['lev'],str(1))
		elif dic2[i]['l']==dic2[i]['r']: #----------ids other than 0 and 1
			rbd.node(str(dic2[i]['id']),dic2[i]['lev'])
			rbd.edge(str(dic2[i]['id']),str(dic2[i]['l']),str('0'+'/'+'1'))

		#------if left child not equal to right child 
		else:
			rbd.node(str(dic2[i]['id']),dic2[i]['lev'])
			rbd.edge(str(dic2[i]['id']),str(dic2[i]['l']),str(0))
			rbd.edge(str(dic2[i]['id']),str(dic2[i]['r']),str(1))

	rbd.render('img/rbd',view=True)
	return

			

#---------------------------------------------------------------------------------------------------------

#--------------------------------------------PROGRAM BEGINS-----------------------------------------------

expp=""
a=list()
var1 = list()
var2 = list()
cp=list()

print("Enter the number of variables in the function:")
n =int(checkinput(3,var1)) #-----------calls checkinput function to take only valid inputs
print("Enter the number of cubes in the function:")
c =int(checkinput(3,var1)) #-----------calls checkinput function to take only valid inputs


print("Enter the variables in the function")

for i in range(n):
	v = input()
	var1.append(v)

dc=0
tautology=0
flag=0
lol="00"
cube=[["00" for x in range(n)] for x in range(c)]

print("Enter the cubes in PCN(in the entered variable order)")

#This part takes input and removes null cubes and checks for don't care cubes Ex:['11','11','11']

for i in range(c):
	for j in range(n):
		cube[i-flag][j]=checkinput(1,var1) #-----------calls checkinput function to take only valid inputs
		if cube[i-flag][j]=="11":
			dc=dc+1
		if cube[i-flag][j]=="00":
#      print("That was a redundant cube.Enter the next cube.")
			for k in range(n-j-1):
				lol=checkinput(1,var1) #-----------calls checkinput function to take only valid inputs
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


var2=copy.deepcopy(var1)

#--------our new c is the number of cubes left after removing null and don't care cubes
c=c-flag
quit='g'

if tautology!=0:
	print("The entered function is a tautology")
	for i in range(2**len(var1)):
		a.append(1)
	while quit!='q':
		print("\n------If you want to quit press (q) else press any other letter")
		quit=input()
		if quit!='q':
			print("Enter the variables in the order you want to split it")
			for i in range(n):
				var2[i] = checkinput(2,var1)  #-----------calls checkinput function to take only valid inputs
			print("\n####################\nFunction=ite("+var2[0]+",1,1)\n####################")
			ROBDD(a,var2)


elif c==0:
	print("All the entered cubes are Null")
	for i in range(2**len(var1)):
		a.append(0)
	while quit!='q':
		print("\n-------If you want to quit press (q) else press any other letter")
		quit=input()
		if quit!='q':
			print("Enter the variables in the order you want to split it")
			for i in range(n):
				var2[i]= input()
			print("\n####################\nFunction=ite("+var2[0]+",0,0)\n####################")
			ROBDD(a,var2)

else:
	print("reduced input:",cube)
	while quit!='q':
		print("\n------If you want to quit press (q) else press any other letter")
		quit=input()

		if quit!='q':
			print("Enter the variables in the order you want to split it")
			for i in range(n):
				var2[i] = input()
			
			#----------takes care of the change in splitting order	
			cp=copy.deepcopy(cube)
			for x in range (len(var2)):
				for y in range (len(var1)):
					if var2[x]==var1[y]:
						for z in range (len(cube)):
							cp[z][x]=cube[z][y]
						break

			rec=list()
			#------rec is a list of list of lists to store cubes at different levels
			rec.append(cp)
			func = list()
			expp=""
		
			OBDD(rec,0,c,func,var2)

			print("Leaf node values in order=",func)
			print("Number of leaf nodes=",len(func))
			a=copy.deepcopy(func)

			#----------printing the ite expression
			print("\n####################\nFunction=",expp,"\n####################")

			#-------calling robdd function which also does the graphviz part
			ROBDD(a,var2)
























