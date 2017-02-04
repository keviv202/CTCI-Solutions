class threeinone:
	def __init__(self,stackcount,n):
		self.n = int(n/3)
		print(self.n)
		self.l = [0] * n
		print (self.l)
		self.top1 = self.l[0]
		self.top2 = self.n
		self.top3 = 2*self.n
	
	def push(self,stacknumber,n):
		if stacknumber == 1:
			if self.top1 == self.n:
				print("stack is full")
			else:
				self.l[self.top1] = n
				self.top1 = self.top1 + 1					
		elif stacknumber == 2:
			if self.top2 == 2*self.n:
				print("stack2 is full")
			else:
				self.l[self.top2] = n
				self.top2 = self.top2 + 1
		elif stacknumber == 3 and self.top2 <3*self.n:
			if self.top3 == 3*self.n:
				print("stack3 is full")
			else:
				self.l[self.top3] = n
				self.top3 = self.top3 + 1					
	
		print(self.l)	

t = threeinone(3,9)
t.push(1,3)
t.push(1,4)
t.push(1,5)
t.push(1,6)
t.push(2,1)
t.push(3,100)		