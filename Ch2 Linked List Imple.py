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



        print(l)
l = linkedlist()
l.insert(1)
l.insert(2)
l.insert(3)
l.insert(4)
l.insert(5)
l.insert(6)

print(l)
#print(l.get_size())
#l.find(7)
#l.remove(5)
