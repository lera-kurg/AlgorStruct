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

            if key > node.data:
                if node.right is None:
                    node.right = Node(key)
                    return
                node = node.right
            elif key < node.data:
                if node.left is None:
                    node.left = Node(key)
                    return
                node = node.left
            else:
                return

    def height(self, node):
        if node is None:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    def balance(self):
        return self._balance(self.root)

    def _balance(self, node):
        if node is None:
            return True
         
        lft = self.height(node.left)
        rht = self.height(node.right)

        if abs(rht - lft) > 1: 
            return False

        return self._balance(node.left) and self._balance(node.right) 


n = list(map(int, input().split()))
p = BinaryTree()

for i in n[:-1]:
    p.insert(i)

if p.balance():
    print("YES")
else:
    print("NO")
