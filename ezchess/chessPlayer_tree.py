from chessLib_queue import *

class tree:
	def __init__(self,x):
        	self.store = [x,[]]
		self.depth = 0

	def AddSuccessor(self,x):
        	self.store[1] = self.store[1] + [x]
        	return True
	def getSuccessors(self):
		return self.store[1]

	def Print_DepthFirst(self,level=0):
	
		indent=""
	
		for i in range (0,level):
			indent=indent+ "   "
	
			print indent + str(self.store[0])
	
		level=level+1

		for j in self.store[1]:
	   		j.Print_DepthFirst(level)
	def GetLevelOrder(self):
       		x=queue()
        	x.enqueue(self.store)
       		accum=[]
        	while True:
            		y=x.dequeue()
            		# y is a 2-list where y[0]=True/False
            		# and y[1] is the actual dequeued value when y[0]=True
            		if (y[0]==False):
                		break
           	 	else:
               			v=y[1]
                		accum=accum+[v[0]]
                		for i in v[1]:
                    			x.enqueue(i.store)
        	return accum
	def isLeaf(self):
		if self.store[1] == []:
			return True
		else:
			return False	


	
	
		
	
