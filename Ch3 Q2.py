class Node:
	def __init__(self,n):
		self.val = n
		self.next = None

class Stack:
	top = None
	min = None
	def push(self,n):
		if self.top is  None:
			self.top = Node(n)
			self.min = n
		elif self.top is not None:
			newNode = Node(n)
			newNode.next = self.top
			self.top = newNode
			if self.min>self.top.val:
				self.min = self.top.val

	def min1(self):
		print(self.min)		

	def __str__(self):
		ret_str = ""
		while(self.top is not None):
			ret_str = ret_str +str(self.top.val)
			self.top = self.top.next
		return ret_str
s = Stack()
s.push(1)
s.push(2)
s.min1()	
print(s)	