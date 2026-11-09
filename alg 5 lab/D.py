class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

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

    def find_max(self):
        if self.root is None:
            return f'{str(None)}'
        return self._max_node(self.root).data

    def _max_node(self, node):
        c = node
        while c.right is not None:
            c = c.right
        return c

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node
        if key < node.data:
            node.left = self._delete(node.left, key)
        elif key > node.data:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            max_node = self._max_node(node.left)
            node.data = max_node.data
            node.left = self._delete(node.left, max_node.data)
        return node

n = list(map(int, input().split()))
p = BinaryTree()
for i in n[:-1]:
    p.insert(i)

p.delete(p.find_max())
print(p.find_max())    
    