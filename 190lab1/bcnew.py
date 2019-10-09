from stackLib import *

def bc(string):
	x=stack()
	L=[0,0]
	strlen=len(string)
	for i in range (0,strlen):
		if (string[i]=='(') or (string[i]=="{") or (string[i]=='['):
			x.push(string[i])
		if (string[i]==')'):
			rval=x.pop()
			if rval==False:
				L = [False, i]
				return L
			if rval!='(':
				L = [False, i]
				return L
		if (string[i]=='}'):
                        rval=x.pop()
                        if rval==False:
                                return [False, i]
                        if rval!='{':
                                L = [False, i]
				return L
		if (string[i]==']'):
                        rval=x.pop()
                        if rval==False:
                                return [False, i]
                        if rval!='[':
				L=[False,i]
                                return L
	

	rval = x.pop()

	if rval!=False:
		L =[False,i]
	if rval==False:
		L=[True,i]
	return L
	

	
			
			
