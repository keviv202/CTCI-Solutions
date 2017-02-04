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

		def sortstack(self):
			s1 = stack()
			temp = self.top
			min = temp.val
			while temp.next is not None:
				if s1.peek() < min:
					min = temp.next.val
				temp = temp.next
			s1.push(s.pop())
			print(s1)

s = stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.sortstack()
print(s)
print()	