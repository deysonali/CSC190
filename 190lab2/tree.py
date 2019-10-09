from Queue import *
import binary_tree

class tree:
	def __init__(self,x):
        	self.store = [x,[]]
		self.depth = 0

	def AddSuccessor(self,x):
        	self.store[1] = self.store[1] + [x]
        	return True

	def Print_DepthFirst(self,level=0):
	
		indent=""
	
		for i in range (0,level):
			indent=indent+ "   "
	
			print indent + str(self.store[0])
	
		level=level+1

		for j in self.store[1]:
	   		j.Print_DepthFirst(level)
	def Get_LevelOrder(self):
        	newlist=[]
		Q=Queue()
		Q.enqueue(self)
		while(Q.empty()==False):
			node = Q.dequeue()
			newlist=newlist+[node.store[0]]
			for i in node.store[1]:
				Q.enqueue(i)
		
		return newlist

	def ConvertToBinaryTree(self):
		v=binary_tree.binary_tree(3)
		return v
	
	
		
	
