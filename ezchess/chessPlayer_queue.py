class queue:
        def __init__(self):
                self.store=[]

        def enqueue(self, x):
                self.store=[x]+self.store
                return True

        def dequeue(self):
                if (len(self.store)==0):
                        val = False
			val2 = []
                else:
			val = True
                        val2=self.store[len(self.store)-1]
                        self.store=self.store[0:len(self.store)-1]
			
                return [val,val2]
	def empty(self):
		if(len(self.store)==0):
			return True
		else:
			return False
	
