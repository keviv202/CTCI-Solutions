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


	def add(self,l,l1):
		temp1 = l.head
		temp2 = l1.head
		carry = 0
		new = None
		while (temp1 != None and temp2 != None):
			a = temp1.val + temp2.val + carry 
			if a >= 10:
				b = a%10
				carry = a//10
				if (new is None):
					new = Node(b)
				elif new is not None:
					temp = new
					while(temp.next!= None):	
						temp = temp.next
					temp.next = Node(b)
			elif a<10:
				if (new is None):
					new = Node(a)
				if new is not None:
					temp = new
					while(temp.next!= None):	
						temp = temp.next
					temp.next = Node(a)
			temp1=temp1.next
			temp2=temp2.next
		temp4 = new
		ret_str = ""
		while(temp4!= None):
			ret_str = ret_str + str(temp4.val)
			temp4 = temp4.next
		print(ret_str)
		

l = linkedlist()
l1 = linkedlist()
l2 = linkedlist()
l.insert(7)
l.insert(1)
l.insert(6)
l1.insert(5)
l1.insert(9)
l1.insert(2)
l2.add(l,l1)