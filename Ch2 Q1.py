class Node:
	def __init__(self,n):
		self.val=n
		self.next=None

class linkedlist:
	head=None

	def insert(self,n):
		if self.head is None:
			self.head = Node(n)

		elif self.head is not None:
			temp = self.head
			while(temp.next != None):
				temp = temp.next
			temp.next = Node(n)

	

	def __str__(self):
		temp = self.head
		ret_str = ""
		while (temp != None):
			ret_str += (str(temp.val))
			temp = temp.next
		return ret_str

	def duplicate(self):
		l1 = []
		temp1 = self.head
		l1.append(temp1.val)
		while(temp1.next != None):
			if temp1.next.val in l1:
				temp1 = temp1.next
				continue
			temp1 = temp1.next	
			l1.append(temp1.val)

		print(l1)

l = linkedlist()
l.insert(1)
l.insert(1)
l.insert(1)
l.insert(2)
l.insert(2)
l.insert(3)
l.insert(4)
l.insert(4)
l.insert(4)
l.insert(5)
l.insert(6)
l.insert(4)
l.duplicate()
print(l)
#print(l.get_size())
#l.find(7)
#l.remove(5)
