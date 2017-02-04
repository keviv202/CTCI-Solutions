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

	def intersect(self,l1,l2):
		ll =[]
		temp1 = l1.head
		temp2 = l2.head
		c1,c2 = 0,0
		i,j = 0,0
		k,m = 0,0
		while(temp1 != None):
			temp1 = temp1.next
			c1 =c1+1
		print(c1)
		while(temp2 != None):
			temp2 = temp2.next
			c2 =c2+1
		print(c2)	
		temp1 = l1.head
		temp2 = l2.head
		a = c1 - c2
		for o in range(a):
			temp1 = temp1.next
		while(i<c1 - a and j <c2):
			if  temp1.val == temp2.val:
				k=k+1
				m=m+1
				ll.append(temp1.val)

			elif temp1.val != temp2.val:
				k = 0
				m = 0
				l=[]
			i = i + 1
			j = j + 1
			temp1 = temp1.next
			temp2 = temp2.next
		if k !=0 and m!=0:
			print("Intersect")
			print(ll[0])
		else:
			print("Do not intersect")

l1 = linkedlist()
l2 = linkedlist()
l1.insert(1)
l1.insert(2)
l1.insert(1)
l1.insert(2)
l1.insert(2)
l1.insert(2)
l1.insert(3)
l1.insert(4)
l2.insert(1)
l2.insert(2)
l2.insert(2)
l2.insert(3)
l2.insert(4)
l1.intersect(l1,l2)
print(l1)
print(l2)