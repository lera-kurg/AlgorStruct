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

    def size(self):
        return self._size(self.root)

    def _size(self, node):
        if node is None:
            return 0
        return 1 + self._size(node.left) + self._size(node.right)

n = list(map(int, input().split()))
p = BinaryTree()
for i in n[:-1]:
    p.insert(i)

print(p.size())