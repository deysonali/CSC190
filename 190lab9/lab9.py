def quick_sort(u,ini,fin):
	if ini < fin:		
		pIndex = partition(u,ini,fin)
		
		quick_sort(u,ini,pIndex-1)
       		quick_sort(u,pIndex+1,fin)
	
	return True

def partition(u,ini,fin):
	pivot = u[ini]

	left = ini+1
	right = fin

	done = False
	while not done:

		while left <= right and u[left] <= pivot:
			left = left + 1

		while u[right] >= pivot and right >= left:
			right = right -1

		if right < left:
			done = True
		else:
			temp = u[left]
			u[left] = u[right]
			u[right] = temp

	temp = u[ini]
	u[ini] = u[right]
	u[right] = temp
	
	pIndex = right
	return pIndex

def hanoi(accum,n,start,tmp,final):
	if n > 0:
		hanoi(accum,n - 1,start,final,tmp)
		final.append(start.pop())
		hanoi(accum,n - 1,tmp,start,final)
		accum += [start, tmp, final]
		print start, tmp, final
		return True
	else:
		return True

#alist = [54,26,93,17,77,31,44,55,20]
#quick_sort(alist,0,len(alist)-1)
#print alist


