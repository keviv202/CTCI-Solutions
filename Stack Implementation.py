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
                print(self.top.val)
                self.top = self.top.next

        def peek(self):
            return self.top.val

        def __str__(self):
            temp = self.top
            ret_str = ""
            while(temp is not None):
                ret_str = ret_str + str(temp.val)
                temp = temp.next
            return ret_str

s = stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.pop()
s.pop()
print(s)
