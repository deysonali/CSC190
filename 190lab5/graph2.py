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

class queue:
	def __init__(self):
		self.storage=[]
		self.cnt = 0

	def empty(self):
		if self.cnt==0:
			return True
		else:
			return False

	def store(self,value):
		self.storage=self.storage+[value]
		self.cnt = self.cnt + 1
		return self.cnt

	def retrieve(self):
		if (self.cnt==0):
			return [False,0]
		else:
			r=self.storage[0]
			self.cnt=self.cnt-1
			self.storage=self.storage[1:]
			return [True,r]
class graph:
	def __init__(self):
		self.store = []

	def addVertex(self,n):
		if n <= 0:
			return -1
		for i in range(0,n):
			self.store = self.store +[[]]
		vertices = len(self.store)
		return vertices

	def addEdge(self,from_idx,to_idx,directed,weight):
		if from_idx < 0 or to_idx < 0:
			return False
		if from_idx >= len(self.store) or to_idx >= len(self.store):
			return False
		if weight <= 0:
			return False
		if directed == True:	
			self.store[from_idx] = self.store[from_idx] + [[to_idx, weight]]
			print self.store
			return True
		if directed == False:
		
			self.store[from_idx] = self.store[from_idx] + [[to_idx, weight]]
			self.store[to_idx] = self.store[to_idx] + [[from_idx, weight]]
			print self.store
			return True

	def traverse(self,start,typeBreadth):
		rval = []
		if typeBreadth == True:
			if start == None:
				subset = []
				C = queue()
				Discovered = []
				Processed = []
				length = len(self.store)
				for i in range(0,length):
					Discovered = Discovered + [False]
					Processed = Processed + [False]
				#initialnode = 0
				#subset = subset + [initialnode]
				#Processed[initialnode] = True
				for v in range(0,len(self.store)):
					
					C.store(v)
					ini = C.retrieve()
					if Processed[ini[1]] == False:
						subset = subset + [ini[1]]
						Processed[ini[1]]==True

					if Discovered[v] == False:
						for i in range(0,len(self.store[v])):
							C.store(self.store[v][i][0])
						Discovered[v] = True
					while C.empty() == False:
						a = C.retrieve()
						w = a[1]
						if Processed[w] == False:
							subset = subset + [w]
							Processed[w] = True
						for x in self.store[w]:							
							if Discovered[x[0]] == False:
								C.store(x[0])
								Discovered[x[0]] = True
					if subset != []:
						rval = rval + [subset]
						subset = []
			else:
				if start >= len(self.store):
					return False
				C = queue()
                                Discovered = []
                                Processed = []
                                length = len(self.store)
                                for i in range(0,length):
                                        Discovered = Discovered + [False]
                                        Processed = Processed + [False]
                                initialnode = start
                                rval = rval + [start]
                                Processed[initialnode] = True
                                for v in self.store[initialnode]:
                                        if Discovered[v[0]] == False:
                                                C.store(v[0])
                                Discovered[initialnode] = True
				while C.empty() == False:
					a = C.retrieve()
					w = a[1]
			
					if Processed[w] == False:
						rval = rval + [w]
						Processed[w] = True
					for x in self.store[w]:
						if Discovered[x[0]] == False:
							C.store(x[0])
							Discovered[x[0]] = True

		if typeBreadth == False:
			if start == None:
				subset = []
				C = stack()
			
				Discovered = []
				Processed = []
				length = len(self.store)
				for i in range(0,length):
					Discovered = Discovered + [False]
					Processed = Processed + [False]
				initialnode = 0
				subset = subset + [initialnode]
				Processed[initialnode] = True
				for v in range(0,len(self.store)):
					if Discovered[v] == False:
						for i in range(0,len(self.store[v])):
							C.store(self.store[v][i][0])
						
						Discovered[v] = True
					while C.empty() == False:
						a = C.retrieve()
						w = a[1]
						if Processed[w] == False:
							subset = subset + [w]
							Processed[w] = True
						for x in self.store[w]:							
							if Discovered[x[0]] == False:
								C.store(x[0])
								Discovered[x[0]] = True
					if subset != []:
						rval = rval + [subset]
						subset = []
			else:
				if start >= len(self.store):
					return False
				C = stack()
                                Discovered = []
                                Processed = []
                                length = len(self.store)
                                for i in range(0,length):
                                        Discovered = Discovered + [False]
                                        Processed = Processed + [False]
                                initialnode = start
				
				if Discovered[v] == False:
					for i in range(0,len(self.store[v])):
						C.store(self.store[v][i][0])
					
					Discovered[v] = True
				while C.empty() == False:
					a = C.retrieve()
					w = a[1]
					if Processed[w] == False:
						subset = subset + [w]
						Processed[w] = True
					for x in self.store[w]:							
						if Discovered[x[0]] == False:
							C.store(x[0])
							Discovered[x[0]] = True
				
				
		return rval

	def connectivity(self, vx, vy):
		if vx >= len(self.store) or vy >= len(self.store):
			return -1
		rval = []
		traversal1 = self.traverse(vx,False)
		print traversal1
		traversal2 = self.traverse(vy,False)
		print traversal2
		
		if vy in traversal1:
			rval = rval + [True]
		else:
			rval = rval + [False]
	
		if vx in traversal2:
			rval = rval + [True]
		else:
			rval = rval + [False]
		return rval

	#def pathway(self
