class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.count = 1

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
                node.count += 1
                return 


    def order_up(self):
        return self._order_up(self.root)

    def _order_up(self, node):
        if node is None:
            return []
        return self._order_up(node.left) + [(node.data, node.count)] + self._order_up(node.right)
n = list(map(int, input().split()))
p = BinaryTree()

for i in n[:-1]:
    p.insert(i)

s = p.order_up()

for i, j in s:
    print(i, j)
