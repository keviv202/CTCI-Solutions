class Node:
    def __init__(self, n):
        self.val = n
        self.next = None


class queue:
    head = None
    tail = None

    def add(self, n):
        if self.head is None:
            self.head = Node(n)
            self.tail = self.head
        elif self.head is not None:
            self.tail.next = Node(n)
            self.tail = self.tail.next

    def remove(self):
        if self.head is not None:
            print(self.head.val)
            self.head = self.head.next
        else:
            print("Queue is empty")

    def __str__(self):
        ret_str = ""
        while (self.head is not None):
            ret_str = ret_str + str(self.head.val)
            self.head = self.head.next
        return ret_str


q = queue()
q.add(1)
q.add(2)
q.add(3)
q.remove()
q.remove()
q.remove()
q.remove()
print(q)
