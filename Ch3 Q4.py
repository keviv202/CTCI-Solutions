class Node:
	def __init__(self,n):
		self.val = n
		self.next = None

class stack:
		top = None

		def push(self,n):
			if self.top is None:
				self.top = Node(n)
			elif self.top is not None:
				newnode = Node(n)
				newnode.next = self.top
				self.top = newnode

		def pop(self):
			if self.top is None:
				return 'Stack is Empty'
			else:
				t = self.top.val
				self.top = self.top.next
				return (t)

		def peek(self):
			return self.top.val

		def __str__(self):
			temp = self.top
			ret_str = ""
			while(temp is not None):
				ret_str = ret_str + str(temp.val)
				temp = temp.next
			return ret_str

class queue:
	s1 = stack()
	s2 = stack()
	def add(self,n):

		self.s1.push(n)

	def remove(self):
		while(self.s1.top is not None):
			self.s2.push(self.s1.pop())
		return self.s2.pop()

	def __str__(self):
		while(self.s1.top is not None):
			self.s2.push(self.s1.top.val)
			self.s1.top = self.s1.top.next

		ret_str = ""
		while (self.s2.top is not None):
			ret_str = ret_str + str(self.s2.pop())
		return ret_str

q = queue()
q.add(1)
q.add(2)
q.add(3)
print(q.remove())
print(q)
