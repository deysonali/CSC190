def selection_sort(u):
	for i in range(len(u)-1,-1,-1):
		max = i
		for j in range(0,i):
			if (u[j] > u[max]):
				max = j
		temp = u[i]
		u[i] = u[max]
		u[max] = temp

	return True

def helper_makeheap(u,end,root):
	max = root
	lc = 2*root+1
	rc = 2*root+2
	if (lc < end) and (u[lc] > u[root]):
		max = lc
	if (rc < end) and (u[rc] > u[max]):
		max = rc

	if max != root:
		temp = u[max]
		u[max] = u[root]
		u[root] = temp
		helper_makeheap(u,end,max)
	
	else:
		return u
	
def heapify(u):
	end = len(u)
	#ALWAYS FROM BOTTOM UP
	for i in range(len(u)-1,-1,-1):
		maxloc = i
		helper_makeheap(u,end,maxloc)
	
	return True
	#print "u heaped", u
	
	
#	temp = u[0]
#        u[0] = u[minloc]
#        u[minloc] = temp
	#heapify rest

#	for i in range(0,end):
#		index = i
#		while True:
#			parentindex = index/2	
#			if parentindex = 0:
#				break
#			if u[parentindex]>u[index]:
#				 temp = u[j]
#	        	         u[j] = u[minloc]
 #        	        	 
#				u[minloc] = temp
 

def reheapify(u,end):
	if end <=1:
		return True
	else:
		helper_makeheap(u,end,0)
	#print "u heaped with end", u, end
	return True

def heap_sort(u):
	heapify(u)
	for i in range(len(u)-1,-1,-1):
		temp = u[0]
		u[0] = u[i]
		u[i] = temp
		reheapify(u,i)
	#	print " u is now", u
	return True

def helper_merge(a,b,u):
	na = len(a)
	nb = len(b)
	n = na+nb
	ia = 0
	ib = 0
	ind = 0
	while ia < na and ib < nb:
		if a[ia] < b[ib]:
			u[ind] = a[ia]
			ia = ia + 1
		else:
			u[ind] = b[ib]	
			ib = ib + 1
		ind = ind + 1
	while ia < na:
		u[ind] = a[ia]
		ia = ia + 1
		ind = ind + 1
	while ib < nb:
		u[ind] = b[ib]
		ib = ib + 1
		ind = ind + 1
	
	return True

def merge_sort(u):
	if len(u)>1:
		middle = (len(u)+1)/2
		lower = u[:middle]
		upper = u[middle:]
		
		merge_sort(lower)
		merge_sort(upper)
		
		helper_merge(lower,upper,u)
		
		
	
	
