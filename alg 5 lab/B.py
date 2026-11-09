class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

class Binarytree:
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

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))

n = list(map(int, input().split()))
p = Binarytree()

for i in n[:-1]:

    p.insert(i)

print(p.height())