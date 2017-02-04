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

    def kthtolast(self, k):
        c = 1
        temp1 = self.head
        while (temp1.next != None):
            temp1 = temp1.next
            c = c + 1
            if c == k:
                ret_str = ""
                while (temp1 != None):
                    ret_str = ret_str + (str(temp1.val))
                    temp1 = temp1.next
                return ret_str
        return "List is not as long as K"


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
print(l.kthtolast(5))
print(l)