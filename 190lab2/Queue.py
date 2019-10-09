class Queue:
        def __init__(self):
                self.store=[]

        def enqueue(self, x):
                self.store=[x]+self.store
                return True

        def dequeue(self):
                if (len(self.store)==0):
                        return False
                else:
                        rval=self.store[len(self.store)-1]
                        self.store=self.store[0:len(self.store)-1]
                        return rval
	def empty(self):
		if(len(self.store)==0):
			return True
		else:
			return False
	
