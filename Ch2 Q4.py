class Node:
    def __init__(self, n):
        self.val = n
        self.next = None


class linkedlist:
    head = None

    def insert(self, n):
        if self.head is None:
            self.head = Node(n)

        elif self.head is not None:
            temp = self.head
            while (temp.next != None):
                temp = temp.next
            temp.next = Node(n)

    def __str__(self):
        temp = self.head
        ret_str = ""
        while (temp != None):
            ret_str += (str(temp.val))
            temp = temp.next
        return ret_str

    def partition(self,n):
        lessthan = None
        greaterthan = None

        temp1 = self.head
        while (temp1 != None):
            if temp1.val < n:
                if lessthan is None:
                    lessthan = Node(temp1.val)
                else:
                    temp = lessthan
                    while(temp.next != None):
                        temp = temp.next
                    temp.next = Node(temp1.val)

            elif temp1.val > n:
                if greaterthan is None:
                    greaterthan = Node(temp1.val)
                else:
                    temp2 = greaterthan
                    while (temp2.next != None):
                        temp2 = temp2.next
                    temp2.next = Node(temp1.val)
            temp1 = temp1.next

        temp = lessthan
        ret_str = ""
        while (temp != None):
            ret_str += (str(temp.val))
            temp = temp.next
        #return ret_str

        temp3 = greaterthan
        ret_str1 = ""
        while (temp3 != None):
            ret_str1 = ret_str1 + str(temp3.val)
            temp3 = temp3.next
        return ret_str + ret_str1

l = linkedlist()
l.insert(7)
l.insert(9)
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
l.insert(1)
print(l)
print(l.partition(3))