class stack:
	def __init__(self):
		self.storage=[]
		self.count=0

	def empty(self):
		if (self.count==0):
			return True
		else:
			return False

	def store(self,x):
		self.storage = self.storage + [x]
		self.count = self.count + 1
		return True

	def retrieve(self):
		if (self.count==0):
			return [False,0]
		else:
			self.count = self.count - 1
			rval = self.storage[-1]
			self.storage = self.storage[0:-1]
			return [True,rval]
