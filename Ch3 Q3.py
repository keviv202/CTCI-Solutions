class Node:
	def __init__(self,n):
		self.val = n
		self.next = None
class Stack:
	def __init__(self,capacity):
		self.capacity = capacity
		self.top = None	
		self.size = 0
	def push(self,n):
		if self.top is None:
			self.top = Node(n)
			self.size = self.size + 1
		elif self.top is not None:
			newnode = Node(n)
			newnode.next = self.top
			self.top = newnode
			self.size = self.size + 1
	def pop(self):
		if self.top is not None:
			print(self.top.val)
		self.top = self.top.next

	def __str__(self):
		ret_str = ""
		while(self.top is not None):
			ret_str = ret_str + str(self.top.val)
			self.top = self.top.next
		return ret_str

class setofstacks:
	def __init__(self,capacity):
		self.capacity = capacity
		#self.current = 0
		self.stack_list = []
	def spush(self,n):
		if len(self.stack_list) == 0:
			stackk = Stack(self.capacity)
			self.stack_list.append(stackk)
			self.stack_list[-1].push(n)
		elif self.stack_list[-1] is not None:
				if self.stack_list[-1].size < self.stack_list[-1].capacity:
					self.stack_list[-1].push(n)
				elif 	self.stack_list[-1].size == self.stack_list[-1].capacity:
					stackk = Stack(self.capacity)
					self.stack_list.append(stackk)
					self.stack_list[-1].push(n)

	def spop(self):
		for i in reversed(range(len(self.stack_list))):
			last = self.stack_list[i]
			return last.pop()

	def __str__(self):
		ret_str = ""
		for i in reversed(range(len(self.stack_list))):
			last = self.stack_list[i]
			while(last.top is not None):
				ret_str = ret_str + str(last.top.val)
				last.top = last.top.next
		return ret_str
		
s = setofstacks(2)
s.spush(1)
s.spush(2)
s.spush(3)
s.spush(4)
(s.spop())
s.spush(5)
(s.spop())

#print(s.s1.capacity1())
print(str(s))
	