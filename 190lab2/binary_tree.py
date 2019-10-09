import tree
from Queue import *

class binary_tree:
	def __init__(self,x):
        	self.node = x
		self.left = None
		self.right = None

	def AddLeft(self,x):
		if(self.left==None):
			self.left=binary_tree(x)
			print "self.left:" +str(self.left)
			return True
		else:
			self.left.AddLeft(x)
	def AddRight(self,x):
		if(self.right==None):
			self.right=binary_tree(x)
			return True
		else:
			self.right.AddRight(x)
	def Get_LevelOrder(self):
		newlist=[]
		Q=Queue()
		Q.enqueue(self)
		while(Q.empty()==False):
			val=Q.dequeue()
			newlist=newlist+[val.node]
			if val.left != None:
				Q.enqueue(val.left)
			if val.right != None:
				Q.enqueue(val.right)
		return newlist
	def ConvertToTree(self):
		stub=tree.tree(1)
		return [True,stub] 
			
	   
        
    
	
	
