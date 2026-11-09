class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            return
        node = self.root

        while True:
            if key < node.data:
                if node.left is None:
                    node.left = Node(key)
                    return
                node = node.left
            elif key > node.data:
                if node.right is None:
                    node.right = Node(key)
                    return
                node = node.right
            else:
                return

    def next(self, key):

        node = self.root
        itog = -1

        while node is not None:
            if key <= node.data:
                itog = node.data
                node = node.left
            else:
                node = node.right
        return itog






n = int(input())
p = BinaryTree()
t = 0
l = 0
for i in range(n):
    z, c = input().split()
    c = int(c)
    if z == '+':
        if t:
            c = (c+l)%(10**9)
        p.insert(c)
        t = 0
    if z =='?':
        l = p.next(c)
        print(l)
        t = 1
        

    