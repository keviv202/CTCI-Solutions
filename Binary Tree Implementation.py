class Node:
    def __init__(self,n):
        val = n
        self.left = None
        self.right = None

class Bst:
    root = None

    def insert(self,n):
        if self.root is None:
           self.root = Node(n)
