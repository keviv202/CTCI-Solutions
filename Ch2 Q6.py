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

	def palindrome(self,l):
		temp = self.head
		l = []
		while(temp != None):
			l.append(temp.val)
			temp = temp.next
		temp1 = self.head
		while (temp1 != None):
			if temp1.val == l.pop():
				temp1 = temp1.next
			else:
				return False
			print(l)


		return True

l = linkedlist()
l.insert(1)
l.insert(2)
l.insert(1)
l.insert(2)
l.insert(2)
print(l.palindrome(l))
print(l)